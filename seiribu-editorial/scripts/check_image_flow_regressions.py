#!/usr/bin/env python3
"""Regression checks for the Seiribu image-production flow."""

from __future__ import annotations

from pathlib import Path
from tempfile import TemporaryDirectory

import clean_image_assets
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
    briefs = image_plan.enrich_briefs(meta, image_plan.parse_cms_blocks(article), config, mode="standard")
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
    [result] = image_plan.enrich_briefs(meta, [brief], config, mode="standard")

    assert result.role == "アイキャッチ素材", result.role
    assert result.size == "1200 x 675", result.size
    assert result.aspect_ratio == "16:9", result.aspect_ratio
    assert result.file_name == "fixture-cutout.png", result.file_name
    assert result.local_composition["engine"] == "Canva手動仕上げ", result.local_composition
    assert result.local_composition["logo_required"] is True, result.local_composition
    assert result.local_composition["canva_role"].startswith("アイキャッチ完成版はCanva"), result.local_composition
    assert "no text" in result.final_prompt, result.final_prompt
    assert "no logo" in result.final_prompt, result.final_prompt
    assert "Do not include a room, wall, floor" in result.final_prompt, result.final_prompt
    assert "Do not reuse" in result.final_prompt, result.final_prompt
    assert result.canva_instructions["logo_required"] is True, result.canva_instructions
    assert "アイキャッチ完成版はCanvaで人間が仕上げる" in result.canva_instructions["logo_rule"], result.canva_instructions
    assert "本文画像・本文図解はCodex側でブランド帰属ロゴを必ず合成する" in result.canva_instructions["logo_rule"], result.canva_instructions


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
    [result] = image_plan.enrich_briefs(meta, [brief], config, mode="standard")

    assert result.role == "アイキャッチ", result.role
    assert result.method == "画像生成素材 + Canva手動仕上げ", result.method
    assert result.size == "1200 x 675", result.size
    assert result.aspect_ratio == "16:9", result.aspect_ratio
    assert result.local_composition["engine"] == "Canva手動仕上げ", result.local_composition
    assert result.local_composition["output_size"] == "1200 x 675", result.local_composition
    assert result.local_composition["logo_required"] is True, result.local_composition
    prompt = result.final_prompt.lower()
    assert "no text" in prompt, result.final_prompt
    assert "no logo" in prompt, result.final_prompt
    assert "background-free" in prompt, result.final_prompt
    assert "Do not include a room, wall, floor" in result.final_prompt, result.final_prompt
    assert "manual Canva eyecatch template" in result.final_prompt, result.final_prompt
    assert result.canva_instructions["logo_required"] is True, result.canva_instructions


