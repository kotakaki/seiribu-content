#!/usr/bin/env python3
"""Generate Seiribu image-production plans from article Markdown files.

The script treats CMS image notes inside an article as production briefs, not as
final prompts. It adds a missing brand eyecatch brief, classifies each image by
production method, and writes Markdown/JSON output for the image-production step.
"""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PROJECT_ROOT = ROOT.parent
DEFAULT_CONFIG = ROOT / "config" / "image-engine.json"
DEFAULT_OUTPUT_DIR = ROOT / "image-briefs"


FIELD_ALIASES = {
    "画像の目的": "目的",
    "目的": "目的",
    "設置位置": "設置位置",
    "伝えたい内容": "伝えたい内容",
    "読者に伝えたい感情": "読者に伝えたい感情",
    "入れたい要素": "入れたい要素",
    "避けたい表現": "避けたい表現",
    "ALT": "ALT",
    "alt": "ALT",
    "キャプション候補": "キャプション候補",
    "ファイル名": "ファイル名",
    "タイトル文言": "タイトル文言",
    "サブタイトル文言": "サブタイトル文言",
    "種類": "種類",
    "指示": "指示",
}


@dataclass
class ArticleMeta:
    path: Path
    title: str
    slug: str
    main_kw: str = ""
    meta_description: str = ""
    target_reader: str = ""
    search_intent: str = ""
    headings: list[str] = field(default_factory=list)


@dataclass
class ImageBrief:
    role: str
    source_header: str
    fields: dict[str, str]
    index: int
    generated: bool = False
    method: str = ""
    size: str = ""
    file_name: str = ""
    wp_title: str = ""
    alt: str = ""
    final_prompt: str = ""
    canva_instructions: dict[str, str] = field(default_factory=dict)


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def relpath(path: Path) -> str:
    try:
        return str(path.relative_to(PROJECT_ROOT))
    except ValueError:
        return str(path)


def strip_markdown(text: str) -> str:
    text = re.sub(r"\*\*(.*?)\*\*", r"\1", text)
    text = re.sub(r"`(.*?)`", r"\1", text)
    return text.strip()


def extract_comment_block(text: str) -> str:
    match = re.search(
        r"<!--\s*===\s*凍結済み設計図（Invariants）\s*===(.*?)===\s*END\s*===\s*-->",
        text,
        flags=re.S,
    )
    return match.group(1).strip() if match else ""


def extract_section(comment: str, name: str) -> str:
    if not comment:
        return ""
    pattern = rf"【{re.escape(name)}】(.*?)(?=\n【|$)"
    match = re.search(pattern, comment, flags=re.S)
    return match.group(1).strip() if match else ""


def extract_list_value(section: str, label: str) -> str:
    match = re.search(rf"^\s*-\s*{re.escape(label)}:\s*(.+)$", section, flags=re.M)
    return match.group(1).strip() if match else ""


def find_title(text: str) -> str:
    for line in text.splitlines():
        if line.startswith("# ") and not line.startswith("## "):
            return strip_markdown(line[2:])
    return "untitled"


def slugify(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"\s+", "-", text)
    text = re.sub(r"[^a-z0-9\-ぁ-んァ-ン一-龥ー]", "", text)
    return text.strip("-") or "untitled"


def article_meta(path: Path, text: str) -> ArticleMeta:
    comment = extract_comment_block(text)
    basic = extract_section(comment, "記事基本情報")
    target_reader = extract_section(comment, "ターゲット読者")
    search_intent = extract_section(comment, "検索意図")
    title = find_title(text)
    headings = [
        strip_markdown(line[3:])
        for line in text.splitlines()
        if line.startswith("## ") and not line.startswith("### ")
    ]
    slug = extract_list_value(basic, "スラッグ") or slugify(path.stem)
    return ArticleMeta(
        path=path,
        title=title,
        slug=slug,
        main_kw=extract_list_value(basic, "メインKW"),
        meta_description=extract_list_value(basic, "Meta Description"),
        target_reader=target_reader,
        search_intent=search_intent,
        headings=headings,
    )


def normalize_key(key: str) -> str:
    key = key.strip().strip("-").strip()
    return FIELD_ALIASES.get(key, key)


