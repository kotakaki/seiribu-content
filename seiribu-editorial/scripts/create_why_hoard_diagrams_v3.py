#!/usr/bin/env python3
"""Create polished v3 diagrams for the why-hoard-things article."""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "assets" / "images" / "why-hoard-things"
LOGO = ROOT / "assets" / "images" / "brand" / "seiribu-logo.png"
FONT_DIR = Path("/Users/dvcong/Library/Fonts")
FONT_REGULAR = FONT_DIR / "NotoSansJP-Regular.ttf"
FONT_BOLD = FONT_DIR / "NotoSansJP-Bold.ttf"
FONT_MEDIUM = FONT_DIR / "NotoSansJP-Medium.ttf"

SCALE = 2
W, H = 1200 * SCALE, 800 * SCALE

COLORS = {
    "cream": "#FBF6EF",
    "cream2": "#FFFDF8",
    "ink": "#24304A",
    "muted": "#5F6675",
    "burgundy": "#7A3454",
    "blue": "#2F5EAE",
    "salmon": "#EE7464",
    "orange": "#F6C47B",
    "green": "#86C79D",
    "teal": "#78C7C0",
    "purple": "#A989C9",
    "line": "#D8D1C8",
    "green_soft": "#EAF7EF",
    "yellow_soft": "#FFF4D8",
    "red_soft": "#FCE9E6",
    "blue_soft": "#EAF1FB",
    "purple_soft": "#F2ECFA",
}


def s(value: int | float) -> int:
    return int(round(value * SCALE))


def font(size: int, weight: str = "regular") -> ImageFont.FreeTypeFont:
    path = FONT_BOLD if weight == "bold" else FONT_MEDIUM if weight == "medium" else FONT_REGULAR
    return ImageFont.truetype(str(path), size=s(size))


def new_canvas(bg: str = "#FBF6EF") -> Image.Image:
    return Image.new("RGBA", (W, H), bg)


def downsample(img: Image.Image) -> Image.Image:
    return img.resize((1200, 800), Image.LANCZOS).convert("RGB")


def text_box(draw: ImageDraw.ImageDraw, text: str, fnt: ImageFont.FreeTypeFont) -> tuple[int, int]:
    box = draw.textbbox((0, 0), text, font=fnt)
    return box[2] - box[0], box[3] - box[1]


def center_text(draw: ImageDraw.ImageDraw, x: int, y: int, text: str, fnt: ImageFont.FreeTypeFont, fill: str) -> None:
    w, h = text_box(draw, text, fnt)
    draw.text((x - w / 2, y - h / 2), text, font=fnt, fill=fill)


def left_text(draw: ImageDraw.ImageDraw, x: int, y: int, text: str, fnt: ImageFont.FreeTypeFont, fill: str) -> None:
    draw.text((x, y), text, font=fnt, fill=fill)


def shadowed_round(
    base: Image.Image,
    box: tuple[int, int, int, int],
    fill: str,
    outline: str | None = None,
    radius: int = 24,
    shadow: bool = True,
    width: int = 2,
) -> None:
    if shadow:
        shadow_layer = Image.new("RGBA", base.size, (0, 0, 0, 0))
        sd = ImageDraw.Draw(shadow_layer)
        offset = s(8)
        sd.rounded_rectangle(
            (box[0] + offset, box[1] + offset, box[2] + offset, box[3] + offset),
            radius=s(radius),
            fill=(74, 60, 46, 28),
        )
        shadow_layer = shadow_layer.filter(ImageFilter.GaussianBlur(s(8)))
        base.alpha_composite(shadow_layer)
    draw = ImageDraw.Draw(base)
    draw.rounded_rectangle(box, radius=s(radius), fill=fill, outline=outline, width=s(width))


def paste_logo(img: Image.Image, width: int = 150, corner: str = "bottom-right") -> None:
    if not LOGO.exists():
        return
    logo = Image.open(LOGO).convert("RGBA")
    target_w = s(width)
    ratio = target_w / logo.width
    logo = logo.resize((target_w, int(logo.height * ratio)), Image.LANCZOS)
    if corner == "bottom-right":
        x = W - target_w - s(42)
        y = H - logo.height - s(32)
    else:
        x, y = s(42), s(32)
    img.alpha_composite(logo, (x, y))


