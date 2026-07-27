#!/usr/bin/env python3
"""Create the checklist diagram for the trusted-buying-services article."""

from __future__ import annotations

import json
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "assets" / "images" / "trusted-buying-services"
DRAFT_DIR = Path("/private/tmp/seiribu-image-work/trusted-buying-services")
LOGO = ROOT / "assets" / "images" / "brand" / "seiribu-logo.png"
PLAN = ROOT / "image-briefs" / "trusted-buying-services-image-plan.json"
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
}


def s(value: int | float) -> int:
    return round(value * SCALE)


def font(size: int, weight: str = "regular") -> ImageFont.FreeTypeFont:
    path = FONT_BOLD if weight == "bold" else FONT_MEDIUM if weight == "medium" else FONT_REGULAR
    return ImageFont.truetype(str(path), size=s(size))


def text_box(draw: ImageDraw.ImageDraw, text: str, fnt: ImageFont.FreeTypeFont) -> tuple[int, int]:
    box = draw.textbbox((0, 0), text, font=fnt)
    return box[2] - box[0], box[3] - box[1]


def draw_center(draw: ImageDraw.ImageDraw, x: int, y: int, text: str, fnt: ImageFont.FreeTypeFont, fill: str) -> None:
    tw, th = text_box(draw, text, fnt)
    draw.text((x - tw / 2, y - th / 2), text, font=fnt, fill=fill)


def draw_left(draw: ImageDraw.ImageDraw, x: int, y: int, text: str, fnt: ImageFont.FreeTypeFont, fill: str) -> None:
    draw.text((x, y), text, font=fnt, fill=fill)


def shadowed_round(
    base: Image.Image,
    box: tuple[int, int, int, int],
    fill: str,
    outline: str,
    radius: int = 26,
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
            fill=(74, 60, 46, 30),
        )
        base.alpha_composite(layer.filter(ImageFilter.GaussianBlur(s(8))))
    draw = ImageDraw.Draw(base)
    draw.rounded_rectangle(box, radius=s(radius), fill=fill, outline=outline, width=s(width))


def draw_check(draw: ImageDraw.ImageDraw, cx: int, cy: int, color: str) -> None:
    draw.ellipse((cx - s(18), cy - s(18), cx + s(18), cy + s(18)), fill=color)
    draw.line((cx - s(8), cy, cx - s(1), cy + s(8), cx + s(11), cy - s(9)), fill="#FFFFFF", width=s(5), joint="curve")


def draw_clipboard_icon(draw: ImageDraw.ImageDraw, x: int, y: int, color: str) -> None:
    draw.rounded_rectangle((x, y + s(8), x + s(54), y + s(66)), radius=s(9), fill="#FFFFFF", outline=color, width=s(4))
    draw.rounded_rectangle((x + s(14), y, x + s(40), y + s(18)), radius=s(7), fill=color)
    for i in range(3):
        yy = y + s(27 + i * 13)
        draw.line((x + s(14), yy, x + s(40), yy), fill=color, width=s(3))


def draw_id_icon(draw: ImageDraw.ImageDraw, x: int, y: int, color: str) -> None:
    draw.rounded_rectangle((x, y + s(6), x + s(64), y + s(56)), radius=s(10), fill="#FFFFFF", outline=color, width=s(4))
    draw.ellipse((x + s(12), y + s(20), x + s(28), y + s(36)), fill=color)
    draw.line((x + s(38), y + s(23), x + s(54), y + s(23)), fill=color, width=s(4))
    draw.line((x + s(38), y + s(36), x + s(54), y + s(36)), fill=color, width=s(4))


def draw_document_icon(draw: ImageDraw.ImageDraw, x: int, y: int, color: str) -> None:
    draw.rounded_rectangle((x + s(6), y, x + s(56), y + s(66)), radius=s(8), fill="#FFFFFF", outline=color, width=s(4))
    draw.polygon([(x + s(42), y), (x + s(56), y + s(14)), (x + s(42), y + s(14))], fill="#EAF3F8", outline=color)
    for i in range(3):
        yy = y + s(25 + i * 13)
        draw.line((x + s(17), yy, x + s(45), yy), fill=color, width=s(3))


