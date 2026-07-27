#!/usr/bin/env python3
"""Create local diagram assets and eyecatch composition for reduce-things."""

from __future__ import annotations

import json
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont


ROOT = Path(__file__).resolve().parents[1]
DRAFT_DIR = Path("/private/tmp/seiribu-image-work/reduce-things")
OUT_DIR = ROOT / "assets" / "images" / "reduce-things"
LOGO = ROOT / "assets" / "images" / "brand" / "seiribu-logo.png"
PLAN = ROOT / "image-briefs" / "reduce-things-image-plan.json"
FONT_DIR = Path("/Users/dvcong/Library/Fonts")
FONT_REGULAR = FONT_DIR / "NotoSansJP-Regular.ttf"
FONT_MEDIUM = FONT_DIR / "NotoSansJP-Medium.ttf"
FONT_BOLD = FONT_DIR / "NotoSansJP-Bold.ttf"

SCALE = 2
W, H = 1200 * SCALE, 675 * SCALE

COLORS = {
    "cream": "#FBF6EF",
    "paper": "#FFFDF8",
    "ink": "#24304A",
    "muted": "#5F6675",
    "line": "#DED5C8",
    "burgundy": "#7A3454",
    "green": "#5F9B75",
    "green_soft": "#EAF7EF",
    "orange": "#DFA434",
    "orange_soft": "#FFF3D8",
    "blue": "#4E83A8",
    "blue_soft": "#EAF3F8",
    "salmon": "#DE6D5F",
    "salmon_soft": "#FCE9E6",
    "purple": "#8E75B8",
    "purple_soft": "#F0ECFA",
}


def s(value: int | float) -> int:
    return round(value * SCALE)


def font(size: int, weight: str = "regular") -> ImageFont.FreeTypeFont:
    path = FONT_BOLD if weight == "bold" else FONT_MEDIUM if weight == "medium" else FONT_REGULAR
    return ImageFont.truetype(str(path), size=s(size))


def text_box(draw: ImageDraw.ImageDraw, text: str, fnt: ImageFont.FreeTypeFont) -> tuple[int, int]:
    box = draw.textbbox((0, 0), text, font=fnt)
    return box[2] - box[0], box[3] - box[1]


def center_text(draw: ImageDraw.ImageDraw, x: int, y: int, text: str, fnt: ImageFont.FreeTypeFont, fill: str) -> None:
    tw, th = text_box(draw, text, fnt)
    draw.text((x - tw / 2, y - th / 2), text, font=fnt, fill=fill)


def left_text(draw: ImageDraw.ImageDraw, x: int, y: int, text: str, fnt: ImageFont.FreeTypeFont, fill: str) -> None:
    draw.text((x, y), text, font=fnt, fill=fill)


def shadowed_round(
    base: Image.Image,
    box: tuple[int, int, int, int],
    fill: str,
    outline: str,
    radius: int = 24,
    shadow: bool = True,
    width: int = 2,
) -> None:
    if shadow:
        layer = Image.new("RGBA", base.size, (0, 0, 0, 0))
        sd = ImageDraw.Draw(layer)
        offset = s(8)
        sd.rounded_rectangle(
            (box[0] + offset, box[1] + offset, box[2] + offset, box[3] + offset),
            radius=s(radius),
            fill=(74, 60, 46, 28),
        )
        base.alpha_composite(layer.filter(ImageFilter.GaussianBlur(s(8))))
    draw = ImageDraw.Draw(base)
    draw.rounded_rectangle(box, radius=s(radius), fill=fill, outline=outline, width=s(width))


def downsample(img: Image.Image) -> Image.Image:
    return img.resize((1200, 675), Image.Resampling.LANCZOS).convert("RGB")


def contain(src: Image.Image, width: int) -> Image.Image:
    ratio = width / src.width
    return src.resize((width, round(src.height * ratio)), Image.Resampling.LANCZOS)