def parse_cms_blocks(text: str) -> list[ImageBrief]:
    lines = text.splitlines()
    blocks: list[ImageBrief] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith("> [!CMS担当者へ"):
            header = line[2:].strip()
            raw: list[str] = [line]
            i += 1
            while i < len(lines) and (lines[i].startswith(">") or lines[i].strip() == ""):
                if lines[i].strip() == "":
                    break
                raw.append(lines[i])
                i += 1
            fields: dict[str, str] = {}
            for raw_line in raw[1:]:
                body = raw_line[1:].strip()
                body = body[2:].strip() if body.startswith("- ") else body
                match = re.match(r"([^：:]+)[：:]\s*(.*)$", body)
                if match:
                    fields[normalize_key(match.group(1))] = match.group(2).strip()
            blocks.append(
                ImageBrief(
                    role="",
                    source_header=header,
                    fields=fields,
                    index=len(blocks) + 1,
                )
            )
            continue
        i += 1
    return blocks


def split_title_for_eyecatch(title: str) -> tuple[str, str]:
    clean = strip_markdown(title)
    if "？" in clean:
        head, tail = clean.split("？", 1)
        return f"{head.strip()}？", tail.strip(" 　:：-") or "迷わない進め方"
    if "?" in clean:
        head, tail = clean.split("?", 1)
        return f"{head.strip()}?", tail.strip(" 　:：-") or "迷わない進め方"
    if "。" in clean:
        head, tail = clean.split("。", 1)
        return head.strip(), tail.strip() or "迷わない進め方"
    if len(clean) > 24:
        return clean[:24], clean[24:].strip() or "迷わない進め方"
    return clean, "悩みを整理して、次の一歩を選ぶ"


def eyecatch_visual(meta: ArticleMeta) -> str:
    joined = " ".join([meta.slug, meta.title, meta.main_kw, meta.search_intent])
    if "買取不可" in joined or "dispose" in joined:
        return (
            "日本の実家の明るい部屋で、40代から60代の子世代と高齢の親が、"
            "買取不可と言われた古い家電、小型家具、段ボールの荷物を前に、"
            "落ち着いて次の手放し方を相談している編集イラスト"
        )
    if "売れる" in joined or "sellable" in joined:
        return (
            "日本の実家のリビングで、古い本、カメラ、レコード、ブランドバッグ、"
            "箱入りの趣味品を親子が確認している明るい編集イラスト"
        )
    if "片付け" in joined or "cleanout" in joined:
        return (
            "日本の実家の室内で、親子が段ボールを前にして、売る物、残す物、"
            "処分する物を落ち着いて分けている編集イラスト"
        )
    if "捨て" in joined or "心理" in joined or "hoard" in joined:
        return (
            "日本の実家で、親子が思い出の品を前に落ち着いて話し合い、"
            "無理に捨てず確認しながら整理している編集イラスト"
        )
    return (
        "日本の実家の明るい部屋で、親子が古い物や段ボールを確認しながら、"
        "売る・残す・処分する判断をしている編集イラスト"
    )


def default_eyecatch(meta: ArticleMeta) -> ImageBrief:
    title, subtitle = split_title_for_eyecatch(meta.title)
    return ImageBrief(
        role="アイキャッチ",
        source_header="[generated] アイキャッチ画像",
        fields={
            "目的": "記事全体の第一印象を作り、読者に「自分の状況に近い」と感じてもらう",
            "読者に伝えたい感情": "焦らず、売れなかった物や実家の荷物を次の行動に分けられる安心感",
            "構図": "左上にロゴ、上部中央に大きな見出し、直下にサブタイトル、下部から中央に人物と実家の物を配置",
            "入れたい人物・物": eyecatch_visual(meta),
            "避けたい表現": "ゴミ屋敷、暗い遺品整理、札束、高額査定、不用品回収業者だけを推す広告感",
            "タイトル文言": title,
            "サブタイトル文言": subtitle,
            "ALT": f"{title}について、実家の荷物を家族で確認しながら整理している様子",
            "ファイル名": f"{meta.slug}-eyecatch-branded.png",
        },
        index=0,
        generated=True,
    )


def infer_role(block: ImageBrief) -> str:
    if block.role == "アイキャッチ" or block.generated:
        return "アイキャッチ"
    text = " ".join([block.source_header, *block.fields.values()])
    explicit = block.fields.get("種類", "")
    if "アイキャッチ" in text:
        return "アイキャッチ"
    if "写真" in explicit or "写真風" in text:
        return "写真風素材"
    if "図解" in text or re.search(r"比較|表|フロー|ステップ|分類|3つ|4つ|チェックリスト|マトリクス|選択肢|理由", text):
        return "記事内図解"
    return "記事内イメージ"


