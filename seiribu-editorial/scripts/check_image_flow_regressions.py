#!/usr/bin/env python3
"""Regression checks for the Seiribu image-production flow."""

from __future__ import annotations

from pathlib import Path

import generate_image_plan as image_plan


def load_config() -> dict:
    return image_plan.read_json(image_plan.DEFAULT_CONFIG)


def check_missing_eyecatch_is_not_auto_generated(config: dict) -> None:
    article = """# 買取不可だったものはどうする？

> [!CMS担当者へ：ここに画像を挿入]
> 種類：記事内図解
> 目的：買取不可になる理由を整理して伝える
> 入れたい要素：状態不良、需要不足、規制の3つ
> ALT：買取不可になる理由を説明する図
"""
    meta = image_plan.ArticleMeta(
        path=Path("fixture.md"),
        title="買取不可だったものはどうする？",
        slug="fixture",
    )
    briefs = image_plan.enrich_briefs(meta, image_plan.parse_cms_blocks(article), config)
    roles = [brief.role for brief in briefs]
    notes = image_plan.quality_notes(briefs)

    assert "アイキャッチ" not in roles, roles
    assert "アイキャッチ素材" not in roles, roles
    assert "アイキャッチまたはアイキャッチ合成用素材の指定がありません。自動補完はしません。" in notes, notes


def check_canva_material_role(config: dict) -> None:
    meta = image_plan.ArticleMeta(
        path=Path("fixture.md"),
        title="実家の不用品を整理する",
        slug="fixture",
    )
    brief = image_plan.ImageBrief(
        role="",
        source_header="[!CMS担当者へ：ここに画像を挿入]",
        fields={
            "種類": "アイキャッチ素材（ローカル合成用）",
            "目的": "Canvaで整えるための背景なし素材を作る",
            "入れたい要素": "査定不可の紙と売れなかった古い家電",
            "ファイル名": "fixture-cutout.png",
        },
        index=1,
    )
    [result] = image_plan.enrich_briefs(meta, [brief], config)

    assert result.role == "アイキャッチ素材", result.role
    assert result.size == "1536 x 1024", result.size
    assert result.aspect_ratio == "3:2", result.aspect_ratio
    assert result.file_name == "fixture-cutout.png", result.file_name
    assert result.local_composition["engine"] == "Pillow", result.local_composition
    assert result.local_composition["logo_required"] is True, result.local_composition
    assert result.local_composition["canva_role"].startswith("任意"), result.local_composition
    assert "no text" in result.final_prompt, result.final_prompt
    assert "no logo" in result.final_prompt, result.final_prompt
    assert "Do not include a room, wall, floor" in result.final_prompt, result.final_prompt
    assert "Do not reuse" in result.final_prompt, result.final_prompt
    assert result.canva_instructions["logo_required"] is True, result.canva_instructions
    assert "完成版にはセイリ部ロゴを必ず" in result.canva_instructions["logo_rule"], result.canva_instructions


def check_regular_eyecatch_has_generation_limits(config: dict) -> None:
    meta = image_plan.ArticleMeta(
        path=Path("fixture.md"),
        title="実家の片付けは何から始める？",
        slug="fixture",
    )
    brief = image_plan.ImageBrief(
        role="",
        source_header="[!CMS担当者へ：アイキャッチ画像]",
        fields={
            "目的": "記事全体の第一印象を作る",
            "入れたい人物・物": "実家のリビングで古い本や段ボールを確認している人物",
            "ファイル名": "fixture-eyecatch.png",
        },
        index=1,
    )
    [result] = image_plan.enrich_briefs(meta, [brief], config)

    assert result.role == "アイキャッチ", result.role
    assert result.method == "画像生成素材 + ローカル合成（Pillow）", result.method
    assert result.aspect_ratio == "16:9", result.aspect_ratio
    assert result.local_composition["engine"] == "Pillow", result.local_composition
    assert result.local_composition["logo_required"] is True, result.local_composition
    prompt = result.final_prompt.lower()
    assert "no text" in prompt, result.final_prompt
    assert "no logo" in prompt, result.final_prompt
    assert "finished later with the local Seiribu Pillow compositor" in result.final_prompt, result.final_prompt
    assert result.canva_instructions["logo_required"] is True, result.canva_instructions