def paste_logo(img: Image.Image, *, x: int, y: int, width: int = 150, backing: bool = False) -> None:
    if not LOGO.exists():
        return
    logo = contain(Image.open(LOGO).convert("RGBA"), s(width))
    if backing:
        draw = ImageDraw.Draw(img)
        pad = s(14)
        draw.rounded_rectangle(
            (x - pad, y - pad, x + logo.width + pad, y + logo.height + pad),
            radius=s(12),
            fill=(255, 255, 255, 220),
        )
    img.alpha_composite(logo, (x, y))


def draw_clock(draw: ImageDraw.ImageDraw, cx: int, cy: int, color: str) -> None:
    draw.ellipse((cx - s(36), cy - s(36), cx + s(36), cy + s(36)), fill="#FFFFFF", outline=color, width=s(5))
    draw.line((cx, cy, cx, cy - s(23)), fill=color, width=s(5))
    draw.line((cx, cy, cx + s(20), cy + s(10)), fill=color, width=s(5))


def draw_broom(draw: ImageDraw.ImageDraw, x: int, y: int, color: str) -> None:
    draw.line((x + s(46), y, x + s(12), y + s(84)), fill=color, width=s(6))
    draw.polygon(
        [(x, y + s(88)), (x + s(38), y + s(72)), (x + s(58), y + s(112)), (x + s(14), y + s(124))],
        fill="#F1C778",
        outline=color,
    )
    for dx in [12, 24, 36]:
        draw.line((x + s(dx), y + s(88), x + s(dx + 8), y + s(114)), fill=color, width=s(2))


def draw_small_room(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], *, tidy: bool) -> None:
    x1, y1, x2, y2 = box
    draw.rounded_rectangle(box, radius=s(18), fill="#FFF7EA", outline=COLORS["line"], width=s(2))
    draw.rectangle((x1 + s(24), y2 - s(80), x2 - s(24), y2 - s(34)), fill="#E8D1AD")
    draw.rectangle((x1 + s(60), y1 + s(54), x1 + s(184), y1 + s(150)), fill="#E7F1F4", outline="#A8C5D1", width=s(3))
    draw.rectangle((x2 - s(170), y2 - s(156), x2 - s(76), y2 - s(80)), fill="#C99666", outline="#8B6444", width=s(3))
    if tidy:
        draw.ellipse((x1 + s(246), y1 + s(120), x1 + s(302), y1 + s(176)), fill="#F6C7B8", outline="#D98E7E", width=s(2))
        draw.rectangle((x1 + s(258), y1 + s(174), x1 + s(290), y1 + s(250)), fill="#5F9B75")
        draw.line((x1 + s(225), y1 + s(250), x1 + s(325), y1 + s(250)), fill="#5F9B75", width=s(4))
        draw.rounded_rectangle((x2 - s(142), y2 - s(204), x2 - s(54), y2 - s(166)), radius=s(8), fill="#EAF7EF", outline="#90B99D", width=s(2))
    else:
        for bx, by, bw, bh, color in [
            (100, 208, 90, 40, "#D7B06D"),
            (220, 224, 110, 34, "#A9B8CC"),
            (352, 196, 92, 44, "#D98E7E"),
            (300, 130, 78, 30, "#C8A1C8"),
        ]:
            draw.rounded_rectangle(
                (x1 + s(bx), y1 + s(by), x1 + s(bx + bw), y1 + s(by + bh)),
                radius=s(8),
                fill=color,
                outline="#A9947C",
                width=s(2),
            )
        draw.arc((x1 + s(250), y1 + s(86), x1 + s(360), y1 + s(182)), 205, 330, fill=COLORS["salmon"], width=s(6))