def infer_suffix(block: ImageBrief) -> str:
    text = " ".join(
        block.fields.get(key, "")
        for key in ["目的", "伝えたい内容", "入れたい要素", "ALT", "キャプション候補", "指示"]
    )
    candidates = [
        ("NG|OK|勝手に捨てる|責める|比較する|選んで|保留箱|聖域", "ng-ok"),
        ("ためこみ症|物持ち|スペクトラム|境界線|専門家", "spectrum"),
        ("ギター|工具|写真立て|父親|思い出|感情を託す", "male-memory"),
        ("損失回避|拡張自己|アニミズム|判断疲れ|孤独感|心理", "psychology"),
        ("鉄則|原則", "principles"),
        ("3箱|箱|仕分け|分類", "three-boxes"),
        ("選択肢|自治体|寄付|回収業者|費用|手間|スピード", "options"),
        ("順番|ステップ|進める", "steps"),
        ("理由|買取不可|断られる", "reasons"),
        ("チェック", "checklist"),
        ("比較", "comparison"),
        ("流れ|フロー", "flow"),
    ]
    for pattern, suffix in candidates:
        if re.search(pattern, text):
            return suffix
    return f"inline-{block.index:02d}"


def ensure_png_filename(name: str) -> str:
    clean = name.strip().strip("`")
    if not clean:
        return clean
    suffix = Path(clean).suffix.lower()
    return clean if suffix in {".png", ".jpg", ".jpeg", ".webp"} else f"{clean}.png"


def infer_wp_title(block: ImageBrief, meta: ArticleMeta) -> str:
    alt = block.fields.get("ALT", "")
    if alt:
        return re.sub(r"（.*?）", "", alt).strip("。")
    if block.role == "アイキャッチ":
        return f"{meta.title}のアイキャッチ"
    position = block.fields.get("設置位置", "")
    h2 = re.search(r"H2「(.+?)」", position)
    return h2.group(1) if h2 else f"{meta.title}の図解"


def prompt_for(block: ImageBrief, meta: ArticleMeta, config: dict[str, Any]) -> str:
    avoid = "、".join(config.get("avoid", []))
    tone = "、".join(config.get("tone", []))
    if block.role == "アイキャッチ":
        return (
            "セイリ部のブランド型アイキャッチ用の背景・人物素材を作る。"
            "画像内に文字は入れない。"
            f"構図: {block.fields.get('構図', config['eyecatch']['layout'])}。"
            f"主なビジュアル: {block.fields.get('入れたい人物・物', '')}。"
            f"トーン: {tone}。"
            f"避ける表現: {block.fields.get('避けたい表現', avoid)}。"
            "上部にはタイトルとサブタイトルをCanvaで載せるため、十分な余白を残す。"
            "人物の顔や重要な品物にロゴが重ならない余白も確保する。"
        )
    if block.role == "記事内図解":
        labels = block.fields.get("入れたい要素") or block.fields.get("伝えたい内容") or block.fields.get("指示")
        return (
            "日本語ラベルを正確に読ませる記事内図解を作る。"
            "画像生成AIに文字を任せず、Canva、Pillow、SVGなどのレイアウト制御で制作する。"
            f"入れる内容: {labels}。"
            f"目的: {block.fields.get('目的', '')}。"
            f"避ける表現: {block.fields.get('避けたい表現', avoid)}。"
            "右下の余白にセイリ部ロゴを小さく配置する。"
        )
    return (
        f"{meta.title}の記事内で使う温かい編集イラスト素材を作る。"
        f"目的: {block.fields.get('目的', '')}。"
        f"入れたい要素: {block.fields.get('入れたい要素', block.fields.get('指示', ''))}。"
        f"トーン: {tone}。"
        "画像内文字は入れない。"
        f"避ける表現: {block.fields.get('避けたい表現', avoid)}。"
    )


