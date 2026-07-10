from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageFilter


ROOT = Path(__file__).resolve().parents[1]
ASSET_DIR = ROOT / "assets" / "images" / "why-hoard-things"
BRAND_DIR = ROOT / "assets" / "images" / "brand"

SOURCE = ASSET_DIR / "why-hoard-things-boundary-source-v1.png"
LOGO = BRAND_DIR / "seiribu-logo.png"
OUTPUT = ASSET_DIR / "why-hoard-things-inline-boundary-v4.png"

FONT_DIR = Path("/Users/dvcong/Library/Fonts")
BOLD_FONT = FONT_DIR / "NotoSansJP-Bold.ttf"
MEDIUM_FONT = FONT_DIR / "NotoSansJP-Medium.ttf"
REGULAR_FONT = FONT_DIR / "NotoSansJP-Regular.ttf"

W, H = 1200, 800


def font(path: Path, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(path), size=size)


def text_size(draw: ImageDraw.ImageDraw, text: str, fnt: ImageFont.FreeTypeFont) -> tuple[int, int]:
    box = draw.textbbox((0, 0), text, font=fnt)
    return box[2] - box[0], box[3] - box[1]


def fit_font(path: Path, text: str, max_width: int, start: int, minimum: int) -> ImageFont.FreeTypeFont:
    probe = Image.new("RGBA", (10, 10))
    draw = ImageDraw.Draw(probe)
    for size in range(start, minimum - 1, -1):
        fnt = font(path, size)
        width, _ = text_size(draw, text, fnt)
        if width <= max_width:
            return fnt
    return font(path, minimum)


def draw_centered(
    draw: ImageDraw.ImageDraw,
    text: str,
    y: int,
    fnt: ImageFont.FreeTypeFont,
    fill: tuple[int, int, int],
    x_center: int = W // 2,
) -> None:
    width, _ = text_size(draw, text, fnt)
    draw.text((x_center - width // 2, y), text, font=fnt, fill=fill)


def rounded_layer(size: tuple[int, int]) -> tuple[Image.Image, ImageDraw.ImageDraw]:
    layer = Image.new("RGBA", size, (0, 0, 0, 0))
    return layer, ImageDraw.Draw(layer)


def draw_label(
    base: Image.Image,
    x: int,
    y: int,
    w: int,
    h: int,
    number: str,
    title: str,
    body: str,
    color: tuple[int, int, int],
) -> None:
    layer, draw = rounded_layer((W, H))

    shadow = Image.new("RGBA", (w + 20, h + 20), (0, 0, 0, 0))
    sd = ImageDraw.Draw(shadow)
    sd.rounded_rectangle((10, 10, w + 10, h + 10), radius=24, fill=(33, 37, 41, 62))
    shadow = shadow.filter(ImageFilter.GaussianBlur(10))
    layer.alpha_composite(shadow, (x - 10, y - 4))

    draw.rounded_rectangle((x, y, x + w, y + h), radius=22, fill=(255, 255, 255, 232))
    draw.rounded_rectangle((x, y, x + w, y + h), radius=22, outline=(*color, 190), width=3)
    draw.rounded_rectangle((x, y, x + 12, y + h), radius=8, fill=(*color, 230))

    cx, cy = x + 38, y + 40
    draw.ellipse((cx - 22, cy - 22, cx + 22, cy + 22), fill=(*color, 255))
    num_font = font(BOLD_FONT, 23)
    nw, nh = text_size(draw, number, num_font)
    draw.text((cx - nw / 2, cy - nh / 2 - 2), number, font=num_font, fill=(255, 255, 255))

    title_font = fit_font(BOLD_FONT, title, w - 86, 22, 18)
    body_font = fit_font(MEDIUM_FONT, body, w - 86, 18, 15)
    draw.text((x + 72, y + 19), title, font=title_font, fill=(38, 45, 52))
    draw.text((x + 72, y + 52), body, font=body_font, fill=(78, 84, 90))

    base.alpha_composite(layer)


def add_logo(base: Image.Image) -> None:
    logo = Image.open(LOGO).convert("RGBA")
    logo_w = 132
    logo_h = round(logo.height * logo_w / logo.width)
    logo = logo.resize((logo_w, logo_h), Image.Resampling.LANCZOS)
    base.alpha_composite(logo, (50, 34))


def main() -> None:
    src = Image.open(SOURCE).convert("RGBA")
    canvas = src.resize((W, H), Image.Resampling.LANCZOS)
    draw = ImageDraw.Draw(canvas)

    add_logo(canvas)

    title = "境界線は「物の量」ではなく生活への影響"
    subtitle = "共有スペースや生活動線に支障が出たら、相談を検討する目安です"

    title_font = fit_font(BOLD_FONT, title, 780, 42, 34)
    subtitle_font = fit_font(REGULAR_FONT, subtitle, 790, 23, 18)
    draw_centered(draw, title, 48, title_font, (43, 50, 62), x_center=646)
    draw_centered(draw, subtitle, 105, subtitle_font, (84, 92, 101), x_center=646)

    labels = [
        (42, 216, "1", "価値観の範囲", "本人の領域で管理できている", (111, 151, 89)),
        (439, 216, "2", "注意ゾーン", "共有スペースに広がり始める", (218, 160, 62)),
        (836, 216, "3", "相談を検討", "生活動線や安全に支障が出る", (218, 104, 82)),
    ]
    for x, y, number, title, body, color in labels:
        draw_label(canvas, x, y, 324, 92, number, title, body, color)

    note = "見るポイント：物の多さそのものではなく、生活・安全・家族関係への影響"
    note_font = fit_font(MEDIUM_FONT, note, 820, 20, 16)
    nw, nh = text_size(draw, note, note_font)
    note_x = (W - nw) // 2
    note_y = 724
    pad_x, pad_y = 22, 12
    draw.rounded_rectangle(
        (note_x - pad_x, note_y - pad_y, note_x + nw + pad_x, note_y + nh + pad_y + 2),
        radius=20,
        fill=(255, 255, 255, 218),
        outline=(222, 215, 205, 185),
        width=2,
    )
    draw.text((note_x, note_y), note, font=note_font, fill=(63, 70, 77))

    canvas.convert("RGB").save(OUTPUT, quality=95)
    print(OUTPUT)


if __name__ == "__main__":
    main()