def make_inline_01() -> Path:
    img = Image.new("RGBA", (W, H), COLORS["cream"])
    draw = ImageDraw.Draw(img)
    center_text(draw, s(600), s(56), "物が減ると、毎日の手間が軽くなる", font(34, "bold"), COLORS["ink"])
    center_text(draw, s(600), s(104), "探し物と掃除前のひと手間を減らす", font(20, "medium"), COLORS["green"])

    left = (s(58), s(154), s(555), s(535))
    right = (s(645), s(154), s(1142), s(535))
    shadowed_round(img, left, COLORS["salmon_soft"], "#E9B0AA", 28)
    shadowed_round(img, right, COLORS["green_soft"], "#9CC9A9", 28)
    draw = ImageDraw.Draw(img)
    draw.rounded_rectangle((s(92), s(184), s(242), s(230)), radius=s(23), fill="#FFFFFF", outline="#E9B0AA", width=s(2))
    center_text(draw, s(167), s(207), "物が多い", font(22, "bold"), COLORS["salmon"])
    draw.rounded_rectangle((s(679), s(184), s(829), s(230)), radius=s(23), fill="#FFFFFF", outline="#9CC9A9", width=s(2))
    center_text(draw, s(754), s(207), "物を減らす", font(22, "bold"), COLORS["green"])

    draw_small_room(draw, (s(98), s(262), s(515), s(454)), tidy=False)
    draw_small_room(draw, (s(685), s(262), s(1102), s(454)), tidy=True)

    draw_clock(draw, s(164), s(493), COLORS["salmon"])
    left_text(draw, s(222), s(472), "探し物が増える", font(23, "bold"), COLORS["ink"])
    left_text(draw, s(222), s(508), "掃除前に物をどかす", font(17, "medium"), COLORS["muted"])

    draw_broom(draw, s(684), s(456), COLORS["green"])
    left_text(draw, s(762), s(472), "すぐ動ける", font(23, "bold"), COLORS["ink"])
    left_text(draw, s(762), s(508), "掃除も外出も軽くなる", font(17, "medium"), COLORS["muted"])

    draw.line((s(574), s(330), s(624), s(330)), fill=COLORS["burgundy"], width=s(6))
    draw.polygon([(s(624), s(330)), (s(604), s(316)), (s(604), s(344))], fill=COLORS["burgundy"])

    draw.rounded_rectangle((s(250), s(590), s(950), s(632)), radius=s(22), fill="#FFFFFF", outline=COLORS["line"], width=s(2))
    center_text(draw, s(600), s(611), "減らす目的は「暮らしの判断」を軽くすること", font(19, "bold"), COLORS["burgundy"])
    out = DRAFT_DIR / "reduce-things-inline-01.png"
    downsample(img).save(out, quality=95)
    return out


def draw_center_item(draw: ImageDraw.ImageDraw, cx: int, cy: int) -> None:
    draw.rounded_rectangle((cx - s(54), cy - s(34), cx + s(54), cy + s(34)), radius=s(12), fill="#B8755B", outline="#7C4F40", width=s(4))
    draw.arc((cx - s(28), cy - s(54), cx + s(28), cy + s(2)), 200, 340, fill="#7C4F40", width=s(4))
    draw.rectangle((cx - s(36), cy - s(94), cx + s(36), cy - s(42)), fill="#D8A062", outline="#8E633D", width=s(3))
    draw.rectangle((cx - s(14), cy - s(126), cx + s(14), cy - s(94)), fill="#DFA434", outline="#8E633D", width=s(3))
    draw.rounded_rectangle((cx - s(20), cy + s(42), cx + s(20), cy + s(94)), radius=s(8), fill="#90B99D", outline="#5F9B75", width=s(3))