def check_light_mode_keeps_first_pass_small(config: dict) -> None:
    article = """# 実家の片付けで母親が逆ギレする理由

> [!CMS担当者へ：アイキャッチ画像]
> 種類：アイキャッチ素材
> 目的：親子の対立と解決への前向きさを伝える
> 入れたい要素：高齢の母親、悩む子供世代、段ボール
> ALT：片付けで対立する親子

> [!CMS担当者へ：ここに画像を挿入]
> 種類：記事内イメージ
> 目的：母親側の不安を伝える
> 入れたい要素：物の前で悩む母親
> ALT：物の前で悩む母親

> [!CMS担当者へ：ここに画像を挿入]
> 種類：記事内イメージ
> 目的：第三者の介入で落ち着く様子を伝える
> 入れたい要素：査定士と話す母親
> ALT：査定士と話す母親

> [!CMS担当者へ：ここに画像を挿入]
> 種類：記事内図解
> 目的：揉めない片付け手順を示す
> 入れたい要素：声かけ、確認、保留箱の3ステップ
> ALT：揉めない片付け手順
"""
    meta = image_plan.ArticleMeta(
        path=Path("fixture.md"),
        title="実家の片付けで母親が逆ギレする理由",
        slug="fixture",
    )
    briefs = image_plan.enrich_briefs(meta, image_plan.parse_cms_blocks(article), config, mode="light")
    active = image_plan.active_briefs(briefs)
    omitted = image_plan.omitted_briefs(briefs)

    assert [brief.role for brief in active] == ["アイキャッチ素材", "記事内イメージ"], active
    assert len(omitted) == 2, omitted
    assert all(not brief.final_prompt for brief in omitted), omitted
    assert active[0].canva_instructions == {}, active[0].canva_instructions
    assert active[0].final_prompt.startswith("Text-free Seiribu eyecatch cutout asset."), active[0].final_prompt
    assert "Purpose:" in active[0].final_prompt, active[0].final_prompt
    assert "Tone:" in active[0].final_prompt, active[0].final_prompt
    assert "Do not reuse composition, character placement, object placement, or background concept" in active[0].final_prompt, active[0].final_prompt
    assert active[1].size == "1200 x 675", active[1].size
    assert active[1].aspect_ratio == "16:9", active[1].aspect_ratio

    notes = image_plan.quality_notes(briefs, mode="light")
    assert "lightモードのため、初回制作は2件に絞り、2件を保留しました。" in notes, notes

    plan = image_plan.json_plan(meta, briefs, config, mode="light")
    assert plan["engine"]["mode"] == "light", plan["engine"]
    storage = plan["engine"]["storage_policy"]
    assert storage["generation_tool"] == "imagegen", storage
    assert storage["diagram_tool"] == "imagegen complete illustrated infographic with model-native short Japanese text + logo overlay", storage
    assert storage["draft_dir"].endswith("/fixture"), storage
    assert storage["final_dir"].endswith("/assets/images/fixture"), storage
    assert storage["archive_root"] == "/private/tmp/seiribu-image-archive", storage
    assert storage["archive_script"].endswith("clean_image_assets.py"), storage
    assert len(plan["images"]) == 2, plan["images"]
    assert all(image["included"] is True for image in plan["images"]), plan["images"]
    assert len(plan["omitted_images"]) == 2, plan["omitted_images"]


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
    [result] = image_plan.enrich_briefs(meta, image_plan.parse_cms_blocks(article), config, mode="standard")

    assert result.role == "記事内図解", result.role
    assert result.size == "1200 x 675", result.size
    assert result.aspect_ratio == "16:9", result.aspect_ratio
    assert "illustrated infographic diagram" in result.final_prompt, result.final_prompt
    assert "rounded bordered panels" in result.final_prompt, result.final_prompt
    assert "Do not create empty placeholder boxes" in result.final_prompt, result.final_prompt
    assert "自治体、寄付、不用品回収業者の比較表" in result.final_prompt, result.final_prompt
    assert "Do not create abstract line art" in result.final_prompt, result.final_prompt
    assert "本文画像・本文図解はブランド帰属表示としてロゴ必須" in result.final_prompt, result.final_prompt
    assert result.logo_overlay["required"] is True, result.logo_overlay


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
    [result] = image_plan.enrich_briefs(meta, image_plan.parse_cms_blocks(article), config, mode="standard")

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
    [result] = image_plan.enrich_briefs(meta, image_plan.parse_cms_blocks(article), config, mode="standard")

    assert result.role == "記事内イメージ", result.role
    assert result.size == "1200 x 675", result.size
    assert result.aspect_ratio == "16:9", result.aspect_ratio
    assert "Create a warm text-free editorial illustration" in result.final_prompt, result.final_prompt


def check_explicit_illustrated_diagram_wins_over_scene_words(config: dict) -> None:
    article = """# 不用品回収と買取の違い

> [!CMS担当者へ：ここに画像を挿入]
> 種類：イラスト図解
> 画像の目的：残す、売る、処分する順番をフローチャートで伝える
> 画像のアイデア（情景・図解の具体案）：Step 1:「残す」アルバムを手にする様子。Step 2:「売る」古いカメラを査定員に見せる様子。Step 3:「処分する」壊れたテレビをスタッフが運ぶ様子。
> ALT：実家の不用品を無駄なく片付ける順番のフローチャート
"""
    meta = image_plan.ArticleMeta(
        path=Path("fixture.md"),
        title="不用品回収と買取の違い",
        slug="fixture",
    )
    [result] = image_plan.enrich_briefs(meta, image_plan.parse_cms_blocks(article), config, mode="standard")

    assert result.role == "記事内図解", result.role
    assert "illustrated infographic diagram" in result.final_prompt, result.final_prompt
    assert "rounded bordered panels" in result.final_prompt, result.final_prompt
    assert "Do not create abstract line art" in result.final_prompt, result.final_prompt
    assert result.logo_overlay["required"] is True, result.logo_overlay


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
    results = image_plan.enrich_briefs(meta, briefs, config, mode="standard")
    file_names = [brief.file_name for brief in results]

    assert len(file_names) == len(set(file_names)), file_names
    assert any(name.endswith("-2.png") for name in file_names), file_names


