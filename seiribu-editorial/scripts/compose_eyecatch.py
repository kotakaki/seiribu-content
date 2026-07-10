#!/usr/bin/env python3
"""Compose a finished Seiribu eyecatch locally without Canva access."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
PROJECT_ROOT = ROOT.parent
DEFAULT_CONFIG = ROOT / "config" / "image-engine.json"
DEFAULT_FONT_DIR = Path("/Users/dvcong/Library/Fonts")
DEFAULT_BOLD_FONT = DEFAULT_FONT_DIR / "NotoSansJP-Bold.ttf"
DEFAULT_REGULAR_FONT = DEFAULT_FONT_DIR / "NotoSansJP-Regular.ttf"

W, H = 1200, 630


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def project_path(value: str | Path) -> Path:
    path = Path(value)
    return path if path.is_absolute() else PROJECT_ROOT / path


def hex_color(value: str, alpha: int = 255) -> tuple[int, int, int, int]:
    clean = value.strip().lstrip("#")
    if len(clean) != 6:
        raise ValueError(f"Unsupported color: {value}")
    return tuple(int(clean[i : i + 2], 16) for i in (0, 2, 4)) + (alpha,)


def load_font(path: Path, size: int) -> ImageFont.FreeTypeFont:
    if not path.exists():
        raise FileNotFoundError(f"Font not found: {path}")
    return ImageFont.truetype(str(path), size=size)


def text_width(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.FreeTypeFont) -> int:
    box = draw.textbbox((0, 0), text, font=font)
    return box[2] - box[0]


def text_height(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.FreeTypeFont) -> int:
    box = draw.textbbox((0, 0), text, font=font)
    return box[3] - box[1]


def wrap_text(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.FreeTypeFont, max_width: int) -> list[str]:
    lines: list[str] = []
    current = ""
    for char in text:
        trial = current + char
        if current and text_width(draw, trial, font) > max_width:
            lines.append(current)
            current = char
        else:
            current = trial
    if current:
        lines.append(current)
    return lines


def fit_lines(
    draw: ImageDraw.ImageDraw,
    text: str,
    font_path: Path,
    max_width: int,
    max_lines: int,
    start: int,
    minimum: int,
) -> tuple[ImageFont.FreeTypeFont, list[str]]:
    for size in range(start, minimum - 1, -1):
        font = load_font(font_path, size)
        lines = wrap_text(draw, text, font, max_width)
        if len(lines) <= max_lines:
            return font, lines

    font = load_font(font_path, minimum)
    lines = wrap_text(draw, text, font, max_width)
    if len(lines) > max_lines:
        kept = lines[: max_lines - 1]
        tail = "".join(lines[max_lines - 1 :])
        kept.append(tail)
        lines = kept
    return font, lines


def draw_centered_lines(
    draw: ImageDraw.ImageDraw,
    lines: list[str],
    font: ImageFont.FreeTypeFont,
    y: int,
    fill: tuple[int, int, int, int],
    max_line_height: int,
    x_center: int = W // 2,
) -> int:
    cursor = y
    for line in lines:
        box = draw.textbbox((0, 0), line, font=font)
        width = box[2] - box[0]
        height = box[3] - box[1]
        draw.text((x_center - width / 2, cursor), line, font=font, fill=fill)
        cursor += max(max_line_height, height + 12)
    return cursor


def cover(src: Image.Image, size: tuple[int, int]) -> Image.Image:
    src = src.convert("RGBA")
    sw, sh = src.size
    tw, th = size
    scale = max(tw / sw, th / sh)
    resized = src.resize((round(sw * scale), round(sh * scale)), Image.Resampling.LANCZOS)
    left = (resized.width - tw) // 2
    top = (resized.height - th) // 2
    return resized.crop((left, top, left + tw, top + th))


def contain(src: Image.Image, box: tuple[int, int]) -> Image.Image:
    src = src.convert("RGBA")
    bw, bh = box
    scale = min(bw / src.width, bh / src.height)
    return src.resize((round(src.width * scale), round(src.height * scale)), Image.Resampling.LANCZOS)


def has_meaningful_alpha(src: Image.Image) -> bool:
    if src.mode != "RGBA":
        return False
    alpha = src.getchannel("A")
    extrema = alpha.getextrema()
    return extrema[0] < 250


def make_background(config: dict[str, Any]) -> Image.Image:
    composition = config.get("local_composition", {})
    bg = hex_color(composition.get("background", "#FAF3EA"))
    canvas = Image.new("RGBA", (W, H), bg)
    draw = ImageDraw.Draw(canvas)
    draw.rectangle((0, 478, W, H), fill=(238, 249, 244, 170))
    draw.rectangle((0, 0, W, 10), fill=(122, 52, 84, 28))
    return canvas


def paste_logo(canvas: Image.Image, config: dict[str, Any]) -> None:
    composition = config.get("local_composition", {})
    logo_path = project_path(config.get("logo_path", ""))
    if not logo_path.exists():
        raise FileNotFoundError(f"Logo not found: {logo_path}")
    logo = Image.open(logo_path).convert("RGBA")
    width = int(composition.get("logo_width", 160))
    height = round(logo.height * width / logo.width)
    logo = logo.resize((width, height), Image.Resampling.LANCZOS)
    canvas.alpha_composite(logo, (56, 44))


def draw_text_block(canvas: Image.Image, title: str, subtitle: str, config: dict[str, Any], source_layout: str) -> None:
    composition = config.get("local_composition", {})
    draw = ImageDraw.Draw(canvas)
    title_color = hex_color(composition.get("title_color", "#7A3454"))
    subtitle_color = hex_color(composition.get("subtitle_color", "#24304A"))

    if source_layout == "background":
        panel = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
        pd = ImageDraw.Draw(panel)
        pd.rounded_rectangle((256, 154, 944, 312), radius=0, fill=(250, 243, 234, 214))
        canvas.alpha_composite(panel)

    title_font, title_lines = fit_lines(draw, title, DEFAULT_BOLD_FONT, 760, 2, 52, 34)
    subtitle_font, subtitle_lines = fit_lines(draw, subtitle, DEFAULT_REGULAR_FONT, 780, 2, 26, 18)

    title_line_height = text_height(draw, "実家", title_font) + 16
    title_y = 176 if len(title_lines) == 1 else 158
    next_y = draw_centered_lines(draw, title_lines, title_font, title_y, title_color, title_line_height)
    subtitle_y = next_y + 10
    subtitle_line_height = text_height(draw, "実家", subtitle_font) + 10
    draw_centered_lines(draw, subtitle_lines, subtitle_font, subtitle_y, subtitle_color, subtitle_line_height)


def paste_source(canvas: Image.Image, source: Path | None, source_layout: str) -> str:
    if not source:
        return "none"
    if not source.exists():
        raise FileNotFoundError(f"Source image not found: {source}")

    raw = Image.open(source).convert("RGBA")
    layout = source_layout
    if layout == "auto":
        layout = "cutout" if has_meaningful_alpha(raw) else "background"

    if layout == "background":
        base = cover(raw, (W, H))
        tint = Image.new("RGBA", (W, H), (250, 243, 234, 70))
        canvas.alpha_composite(base)
        canvas.alpha_composite(tint)
        return layout

    visual = contain(raw, (730, 340))
    x = (W - visual.width) // 2
    y = H - visual.height - 28
    canvas.alpha_composite(visual, (x, y))
    return "cutout"


def compose(
    title: str,
    subtitle: str,
    output: Path,
    config: dict[str, Any],
    source: Path | None = None,
    source_layout: str = "auto",
) -> Path:
    canvas = make_background(config)
    resolved_layout = paste_source(canvas, source, source_layout)
    paste_logo(canvas, config)
    draw_text_block(canvas, title, subtitle, config, resolved_layout)
    output.parent.mkdir(parents=True, exist_ok=True)
    if output.suffix.lower() == ".webp":
        canvas.convert("RGB").save(output, quality=92, method=6)
    else:
        canvas.convert("RGB").save(output, quality=95)
    return output


def first_eyecatch(plan: dict[str, Any]) -> dict[str, Any]:
    for image in plan.get("images", []):
        if image.get("role") in {"アイキャッチ", "アイキャッチ素材"}:
            return image
    raise ValueError("Plan does not contain an eyecatch image.")


def parse_size(value: str) -> tuple[int, int]:
    parts = [p.strip() for p in value.lower().replace("×", "x").split("x")]
    if len(parts) != 2:
        return W, H
    return int(parts[0]), int(parts[1])


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Compose a finished Seiribu eyecatch locally.")
    parser.add_argument("--config", type=Path, default=DEFAULT_CONFIG)
    parser.add_argument("--plan", type=Path, help="Image plan JSON. Uses the first eyecatch brief.")
    parser.add_argument("--source", type=Path, help="Generated visual material to place into the eyecatch.")
    parser.add_argument("--source-layout", choices=["auto", "background", "cutout"], default="auto")
    parser.add_argument("--title", help="Eyecatch title. Overrides plan title.")
    parser.add_argument("--subtitle", help="Eyecatch subtitle. Overrides plan subtitle.")
    parser.add_argument("--output", type=Path, help="Output image path.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    config = read_json(args.config)
    title = args.title
    subtitle = args.subtitle
    output = args.output

    if args.plan:
        plan = read_json(args.plan)
        image = first_eyecatch(plan)
        local = image.get("local_composition") or image.get("canva_instructions", {})
        title = title or local.get("title") or plan.get("article", {}).get("title", "")
        subtitle = subtitle or local.get("subtitle") or ""
        output = output or project_path(f"seiribu-editorial/assets/images/{plan['article']['slug']}/{image['file_name']}")

    if not title:
        raise ValueError("--title or --plan is required")
    if subtitle is None:
        subtitle = ""
    if not output:
        raise ValueError("--output is required when --plan is not used")

    configured_size = parse_size(config.get("local_composition", {}).get("eyecatch_output_size", f"{W} x {H}"))
    if configured_size != (W, H):
        raise ValueError(f"compose_eyecatch.py currently supports {W} x {H}, got {configured_size}")

    written = compose(title, subtitle, output, config, args.source, args.source_layout)
    print(f"Wrote {written}")


if __name__ == "__main__":
    main()