def header(draw: ImageDraw.ImageDraw, title: str, subtitle: str = "") -> None:
    center_text(draw, s(600), s(58), title, font(34, "bold"), COLORS["ink"])
    if subtitle:
        center_text(draw, s(600), s(108), subtitle, font(21), COLORS["muted"])


def icon_box(draw: ImageDraw.ImageDraw, cx: int, cy: int, color: str, label: str) -> None:
    draw.rounded_rectangle((cx - s(31), cy - s(31), cx + s(31), cy + s(31)), radius=s(18), fill=color)
    center_text(draw, cx, cy - s(1), label, font(25, "bold"), "#FFFFFF")


def curved_line(draw: ImageDraw.ImageDraw, start: tuple[int, int], end: tuple[int, int], fill: str) -> None:
    draw.line((*start, *end), fill=fill, width=s(4))


def card_with_badge(
    img: Image.Image,
    box: tuple[int, int, int, int],
    title: str,
    desc: str,
    accent: str,
    badge: str,
) -> None:
    shadowed_round(img, box, "#FFFFFF", "#DED8CF", 22, True, 2)
    draw = ImageDraw.Draw(img)
    x1, y1, x2, _ = box
    icon_box(draw, x1 + s(58), y1 + s(58), accent, badge)
    left_text(draw, x1 + s(108), y1 + s(32), title, font(25, "bold"), COLORS["ink"])
    left_text(draw, x1 + s(108), y1 + s(74), desc, font(19), COLORS["muted"])


def make_psychology_v3() -> Path:
    img = new_canvas()
    draw = ImageDraw.Draw(img)
    header(draw, "物を捨てられない心理に隠された5つの理由", "責める前に、背景にある気持ちを整理する")

    # Soft background blob.
    draw.ellipse((s(382), s(234), s(818), s(574)), fill="#FFF1D8", outline="#E4D4BB", width=s(2))
    center = (s(600), s(405))
    cards = [
        ((s(74), s(165), s(430), s(288)), "損失回避", "捨てたら損するかも", COLORS["salmon"], "損", (s(430), s(226))),
        ((s(770), s(165), s(1126), s(288)), "拡張自己", "物は自分の一部", COLORS["blue"], "拡", (s(770), s(226))),
        ((s(74), s(492), s(430), s(615)), "アニミズム", "物に魂が宿る", COLORS["purple"], "魂", (s(430), s(553))),
        ((s(770), s(492), s(1126), s(615)), "判断疲れ", "決める気力がない", COLORS["orange"], "判", (s(770), s(553))),
        ((s(422), s(610), s(778), s(733)), "孤独感・不安", "物に囲まれると安心", COLORS["green"], "安", (s(600), s(610))),
    ]
    for _, _, _, _, _, anchor in cards:
        curved_line(draw, center, anchor, "#D8D1C8")

    shadowed_round(img, (s(420), s(290), s(780), s(520)), "#FFFFFF", "#D6CEC3", 115, True, 3)
    draw = ImageDraw.Draw(img)
    center_text(draw, s(600), s(376), "物を", font(35, "bold"), COLORS["burgundy"])
    center_text(draw, s(600), s(430), "捨てられない", font(35, "bold"), COLORS["burgundy"])

    for box, title, desc, accent, badge, _ in cards:
        card_with_badge(img, box, title, desc, accent, badge)

    paste_logo(img)
    out = OUT_DIR / "why-hoard-things-inline-psychology-v3.png"
    downsample(img).save(out, quality=95)
    return out


