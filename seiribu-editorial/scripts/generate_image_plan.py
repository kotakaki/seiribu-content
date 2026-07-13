#!/usr/bin/env python3
"""Generate Seiribu image-production plans from article Markdown files.

The script treats CMS image notes inside an article as production briefs, not as
final prompts. It classifies each requested image by production method and writes
Markdown/JSON output for the image-production step. Missing eyecatches are
reported instead of silently filled with a generic scene.
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
    "画像種別": "種類",
    "素材種別": "種類",
    "アセット種別": "種類",
    "画像のアイデア": "入れたい要素",
    "画像のアイデア（情景・図解の具体案）": "入れたい要素",
    "画像概要": "入れたい要素",
    "入れたい人物・物": "入れたい人物・物",
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
    included: bool = True
    omitted_reason: str = ""
    method: str = ""
    size: str = ""
    aspect_ratio: str = ""
    file_name: str = ""
    wp_title: str = ""
    alt: str = ""
    final_prompt: str = ""
    local_composition: dict[str, Any] = field(default_factory=dict)
    canva_instructions: dict[str, Any] = field(default_factory=dict)


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
    if key.startswith("画像のアイデア"):
        return "入れたい要素"
    if key.startswith("入れたい要素"):
        return "入れたい要素"
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


def infer_role(block: ImageBrief) -> str:
    if block.role == "アイキャッチ" or block.generated:
        return "アイキャッチ"
    text = " ".join([block.source_header, *block.fields.values()])
    explicit = block.fields.get("種類", "")
    if "アイキャッチ" in text and re.search(r"素材|Canva|透過|背景なし|切り抜き|カットアウト", text):
        return "アイキャッチ素材"
    if "アイキャッチ" in text:
        return "アイキャッチ"
    if re.search(r"図解用小物|小物素材|アイコン素材|単体アイコン|挿絵パーツ", text):
        return "図解用小物素材"
    if "写真" in explicit or "写真風" in text:
        return "写真風素材"
    if "記事内イメージ" in explicit or re.search(r"情景|情景イラスト|風景|様子|場面", text):
        return "記事内イメージ"
    if "図解" in explicit or re.search(
        r"図解|比較表|フロー|ステップ図|手順図|分類図|チェックリスト|マトリクス|早見表|3択比較|比較軸|チャート",
        text,
    ):
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


def dedupe_file_names(briefs: list[ImageBrief]) -> None:
    seen: dict[str, int] = {}
    for brief in briefs:
        count = seen.get(brief.file_name, 0) + 1
        seen[brief.file_name] = count
        if count == 1:
            continue
        path = Path(brief.file_name)
        brief.file_name = f"{path.stem}-{count}{path.suffix}"


def infer_wp_title(block: ImageBrief, meta: ArticleMeta) -> str:
    alt = block.fields.get("ALT", "")
    if alt:
        return re.sub(r"（.*?）", "", alt).strip("。")
    if block.role == "アイキャッチ":
        return f"{meta.title}のアイキャッチ"
    position = block.fields.get("設置位置", "")
    h2 = re.search(r"H2「(.+?)」", position)
    return h2.group(1) if h2 else f"{meta.title}の図解"


def brief_visual(block: ImageBrief) -> str:
    return (
        block.fields.get("入れたい要素")
        or block.fields.get("入れたい人物・物")
        or block.fields.get("伝えたい内容")
        or block.fields.get("指示")
        or "記事内容に合う人物と物"
    )


def forbidden_generation_text(config: dict[str, Any]) -> str:
    return ", ".join(config.get("generation_forbidden", []))


def generation_style(config: dict[str, Any], key: str) -> str:
    return config.get("generation_style", {}).get(key, "")


def generation_tone(config: dict[str, Any], *, exclude_family: bool = False) -> str:
    items = config.get("tone", [])
    if exclude_family:
        items = [item for item in items if "親子" not in item and "家族" not in item]
    return "、".join(items)


def brand_signature(config: dict[str, Any]) -> dict[str, Any]:
    return config.get("brand_signature", {})


def local_composition_config(config: dict[str, Any]) -> dict[str, Any]:
    return config.get("local_composition", {})


def mode_settings(config: dict[str, Any], mode: str) -> dict[str, Any]:
    return config.get("modes", {}).get(mode, {})


def resolve_mode(config: dict[str, Any], requested: str | None = None) -> str:
    mode = requested or config.get("default_mode", "standard")
    if mode not in {"light", "standard"}:
        raise ValueError(f"Unsupported image engine mode: {mode}")
    return mode


def active_briefs(briefs: list[ImageBrief]) -> list[ImageBrief]:
    return [brief for brief in briefs if brief.included]


def omitted_briefs(briefs: list[ImageBrief]) -> list[ImageBrief]:
    return [brief for brief in briefs if not brief.included]


def compact_prompt_enabled(config: dict[str, Any], mode: str) -> bool:
    return bool(mode_settings(config, mode).get("compact_prompts", False))


def canva_detail_enabled(config: dict[str, Any], mode: str) -> bool:
    return not bool(mode_settings(config, mode).get("omit_canva_detail", False))


def apply_mode_limits(briefs: list[ImageBrief], config: dict[str, Any], mode: str) -> None:
    if mode != "light":
        return

    settings = mode_settings(config, mode)
    max_eyecatches = int(settings.get("max_eyecatches", 1))
    max_inline = int(settings.get("max_inline_images", 1))
    eyecatch_seen = 0
    inline_seen = 0

    for brief in briefs:
        if brief.role in {"アイキャッチ", "アイキャッチ素材"}:
            eyecatch_seen += 1
            if eyecatch_seen > max_eyecatches:
                brief.included = False
                brief.omitted_reason = "lightモードではアイキャッチ系画像を1件までに絞ります。"
            continue

        inline_seen += 1
        if inline_seen > max_inline:
            brief.included = False
            brief.omitted_reason = f"lightモードでは本文画像を{max_inline}件までに絞ります。必要なら --mode standard で出力します。"


def build_local_composition(block: ImageBrief, meta: ArticleMeta, config: dict[str, Any]) -> dict[str, Any]:
    composition = local_composition_config(config)
    title, subtitle = split_title_for_eyecatch(meta.title)
    return {
        "standard": composition.get("standard", True),
        "engine": composition.get("engine", "Pillow"),
        "script": composition.get("script", "seiribu-editorial/scripts/compose_eyecatch.py"),
        "title": block.fields.get("タイトル文言") or title,
        "subtitle": block.fields.get("サブタイトル文言") or subtitle,
        "logo": config.get("logo_path", ""),
        "logo_required": brand_signature(config).get("required_in_final_outputs", True),
        "logo_position": composition.get("logo_position", config["eyecatch"].get("logo_position", "左上")),
        "logo_rule": brand_signature(config).get("rule", ""),
        "output_size": composition.get("eyecatch_output_size", config["eyecatch"].get("size", "1200 x 630")),
        "source_material_file": block.file_name if block.role == "アイキャッチ素材" else "",
        "output_file": f"{meta.slug}-eyecatch-branded.png" if block.role == "アイキャッチ素材" else block.file_name,
        "headline_font": config["eyecatch"].get("headline_font", ""),
        "fallback_headline_font": config["eyecatch"].get("fallback_headline_font", ""),
        "subtitle_font": config["eyecatch"].get("subtitle_font", ""),
        "canva_role": composition.get("canva_role", "任意の手動微調整"),
    }


def compact_prompt_for(block: ImageBrief, meta: ArticleMeta, config: dict[str, Any]) -> str:
    avoid = block.fields.get("避けたい表現") or "暗さ、ゴミ屋敷感、高額査定広告感、既存構図の流用"
    forbidden = forbidden_generation_text(config)
    visual = brief_visual(block)
    purpose = block.fields.get("目的", "")
    reuse_guard = "Do not reuse composition, character placement, object placement, or background concept from existing Seiribu article images."

    if block.role == "記事内図解":
        labels = block.fields.get("入れたい要素") or block.fields.get("伝えたい内容") or block.fields.get("指示") or "未指定"
        return (
            f"画像生成AIには渡さない。{block.size} / {block.aspect_ratio} の図解として、Pillow・SVG・Canvaなどで制作。"
            f"内容: {labels}。目的: {block.fields.get('目的', '')}。"
            "日本語ラベル、表、矢印、ロゴは後工程で正確に配置する。"
        )

    if block.role == "アイキャッチ素材":
        return (
            f"Text-free Seiribu eyecatch cutout asset. Aspect ratio: {block.aspect_ratio}. "
            f"Style: {generation_style(config, 'cutout')}. Subject: {visual}. "
            f"Purpose: {purpose}. Tone: {generation_tone(config, exclude_family=True)}. "
            "Transparent background, or single flat light background for easy removal. "
            "No room, wall, floor, shadow, title area, logo area, frame. "
            f"Avoid: {forbidden}; {avoid}. {reuse_guard}"
        )

    if block.role == "アイキャッチ":
        return (
            f"Text-free Seiribu eyecatch illustration for '{meta.title}'. Aspect ratio: {block.aspect_ratio}. "
            f"Style: {generation_style(config, 'illustration')}. Main visual: {visual}. "
            f"Purpose: {purpose}. Tone: {generation_tone(config)}. "
            "Leave calm space for local title/logo composition; do not draw text panels. "
            f"Avoid: {forbidden}; {avoid}. {reuse_guard}"
        )

    if block.role == "図解用小物素材":
        return (
            f"Small standalone Seiribu diagram asset. Aspect ratio: {block.aspect_ratio}. "
            f"Style: {generation_style(config, 'cutout')}. Subject: {visual}. "
            f"Purpose: {purpose}. "
            f"Avoid: {forbidden}; {avoid}."
        )

    if block.role == "写真風素材":
        return (
            f"Bright realistic editorial photo-style visual for '{meta.title}'. Aspect ratio: {block.aspect_ratio}. "
            f"Main visual: {visual}. Natural daylight, clean lived-in Japanese home. "
            f"Purpose: {purpose}. Tone: {generation_tone(config)}. "
            f"Avoid: {forbidden}; {avoid}. {reuse_guard}"
        )

    return (
        f"Warm text-free Seiribu editorial illustration for '{meta.title}'. Aspect ratio: {block.aspect_ratio}. "
        f"Style: {generation_style(config, 'illustration')}. Main visual: {visual}. "
        f"Purpose: {purpose}. Tone: {generation_tone(config)}. "
        f"Avoid: {forbidden}; {avoid}. {reuse_guard}"
    )


def prompt_for(block: ImageBrief, meta: ArticleMeta, config: dict[str, Any], mode: str = "standard") -> str:
    if compact_prompt_enabled(config, mode):
        return compact_prompt_for(block, meta, config)

    avoid = "、".join(config.get("avoid", []))
    forbidden = forbidden_generation_text(config)
    if block.role == "アイキャッチ素材":
        visual = brief_visual(block)
        return (
            f"Create an eyecatch cutout asset for the Seiribu article '{meta.title}'. "
            f"Aspect ratio: {block.aspect_ratio}. "
            f"Style: {generation_style(config, 'cutout')}. "
            "Transparent background if possible; if transparency is not available, use a single flat light background that is easy to remove. "
            "Do not include a room, wall, floor, cast shadow, title area, logo area, or decorative frame. "
            f"Main subject: {visual}. "
            f"Purpose: {block.fields.get('目的', '')}. "
            f"Tone: {generation_tone(config, exclude_family=True)}. "
            f"Must avoid: {forbidden}. "
            f"Also avoid: {block.fields.get('避けたい表現', avoid)}. "
            "Do not reuse the composition, character placement, object placement, or background concept from any existing Seiribu article image."
        )
    if block.role == "アイキャッチ":
        return (
            f"Create a text-free eyecatch background and subject illustration for the Seiribu article '{meta.title}'. "
            f"Aspect ratio: {block.aspect_ratio}. "
            f"Style: {generation_style(config, 'illustration')}. "
            "This image will be finished later with the local Seiribu Pillow compositor, so leave calm uncluttered space for a title and logo to be added later, but do not draw any placeholder cards or panels with text. "
            f"Composition: {block.fields.get('構図', config['eyecatch']['layout'])}. "
            f"Main visual: {brief_visual(block)}. "
            f"Purpose: {block.fields.get('目的', '')}. "
            f"Tone: {generation_tone(config)}. "
            f"Must avoid: {forbidden}. "
            f"Also avoid: {block.fields.get('避けたい表現', avoid)}. "
            "Do not reuse the composition, character placement, object placement, or background concept from any existing Seiribu article image."
        )
    if block.role == "記事内図解":
        labels = block.fields.get("入れたい要素") or block.fields.get("伝えたい内容") or block.fields.get("指示") or "未指定"
        return (
            "画像生成AIには渡さない。Canva、Pillow、SVGなど、文字とレイアウトを制御できる方法で記事内図解を制作する。"
            f"最終サイズ: {block.size}。アスペクト比: {block.aspect_ratio}。"
            f"入れる内容: {labels}。"
            f"目的: {block.fields.get('目的', '')}。"
            f"避ける表現: {block.fields.get('避けたい表現', avoid)}。"
            "日本語ラベル、表、矢印、比較軸は後工程で正確に配置する。ロゴは右下などの余白に小さく配置し、本文ラベルを邪魔しない。"
        )
    if block.role == "図解用小物素材":
        return (
            f"Create a small supporting visual asset for a Seiribu article diagram. "
            f"Aspect ratio: {block.aspect_ratio}. "
            f"Style: {generation_style(config, 'cutout')}. "
            "Make it a simple standalone object or icon-like illustration that can be placed inside a Canva, SVG, or Python-made diagram. "
            "Use transparent background if possible; otherwise use a single flat light background that is easy to remove. "
            f"Main subject: {brief_visual(block)}. "
            f"Purpose: {block.fields.get('目的', '')}. "
            f"Must avoid: {forbidden}. "
            f"Also avoid: {block.fields.get('避けたい表現', avoid)}."
        )
    if block.role == "写真風素材":
        return (
            f"Create a bright realistic editorial photo-style visual for the Seiribu article '{meta.title}'. "
            f"Aspect ratio: {block.aspect_ratio}. "
            f"Style: {generation_style(config, 'photo')}. "
            f"Main visual: {brief_visual(block)}. "
            f"Purpose: {block.fields.get('目的', '')}. "
            f"Tone: {generation_tone(config)}. "
            f"Must avoid: {forbidden}. "
            f"Also avoid: {block.fields.get('避けたい表現', avoid)}."
        )
    return (
        f"Create a warm text-free editorial illustration for the Seiribu article '{meta.title}'. "
        f"Aspect ratio: {block.aspect_ratio}. "
        f"Style: {generation_style(config, 'illustration')}. "
        f"Main visual: {brief_visual(block)}. "
        f"Purpose: {block.fields.get('目的', '')}. "
        f"Tone: {generation_tone(config)}. "
        f"Must avoid: {forbidden}. "
        f"Also avoid: {block.fields.get('避けたい表現', avoid)}."
    )


def enrich_briefs(
    meta: ArticleMeta,
    blocks: list[ImageBrief],
    config: dict[str, Any],
    mode: str | None = None,
) -> list[ImageBrief]:
    mode = resolve_mode(config, mode)
    briefs = list(blocks)

    inline_count = 0
    for block in briefs:
        block.role = infer_role(block)
        if block.role == "アイキャッチ素材":
            block.method = config.get("eyecatch_material", {}).get("method", "画像生成素材 + 背景透過（ローカル合成で仕上げ）")
            block.size = config.get("eyecatch_material", {}).get("size", "1536 x 1024")
            block.aspect_ratio = config.get("eyecatch_material", {}).get("aspect_ratio", "3:2")
            block.file_name = ensure_png_filename(
                block.fields.get("ファイル名") or f"{meta.slug}-eyecatch-cutout.png"
            )
            block.local_composition = build_local_composition(block, meta, config)
            block.canva_instructions = {
                "status": "optional_manual",
                "template_url": config.get("canva_template_url", ""),
                "title": block.fields.get("タイトル文言") or split_title_for_eyecatch(meta.title)[0],
                "subtitle": block.fields.get("サブタイトル文言") or split_title_for_eyecatch(meta.title)[1],
                "logo": config.get("logo_path", ""),
                "logo_required": brand_signature(config).get("required_in_final_outputs", True),
                "logo_rule": brand_signature(config).get("rule", ""),
                "logo_position": config["eyecatch"].get("logo_position", "左上"),
                "headline_font": config["eyecatch"].get("headline_font", ""),
                "subtitle_font": config["eyecatch"].get("subtitle_font", ""),
            }
        elif block.role == "アイキャッチ":
            block.method = "画像生成素材 + ローカル合成（Pillow）"
            block.size = config["eyecatch"]["size"]
            block.aspect_ratio = config["eyecatch"].get("aspect_ratio", "16:9")
            block.file_name = ensure_png_filename(
                block.fields.get("ファイル名") or f"{meta.slug}-eyecatch-branded.png"
            )
            block.local_composition = build_local_composition(block, meta, config)
            block.canva_instructions = {
                "status": "optional_manual",
                "template_url": config.get("canva_template_url", ""),
                "title": block.fields.get("タイトル文言") or split_title_for_eyecatch(meta.title)[0],
                "subtitle": block.fields.get("サブタイトル文言") or split_title_for_eyecatch(meta.title)[1],
                "logo": config.get("logo_path", ""),
                "logo_required": brand_signature(config).get("required_in_final_outputs", True),
                "logo_rule": brand_signature(config).get("rule", ""),
                "logo_position": config["eyecatch"].get("logo_position", "左上"),
                "headline_font": config["eyecatch"].get("headline_font", ""),
                "subtitle_font": config["eyecatch"].get("subtitle_font", ""),
            }
        elif block.role == "記事内図解":
            inline_count += 1
            block.method = config["inline_diagram"]["method"]
            block.size = config["inline_diagram"]["size"]
            block.aspect_ratio = config["inline_diagram"].get("aspect_ratio", "3:2")
            block.file_name = ensure_png_filename(
                block.fields.get("ファイル名") or f"{meta.slug}-inline-{infer_suffix(block)}.png"
            )
        elif block.role == "図解用小物素材":
            inline_count += 1
            material_config = config.get("diagram_asset", {})
            block.method = material_config.get("method", "図解用小物素材")
            block.size = material_config.get("size", "1024 x 1024")
            block.aspect_ratio = material_config.get("aspect_ratio", "1:1")
            block.file_name = ensure_png_filename(
                block.fields.get("ファイル名") or f"{meta.slug}-diagram-asset-{infer_suffix(block)}.png"
            )
        else:
            inline_count += 1
            material_config = config.get("photo_material", {}) if block.role == "写真風素材" else config.get("inline_image", {})
            block.method = material_config.get("method", "画像生成素材")
            block.size = material_config.get("size", "1200 x 800")
            block.aspect_ratio = material_config.get("aspect_ratio", "3:2")
            suffix = "photo" if block.role == "写真風素材" else f"inline-{infer_suffix(block)}"
            block.file_name = ensure_png_filename(block.fields.get("ファイル名") or f"{meta.slug}-{suffix}.png")

        block.alt = block.fields.get("ALT") or f"{meta.title}に関する{block.role}"
        block.wp_title = infer_wp_title(block, meta)
    dedupe_file_names(briefs)
    apply_mode_limits(briefs, config, mode)
    for block in briefs:
        if block.role in {"アイキャッチ", "アイキャッチ素材"}:
            block.local_composition = build_local_composition(block, meta, config)

        if not canva_detail_enabled(config, mode):
            block.canva_instructions = {}

        block.final_prompt = prompt_for(block, meta, config, mode) if block.included else ""

    return sorted(briefs, key=lambda brief: 0 if brief.role in {"アイキャッチ", "アイキャッチ素材"} else 1)


def position_for(brief: ImageBrief) -> str:
    if brief.fields.get("設置位置"):
        return brief.fields["設置位置"]
    if brief.role == "アイキャッチ素材":
        return "アイキャッチ合成用素材"
    return "アイキャッチ" if brief.role == "アイキャッチ" else "本文中のCMSブリーフ位置"


def quality_notes(briefs: list[ImageBrief], mode: str = "standard") -> list[str]:
    active = active_briefs(briefs)
    omitted = omitted_briefs(briefs)
    eyecatches = [b for b in active if b.role in {"アイキャッチ", "アイキャッチ素材"}]
    inline = [b for b in active if b.role not in {"アイキャッチ", "アイキャッチ素材"}]
    notes = []
    if not eyecatches:
        notes.append("アイキャッチまたはアイキャッチ合成用素材の指定がありません。自動補完はしません。")
    elif eyecatches[0].role == "アイキャッチ素材":
        notes.append("ローカル合成で仕上げるためのアイキャッチ素材指定を利用しています。")
    else:
        notes.append("記事内のアイキャッチ指定を利用しています。")

    if mode == "light" and omitted:
        notes.append("本文画像はlightモードの初回範囲です。追加画像は保留分から必要に応じて選びます。")
    elif len(inline) < 2:
        notes.append("本文画像が少なめです。ピラー記事では図解をもう1枚検討してください。")
    elif len(inline) > 3:
        notes.append("本文画像が多めです。公開時は重要な2〜3枚に絞ることも検討してください。")
    else:
        notes.append("本文画像の枚数は適正範囲です。")

    if mode == "light":
        if omitted:
            notes.append(f"lightモードのため、初回制作は{len(active)}件に絞り、{len(omitted)}件を保留しました。")
        else:
            notes.append("lightモードですが、保留対象はありません。")
    return notes


def markdown_plan(meta: ArticleMeta, briefs: list[ImageBrief], config: dict[str, Any], mode: str | None = None) -> str:
    mode = resolve_mode(config, mode)
    active = active_briefs(briefs)
    omitted = omitted_briefs(briefs)
    settings = mode_settings(config, mode)
    lines: list[str] = [
        f"# 画像制作プラン: {meta.title}",
        "",
        "## 記事情報",
        "",
        f"- 記事ファイル: `{relpath(meta.path)}`",
        f"- スラッグ: `{meta.slug}`",
        f"- メインKW: {meta.main_kw or '未設定'}",
        f"- 出力モード: {mode}（{settings.get('description', '標準出力')}）",
        f"- 標準仕上げ: ローカル合成（{local_composition_config(config).get('engine', 'Pillow')}）",
        f"- Canvaテンプレ: {config.get('canva_template_url', '未設定')}（任意・手動微調整）",
        f"- ロゴ: `{config.get('logo_path', '')}`",
        f"- 完成版ロゴ必須: {'はい' if brand_signature(config).get('required_in_final_outputs', True) else 'いいえ'}",
        "",
        "## 判定サマリー",
        "",
        "| No | 用途 | 制作方法 | 最終サイズ | 生成時の比率 | ファイル名 | 設置位置 |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    for no, brief in enumerate(active, 1):
        lines.append(
            f"| {no} | {brief.role} | {brief.method} | {brief.size} | {brief.aspect_ratio} | `{brief.file_name}` | {position_for(brief)} |"
        )

    if omitted:
        lines += [
            "",
            "## 保留した画像",
            "",
            "| 用途 | ファイル名 | 保留理由 |",
            "| --- | --- | --- |",
        ]
        for brief in omitted:
            lines.append(f"| {brief.role} | `{brief.file_name}` | {brief.omitted_reason} |")

    lines += ["", "## 制作ブリーフ", ""]

    for no, brief in enumerate(active, 1):
        lines += [
            f"### {no}. {brief.role}",
            "",
            f"- ファイル名: `{brief.file_name}`",
            f"- WordPress画像タイトル: {brief.wp_title}",
            f"- ALT: {brief.alt}",
            f"- 最終サイズ: {brief.size}",
            f"- 生成時の比率: {brief.aspect_ratio}",
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
            "#### 生成プロンプト / レイアウト仕様",
            "",
            brief.final_prompt,
            "",
        ]
        if brief.local_composition:
            lines += [
                "#### ローカル合成",
                "",
                f"- 合成スクリプト: `{brief.local_composition.get('script', '')}`",
                f"- タイトル: {brief.local_composition.get('title', '')}",
                f"- サブタイトル: {brief.local_composition.get('subtitle', '')}",
                f"- 出力サイズ: {brief.local_composition.get('output_size', '')}",
                f"- 出力ファイル: `{brief.local_composition.get('output_file', '')}`",
                f"- ロゴ: `{brief.local_composition.get('logo', '')}`",
                f"- ロゴ必須: {'はい' if brief.local_composition.get('logo_required', True) else 'いいえ'}",
                f"- ロゴ位置: {brief.local_composition.get('logo_position', '')}",
                f"- ロゴ配置ルール: {brief.local_composition.get('logo_rule', '')}",
                f"- Canvaの扱い: {brief.local_composition.get('canva_role', '')}",
                "",
            ]
        if brief.canva_instructions:
            lines += [
                "#### Canva任意微調整",
                "",
                f"- 状態: {brief.canva_instructions.get('status', 'optional_manual')}",
                f"- テンプレートURL: {brief.canva_instructions.get('template_url', '')}",
                f"- タイトル: {brief.canva_instructions.get('title', '')}",
                f"- サブタイトル: {brief.canva_instructions.get('subtitle', '')}",
                f"- ロゴ: `{brief.canva_instructions.get('logo', '')}`",
                f"- ロゴ必須: {'はい' if brief.canva_instructions.get('logo_required', True) else 'いいえ'}",
                f"- ロゴ位置: {brief.canva_instructions.get('logo_position', '')}",
                f"- ロゴ配置ルール: {brief.canva_instructions.get('logo_rule', '')}",
                f"- 見出しフォント: {brief.canva_instructions.get('headline_font', '')}",
                f"- サブタイトルフォント: {brief.canva_instructions.get('subtitle_font', '')}",
                "",
            ]

    lines += ["## 品質チェック", ""]
    lines += [f"- {note}" for note in quality_notes(briefs, mode)]
    lines += [
        "- 画像生成AIに文字、日本語ラベル、ロゴ、透かし、看板を描かせない。",
        "- 日本語ラベルがある図解は、画像生成AIに文字を任せずレイアウト生成で作る。",
        "- ロゴとタイトルは標準ではローカル合成（Pillow）、必要に応じてSVGやCanvaの手動微調整で配置する。",
        "- アイキャッチ完成版と本文図解完成版では、セイリ部ロゴを必ず小さなブランド署名として配置する。",
        "- 暗い遺品整理、ゴミ屋敷、高額査定広告の印象を避ける。",
        "",
    ]
    return "\n".join(lines)


def json_plan(meta: ArticleMeta, briefs: list[ImageBrief], config: dict[str, Any], mode: str | None = None) -> dict[str, Any]:
    mode = resolve_mode(config, mode)
    return {
        "engine": {
            "mode": mode,
            "mode_settings": mode_settings(config, mode),
        },
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
            "canva_mode": config.get("canva_mode", "optional_manual"),
            "logo_path": config.get("logo_path"),
            "brand_signature": brand_signature(config),
            "local_composition": local_composition_config(config),
        },
        "images": [
            {
                "role": b.role,
                "generated": b.generated,
                "included": b.included,
                "omitted_reason": b.omitted_reason,
                "file_name": b.file_name,
                "size": b.size,
                "aspect_ratio": b.aspect_ratio,
                "method": b.method,
                "wp_title": b.wp_title,
                "alt": b.alt,
                "position": position_for(b),
                "caption": b.fields.get("キャプション候補", ""),
                "fields": b.fields,
                "final_prompt": b.final_prompt,
                "local_composition": b.local_composition,
                "canva_instructions": b.canva_instructions,
            }
            for b in active_briefs(briefs)
        ],
        "omitted_images": [
            {
                "role": b.role,
                "file_name": b.file_name,
                "reason": b.omitted_reason,
                "position": position_for(b),
            }
            for b in omitted_briefs(briefs)
        ],
        "quality_notes": quality_notes(briefs, mode),
    }


def write_plan(
    article: Path,
    config: dict[str, Any],
    output_dir: Path,
    output_format: str,
    mode: str | None = None,
) -> list[Path]:
    mode = resolve_mode(config, mode)
    text = article.read_text(encoding="utf-8")
    meta = article_meta(article, text)
    briefs = enrich_briefs(meta, parse_cms_blocks(text), config, mode)
    output_dir.mkdir(parents=True, exist_ok=True)
    written: list[Path] = []

    if output_format in {"md", "both"}:
        md_path = output_dir / f"{meta.slug}-image-plan.md"
        md_path.write_text(markdown_plan(meta, briefs, config, mode), encoding="utf-8")
        written.append(md_path)
    if output_format in {"json", "both"}:
        json_path = output_dir / f"{meta.slug}-image-plan.json"
        json_path.write_text(
            json.dumps(json_plan(meta, briefs, config, mode), ensure_ascii=False, indent=2) + "\n",
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
        "--mode",
        choices=["light", "standard"],
        help="Output mode. Defaults to config default_mode.",
    )
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
    mode = resolve_mode(config, args.mode)
    all_written: list[Path] = []
    for article in args.articles:
        all_written.extend(write_plan(article, config, args.output_dir, args.format, mode))
    for path in all_written:
        print(f"Wrote {path}")


if __name__ == "__main__":
    main()
