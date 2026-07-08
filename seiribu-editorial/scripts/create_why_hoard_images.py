#!/usr/bin/env python3
"""Create article images for the why-hoard-things article."""

from __future__ import annotations

import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "assets" / "images" / "why-hoard-things"
LOGO = ROOT / "assets" / "images" / "brand" / "seiribu-logo.png"
FONT_DIR = Path("/Users/dvcong/Library/Fonts")
FONT_REGULAR = FONT_DIR / "NotoSansJP-Regular.ttf"
FONT_BOLD = FONT_DIR / "NotoSansJP-Bold.ttf"
FONT_MEDIUM = FONT_DIR / "NotoSansJP-Medium.ttf"


COLORS = {
    "cream": "#F8F1E9",
    "mint": "#EEF9F4",
    "light": "#FFFCF7",
    "ink": "#24304A",
    "muted": "#5F6675",
    "blue": "#2F5EAE",
    "burgundy": "#7A3454",
    "salmon": "#EE7464",
    "orange": "#F6C47B",
    "yellow": "#FFE6A8",
    "green": "#87C7A2",
    "teal": "#7FC7C2",
    "purple": "#A988C8",
    "gray": "#DCE3E0",
    "line": "#D8D1C8",
    "red_soft": "#FCE9E6",
    "green_soft": "#EAF7EF",
}


def font(size: int, weight: str = "regular") -> ImageFont.FreeTypeFont:
    path = FONT_BOLD if weight == "bold" else FONT_MEDIUM if weight == "medium" else FONT_REGULAR
    return ImageFont.truetype(str(path), size=size)


def text_size(draw: ImageDraw.ImageDraw, text: str, fnt: ImageFont.FreeTypeFont) -> tuple[int, int]:
    box = draw.textbbox((0, 0), text, font=fnt)
    return box[2] - box[0], box[3] - box[1]


def draw_center(draw: ImageDraw.ImageDraw, xy: tuple[int, int], text: str, fnt: ImageFont.FreeTypeFont, fill: str) -> None:
    x, y = xy
    w, h = text_size(draw, text, fnt)
    draw.text((x - w / 2, y - h / 2), text, font=fnt, fill=fill)


def wrap_text(draw: ImageDraw.ImageDraw, text: str, fnt: ImageFont.FreeTypeFont, max_width: int) -> list[str]:
    lines: list[str] = []
    current = ""
    for char in text:
        candidate = current + char
        if char == "\n":
            lines.append(current)
            current = ""
            continue
        if text_size(draw, candidate, fnt)[0] <= max_width or not current:
            current = candidate
        else:
            lines.append(current)
            current = char
    if current:
        lines.append(current)
    return lines


def draw_multiline_center(
    draw: ImageDraw.ImageDraw,
    center_x: int,
    top: int,
    text: str,
    fnt: ImageFont.FreeTypeFont,
    fill: str,
    max_width: int,
    leading: int = 8,
) -> int:
    lines = wrap_text(draw, text, fnt, max_width)
    y = top
    for line in lines:
        w, h = text_size(draw, line, fnt)
        draw.text((center_x - w / 2, y), line, font=fnt, fill=fill)
        y += h + leading
    return y


def rounded(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], fill: str, outline: str | None = None, radius: int = 24, width: int = 2) -> None:
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def paste_logo(img: Image.Image, width: int = 160, position: str = "top-left") -> None:
    if not LOGO.exists():
        return
    logo = Image.open(LOGO).convert("RGBA")
    ratio = width / logo.width
    logo = logo.resize((width, int(logo.height * ratio)), Image.LANCZOS)
    if position == "bottom-right":
        x = img.width - width - 42
        y = img.height - logo.height - 32
    else:
        x = 44
        y = 34
    img.alpha_composite(logo, (x, y))