def draw_compare_icon(draw: ImageDraw.ImageDraw, x: int, y: int, color: str) -> None:
    for i, h in enumerate([54, 42, 64]):
        bx = x + s(i * 22)
        draw.rounded_rectangle((bx, y + s(68 - h), bx + s(14), y + s(68)), radius=s(5), fill=color)
    draw.line((x - s(2), y + s(68), x + s(60), y + s(68)), fill=color, width=s(4))


def draw_item(
    draw: ImageDraw.ImageDraw,
    x: int,
    y: int,
    title: str,
    desc: str,
    color: str,
    icon_name: str,
) -> None:
    draw_check(draw, x + s(18), y + s(34), color)
    icon_x = x + s(56)
    icon_y = y + s(2)
    if icon_name == "id":
        draw_id_icon(draw, icon_x, icon_y, color)
    elif icon_name == "doc":
        draw_document_icon(draw, icon_x, icon_y, color)
    elif icon_name == "compare":
        draw_compare_icon(draw, icon_x, icon_y, color)
    else:
        draw_clipboard_icon(draw, icon_x, icon_y, color)
    draw_left(draw, x + s(142), y + s(1), title, font(25, "bold"), COLORS["ink"])
    draw_left(draw, x + s(142), y + s(42), desc, font(17, "medium"), COLORS["muted"])


def paste_logo(img: Image.Image) -> None:
    if not LOGO.exists():
        return
    logo = Image.open(LOGO).convert("RGBA")
    target_w = s(116)
    ratio = target_w / logo.width
    logo = logo.resize((target_w, round(logo.height * ratio)), Image.Resampling.LANCZOS)
    pad = s(14)
    x = W - target_w - s(42)
    y = H - logo.height - s(28)
    draw = ImageDraw.Draw(img)
    draw.rounded_rectangle(
        (x - pad, y - pad, x + logo.width + pad, y + logo.height + pad),
        radius=s(12),
        fill=(255, 255, 255, 218),
    )
    img.alpha_composite(logo, (x, y))


def downsample(img: Image.Image) -> Image.Image:
    return img.resize((1200, 675), Image.Resampling.LANCZOS).convert("RGB")