def check_diagram_is_not_image_generation_prompt(config: dict) -> None:
    article = """# 売れなかった不用品を手放す方法

> [!CMS担当者へ：ここに画像を挿入]
> 画像の目的：3つの処分方法を比較する
> 画像のアイデア（情景・図解の具体案）：自治体、寄付、不用品回収業者の比較表
> ALT：売れなかった不用品の処分方法を比較する図
"""
    meta = image_plan.ArticleMeta(
        path=Path("fixture.md"),
        title="売れなかった不用品を手放す方法",
        slug="fixture",
    )
    [result] = image_plan.enrich_briefs(meta, image_plan.parse_cms_blocks(article), config)

    assert result.role == "記事内図解", result.role
    assert result.aspect_ratio == "3:2", result.aspect_ratio
    assert "画像生成AIには渡さない" in result.final_prompt, result.final_prompt
    assert "自治体、寄付、不用品回収業者の比較表" in result.final_prompt, result.final_prompt


def check_diagram_asset_can_be_generated(config: dict) -> None:
    article = """# 実家で売れるもの一覧

> [!CMS担当者へ：ここに画像を挿入]
> 種類：図解用小物素材
> 画像の目的：図解内で使うカメラの単体アイコンを作る
> 画像のアイデア（情景・図解の具体案）：古いフィルムカメラの小物素材
> ALT：古いフィルムカメラの小物素材
"""
    meta = image_plan.ArticleMeta(
        path=Path("fixture.md"),
        title="実家で売れるもの一覧",
        slug="fixture",
    )
    [result] = image_plan.enrich_briefs(meta, image_plan.parse_cms_blocks(article), config)

    assert result.role == "図解用小物素材", result.role
    assert result.aspect_ratio == "1:1", result.aspect_ratio
    assert "supporting visual asset" in result.final_prompt, result.final_prompt
    assert "no text" in result.final_prompt.lower(), result.final_prompt


def check_scene_illustration_is_not_misclassified_as_diagram(config: dict) -> None:
    article = """# 買取不可だったものはどうする？

> [!CMS担当者へ：ここに画像を挿入]
> 画像の目的：3つの理由を知って落ち込みを和らげる
> 画像のアイデア（情景イラスト案）：業者が帰った後、残された荷物を前に家族が穏やかに話している風景
> ALT：残された荷物を前に穏やかに話している家族
"""
    meta = image_plan.ArticleMeta(
        path=Path("fixture.md"),
        title="買取不可だったものはどうする？",
        slug="fixture",
    )
    [result] = image_plan.enrich_briefs(meta, image_plan.parse_cms_blocks(article), config)

    assert result.role == "記事内イメージ", result.role
    assert "Create a warm text-free editorial illustration" in result.final_prompt, result.final_prompt


def check_duplicate_file_names_are_disambiguated(config: dict) -> None:
    meta = image_plan.ArticleMeta(
        path=Path("fixture.md"),
        title="実家の片付け",
        slug="fixture",
    )
    briefs = [
        image_plan.ImageBrief(role="", source_header="[!CMS担当者へ：ここに画像を挿入]", fields={"画像の目的": "箱を使った仕分け", "入れたい要素": "段ボール箱"}, index=1),
        image_plan.ImageBrief(role="", source_header="[!CMS担当者へ：ここに画像を挿入]", fields={"画像の目的": "箱を使った別の仕分け", "入れたい要素": "段ボール箱"}, index=2),
    ]
    results = image_plan.enrich_briefs(meta, briefs, config)
    file_names = [brief.file_name for brief in results]

    assert len(file_names) == len(set(file_names)), file_names
    assert any(name.endswith("-2.png") for name in file_names), file_names


def main() -> None:
    config = load_config()
    check_missing_eyecatch_is_not_auto_generated(config)
    check_canva_material_role(config)
    check_regular_eyecatch_has_generation_limits(config)
    check_diagram_is_not_image_generation_prompt(config)
    check_diagram_asset_can_be_generated(config)
    check_scene_illustration_is_not_misclassified_as_diagram(config)
    check_duplicate_file_names_are_disambiguated(config)
    print("image flow regression checks passed")


if __name__ == "__main__":
    main()