def enrich_briefs(meta: ArticleMeta, blocks: list[ImageBrief], config: dict[str, Any]) -> list[ImageBrief]:
    briefs = list(blocks)
    has_eyecatch = any("アイキャッチ" in " ".join([b.source_header, *b.fields.values()]) for b in briefs)
    if not has_eyecatch:
        briefs.insert(0, default_eyecatch(meta))

    inline_count = 0
    for block in briefs:
        block.role = infer_role(block)
        if block.role == "アイキャッチ":
            block.method = "Canvaテンプレ + 画像生成素材"
            block.size = config["eyecatch"]["size"]
            block.file_name = ensure_png_filename(
                block.fields.get("ファイル名") or f"{meta.slug}-eyecatch-branded.png"
            )
            block.canva_instructions = {
                "template_url": config.get("canva_template_url", ""),
                "title": block.fields.get("タイトル文言") or split_title_for_eyecatch(meta.title)[0],
                "subtitle": block.fields.get("サブタイトル文言") or split_title_for_eyecatch(meta.title)[1],
                "logo": config.get("logo_path", ""),
                "logo_position": config["eyecatch"].get("logo_position", "左上"),
                "headline_font": config["eyecatch"].get("headline_font", ""),
                "subtitle_font": config["eyecatch"].get("subtitle_font", ""),
            }
        elif block.role == "記事内図解":
            inline_count += 1
            block.method = config["inline_diagram"]["method"]
            block.size = config["inline_diagram"]["size"]
            block.file_name = ensure_png_filename(
                block.fields.get("ファイル名") or f"{meta.slug}-inline-{infer_suffix(block)}.png"
            )
        else:
            inline_count += 1
            block.method = "画像生成素材"
            block.size = "1200 x 800"
            suffix = "photo" if block.role == "写真風素材" else f"inline-{infer_suffix(block)}"
            block.file_name = ensure_png_filename(block.fields.get("ファイル名") or f"{meta.slug}-{suffix}.png")

        block.alt = block.fields.get("ALT") or f"{meta.title}に関する{block.role}"
        block.wp_title = infer_wp_title(block, meta)
        block.final_prompt = prompt_for(block, meta, config)

    return sorted(briefs, key=lambda brief: 0 if brief.role == "アイキャッチ" else 1)


def position_for(brief: ImageBrief) -> str:
    if brief.fields.get("設置位置"):
        return brief.fields["設置位置"]
    return "アイキャッチ" if brief.role == "アイキャッチ" else "本文中のCMSブリーフ位置"


def quality_notes(briefs: list[ImageBrief]) -> list[str]:
    eyecatches = [b for b in briefs if b.role == "アイキャッチ"]
    inline = [b for b in briefs if b.role != "アイキャッチ"]
    notes = []
    if not eyecatches:
        notes.append("アイキャッチがありません。1枚追加してください。")
    elif eyecatches[0].generated:
        notes.append("記事内にアイキャッチ指定がなかったため、エンジンがブランド型アイキャッチを補完しました。")
    else:
        notes.append("記事内のアイキャッチ指定を利用しています。")

    if len(inline) < 2:
        notes.append("本文画像が少なめです。ピラー記事では図解をもう1枚検討してください。")
    elif len(inline) > 3:
        notes.append("本文画像が多めです。公開時は重要な2〜3枚に絞ることも検討してください。")
    else:
        notes.append("本文画像の枚数は適正範囲です。")
    return notes