def make_options() -> Path:
    img = Image.new("RGBA", (W, H), COLORS["cream"])
    draw = ImageDraw.Draw(img)
    center_text(draw, s(600), s(56), "捨てる・残すだけで考えない", font(34, "bold"), COLORS["ink"])
    center_text(draw, s(600), s(104), "迷う物には5つの行き先を用意する", font(20, "medium"), COLORS["green"])

    center = (s(600), s(336))
    draw.ellipse((center[0] - s(122), center[1] - s(122), center[0] + s(122), center[1] + s(122)), fill="#FFF7EA", outline="#E4D4BB", width=s(3))
    draw_center_item(draw, *center)
    center_text(draw, s(600), s(468), "迷う物", font(25, "bold"), COLORS["ink"])

    items = [
        ("残す", "今使う物", COLORS["green"], COLORS["green_soft"], s(280), s(212)),
        ("売る", "価値を確認", COLORS["orange"], COLORS["orange_soft"], s(600), s(188)),
        ("譲る", "使う人へ", COLORS["blue"], COLORS["blue_soft"], s(920), s(212)),
        ("保留", "日を決めて見直す", COLORS["purple"], COLORS["purple_soft"], s(370), s(532)),
        ("処分", "ルールに沿って手放す", COLORS["salmon"], COLORS["salmon_soft"], s(830), s(532)),
    ]
    for title, desc, color, fill, cx, cy in items:
        shadowed_round(img, (cx - s(118), cy - s(55), cx + s(118), cy + s(55)), fill, color, 24, True, 3)
        draw = ImageDraw.Draw(img)
        center_text(draw, cx, cy - s(15), title, font(28, "bold"), color)
        center_text(draw, cx, cy + s(24), desc, font(16, "medium"), COLORS["muted"])
        start_x = center[0] + (s(112) if cx > center[0] else -s(112) if cx < center[0] else 0)
        start_y = center[1] + (s(92) if cy > center[1] else -s(92) if cy < center[1] else 0)
        end_x = cx + (-s(125) if cx > center[0] else s(125) if cx < center[0] else 0)
        end_y = cy + (-s(62) if cy > center[1] else s(62) if cy < center[1] else 0)
        draw.line((start_x, start_y, end_x, end_y), fill=color, width=s(5))
        angle = 1 if cx >= center[0] else -1
        draw.polygon(
            [(end_x, end_y), (end_x - s(16) * angle, end_y - s(9)), (end_x - s(16) * angle, end_y + s(9))],
            fill=color,
        )

    draw.rounded_rectangle((s(245), s(602), s(955), s(642)), radius=s(20), fill="#FFFFFF", outline=COLORS["line"], width=s(2))
    center_text(draw, s(600), s(622), "選択肢が増えると、手放す罪悪感が軽くなる", font(18, "bold"), COLORS["burgundy"])
    out = DRAFT_DIR / "reduce-things-inline-options.png"
    downsample(img).save(out, quality=95)
    return out