def make_diagram(*, with_logo: bool) -> Image.Image:
    img = Image.new("RGBA", (W, H), COLORS["cream"])
    draw = ImageDraw.Draw(img)

    for x, y, r, color in [
        (92, 98, 4, "#D6C3A8"),
        (1090, 116, 5, "#C7D6CE"),
        (136, 590, 4, "#DEC697"),
        (1008, 578, 4, "#D6C3A8"),
    ]:
        draw.ellipse((s(x - r), s(y - r), s(x + r), s(y + r)), fill=color)

    draw_center(draw, s(600), s(62), "安全な買取業者を見分けるチェックリスト", font(35, "bold"), COLORS["ink"])
    draw_center(draw, s(600), s(111), "依頼前と当日の確認で、訪問買取トラブルを防ぐ", font(20, "medium"), COLORS["green"])

    left_card = (s(62), s(154), s(576), s(565))
    right_card = (s(624), s(154), s(1138), s(565))
    shadowed_round(img, left_card, COLORS["paper"], COLORS["line"])
    shadowed_round(img, right_card, COLORS["paper"], COLORS["line"])

    draw = ImageDraw.Draw(img)
    draw.rounded_rectangle((s(96), s(185), s(272), s(233)), radius=s(24), fill=COLORS["orange_soft"], outline="#E5C980", width=s(2))
    draw_center(draw, s(184), s(209), "業者を呼ぶ前", font(22, "bold"), COLORS["orange"])
    draw.rounded_rectangle((s(658), s(185), s(834), s(233)), radius=s(24), fill=COLORS["blue_soft"], outline="#BBD2DF", width=s(2))
    draw_center(draw, s(746), s(209), "訪問当日", font(22, "bold"), COLORS["blue"])

    left_items = [
        ("許可番号", "古物商許可と会社情報を確認", "id"),
        ("料金条件", "査定料・出張費・キャンセル料", "doc"),
        ("相見積もり", "2社以上で比べて即決を避ける", "compare"),
    ]
    right_items = [
        ("身分証", "担当者名・行商従業者証を確認", "id"),
        ("明細・書面", "品名・価格・契約条件を残す", "doc"),
        ("家族相談", "迷ったらその場で決めない", "clipboard"),
    ]

    for i, (title, desc, icon_name) in enumerate(left_items):
        draw_item(draw, s(106), s(270 + i * 86), title, desc, COLORS["orange"], icon_name)
    for i, (title, desc, icon_name) in enumerate(right_items):
        draw_item(draw, s(668), s(270 + i * 86), title, desc, COLORS["blue"], icon_name)

    draw.line((s(592), s(276), s(608), s(276)), fill=COLORS["burgundy"], width=s(5))
    draw.line((s(592), s(333), s(608), s(333)), fill=COLORS["burgundy"], width=s(5))
    draw.line((s(592), s(390), s(608), s(390)), fill=COLORS["burgundy"], width=s(5))
    draw.polygon([(s(612), s(333)), (s(592), s(320)), (s(592), s(346))], fill=COLORS["burgundy"])

    draw.rounded_rectangle((s(222), s(594), s(978), s(635)), radius=s(22), fill="#FFFFFF", outline=COLORS["line"], width=s(2))
    draw_center(draw, s(600), s(614), "合言葉は「条件を先に確認」「迷ったら持ち帰る」", font(19, "bold"), COLORS["burgundy"])

    if with_logo:
        paste_logo(img)
    return downsample(img)


def write_readme() -> None:
    text = """# 実家の不用品買取で失敗しない業者選び 画像

## 今回作成した図解

| 用途 | ファイル | サイズ | WordPress画像タイトル | ALT |
| --- | --- | --- | --- | --- |
| 記事内図解 | `trusted-buying-services-inline-checklist.png` | 1200 x 675 | 不用品買取の安全な業者を見分けるチェックリスト | 不用品買取の安全な業者を見分けるチェックリスト |

## 設置位置・キャプション

- 設置位置: 本文中のCMSブリーフ位置
- キャプション候補: 依頼前と当日のチェックポイント
- ロゴ: 右下に白背景付きセイリ部ロゴを配置済み

## 制作メモ

- 日本語ラベルの正確性を優先し、画像生成AIではなくローカルの図解生成スクリプトで作成
- 「業者を呼ぶ前」と「訪問当日」の確認項目を3つずつに絞り、文字の詰め込みすぎを避けた
- 画像生成素材にはロゴを描かせず、完成画像の後工程としてセイリ部ロゴを合成
"""
    (OUT_DIR / "README.md").write_text(text, encoding="utf-8")


def write_manifest(final_path: Path, source_path: Path) -> None:
    manifest = {
        "plan": str(PLAN),
        "images": [
            {
                "role": "記事内図解_slide",
                "file_name": final_path.name,
                "source": str(source_path),
                "output": str(final_path),
                "logo_mode": "white-backed:右下",
                "alt": "不用品買取の安全な業者を見分けるチェックリスト",
                "caption": "依頼前と当日のチェックポイント",
                "position": "本文中のCMSブリーフ位置",
            }
        ],
    }
    (OUT_DIR / "finish-manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    DRAFT_DIR.mkdir(parents=True, exist_ok=True)

    source_path = DRAFT_DIR / "trusted-buying-services-inline-checklist.png"
    final_path = OUT_DIR / "trusted-buying-services-inline-checklist.png"

    make_diagram(with_logo=False).save(source_path, quality=95)
    make_diagram(with_logo=True).save(final_path, quality=95)
    write_readme()
    write_manifest(final_path, source_path)

    print(f"Wrote {source_path}")
    print(f"Wrote {final_path}")


if __name__ == "__main__":
    main()
