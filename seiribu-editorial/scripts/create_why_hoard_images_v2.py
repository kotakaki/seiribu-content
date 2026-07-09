#!/usr/bin/env python3
"""Compose higher-quality v2 images for why-hoard-things from generated art."""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "assets" / "images" / "why-hoard-things"
LOGO = ROOT / "assets" / "images" / "brand" / "seiribu-logo.png"
FONT_DIR = Path("/Users/dvcong/Library/Fonts")
FONT_REGULAR = FONT_DIR / "NotoSansJP-Regular.ttf"
FONT_BOLD = FONT_DIR / "NotoSansJP-Bold.ttf"

INK = "#24304A"
BURGUNDY = "#7A3454"
CREAM = "#F8F1E9"
MINT = "#EEF9F4"


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(FONT_BOLD if bold else FONT_REGULAR), size=size)


def text_size(draw: ImageDraw.ImageDraw, text: str, fnt: ImageFont.FreeTypeFont) -> tuple[int, int]:
    box = draw.textbbox((0, 0), text, font=fnt)
    return box[2] - box[0], box[3] - box[1]


def center_text(draw: ImageDraw.ImageDraw, x: int, y: int, text: str, fnt: ImageFont.FreeTypeFont, fill: str) -> None:
    w, h = text_size(draw, text, fnt)
    draw.text((x - w / 2, y - h / 2), text, font=fnt, fill=fill)


def paste_logo(img: Image.Image, width: int = 160, x: int = 44, y: int = 34) -> None:
    if not LOGO.exists():
        return
    logo = Image.open(LOGO).convert("RGBA")
    ratio = width / logo.width
    logo = logo.resize((width, int(logo.height * ratio)), Image.LANCZOS)
    img.alpha_composite(logo, (x, y))


def cover_image(src: Image.Image, size: tuple[int, int]) -> Image.Image:
    src = src.convert("RGB")
    sw, sh = src.size
    tw, th = size
    scale = max(tw / sw, th / sh)
    resized = src.resize((int(sw * scale), int(sh * scale)), Image.LANCZOS)
    left = (resized.width - tw) // 2
    top = (resized.height - th) // 2
    return resized.crop((left, top, left + tw, top + th)).convert("RGBA")


def make_eyecatch(source: Path) -> Path:
    base = cover_image(Image.open(source), (1200, 630))
    overlay = Image.new("RGBA", base.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(overlay)
    draw.rectangle((0, 0, 1200, 630), fill=(248, 241, 233, 38))
    draw.rectangle((104, 92, 665, 264), fill=(248, 241, 233, 196))
    img = Image.alpha_composite(base, overlay)
    draw = ImageDraw.Draw(img)
    paste_logo(img, 150, 44, 34)
    center_text(draw, 385, 137, "物を捨てられない", font(42, True), BURGUNDY)
    center_text(draw, 385, 188, "人の心理とは？", font(42, True), BURGUNDY)
    center_text(draw, 385, 238, "夫や父親など男性に多い理由と接し方", font(23), INK)
    out = OUT_DIR / "why-hoard-things-eyecatch-v2.png"
    img.convert("RGB").save(out, quality=95)
    return out


def make_memory(source: Path) -> Path:
    img = cover_image(Image.open(source), (1200, 800))
    tint = Image.new("RGBA", img.size, (238, 249, 244, 24))
    img = Image.alpha_composite(img, tint)
    draw = ImageDraw.Draw(img)
    draw.rounded_rectangle((135, 32, 1065, 114), radius=0, fill=(238, 249, 244, 220))
    center_text(draw, 600, 72, "物には、言葉にできない感情が託されている", font(35, True), INK)
    paste_logo(img, 150, 1004, 734)
    out = OUT_DIR / "why-hoard-things-inline-male-memory-v2.png"
    img.convert("RGB").save(out, quality=95)
    return out


def make_diagram_polish(source: Path, output: str) -> Path:
    img = Image.open(source).convert("RGBA")
    enhancer = ImageEnhance.Contrast(img.convert("RGB"))
    img = enhancer.enhance(1.04).convert("RGBA")
    out = OUT_DIR / output
    img.convert("RGB").save(out, quality=95)
    return out


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Compose v2 article images.")
    parser.add_argument("--eyecatch-source", required=True, type=Path)
    parser.add_argument("--memory-source", required=True, type=Path)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    paths = [
        make_eyecatch(args.eyecatch_source),
        make_memory(args.memory_source),
        make_diagram_polish(OUT_DIR / "why-hoard-things-inline-psychology.png", "why-hoard-things-inline-psychology-v2.png"),
        make_diagram_polish(OUT_DIR / "why-hoard-things-inline-spectrum.png", "why-hoard-things-inline-spectrum-v2.png"),
        make_diagram_polish(OUT_DIR / "why-hoard-things-inline-ng-ok.png", "why-hoard-things-inline-ng-ok-v2.png"),
    ]
    for path in paths:
        print(f"Wrote {path}")


if __name__ == "__main__":
    main()
