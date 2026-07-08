---
description: セイリ部の記事Markdownから、アイキャッチと記事内画像の制作プランを生成する画像制作エンジン
---

# セイリ部 画像制作エンジン

完成済みの記事Markdownを入力にして、画像制作プランを生成する。

このエンジンは本文を書き換えない。記事内のCMS画像ブリーフを読み取り、足りないアイキャッチ指定を補完し、制作方法・最終プロンプト・Canva流し込み指示・ALT・ファイル名を整理する。

## 起動方法

```bash
python3 seiribu-editorial/scripts/generate_image_plan.py \
  seiribu-editorial/drafts/pillars/sell-or-dispose-clean.md
```

複数記事をまとめて処理する場合:

```bash
python3 seiribu-editorial/scripts/generate_image_plan.py \
  seiribu-editorial/drafts/pillars/home-cleanout-clean.md \
  seiribu-editorial/drafts/pillars/sell-or-dispose-clean.md
```

## 入力

- 記事Markdown
- `> [!CMS担当者へ：ここに図解を挿入]` 形式の本文画像ブリーフ
- `seiribu-editorial/config/image-engine.json` のブランド設定

## 出力

`seiribu-editorial/image-briefs/` に以下を出力する。

- `{slug}-image-plan.md`: 人間確認用の制作プラン
- `{slug}-image-plan.json`: 画像制作エンジンや自動化用の構造化データ

## 判断ルール

- 記事内にアイキャッチ指定がない場合は、ブランド型アイキャッチを1枚補完する
- 日本語ラベル・比較表・フロー・手順を含む画像は、画像生成AIではなくCanva、Pillow、SVGなどで作る
- 情景イラストや写真風素材だけを画像生成エンジンに渡す
- アイキャッチはCanvaテンプレにタイトル・サブタイトル・ロゴ・画像素材を流し込む
- ロゴは見出し、人物の顔、重要な品物を避けて配置する

## Canvaテンプレ

テンプレートURLは `seiribu-editorial/config/image-engine.json` の `canva_template_url` で管理する。

現在のテンプレート:

https://canva.link/mqlqak3adj01g1i

## セイリ部ブランド型アイキャッチ

- サイズ: 1200 x 630
- ロゴ: 左上
- 見出し: 上部中央、大きく配置
- サブタイトル: 見出し直下
- ビジュアル: 下部から中央に、人物や実家の物を配置
- 見出しフォント: UDモトヤアポロ 太字
- サブタイトルフォント: Noto Sans JP Regular
- フォント未導入時: Noto Sans JP Boldで仮制作し、Canva側で差し替える

## 品質チェック

- アイキャッチが1枚あるか
- 本文画像は2から3枚程度か
- 図解の日本語ラベルが崩れない制作方法になっているか
- ゴミ屋敷、暗い遺品整理、高額査定広告の印象になっていないか
- WordPress画像タイトル、ALT、キャプション候補、設置位置が揃っているか