def make_spectrum_v3() -> Path:
    img = new_canvas("#F7FAF7")
    draw = ImageDraw.Draw(img)
    header(draw, "「物の多さ」より、生活への影響で見る", "不安をあおらず、相談の目安を段階で整理する")

    zones = [
        ("01", "個人の価値観の範囲", ["趣味の部屋に物が多い", "共有スペースは整理", "本人も家族も困っていない"], COLORS["green_soft"], "#579872"),
        ("02", "注意ゾーン", ["共有スペースに侵食", "家族が困り始めている", "話し合いが必要"], COLORS["yellow_soft"], "#C8912F"),
        ("03", "専門家への相談を検討", ["生活動線がふさがる", "料理・入浴・睡眠に支障", "強い不安やパニック"], COLORS["red_soft"], "#D46358"),
    ]
    xs = [s(72), s(430), s(788)]
    for x, (num, title, items, fill, accent) in zip(xs, zones):
        box = (x, s(190), x + s(340), s(580))
        shadowed_round(img, box, fill, accent, 28, True, 3)
        draw = ImageDraw.Draw(img)
        draw.rounded_rectangle((x + s(28), s(218), x + s(88), s(278)), radius=s(18), fill=accent)
        center_text(draw, x + s(58), s(248), num, font(22, "bold"), "#FFFFFF")
        left_text(draw, x + s(108), s(220), title, font(25, "bold"), COLORS["ink"])
        y = s(322)
        for item in items:
            draw.ellipse((x + s(42), y + s(9), x + s(56), y + s(23)), fill=accent)
            left_text(draw, x + s(78), y, item, font(20), COLORS["ink"])
            y += s(55)

    # Severity meter.
    draw.rounded_rectangle((s(118), s(632), s(1082), s(674)), radius=s(21), fill="#E5E2DA")
    draw.rounded_rectangle((s(118), s(632), s(500), s(674)), radius=s(21), fill="#87C9A0")
    draw.rectangle((s(490), s(632), s(808), s(674)), fill="#F3C869")
    draw.rounded_rectangle((s(792), s(632), s(1082), s(674)), radius=s(21), fill="#EA8178")
    left_text(draw, s(126), s(704), "軽い", font(22, "bold"), "#579872")
    left_text(draw, s(1018), s(704), "重い", font(22, "bold"), "#D46358")
    draw.line((s(188), s(718), s(1000), s(718)), fill="#AAB7B3", width=s(4))
    draw.polygon([(s(1000), s(718)), (s(980), s(706)), (s(980), s(730))], fill="#AAB7B3")

    paste_logo(img)
    out = OUT_DIR / "why-hoard-things-inline-spectrum-v3.png"
    downsample(img).save(out, quality=95)
    return out


def make_ng_ok_v3() -> Path:
    img = new_canvas()
    draw = ImageDraw.Draw(img)
    header(draw, "「捨てて」ではなく「選んで」に変える", "相手の物を否定せず、本人が選べる形にする")

    shadowed_round(img, (s(70), s(168), s(552), s(635)), COLORS["red_soft"], "#E28C86", 30, True, 3)
    shadowed_round(img, (s(648), s(168), s(1130), s(635)), COLORS["green_soft"], "#74B78C", 30, True, 3)
    draw = ImageDraw.Draw(img)
    center_text(draw, s(311), s(224), "NG対応", font(32, "bold"), "#C84F48")
    center_text(draw, s(889), s(224), "OK対応", font(32, "bold"), "#388B5F")
    draw.line((s(570), s(420), s(630), s(420)), fill=COLORS["burgundy"], width=s(5))
    draw.polygon([(s(630), s(420)), (s(612), s(408)), (s(612), s(432))], fill=COLORS["burgundy"])

    ng_items = ["勝手に捨てる", "責める", "他人と比較する"]
    ok_items = ["「選んで」と聞く", "保留箱を使う", "聖域ルールを作る", "売る・譲る出口を示す"]
    y = s(300)
    for item in ng_items:
        draw.ellipse((s(130), y - s(8), s(178), y + s(40)), fill="#C84F48")
        center_text(draw, s(154), y + s(16), "×", font(27, "bold"), "#FFFFFF")
        left_text(draw, s(210), y, item, font(28, "bold"), COLORS["ink"])
        y += s(92)

    y = s(288)
    for item in ok_items:
        draw.ellipse((s(700), y - s(6), s(748), y + s(42)), fill="#388B5F")
        center_text(draw, s(724), y + s(18), "○", font(24, "bold"), "#FFFFFF")
        left_text(draw, s(780), y, item, font(26, "bold"), COLORS["ink"])
        y += s(78)

    draw.rounded_rectangle((s(360), s(680), s(840), s(732)), radius=s(26), fill="#FFFFFF", outline="#D6CEC3", width=s(2))
    center_text(draw, s(600), s(706), "目標は「捨てさせる」ではなく「自分で選べた」状態", font(19, "bold"), COLORS["burgundy"])
    paste_logo(img)
    out = OUT_DIR / "why-hoard-things-inline-ng-ok-v3.png"
    downsample(img).save(out, quality=95)
    return out


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for path in [make_psychology_v3(), make_spectrum_v3(), make_ng_ok_v3()]:
        print(f"Wrote {path}")


if __name__ == "__main__":
    main()