def check_cleanup_finds_non_recommended_assets() -> None:
    with TemporaryDirectory() as tmp:
        tmp_root = Path(tmp)
        image_root = tmp_root / "assets" / "images"
        article_dir = image_root / "sample-article"
        article_dir.mkdir(parents=True)
        (article_dir / "README.md").write_text(
            """# sample

## 推奨画像

| 用途 | ファイル |
| --- | --- |
| アイキャッチ | `keep.png` |

## 素材画像

| 用途 | ファイル |
| --- | --- |
| 生成素材 | `material.png` |
""",
            encoding="utf-8",
        )
        for name in ["keep.png", "material.png", "old-v2.png"]:
            (article_dir / name).touch()

        reports = clean_image_assets.build_reports(
            image_root,
            tmp_root / "archive",
            "test-run",
            article="sample-article",
        )
        [report] = reports
        candidate_names = {candidate.source.name for candidate in report.candidates}

        assert {path.name for path in report.kept} == {"keep.png"}, report
        assert candidate_names == {"material.png", "old-v2.png"}, candidate_names

        cautious_reports = clean_image_assets.build_reports(
            image_root,
            tmp_root / "archive",
            "test-run",
            article="sample-article",
            keep_all_readme_references=True,
        )
        [cautious_report] = cautious_reports
        cautious_candidate_names = {candidate.source.name for candidate in cautious_report.candidates}

        assert {path.name for path in cautious_report.kept} == {"keep.png", "material.png"}, cautious_report
        assert cautious_candidate_names == {"old-v2.png"}, cautious_candidate_names


def check_cleanup_accepts_completed_image_sections() -> None:
    with TemporaryDirectory() as tmp:
        tmp_root = Path(tmp)
        image_root = tmp_root / "assets" / "images"
        article_dir = image_root / "completed-article"
        article_dir.mkdir(parents=True)
        (article_dir / "README.md").write_text(
            """# sample

## 完成画像

| 用途 | ファイル |
| --- | --- |
| アイキャッチ | `final.webp` |

## 素材・生成ファイル

| 用途 | ファイル |
| --- | --- |
| 生成素材 | `source.png` |
""",
            encoding="utf-8",
        )
        for name in ["final.webp", "source.png"]:
            (article_dir / name).touch()

        [report] = clean_image_assets.build_reports(
            image_root,
            Path("/private/tmp/seiribu-image-archive"),
            "test-run",
            article="completed-article",
        )

        assert {path.name for path in report.kept} == {"final.webp"}, report
        assert {candidate.source.name for candidate in report.candidates} == {"source.png"}, report


def main() -> None:
    config = load_config()
    check_missing_eyecatch_is_not_auto_generated(config)
    check_canva_material_role(config)
    check_regular_eyecatch_has_generation_limits(config)
    check_light_mode_keeps_first_pass_small(config)
    check_diagram_is_not_image_generation_prompt(config)
    check_diagram_asset_can_be_generated(config)
    check_scene_illustration_is_not_misclassified_as_diagram(config)
    check_explicit_illustrated_diagram_wins_over_scene_words(config)
    check_duplicate_file_names_are_disambiguated(config)
    check_cleanup_finds_non_recommended_assets()
    check_cleanup_accepts_completed_image_sections()
    print("image flow regression checks passed")


if __name__ == "__main__":
    main()
