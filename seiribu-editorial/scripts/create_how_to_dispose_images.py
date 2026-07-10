#!/usr/bin/env python3
"""Create article images for the how-to-dispose article."""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "assets" / "images" / "how-to-dispose"
LOGO = ROOT / "assets" / "images" / "brand" / "seiribu-logo.png"
FONT_DIR = Path("/Users/dvcong/Library/Fonts")
FONT_REGULAR = FONT_DIR / "NotoSansJP-Regular.ttf"
FONT_BOLD = FONT_DIR / "NotoSansJP-Bold.ttf"
FONT_MEDIUM = FONT_DIR / "NotoSansJP-Medium.ttf"

WIDE = (1200, 630)
INLINE = (1200, 800)

COLORS = {
    "cream": "#FBF4EA",
    "cream_deep": "#F4E7D4",
    "paper": "#FFFDF8",
    "mint": "#EAF7EF",
    "mint_deep": "#88C5A2",
    "ink": "#24304A",
    "muted": "#5F6675",
    "line": "#D9D1C4",
    "burgundy": "#7A3454",
    "blue": "#5E94AF",
    "green": "#6EA77B",
    "orange": "#E2A33B",
    "salmon": "#D96E5F",
    "yellow": "#F8D982",
    "lavender": "#BDA8D6",
    "brown": "#B87843",
    "soft_red": "#FBE9E4",
    "soft_yellow": "#FFF3D7",
    "soft_blue": "#EAF2F6",
    "shadow": "#E8D9C4",
}


def font(size: int, weight: str = "regular") -> ImageFont.FreeTypeFont:
    path = FONT_BOLD if weight == "bold" else FONT_MEDIUM if weight == "medium" else FONT_REGULAR
    return ImageFont.truetype(str(path), size=size)


def text_size(draw: ImageDraw.ImageDraw, text: str, fnt: ImageFont.FreeTypeFont) -> tuple[int, int]:
    box = draw.textbbox((0, 0), text, font=fnt, spacing=6)
    return box[2] - box[0], box[3] - box[1]


def wrap_text(draw: ImageDraw.ImageDraw, text: str, fnt: ImageFont.FreeTypeFont, max_width: int) -> list[str]:
    lines: list[str] = []
    current = ""
    for char in text:
        if char == "\n":
            lines.append(current)
            current = ""
            continue
        candidate = current + char
        if current and text_size(draw, candidate, fnt)[0] > max_width:
            lines.append(current)
            current = char
        else:
            current = candidate
    if current:
        lines.append(current)
    return lines


def draw_center(draw: ImageDraw.ImageDraw, xy: tuple[int, int], text: str, fnt: ImageFont.FreeTypeFont, fill: str) -> None:
    x, y = xy
    lines = text.split("\n")
    line_heights = [text_size(draw, line, fnt)[1] for line in lines]
    total_h = sum(line_heights) + 8 * (len(lines) - 1)
    cursor = y - total_h / 2
    for line, line_h in zip(lines, line_heights, strict=True):
        w, _ = text_size(draw, line, fnt)
        draw.text((x - w / 2, cursor), line, font=fnt, fill=fill)
        cursor += line_h + 8


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