def compose_eyecatch() -> Path:
    source = DRAFT_DIR / "reduce-things-eyecatch-branded.png"
    if not source.exists():
        raise FileNotFoundError(source)
    base = Image.open(source).convert("RGBA")
    scale = max(W / base.width, H / base.height)
    resized = base.resize((round(base.width * scale), round(base.height * scale)), Image.Resampling.LANCZOS)
    canvas = resized.crop(((resized.width - W) // 2, (resized.height - H) // 2, (resized.width - W) // 2 + W, (resized.height - H) // 2 + H))

    overlay = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    draw.rounded_rectangle((s(672), s(130), s(1126), s(438)), radius=s(28), fill=(255, 250, 240, 218), outline=(222, 211, 194, 180), width=s(2))
    canvas.alpha_composite(overlay)
    draw = ImageDraw.Draw(canvas)
    paste_logo(canvas, x=s(58), y=s(42), width=150, backing=True)
    left_text(draw, s(724), s(178), "物を減らすと", font(42, "bold"), COLORS["burgundy"])
    left_text(draw, s(724), s(240), "楽になる理由", font(42, "bold"), COLORS["burgundy"])
    draw.rounded_rectangle((s(724), s(314), s(1052), s(358)), radius=s(22), fill="#EAF7EF", outline="#9CC9A9", width=s(2))
    center_text(draw, s(888), s(336), "何から始める？", font(24, "bold"), COLORS["green"])
    left_text(draw, s(724), s(388), "無理なく続ける整理のコツ", font(23, "medium"), COLORS["ink"])
    draw.rounded_rectangle((s(724), s(458), s(946), s(468)), radius=s(5), fill=COLORS["orange"])
    out = OUT_DIR / "reduce-things-eyecatch-branded.png"
    downsample(canvas).save(out, quality=95)
    return out


def write_readme() -> None:
    text = """# 物を減らすと楽になる理由 画像

## 完成画像

| 用途 | ファイル | サイズ | WordPress画像タイトル | ALT |
| --- | --- | --- | --- | --- |
| アイキャッチ | `reduce-things-eyecatch-branded.png` | 1200 x 675 | 物を減らすには何から始めるかを考えながら小さな場所から整理する人 | 物を減らすには何から始めるかを考えながら小さな場所から整理する人 |
| 記事内図解_scene | `reduce-things-inline-01.png` | 1200 x 675 | 物を減らすことで探し物や掃除の時間が減るメリットの図解 | 物を減らすことで探し物や掃除の時間が減るメリットの図解 |
| 記事内図解_slide | `reduce-things-inline-options.png` | 1200 x 675 | 捨てるか残すかだけでなく、売る・譲る・保留を加えた5つの選択肢 | 捨てるか残すかだけでなく、売る・譲る・保留を加えた5つの選択肢 |
| 記事内イメージ | `reduce-things-inline-three-boxes.png` | 1200 x 675 | まずは財布など小さな場所から物を減らす様子 | まずは財布など小さな場所から物を減らす様子 |
| 記事内イメージ | `reduce-things-inline-ng-ok.png` | 1200 x 675 | 実家の片付けで親と一緒に荷物を確認する親子 | 実家の片付けで親と一緒に荷物を確認する親子 |

## 設置位置・キャプション

### `reduce-things-eyecatch-branded.png`

- 設置位置: アイキャッチ
- キャプション候補: なし
- ロゴ: 左上に白背景付きセイリ部ロゴを配置済み

### `reduce-things-inline-01.png`

- 設置位置: 本文中のCMSブリーフ位置
- キャプション候補: 物が減ると、掃除や探し物の時間が大きく減ります
- ロゴ: 本文画像として合成済み

### `reduce-things-inline-options.png`

- 設置位置: 本文中のCMSブリーフ位置
- キャプション候補: 捨てる以外の選択肢を持つと、判断が楽になります
- ロゴ: 本文画像として合成済み

### `reduce-things-inline-three-boxes.png`

- 設置位置: 本文中のCMSブリーフ位置
- キャプション候補: まずは15分で終わる小さな場所から始めましょう
- ロゴ: 本文画像として合成済み

### `reduce-things-inline-ng-ok.png`

- 設置位置: 本文中のCMSブリーフ位置
- キャプション候補: 「捨てる」のではなく「確認する」スタンスで進めましょう
- ロゴ: 本文画像として合成済み

## 制作メモ

- 日本語ラベルの正確性が必要な2枚は、画像生成AIに文字を任せずローカル図解として作成
- アイキャッチは生成素材にタイトル、サブタイトル、セイリ部ロゴをローカル合成
- 本文画像は生成AIに文字やロゴを描かせず、仕上げ工程でブランド帰属ロゴを合成
"""
    (OUT_DIR / "README.md").write_text(text, encoding="utf-8")


def update_manifest() -> None:
    manifest = {
        "plan": str(PLAN),
        "images": [
            {
                "role": role,
                "file_name": name,
                "output": str(OUT_DIR / name),
                "alt": alt,
                "caption": caption,
            }
            for role, name, alt, caption in [
                ("アイキャッチ", "reduce-things-eyecatch-branded.png", "物を減らすには何から始めるかを考えながら小さな場所から整理する人", ""),
                ("記事内図解_scene", "reduce-things-inline-01.png", "物を減らすことで探し物や掃除の時間が減るメリットの図解", "物が減ると、掃除や探し物の時間が大きく減ります"),
                ("記事内図解_slide", "reduce-things-inline-options.png", "捨てるか残すかだけでなく、売る・譲る・保留を加えた5つの選択肢", "捨てる以外の選択肢を持つと、判断が楽になります"),
                ("記事内イメージ", "reduce-things-inline-three-boxes.png", "まずは財布など小さな場所から物を減らす様子", "まずは15分で終わる小さな場所から始めましょう"),
                ("記事内イメージ", "reduce-things-inline-ng-ok.png", "実家の片付けで親と一緒に荷物を確認する親子", "「捨てる」のではなく「確認する」スタンスで進めましょう"),
            ]
        ],
    }
    (OUT_DIR / "finish-manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")


def main() -> None:
    DRAFT_DIR.mkdir(parents=True, exist_ok=True)
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for path in [make_inline_01(), make_options()]:
        print(f"Wrote {path}")
    print(f"Wrote {compose_eyecatch()}")
    write_readme()
    update_manifest()


if __name__ == "__main__":
    main()
