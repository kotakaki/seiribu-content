#!/usr/bin/env python3
"""Finish generated Seiribu images from an image-plan JSON.

This script does not call the image model. Codex calls imagegen, saves generated
source images into the plan draft_dir using the planned file names, then this
script resizes/crops images, overlays the Seiribu logo on inline images, and
writes the final assets README.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
from dataclasses import dataclass
from pathlib import Path
from typing import Any

try:
    from PIL import Image, ImageDraw, ImageFont, ImageStat
except ModuleNotFoundError as exc:  # pragma: no cover - user-facing guard
    raise SystemExit(
        "Pillow is required. Run with the bundled Codex Python: "
        "/Users/kota/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3"
    ) from exc


ROOT = Path(__file__).resolve().parents[1]
PROJECT_ROOT = ROOT.parent
DEFAULT_LOGO = ROOT / "assets" / "images" / "brand" / "seiribu-logo.png"
IMAGE_SUFFIXES = {".png", ".jpg", ".jpeg", ".webp"}
FONT_CANDIDATES = [
    Path("/System/Library/Fonts/ヒラギノ角ゴシック W8.ttc"),
    Path("/System/Library/Fonts/AppleSDGothicNeo.ttc"),
    Path("/System/Library/Fonts/Supplemental/AppleGothic.ttf"),
]


@dataclass
class FinishedImage:
    role: str
    file_name: str
    title: str
    alt: str
    caption: str
    position: str
    size: str
    logo_mode: str
    source: Path
    output: Path


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def project_path(value: str | Path) -> Path:
    path = Path(value)
    return path if path.is_absolute() else PROJECT_ROOT / path


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def parse_size(value: str) -> tuple[int, int]:
    clean = value.lower().replace("×", "x")
    parts = [part.strip() for part in clean.split("x")]
    if len(parts) != 2:
        return (1200, 675)
    try:
        return (int(parts[0]), int(parts[1]))
    except ValueError:
        return (1200, 675)


def cover(src: Image.Image, size: tuple[int, int]) -> Image.Image:
    src = src.convert("RGBA")
    sw, sh = src.size
    tw, th = size
    scale = max(tw / sw, th / sh)
    resized = src.resize((round(sw * scale), round(sh * scale)), Image.Resampling.LANCZOS)
    left = (resized.width - tw) // 2
    top = (resized.height - th) // 2
    return resized.crop((left, top, left + tw, top + th))


def contain(src: Image.Image, width: int) -> Image.Image:
    src = src.convert("RGBA")
    height = round(src.height * width / src.width)
    return src.resize((width, height), Image.Resampling.LANCZOS)


def font_path() -> Path | None:
    for path in FONT_CANDIDATES:
        if path.exists():
            return path
    return None


def load_font(size: int) -> ImageFont.ImageFont:
    path = font_path()
    if path:
        return ImageFont.truetype(str(path), size=size)
    return ImageFont.load_default()


def text_size(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.ImageFont) -> tuple[int, int]:
    box = draw.textbbox((0, 0), text, font=font)
    return box[2] - box[0], box[3] - box[1]


def extract_short_labels(image: dict[str, Any]) -> list[str]:
    fields = image.get("fields", {})
    text = " ".join(
        str(fields.get(key, ""))
        for key in ["入れたい要素", "画像のアイデア", "目的", "ALT"]
    )
    labels: list[str] = []
    for label in re.findall(r"Step\s*\d+\s*[:：]\s*[「『](.{1,12}?)[」』]", text, flags=re.I):
        labels.append(label)
    for label in re.findall(r"[「『](.{1,10}?)[」』]", text):
        if label not in labels and not re.search(r"[。、，,.]", label):
            labels.append(label)
    for label in re.findall(r"[①②③④⑤]\s*([^①②③④⑤、。]{1,12})", text):
        label = label.strip()
        if label and label not in labels:
            labels.append(label)
    return labels[:4]


def draw_label_chip(
    canvas: Image.Image,
    draw: ImageDraw.ImageDraw,
    text: str,
    center_x: int,
    y: int,
    *,
    fill: tuple[int, int, int, int],
    outline: tuple[int, int, int, int],
) -> None:
    font = load_font(max(24, round(canvas.width * 0.027)))
    tw, th = text_size(draw, text, font)
    pad_x = round(canvas.width * 0.018)
    pad_y = round(canvas.height * 0.012)
    x1 = max(20, center_x - tw // 2 - pad_x)
    x2 = min(canvas.width - 20, center_x + tw // 2 + pad_x)
    y1 = y
    y2 = y + th + pad_y * 2
    draw.rectangle((x1, y1, x2, y2), fill=fill, outline=outline, width=max(2, round(canvas.width * 0.002)))
    draw.text((center_x - tw / 2, y1 + pad_y - 2), text, font=font, fill=(32, 42, 60, 255))


def draw_diagram_labels(canvas: Image.Image, image: dict[str, Any]) -> str:
    if image.get("role") != "記事内図解":
        return "none"
    labels = extract_short_labels(image)
    if not labels:
        return "none"

    overlay = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    y = round(canvas.height * 0.055)
    count = len(labels)
    fill = (255, 255, 255, 226)
    outline = (214, 196, 150, 220)
    for index, label in enumerate(labels):
        center_x = round(canvas.width * (index + 1) / (count + 1))
        draw_label_chip(overlay, draw, label, center_x, y, fill=fill, outline=outline)
    canvas.alpha_composite(overlay)
    return ",".join(labels)


def luminance_and_variance(region: Image.Image) -> tuple[float, float]:
    gray = region.convert("L")
    stat = ImageStat.Stat(gray)
    mean = float(stat.mean[0])
    variance = float(stat.var[0])
    return mean, variance


def placement_box(
    position: str,
    canvas_size: tuple[int, int],
    logo_size: tuple[int, int],
    margin: int,
    padding: int,
) -> tuple[int, int, int, int]:
    cw, ch = canvas_size
    lw, lh = logo_size
    bw = lw + padding * 2
    bh = lh + padding * 2
    if position == "右上":
        x, y = cw - margin - bw, margin
    elif position == "右下":
        x, y = cw - margin - bw, ch - margin - bh
    elif position == "左下":
        x, y = margin, ch - margin - bh
    else:
        x, y = margin, margin
    return (x, y, x + bw, y + bh)


def choose_logo_placement(
    canvas: Image.Image,
    logo: Image.Image,
    preferred: list[str],
    margin: int,
    padding: int,
) -> tuple[str, bool, tuple[int, int, int, int]]:
    candidates = preferred or ["左上", "右上", "右下", "左下"]
    best: tuple[float, str, bool, tuple[int, int, int, int]] | None = None
    for position in candidates:
        box = placement_box(position, canvas.size, logo.size, margin, padding)
        region = canvas.crop(box)
        mean, variance = luminance_and_variance(region)
        needs_backing = mean < 178 or variance > 850
        score = variance + (120 if needs_backing else 0)
        if best is None or score < best[0]:
            best = (score, position, needs_backing, box)
    assert best is not None
    return best[1], best[2], best[3]


def paste_logo(canvas: Image.Image, logo_path: Path, overlay: dict[str, Any]) -> str:
    if not logo_path.exists():
        raise FileNotFoundError(f"Logo not found: {logo_path}")
    logo = Image.open(logo_path).convert("RGBA")
    logo_width = max(90, min(110, round(canvas.width * 0.085)))
    logo = contain(logo, logo_width)
    margin = max(24, round(canvas.width * 0.027))
    padding_x = round(logo.width * 0.08)
    padding_y = round(logo.height * 0.22)
    preferred = [str(item) for item in overlay.get("preferred_positions", [])]
    position, needs_backing, box = choose_logo_placement(canvas, logo, preferred, margin, max(padding_x, padding_y))
    needs_backing = True

    x1, y1, x2, y2 = box
    x = x1 + max(padding_x, padding_y)
    y = y1 + max(padding_x, padding_y)
    if needs_backing:
        panel = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
        draw = ImageDraw.Draw(panel)
        draw.rectangle((x1, y1, x2, y2), fill=(255, 255, 255, 205))
        canvas.alpha_composite(panel)
        mode = f"white-backed:{position}"
    else:
        mode = f"transparent:{position}"
    canvas.alpha_composite(logo, (x, y))
    return mode


def source_path_for(image: dict[str, Any], draft_dir: Path) -> Path:
    file_name = image["file_name"]
    direct = draft_dir / file_name
    if direct.exists():
        return direct
    stem = Path(file_name).stem
    for suffix in IMAGE_SUFFIXES:
        candidate = draft_dir / f"{stem}{suffix}"
        if candidate.exists():
            return candidate
    return direct


def build_finished_image(
    image: dict[str, Any],
    source: Path,
    output: Path,
    logo_mode: str,
) -> FinishedImage:
    return FinishedImage(
        role=image.get("role", ""),
        file_name=output.name,
        title=image.get("wp_title", ""),
        alt=image.get("alt", ""),
        caption=image.get("caption", ""),
        position=image.get("position", ""),
        size=image.get("size", ""),
        logo_mode=logo_mode,
        source=source,
        output=output,
    )


def finish_image(
    image: dict[str, Any],
    draft_dir: Path,
    final_dir: Path,
    logo_path: Path,
    *,
    dry_run: bool,
) -> FinishedImage:
    source = source_path_for(image, draft_dir)
    if not source.exists():
        raise FileNotFoundError(f"Generated source image is missing: {source}")

    output = final_dir / image["file_name"]
    target_size = parse_size(image.get("size", "1200 x 675"))
    logo_overlay = image.get("logo_overlay", {})
    logo_required = bool(logo_overlay.get("required"))

    if dry_run:
        return build_finished_image(image, source, output, "dry-run-required" if logo_required else "dry-run-none")

    ensure_dir(final_dir)
    canvas = cover(Image.open(source), target_size)
    label_mode = "model-native-text" if image.get("role") == "記事内図解" else "none"
    logo_mode = "none"
    if logo_required:
        overlay_settings = dict(logo_overlay)
        logo_mode = paste_logo(canvas, logo_path, overlay_settings)
    if label_mode != "none":
        logo_mode = f"{logo_mode}; {label_mode}"
    canvas.convert("RGBA").save(output)
    return build_finished_image(image, source, output, logo_mode)


def readme_for(plan: dict[str, Any], finished: list[FinishedImage]) -> str:
    article = plan.get("article", {})
    title = article.get("title", "セイリ部記事")
    lines = [
        f"# {title} 画像",
        "",
        "## 完成画像",
        "",
        "| 用途 | ファイル | サイズ | WordPress画像タイトル | ALT |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in finished:
        lines.append(f"| {item.role} | `{item.file_name}` | {item.size} | {item.title} | {item.alt} |")

    lines.extend(["", "## 設置位置・キャプション", ""])
    for item in finished:
        lines.extend(
            [
                f"### `{item.file_name}`",
                "",
                f"- 設置位置: {item.position or '未指定'}",
                f"- キャプション候補: {item.caption or 'なし'}",
                f"- ロゴ: {item.logo_mode}",
                "",
            ]
        )

    lines.extend(
        [
            "## 運用メモ",
            "",
            "- アイキャッチ素材はCanvaでタイトル、サブタイトル、ロゴを手動仕上げする",
            "- 本文画像・図解はブランド帰属表示としてセイリ部ロゴを合成済み",
            "- WordPressアップロード後、記事本文内のCMSブリーフは削除する",
            "",
        ]
    )
    return "\n".join(lines)


def write_manifest(final_dir: Path, plan_path: Path, finished: list[FinishedImage]) -> None:
    manifest = {
        "plan": str(plan_path),
        "images": [
            {
                "role": item.role,
                "file_name": item.file_name,
                "source": str(item.source),
                "output": str(item.output),
                "logo_mode": item.logo_mode,
                "alt": item.alt,
                "caption": item.caption,
                "position": item.position,
            }
            for item in finished
        ],
    }
    (final_dir / "finish-manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")


def finish_plan(plan_path: Path, *, dry_run: bool = False) -> list[FinishedImage]:
    plan = read_json(plan_path)
    storage = plan.get("engine", {}).get("storage_policy", {})
    draft_dir = project_path(storage.get("draft_dir", ""))
    final_dir = project_path(storage.get("final_dir", ""))
    logo_path = project_path(plan.get("brand", {}).get("logo_path", "")) if plan.get("brand") else DEFAULT_LOGO
    if not logo_path.exists():
        logo_path = DEFAULT_LOGO

    images = [image for image in plan.get("images", []) if image.get("included", True)]
    finished: list[FinishedImage] = []
    missing: list[str] = []
    for image in images:
        try:
            finished.append(finish_image(image, draft_dir, final_dir, logo_path, dry_run=dry_run))
        except FileNotFoundError as exc:
            missing.append(str(exc))

    if missing:
        raise SystemExit("\n".join(missing))

    if not dry_run:
        ensure_dir(final_dir)
        (final_dir / "README.md").write_text(readme_for(plan, finished), encoding="utf-8")
        write_manifest(final_dir, plan_path, finished)
    return finished


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Finish generated Seiribu images from an image-plan JSON.")
    parser.add_argument("plan", type=Path, help="Path to image-plan.json")
    parser.add_argument("--dry-run", action="store_true", help="Check expected generated source paths without writing outputs")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    finished = finish_plan(args.plan, dry_run=args.dry_run)
    action = "Would finish" if args.dry_run else "Finished"
    for item in finished:
        print(f"{action}: {item.source} -> {item.output} ({item.logo_mode})")


if __name__ == "__main__":
    main()