def draw_multiline_left(
    draw: ImageDraw.ImageDraw,
    x: int,
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
        _, h = text_size(draw, line, fnt)
        draw.text((x, y), line, font=fnt, fill=fill)
        y += h + leading
    return y


def rounded(
    draw: ImageDraw.ImageDraw,
    box: tuple[int, int, int, int],
    fill: str,
    outline: str | None = None,
    radius: int = 24,
    width: int = 2,
) -> None:
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def paste_logo(img: Image.Image, width: int = 150, position: str = "bottom-right") -> None:
    if not LOGO.exists():
        return
    logo = Image.open(LOGO).convert("RGBA")
    ratio = width / logo.width
    logo = logo.resize((width, int(logo.height * ratio)), Image.Resampling.LANCZOS)
    if position == "top-left":
        x, y = 48, 36
    else:
        x = img.width - width - 44
        y = img.height - logo.height - 32
    img.alpha_composite(logo, (x, y))


def new_canvas(size: tuple[int, int] = INLINE, bg: str = COLORS["cream"]) -> Image.Image:
    img = Image.new("RGBA", size, bg)
    draw = ImageDraw.Draw(img)
    draw.rectangle((0, size[1] - 150, size[0], size[1]), fill="#F6ECD9")
    for x, y, r, color in [
        (78, 110, 4, "#D8C5AC"),
        (1110, 95, 5, "#D2C0AA"),
        (155, 700, 4, "#D8C5AC"),
        (1030, 640, 4, "#D8C5AC"),
    ]:
        draw.ellipse((x - r, y - r, x + r, y + r), fill=color)
    return img


def save(img: Image.Image, name: str) -> Path:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    path = OUT_DIR / name
    if path.suffix.lower() == ".webp":
        img.convert("RGB").save(path, quality=92, method=6)
    else:
        img.convert("RGB").save(path, quality=95)
    return path


def draw_box(draw: ImageDraw.ImageDraw, x: int, y: int, w: int, h: int, color: str = "#D7A66E") -> None:
    draw.polygon([(x, y + 22), (x + w // 2, y), (x + w, y + 22), (x + w // 2, y + 44)], fill="#E8BD85", outline="#8E6042")
    draw.rectangle((x, y + 22, x + w, y + h), fill=color, outline="#8E6042", width=3)
    draw.line((x + w // 2, y + 44, x + w // 2, y + h), fill="#8E6042", width=2)
    draw.rectangle((x + w // 2 - 17, y + 57, x + w // 2 + 17, y + 88), fill="#F2D2A8", outline="#8E6042")


def draw_simple_person(draw: ImageDraw.ImageDraw, x: int, y: int, scale: float, shirt: str, hair: str, pose: str = "open") -> None:
    head = int(50 * scale)
    body_w = int(88 * scale)
    body_h = int(126 * scale)
    skin = "#F0B28E"
    draw.ellipse((x - head // 2, y - head, x + head // 2, y), fill=skin, outline="#9C6758", width=max(1, int(2 * scale)))
    draw.pieslice((x - head // 2 - 4, y - head - 7, x + head // 2 + 4, y + 8), 180, 360, fill=hair)
    draw.ellipse((x - int(15 * scale), y - int(31 * scale), x - int(10 * scale), y - int(26 * scale)), fill="#423433")
    draw.ellipse((x + int(10 * scale), y - int(31 * scale), x + int(15 * scale), y - int(26 * scale)), fill="#423433")
    draw.arc((x - int(13 * scale), y - int(22 * scale), x + int(13 * scale), y - int(7 * scale)), 20, 160, fill="#875C51", width=max(1, int(2 * scale)))
    rounded(draw, (x - body_w // 2, y + 4, x + body_w // 2, y + body_h), shirt, radius=int(28 * scale))
    if pose == "write":
        draw.line((x - int(42 * scale), y + int(44 * scale), x - int(72 * scale), y + int(106 * scale)), fill="#A65F4C", width=int(8 * scale))
        draw.line((x + int(43 * scale), y + int(44 * scale), x + int(15 * scale), y + int(112 * scale)), fill="#A65F4C", width=int(8 * scale))
    else:
        draw.line((x - int(42 * scale), y + int(40 * scale), x - int(82 * scale), y + int(84 * scale)), fill="#A65F4C", width=int(8 * scale))
        draw.line((x + int(42 * scale), y + int(40 * scale), x + int(82 * scale), y + int(84 * scale)), fill="#A65F4C", width=int(8 * scale))


def draw_room_scene(draw: ImageDraw.ImageDraw) -> None:
    draw.rectangle((0, 370, 1200, 630), fill="#F3E4C7")
    draw.line((0, 370, 1200, 370), fill="#D3BA91", width=4)
    draw.rectangle((900, 64, 1160, 300), fill="#FFF8E8", outline="#D9C5A0", width=5)
    draw.rectangle((932, 88, 1132, 278), fill="#EAF5EF")
    for x in [990, 1040, 1090]:
        draw.line((x, 92, x - 50, 276), fill="#CFDFD7", width=3)
    draw.rectangle((58, 360, 250, 410), fill="#B98457")
    draw.rectangle((76, 270, 232, 365), fill="#D6A877", outline="#9C6A44", width=3)
    for i, color in enumerate(["#6D9AA9", "#E08E65", "#8DBB8F", "#D9B55F", "#9C83B7"]):
        draw.rectangle((96 + i * 25, 292, 115 + i * 25, 348), fill=color)
    draw_box(draw, 650, 418, 155, 122, "#D4A063")
    draw_box(draw, 860, 430, 150, 112, "#C99458")
    draw_box(draw, 1000, 456, 130, 96, "#D7A66E")
    draw_simple_person(draw, 670, 318, 1.22, "#8CACD3", "#67534A", "open")
    draw_simple_person(draw, 875, 332, 1.02, "#E9A759", "#7A473D", "write")
    draw.ellipse((620, 355, 1000, 458), fill="#DFC697")
    draw.rectangle((678, 397, 850, 512), fill="#FFFFFF", outline="#C7BBA8", width=3)
    draw.line((700, 432, 826, 432), fill="#607F91", width=4)
    draw.line((700, 462, 808, 462), fill="#7FAE8A", width=4)
    draw.line((700, 492, 828, 492), fill="#D9AA5E", width=4)
    draw.rounded_rectangle((862, 410, 928, 548), radius=10, fill="#E6EAF2", outline="#7C8B9A", width=3)
    draw.rectangle((880, 438, 910, 510), fill="#C7D8E4")
    draw.line((845, 445, 890, 422), fill="#3E5363", width=5)
    draw.ellipse((884, 411, 907, 434), fill="#3E5363")


def make_eyecatch() -> Path:
    img = Image.new("RGBA", WIDE, COLORS["cream"])
    draw = ImageDraw.Draw(img)
    draw.rectangle((0, 0, 1200, 630), fill=COLORS["cream"])
    draw.ellipse((615, 250, 1290, 750), fill="#F4D8AA")
    draw.ellipse((715, 285, 1195, 655), fill="#FFF5DF")
    draw_room_scene(draw)
    paste_logo(img, 150, "top-left")
    rounded(draw, (102, 122, 612, 300), "#FFF8EED9", "#ECDCC4", 22, 2)
    draw_multiline_center(draw, 357, 147, "実家の不用品を\n安く処分する方法", font(42, "bold"), COLORS["ink"], 450, 10)
    draw_center(draw, (357, 274), "粗大ごみ・持ち込み・回収業者の費用比較", font(23, "medium"), "#2F695E")
    draw.rounded_rectangle((220, 310, 494, 318), radius=4, fill=COLORS["orange"])
    return save(img, "how-to-dispose-eyecatch.webp")


def step_icon(draw: ImageDraw.ImageDraw, center: tuple[int, int], kind: str, color: str) -> None:
    x, y = center
    draw.ellipse((x - 42, y - 42, x + 42, y + 42), fill="#FFFFFF", outline=color, width=5)
    if kind == "sell":
        draw.polygon([(x - 24, y - 18), (x + 18, y - 18), (x + 30, y - 2), (x - 12, y + 26), (x - 32, y + 4)], fill="#F4D17C", outline=color)
        draw.ellipse((x - 16, y - 10, x - 7, y - 1), fill="#FFFFFF", outline=color)
        draw.line((x + 1, y - 4, x + 16, y + 12), fill=color, width=4)
    elif kind == "home":
        draw.rounded_rectangle((x - 26, y - 20, x + 26, y + 28), radius=8, fill="#E8F3ED", outline=color, width=3)
        draw.line((x - 33, y - 18, x, y - 42, x + 33, y - 18), fill=color, width=4)
        draw.rectangle((x - 8, y + 3, x + 8, y + 28), fill="#FFFFFF", outline=color, width=2)
    elif kind == "truck":
        draw.rectangle((x - 34, y - 14, x + 9, y + 18), fill="#DDEAF2", outline=color, width=3)
        draw.rectangle((x + 9, y - 4, x + 34, y + 18), fill="#F3D18B", outline=color, width=3)
        draw.ellipse((x - 24, y + 13, x - 8, y + 29), fill=color)
        draw.ellipse((x + 16, y + 13, x + 32, y + 29), fill=color)


def make_funnel() -> Path:
    img = new_canvas(INLINE, "#FBF6ED")
    draw = ImageDraw.Draw(img)
    draw_center(draw, (600, 70), "実家の不用品処分費用を安く抑える3つの手順", font(36, "bold"), COLORS["ink"])
    draw_center(draw, (600, 118), "売る・家庭ごみ・残りだけ依頼の順で、費用がかかる量を減らす", font(23, "medium"), "#376A61")

    bands = [
        ((130, 170, 1070, 315), COLORS["soft_yellow"], COLORS["orange"], "1", "売れるものを先に売る", "本・カメラ・工具などは処分前に査定", "sell"),
        ((230, 340, 970, 485), COLORS["mint"], COLORS["green"], "2", "小さな不用品は家庭ごみへ", "分別ルールに沿って、帰省ごとに少しずつ", "home"),
        ((350, 510, 850, 655), COLORS["soft_blue"], COLORS["blue"], "3", "大きい・重い物だけ依頼", "粗大ごみや回収業者に任せる量を最小化", "truck"),
    ]
    for box, fill, accent, num, title, sub, icon in bands:
        x1, y1, x2, y2 = box
        draw.polygon([(x1, y1), (x2, y1), (x2 - 70, y2), (x1 + 70, y2)], fill=COLORS["shadow"])
        draw.polygon([(x1, y1 - 9), (x2, y1 - 9), (x2 - 70, y2 - 9), (x1 + 70, y2 - 9)], fill=fill, outline=accent)
        draw.ellipse((x1 + 44, y1 + 26, x1 + 104, y1 + 86), fill=accent)
        draw_center(draw, (x1 + 74, y1 + 56), num, font(32, "bold"), "#FFFFFF")
        step_icon(draw, (x1 + 162, y1 + 60), icon, accent)
        draw.text((x1 + 230, y1 + 30), title, font=font(31, "bold"), fill=COLORS["ink"])
        draw.text((x1 + 230, y1 + 82), sub, font=font(21), fill=COLORS["muted"])

    for x, y, scale in [(1088, 214, 1.0), (1034, 252, 0.75), (996, 276, 0.58), (994, 388, 0.78), (951, 425, 0.58), (988, 566, 0.68)]:
        draw_box(draw, x, y, int(62 * scale), int(56 * scale), "#D7A66E")

    draw.rounded_rectangle((397, 680, 803, 725), radius=22, fill="#FFFDF8", outline="#DED2C4", width=2)
    draw_center(draw, (600, 702), "業者に頼む分だけを小さくする", font(22, "bold"), COLORS["burgundy"])
    paste_logo(img, 148, "bottom-right")
    return save(img, "how-to-dispose-inline-funnel.png")


def matrix_point(
    draw: ImageDraw.ImageDraw,
    center: tuple[int, int],
    label: str,
    sub: str,
    fill: str,
    outline: str,
    max_width: int = 210,
) -> None:
    x, y = center
    rounded(draw, (x - 130, y - 54, x + 130, y + 54), fill, outline, 22, 3)
    draw_center(draw, (x, y - 14), label, font(24, "bold"), COLORS["ink"])
    draw_multiline_center(draw, x, y + 14, sub, font(17), COLORS["muted"], max_width, 3)


def make_method_matrix() -> Path:
    img = new_canvas(INLINE, "#FBF6ED")
    draw = ImageDraw.Draw(img)
    draw_center(draw, (600, 66), "不用品を手放す4つの方法：費用と手間の比較", font(36, "bold"), COLORS["ink"])
    draw_center(draw, (600, 112), "予算・時間・体力に合わせて、無理のない方法を選ぶ", font(23, "medium"), "#376A61")

    left, top, right, bottom = 170, 180, 1040, 660
    rounded(draw, (left - 18, top - 18, right + 18, bottom + 18), "#FFFDF8", "#E5D9C9", 26, 2)
    draw.line((left, bottom, right, bottom), fill="#7B8794", width=4)
    draw.line((left, bottom, left, top), fill="#7B8794", width=4)
    draw.polygon([(right, bottom), (right - 22, bottom - 11), (right - 22, bottom + 11)], fill="#7B8794")
    draw.polygon([(left, top), (left - 11, top + 22), (left + 11, top + 22)], fill="#7B8794")
    for x in [left + 218, left + 436, left + 654]:
        draw.line((x, top, x, bottom), fill="#E7DED2", width=2)
    for y in [top + 120, top + 240, top + 360]:
        draw.line((left, y, right, y), fill="#E7DED2", width=2)

    draw.text((left - 70, top - 52), "手間が\nかかる", font=font(20, "bold"), fill=COLORS["muted"], spacing=4)
    draw.text((left - 56, bottom - 4), "手間\nなし", font=font(20, "bold"), fill=COLORS["muted"], spacing=4)
    draw.text((left - 20, bottom + 34), "費用が安い", font=font(20, "bold"), fill=COLORS["muted"])
    draw.text((right - 90, bottom + 34), "高い", font=font(20, "bold"), fill=COLORS["muted"])

    matrix_point(draw, (320, 250), "持ち込み", "最安だが車と搬出が必要", "#FFF3D7", COLORS["orange"])
    matrix_point(draw, (520, 363), "ジモティー等", "無料でも調整に時間が必要", "#F1EAF8", COLORS["lavender"])
    matrix_point(draw, (395, 500), "粗大ごみ", "安いが申込と搬出が必要", "#EAF7EF", COLORS["green"])
    matrix_point(draw, (850, 540), "回収業者", "費用は高めだが早くて楽", "#EAF2F6", COLORS["blue"])

    draw.rounded_rectangle((738, 210, 1004, 288), radius=20, fill="#F8FBFD", outline="#D3E1E7", width=2)
    draw_center(draw, (871, 235), "大量・大型・急ぎなら", font(19, "medium"), COLORS["muted"])
    draw_center(draw, (871, 264), "右下の方法も現実的", font(21, "bold"), COLORS["ink"])
    paste_logo(img, 148, "bottom-right")
    return save(img, "how-to-dispose-inline-method-matrix.png")


def checklist_icon(draw: ImageDraw.ImageDraw, center: tuple[int, int], kind: str, color: str) -> None:
    x, y = center
    draw.ellipse((x - 50, y - 50, x + 50, y + 50), fill="#FFFFFF", outline=color, width=5)
    if kind == "recycle":
        draw.arc((x - 24, y - 26, x + 30, y + 28), 30, 290, fill=color, width=5)
        draw.polygon([(x + 27, y - 20), (x + 41, y - 4), (x + 20, y - 1)], fill=color)
        draw.rectangle((x - 22, y + 8, x + 22, y + 28), fill="#E8F3ED", outline=color, width=3)
    elif kind == "stairs":
        for i in range(4):
            draw.rectangle((x - 35 + i * 17, y + 20 - i * 15, x - 18 + i * 17, y + 35 - i * 15), fill="#F4D18D", outline=color)
        draw.rounded_rectangle((x + 5, y - 26, x + 36, y + 18), radius=5, fill="#DCEAF2", outline=color, width=3)
    elif kind == "calendar":
        draw.rounded_rectangle((x - 30, y - 28, x + 30, y + 30), radius=8, fill="#FFFFFF", outline=color, width=3)
        draw.rectangle((x - 30, y - 28, x + 30, y - 8), fill="#F4D18D", outline=color)
        draw.line((x - 16, y + 7, x + 16, y + 7), fill=color, width=3)
        draw.line((x - 16, y + 20, x + 4, y + 20), fill=color, width=3)


def checklist_card(
    draw: ImageDraw.ImageDraw,
    box: tuple[int, int, int, int],
    num: str,
    title: str,
    sub: str,
    icon: str,
    accent: str,
) -> None:
    x1, y1, x2, y2 = box
    rounded(draw, box, "#FFFDF8", "#E5D9C9", 26, 2)
    draw.rounded_rectangle((x1 + 28, y1 + 28, x1 + 78, y1 + 78), radius=13, fill="#FFFFFF", outline=accent, width=4)
    draw.line((x1 + 41, y1 + 53, x1 + 53, y1 + 66, x1 + 68, y1 + 39), fill=accent, width=6)
    draw.ellipse((x1 + 102, y1 + 31, x1 + 146, y1 + 75), fill=accent)
    draw_center(draw, (x1 + 124, y1 + 53), num, font(24, "bold"), "#FFFFFF")
    checklist_icon(draw, (x1 + 96, y1 + 110), icon, accent)
    draw_multiline_left(draw, x1 + 190, y1 + 35, title, font(27, "bold"), COLORS["ink"], x2 - x1 - 230, 6)
    draw_multiline_left(draw, x1 + 190, y1 + 86, sub, font(20), COLORS["muted"], x2 - x1 - 230, 5)


def make_boundary_checklist() -> Path:
    img = new_canvas(INLINE, "#FBF6ED")
    draw = ImageDraw.Draw(img)
    draw_center(draw, (600, 66), "自力での処分をやめる3つの境界線", font(37, "bold"), COLORS["ink"])
    draw_center(draw, (600, 113), "危険・割高・時間切れになりそうなら、プロへの相談も選択肢", font(23, "medium"), "#376A61")

    checklist_card(
        draw,
        (86, 158, 1114, 305),
        "1",
        "家電リサイクル対象品がある",
        "テレビ・冷蔵庫・洗濯機・エアコンは自治体の粗大ごみに出せません。",
        "recycle",
        COLORS["blue"],
    )
    checklist_card(
        draw,
        (86, 326, 1114, 473),
        "2",
        "階段で大型家具を搬出する必要がある",
        "無理な運搬はケガや壁・床の破損につながるため、人数と動線を確認します。",
        "stairs",
        COLORS["salmon"],
    )
    checklist_card(
        draw,
        (86, 494, 1114, 641),
        "3",
        "帰省の日数や体力に限界がある",
        "何度も通う費用や時間が膨らむなら、まとめて依頼した方が現実的です。",
        "calendar",
        COLORS["green"],
    )
    draw.rounded_rectangle((252, 666, 948, 731), radius=30, fill=COLORS["burgundy"])
    draw_center(draw, (600, 697), "1つでも当てはまるなら、プロへの相談を検討", font(27, "bold"), "#FFFFFF")
    paste_logo(img, 148, "bottom-right")
    return save(img, "how-to-dispose-inline-pro-boundary.png")


def main() -> None:
    paths = [
        make_eyecatch(),
        make_funnel(),
        make_method_matrix(),
        make_boundary_checklist(),
    ]
    for path in paths:
        print(f"Wrote {path}")


if __name__ == "__main__":
    main()