def draw_person(draw: ImageDraw.ImageDraw, x: int, y: int, scale: float, shirt: str, hair: str, pose: str = "neutral") -> None:
    head = int(58 * scale)
    body_w = int(100 * scale)
    body_h = int(138 * scale)
    skin = "#F2B08F"
    pants = "#6E8DB5"
    draw.ellipse((x - head // 2, y - head, x + head // 2, y), fill=skin, outline="#A66D59", width=max(1, int(2 * scale)))
    draw.pieslice((x - head // 2 - 5, y - head - 8, x + head // 2 + 5, y + 8), 180, 360, fill=hair)
    draw.ellipse((x - int(18 * scale), y - int(35 * scale), x - int(12 * scale), y - int(29 * scale)), fill="#40312F")
    draw.ellipse((x + int(12 * scale), y - int(35 * scale), x + int(18 * scale), y - int(29 * scale)), fill="#40312F")
    draw.arc((x - int(16 * scale), y - int(24 * scale), x + int(16 * scale), y - int(5 * scale)), 20, 160, fill="#875C51", width=max(1, int(2 * scale)))
    rounded(draw, (x - body_w // 2, y + 4, x + body_w // 2, y + body_h), shirt, radius=int(28 * scale))
    draw.rectangle((x - int(42 * scale), y + body_h, x - int(6 * scale), y + body_h + int(90 * scale)), fill=pants)
    draw.rectangle((x + int(6 * scale), y + body_h, x + int(42 * scale), y + body_h + int(90 * scale)), fill=pants)
    if pose == "arms-crossed":
        draw.line((x - int(58 * scale), y + int(50 * scale), x + int(28 * scale), y + int(88 * scale)), fill="#A65F4C", width=int(9 * scale))
        draw.line((x + int(58 * scale), y + int(52 * scale), x - int(25 * scale), y + int(88 * scale)), fill="#A65F4C", width=int(9 * scale))
    elif pose == "open":
        draw.line((x - int(50 * scale), y + int(42 * scale), x - int(95 * scale), y + int(90 * scale)), fill="#A65F4C", width=int(9 * scale))
        draw.line((x + int(48 * scale), y + int(42 * scale), x + int(92 * scale), y + int(82 * scale)), fill="#A65F4C", width=int(9 * scale))
    else:
        draw.line((x - int(48 * scale), y + int(42 * scale), x - int(68 * scale), y + int(118 * scale)), fill="#A65F4C", width=int(9 * scale))
        draw.line((x + int(48 * scale), y + int(42 * scale), x + int(68 * scale), y + int(118 * scale)), fill="#A65F4C", width=int(9 * scale))


def draw_bookshelf(draw: ImageDraw.ImageDraw, x: int, y: int, w: int, h: int) -> None:
    wood = "#C28A58"
    draw.rounded_rectangle((x, y, x + w, y + h), radius=10, fill="#E4B279", outline="#9A633C", width=3)
    for row in range(3):
        yy = y + 24 + row * (h // 3)
        draw.line((x + 12, yy + 65, x + w - 12, yy + 65), fill="#9A633C", width=3)
        for i in range(7):
            bx = x + 24 + i * 28
            bh = 40 + (i % 3) * 9
            color = ["#6EA5B7", "#EE7464", "#F6C47B", "#8DBD83", "#9C83B7"][i % 5]
            draw.rectangle((bx, yy + 20, bx + 18, yy + 20 + bh), fill=color)
    draw.ellipse((x + w - 88, y + h - 58, x + w - 42, y + h - 12), fill="#B7D9C2", outline="#658D70", width=2)


def draw_box(draw: ImageDraw.ImageDraw, x: int, y: int, w: int, h: int, fill: str = "#D49A5A") -> None:
    draw.polygon([(x, y + 20), (x + w // 2, y), (x + w, y + 20), (x + w // 2, y + 42)], fill="#E1AD72", outline="#7C5639")
    draw.rectangle((x, y + 20, x + w, y + h), fill=fill, outline="#7C5639", width=3)
    draw.line((x + w // 2, y + 42, x + w // 2, y + h), fill="#7C5639", width=2)


def draw_guitar(draw: ImageDraw.ImageDraw, x: int, y: int, scale: float = 1.0) -> None:
    body = int(70 * scale)
    draw.ellipse((x, y, x + body, y + int(95 * scale)), fill="#B76A3B", outline="#663B25", width=3)
    draw.ellipse((x + int(35 * scale), y + int(20 * scale), x + int(95 * scale), y + int(92 * scale)), fill="#C9834D", outline="#663B25", width=3)
    draw.ellipse((x + int(48 * scale), y + int(42 * scale), x + int(66 * scale), y + int(60 * scale)), fill="#2E2525")
    draw.line((x + int(88 * scale), y + int(36 * scale), x + int(190 * scale), y - int(40 * scale)), fill="#6B4A35", width=int(12 * scale))
    draw.rectangle((x + int(180 * scale), y - int(52 * scale), x + int(210 * scale), y - int(30 * scale)), fill="#6B4A35")


def new_canvas(size: tuple[int, int], bg: str) -> Image.Image:
    return Image.new("RGBA", size, bg)


def make_eyecatch() -> Path:
    img = new_canvas((1200, 630), COLORS["cream"])
    draw = ImageDraw.Draw(img)
    paste_logo(img, 150, "top-left")
    draw_multiline_center(draw, 620, 120, "物を捨てられない人の心理とは？", font(43, "bold"), COLORS["burgundy"], 760, 8)
    draw_center(draw, (620, 195), "夫や父親など男性に多い理由と接し方", font(27), COLORS["ink"])
    draw.ellipse((565, 270, 1180, 675), fill="#F8CF9C")
    draw.ellipse((650, 300, 1100, 650), fill="#FFF4DF")
    draw_bookshelf(draw, 675, 310, 250, 230)
    draw_box(draw, 940, 435, 120, 100, "#CF9056")
    draw_box(draw, 1030, 465, 110, 85, "#D9A56D")
    draw_person(draw, 350, 330, 1.25, COLORS["salmon"], "#5B463E", "arms-crossed")
    draw_person(draw, 540, 352, 1.05, "#F3B25F", "#784235", "open")
    draw.rounded_rectangle((170, 278, 285, 345), radius=32, fill="#FFFFFF", outline="#A8B6B2", width=4)
    draw.ellipse((138, 245, 205, 312), fill="#FFFFFF", outline="#A8B6B2", width=4)
    draw.ellipse((235, 245, 310, 320), fill="#FFFFFF", outline="#A8B6B2", width=4)
    draw.line((185, 315, 263, 282), fill="#A8B6B2", width=5)
    for bx, by in [(210, 575), (835, 548), (970, 565)]:
        draw.ellipse((bx, by, bx + 18, by + 18), fill="#C9B5A3")
    return save(img, "why-hoard-things-eyecatch.png")


def card(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], title: str, sub: str, color: str) -> None:
    rounded(draw, box, "#FFFFFF", "#D9D5CC", 22, 2)
    x1, y1, x2, _ = box
    draw.ellipse((x1 + 24, y1 + 28, x1 + 76, y1 + 80), fill=color)
    draw_center(draw, (x1 + 50, y1 + 54), title[:1], font(27, "bold"), "#FFFFFF")
    draw.text((x1 + 92, y1 + 25), title, font=font(26, "bold"), fill=COLORS["ink"])
    draw_multiline_center(draw, (x1 + x2) // 2 + 34, y1 + 70, sub, font(20), COLORS["muted"], x2 - x1 - 120, 4)


def make_psychology() -> Path:
    img = new_canvas((1200, 800), "#FBF7EE")
    draw = ImageDraw.Draw(img)
    draw_center(draw, (600, 66), "物を捨てられない心理に隠された5つの理由", font(36, "bold"), COLORS["ink"])
    center = (600, 405)
    cards = [
        ((70, 150, 420, 270), "損失回避", "捨てたら損するかも", COLORS["salmon"]),
        ((775, 150, 1130, 270), "拡張自己", "物は自分の一部", COLORS["blue"]),
        ((70, 495, 420, 615), "アニミズム", "物に魂が宿る", COLORS["purple"]),
        ((775, 495, 1130, 615), "判断疲れ", "決める気力がない", COLORS["orange"]),
        ((425, 610, 775, 730), "孤独感・不安", "物に囲まれると安心", COLORS["green"]),
    ]
    for box, title, sub, color in cards:
        bx = (box[0] + box[2]) // 2
        by = (box[1] + box[3]) // 2
        draw.line((center[0], center[1], bx, by), fill="#D7CFC4", width=5)
    draw.ellipse((425, 280, 775, 530), fill="#FFFFFF", outline="#D7CFC4", width=4)
    draw_center(draw, center, "物を\n捨てられない", font(36, "bold"), COLORS["burgundy"])
    for box, title, sub, color in cards:
        card(draw, box, title, sub, color)
    paste_logo(img, 155, "bottom-right")
    return save(img, "why-hoard-things-inline-psychology.png")


def make_male_memory() -> Path:
    img = new_canvas((1200, 800), COLORS["mint"])
    draw = ImageDraw.Draw(img)
    draw_center(draw, (600, 66), "物には、言葉にできない感情が託されている", font(35, "bold"), COLORS["ink"])
    draw.ellipse((90, 145, 760, 760), fill="#FFF7E8")
    draw.rounded_rectangle((115, 580, 720, 665), radius=20, fill="#C28A58")
    draw_person(draw, 390, 350, 1.45, "#8FB77D", "#6D554A", "neutral")
    draw_guitar(draw, 455, 418, 0.95)
    draw_box(draw, 160, 470, 130, 120, "#C98B55")
    for i in range(4):
        draw.rectangle((175 + i * 24, 500, 192 + i * 24, 555), fill=["#617BA7", "#CB665E", "#E6C46A", "#7BAF93"][i])
    rounded(draw, (760, 160, 1080, 510), "#FFFFFF", "#C8D7D4", 36, 3)
    draw.ellipse((730, 470, 780, 520), fill="#FFFFFF", outline="#C8D7D4", width=3)
    draw.ellipse((690, 525, 725, 560), fill="#FFFFFF", outline="#C8D7D4", width=3)
    draw_center(draw, (920, 215), "あの頃の記憶", font(27, "bold"), COLORS["burgundy"])
    draw.rectangle((820, 260, 940, 350), fill="#F6D7A6", outline="#A06A4D", width=3)
    draw.ellipse((845, 280, 890, 325), fill="#F1B08C")
    draw.rectangle((860, 322, 910, 350), fill="#6EA5B7")
    draw.rectangle((965, 278, 1035, 390), fill="#C2A680", outline="#7A573E", width=3)
    draw.line((985, 278, 1005, 390), fill="#6D4A35", width=4)
    draw.line((1015, 278, 995, 390), fill="#6D4A35", width=4)
    draw.text((825, 410), "大切にしてきた時間が、\n物に重なって見える", font=font(21), fill=COLORS["muted"], spacing=6)
    paste_logo(img, 155, "bottom-right")
    return save(img, "why-hoard-things-inline-male-memory.png")


def make_spectrum() -> Path:
    img = new_canvas((1200, 800), "#F7FAF7")
    draw = ImageDraw.Draw(img)
    draw_center(draw, (600, 66), "「物の多さ」より、生活への影響で見る", font(36, "bold"), COLORS["ink"])
    draw_center(draw, (600, 115), "ただの物持ちから、相談を検討する段階まで", font(24), COLORS["muted"])
    zones = [
        (80, 240, 410, 570, COLORS["green_soft"], "#5E9A78", "個人の価値観の範囲", ["趣味の部屋に物が多い", "共有スペースは整理", "本人も家族も困っていない"]),
        (435, 240, 765, 570, "#FFF6D9", "#C9963D", "注意ゾーン", ["共有スペースに侵食", "家族が困り始めている", "話し合いが必要"]),
        (790, 240, 1120, 570, "#FDEDEA", "#D36A5E", "専門家への相談を検討", ["生活動線がふさがる", "料理・入浴・睡眠に支障", "強い不安やパニック"]),
    ]
    draw.rounded_rectangle((120, 610, 1080, 650), radius=20, fill="#E6E2DB")
    draw.polygon([(120, 610), (520, 610), (520, 650), (120, 650)], fill="#8EC9A4")
    draw.polygon([(505, 610), (820, 610), (820, 650), (505, 650)], fill="#F4C86D")
    draw.polygon([(805, 610), (1080, 610), (1080, 650), (805, 650)], fill="#EA867B")
    for x1, y1, x2, y2, fill, accent, title, bullets in zones:
        rounded(draw, (x1, y1, x2, y2), fill, accent, 26, 3)
        draw_center(draw, ((x1 + x2) // 2, y1 + 48), title, font(27, "bold"), COLORS["ink"])
        y = y1 + 105
        for bullet in bullets:
            draw.ellipse((x1 + 34, y + 9, x1 + 46, y + 21), fill=accent)
            draw.text((x1 + 62, y), bullet, font=font(22), fill=COLORS["ink"])
            y += 56
    draw.text((130, 675), "軽い", font=font(22, "bold"), fill="#5E9A78")
    draw.text((1015, 675), "重い", font=font(22, "bold"), fill="#D36A5E")
    draw.line((185, 688, 1000, 688), fill="#AEB9B5", width=4)
    draw.polygon([(1000, 688), (980, 676), (980, 700)], fill="#AEB9B5")
    paste_logo(img, 155, "bottom-right")
    return save(img, "why-hoard-things-inline-spectrum.png")


def make_ng_ok() -> Path:
    img = new_canvas((1200, 800), COLORS["light"])
    draw = ImageDraw.Draw(img)
    draw_center(draw, (600, 65), "「捨てて」ではなく「選んで」に変える", font(37, "bold"), COLORS["ink"])
    rounded(draw, (70, 140, 565, 670), COLORS["red_soft"], "#E79A91", 28, 3)
    rounded(draw, (635, 140, 1130, 670), COLORS["green_soft"], "#80B993", 28, 3)
    draw_center(draw, (318, 190), "NG対応", font(34, "bold"), "#C84F48")
    draw_center(draw, (882, 190), "OK対応", font(34, "bold"), "#3E8D61")
    ng_items = ["勝手に捨てる", "責める", "他人と比較する"]
    ok_items = ["「選んで」と聞く", "保留箱を使う", "聖域ルールを作る", "売る・譲る出口を示す"]
    y = 255
    for item in ng_items:
        draw.ellipse((130, y - 4, 174, y + 40), fill="#C84F48")
        draw_center(draw, (152, y + 17), "×", font(28, "bold"), "#FFFFFF")
        draw.text((205, y), item, font=font(28, "bold"), fill=COLORS["ink"])
        y += 90
    y = 245
    for item in ok_items:
        draw.ellipse((695, y - 2, 739, y + 42), fill="#3E8D61")
        draw_center(draw, (717, y + 19), "○", font(26, "bold"), "#FFFFFF")
        draw.text((770, y), item, font=font(27, "bold"), fill=COLORS["ink"])
        y += 78
    draw.rounded_rectangle((430, 685, 770, 735), radius=25, fill="#FFFFFF", outline="#D5D0C7", width=2)
    draw_center(draw, (600, 710), "相手の物を否定せず、本人が選べる形にする", font(22, "medium"), COLORS["burgundy"])
    paste_logo(img, 150, "bottom-right")
    return save(img, "why-hoard-things-inline-ng-ok.png")


def save(img: Image.Image, name: str) -> Path:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    path = OUT_DIR / name
    img.convert("RGB").save(path, quality=95)
    return path


def main() -> None:
    paths = [
        make_eyecatch(),
        make_psychology(),
        make_male_memory(),
        make_spectrum(),
        make_ng_ok(),
    ]
    for path in paths:
        print(f"Wrote {path}")


if __name__ == "__main__":
    main()