def markdown_plan(meta: ArticleMeta, briefs: list[ImageBrief], config: dict[str, Any]) -> str:
    lines: list[str] = [
        f"# 画像制作プラン: {meta.title}",
        "",
        "## 記事情報",
        "",
        f"- 記事ファイル: `{relpath(meta.path)}`",
        f"- スラッグ: `{meta.slug}`",
        f"- メインKW: {meta.main_kw or '未設定'}",
        f"- Canvaテンプレ: {config.get('canva_template_url', '未設定')}",
        f"- ロゴ: `{config.get('logo_path', '')}`",
        "",
        "## 判定サマリー",
        "",
        "| No | 用途 | 制作方法 | サイズ | ファイル名 | 設置位置 |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for no, brief in enumerate(briefs, 1):
        lines.append(
            f"| {no} | {brief.role} | {brief.method} | {brief.size} | `{brief.file_name}` | {position_for(brief)} |"
        )
    lines += ["", "## 制作ブリーフ", ""]

    for no, brief in enumerate(briefs, 1):
        lines += [
            f"### {no}. {brief.role}",
            "",
            f"- ファイル名: `{brief.file_name}`",
            f"- WordPress画像タイトル: {brief.wp_title}",
            f"- ALT: {brief.alt}",
            f"- サイズ: {brief.size}",
            f"- 制作方法: {brief.method}",
            f"- 設置位置: {position_for(brief)}",
            f"- キャプション候補: {brief.fields.get('キャプション候補', 'なし')}",
            "",
            "#### 制作意図",
            "",
            f"- 目的: {brief.fields.get('目的', '未指定')}",
            f"- 読者に伝えたい感情: {brief.fields.get('読者に伝えたい感情', '未指定')}",
            f"- 入れたい要素: {brief.fields.get('入れたい要素', brief.fields.get('入れたい人物・物', brief.fields.get('伝えたい内容', '未指定')))}",
            f"- 避けたい表現: {brief.fields.get('避けたい表現', '未指定')}",
            "",
            "#### 最終プロンプト",
            "",
            brief.final_prompt,
            "",
        ]
        if brief.canva_instructions:
            lines += [
                "#### Canva流し込み",
                "",
                f"- テンプレートURL: {brief.canva_instructions.get('template_url', '')}",
                f"- タイトル: {brief.canva_instructions.get('title', '')}",
                f"- サブタイトル: {brief.canva_instructions.get('subtitle', '')}",
                f"- ロゴ: `{brief.canva_instructions.get('logo', '')}`",
                f"- ロゴ位置: {brief.canva_instructions.get('logo_position', '')}",
                f"- 見出しフォント: {brief.canva_instructions.get('headline_font', '')}",
                f"- サブタイトルフォント: {brief.canva_instructions.get('subtitle_font', '')}",
                "",
            ]

    lines += ["## 品質チェック", ""]
    lines += [f"- {note}" for note in quality_notes(briefs)]
    lines += [
        "- 日本語ラベルがある図解は、画像生成AIに文字を任せずレイアウト生成で作る。",
        "- ロゴは見出し、人物の顔、重要な品物に重ねない。",
        "- 暗い遺品整理、ゴミ屋敷、高額査定広告の印象を避ける。",
        "",
    ]
    return "\n".join(lines)


def json_plan(meta: ArticleMeta, briefs: list[ImageBrief], config: dict[str, Any]) -> dict[str, Any]:
    return {
        "article": {
            "path": relpath(meta.path),
            "title": meta.title,
            "slug": meta.slug,
            "main_kw": meta.main_kw,
            "target_reader": meta.target_reader,
            "search_intent": meta.search_intent,
        },
        "brand": {
            "name": config.get("brand_name"),
            "canva_template_url": config.get("canva_template_url"),
            "logo_path": config.get("logo_path"),
        },
        "images": [
            {
                "role": b.role,
                "generated": b.generated,
                "file_name": b.file_name,
                "size": b.size,
                "method": b.method,
                "wp_title": b.wp_title,
                "alt": b.alt,
                "position": position_for(b),
                "caption": b.fields.get("キャプション候補", ""),
                "fields": b.fields,
                "final_prompt": b.final_prompt,
                "canva_instructions": b.canva_instructions,
            }
            for b in briefs
        ],
        "quality_notes": quality_notes(briefs),
    }


def write_plan(article: Path, config: dict[str, Any], output_dir: Path, output_format: str) -> list[Path]:
    text = article.read_text(encoding="utf-8")
    meta = article_meta(article, text)
    briefs = enrich_briefs(meta, parse_cms_blocks(text), config)
    output_dir.mkdir(parents=True, exist_ok=True)
    written: list[Path] = []

    if output_format in {"md", "both"}:
        md_path = output_dir / f"{meta.slug}-image-plan.md"
        md_path.write_text(markdown_plan(meta, briefs, config), encoding="utf-8")
        written.append(md_path)
    if output_format in {"json", "both"}:
        json_path = output_dir / f"{meta.slug}-image-plan.json"
        json_path.write_text(
            json.dumps(json_plan(meta, briefs, config), ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        written.append(json_path)
    return written


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate Seiribu image plans from article Markdown files."
    )
    parser.add_argument("articles", nargs="+", type=Path, help="Article Markdown file(s).")
    parser.add_argument("--config", type=Path, default=DEFAULT_CONFIG)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument(
        "--format",
        choices=["md", "json", "both"],
        default="both",
        help="Output format. Default: both.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    config = read_json(args.config)
    all_written: list[Path] = []
    for article in args.articles:
        all_written.extend(write_plan(article, config, args.output_dir, args.format))
    for path in all_written:
        print(f"Wrote {path}")


if __name__ == "__main__":
    main()
