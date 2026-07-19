# 画像制作プラン: 実家の片付けで売れるもの一覧｜捨てる前に確認する品物と整理手順

## 記事情報

- 記事ファイル: `seiribu-editorial/drafts/pillars/sellable-disused-items-rewrite-v2.md`
- スラッグ: `sellable-disused-items`
- メインKW: 実家 片付け 売れるもの
- 出力モード: standard（記事内のCMS画像指定をすべて展開する標準モード。アイキャッチ素材1件と本文画像・図解4件を基本にする）
- アイキャッチ仕上げ: Canva手動仕上げ
- Canvaテンプレ: https://canva.link/mqlqak3adj01g1i（任意・手動微調整）
- ロゴ: `seiribu-editorial/assets/images/brand/seiribu-logo.png`
- ロゴ必須対象: アイキャッチ完成版, Canva仕上げ画像
- 本文画像のロゴ: 本文画像・本文図解はブランド帰属表示としてロゴ必須。背景が薄い場合は透過ロゴ、濃い・複雑な場合は薄い白背景付きロゴを、上部または下部の余白に小さく配置する。
- 画像生成ツール: imagegen
- 図解レイアウトツール: imagegen illustration base + Pillow / SVG / Canva label and logo overlay
- 生成候補の一時置き場: `/private/tmp/seiribu-image-work/sellable-disused-items`
- 採用画像の公開用置き場: `seiribu-editorial/assets/images/sellable-disused-items`
- 画像掃除スクリプト: `seiribu-editorial/scripts/clean_image_assets.py`

## 判定サマリー

| No | 用途 | 制作方法 | 最終サイズ | 生成時の比率 | ファイル名 | 設置位置 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 記事内イメージ | 画像生成素材 + ブランド帰属ロゴ合成 | 1200 x 675 | 16:9 | `sellable-disused-items-inline-01.png` | 導入文の直後（最初のH2の上） |
| 2 | 記事内図解 | 画像生成でサンプルのようなイラスト図解ベースを作り、Pillow、SVG、またはCanvaで短いラベルとロゴを正確に合成する | 1200 x 675 | 16:9 | `sellable-disused-items-inline-three-boxes.png` | H2「実家の片付けで売れるものは、捨てる前の確認で見つかる」の直下 |

## 制作ブリーフ

### 1. 記事内イメージ

- ファイル名: `sellable-disused-items-inline-01.png`
- WordPress画像タイトル: 実家の片付けで出てきた古い本やカメラ、レコード、ブランド品を親子で確認している様子
- ALT: 実家の片付けで出てきた古い本やカメラ、レコード、ブランド品を親子で確認している様子
- 最終サイズ: 1200 x 675
- 生成時の比率: 16:9
- 制作方法: 画像生成素材 + ブランド帰属ロゴ合成
- 設置位置: 導入文の直後（最初のH2の上）
- キャプション候補: 実家には、捨ててしまうにはもったいない品物がたくさん眠っています。

#### 制作意図

- 目的: 実家の片付けで出てきた様々な「売れるかもしれない物」を確認している様子をイメージさせる
- 読者に伝えたい感情: 未指定
- 入れたい要素: 親子（40代の子と70代の親）、段ボール、カメラ、レコード、ブランド品
- 避けたい表現: 暗い雰囲気、ゴミ屋敷のような散らかりすぎた部屋

#### 生成プロンプト / レイアウト仕様

Create a warm text-free editorial illustration for the Seiribu article '実家の片付けで売れるもの一覧｜捨てる前に確認する品物と整理手順'. Aspect ratio: 16:9. Style: warm watercolor-like editorial illustration, high-quality Japanese picture-book style, soft natural colors, realistic household objects, contemporary Japanese everyday home, clean but lived-in. Main visual: 親子（40代の子と70代の親）、段ボール、カメラ、レコード、ブランド品. Purpose: 実家の片付けで出てきた様々な「売れるかもしれない物」を確認している様子をイメージさせる. Tone: 日本の実家らしさ、読者が状況を想像しやすい生活感、明るく清潔、不安を煽らない、買取業者っぽくしすぎない、捨てるより確認する・分けるを見せる. Must avoid: no text, no letters, no numbers, no Japanese characters, no English words, no labels, no logo, no watermark, no signage, no speech bubbles. Also avoid: 暗い雰囲気、ゴミ屋敷のような散らかりすぎた部屋.

#### ブランド帰属ロゴ

- ロゴ必須: はい
- ロゴ: `seiribu-editorial/assets/images/brand/seiribu-logo.png`
- 表示モード: auto
- 透過ロゴ: 背景が薄く、ロゴが十分に読める場合
- 白背景付きロゴ: 背景が濃い、複雑、またはロゴが沈む場合
- 配置候補: 左上, 右上, 右下, 左下
- 配置ルール: 人物の顔、重要な品物、図解ラベル、キャプションを邪魔しない上部または下部の余白に小さく配置する。
- 理由: Google画像検索、Pinterest、無断転載先で画像が単体流通したときのブランド帰属表示。

### 2. 記事内図解

- ファイル名: `sellable-disused-items-inline-three-boxes.png`
- WordPress画像タイトル: 実家の荷物を売れる可能性がある物、確認してから判断する物、処分方法を確認する物に分ける図
- ALT: 実家の荷物を売れる可能性がある物、確認してから判断する物、処分方法を確認する物に分ける図
- 最終サイズ: 1200 x 675
- 生成時の比率: 16:9
- 制作方法: 画像生成でサンプルのようなイラスト図解ベースを作り、Pillow、SVG、またはCanvaで短いラベルとロゴを正確に合成する
- 設置位置: H2「実家の片付けで売れるものは、捨てる前の確認で見つかる」の直下
- キャプション候補: まずは「売る・確認する・処分する」の3つに分けることから始めましょう。

#### 制作意図

- 目的: 荷物をすぐに捨てず、3つの選択肢に分ける基本フローを視覚的に理解させる
- 読者に伝えたい感情: 未指定
- 入れたい要素: 3つの箱（左から緑色・黄色・グレーの順）、各箱の下に代表的な品物の小さなイラスト、フロー図
- 避けたい表現: 文字が多すぎる複雑な図解

#### 生成プロンプト / レイアウト仕様

Create a text-free illustrated diagram base for a Seiribu article. Aspect ratio: 16:9. Style: warm Japanese picture-book style illustrated diagram, scene-based panels with people, household items, rooms, boxes, kimono, books, cameras or other concrete objects, not abstract line art, not plain geometric shapes. Content to show as warm scene-based panels or a comparison illustration: 3つの箱（左から緑色・黄色・グレーの順）、各箱の下に代表的な品物の小さなイラスト、フロー図. Purpose: 荷物をすぐに捨てず、3つの選択肢に分ける基本フローを視覚的に理解させる. Must avoid: no text, no letters, no numbers, no Japanese characters, no English words, no labels, no logo, no watermark, no signage, no speech bubbles. Also avoid: 文字が多すぎる複雑な図解. Do not create abstract line art, a generic flowchart, wireframe boxes, plain circles, arrows-only diagrams, or free-icon-style graphics. Use concrete scenes with people, household items, rooms, boxes, kimono, books, cameras, documents, or other article-specific objects. Do not include readable text, Japanese labels, numbers, logo, watermark, signage, or speech bubbles in the generated image; short Japanese labels and captions will be added later with Pillow, SVG, or Canva. Leave quiet margin space for a small Seiribu brand logo overlay. ロゴ: 本文画像・本文図解はブランド帰属表示としてロゴ必須。背景が薄い場合は透過ロゴ、濃い・複雑な場合は薄い白背景付きロゴを、上部または下部の余白に小さく配置する。

#### ブランド帰属ロゴ

- ロゴ必須: はい
- ロゴ: `seiribu-editorial/assets/images/brand/seiribu-logo.png`
- 表示モード: auto
- 透過ロゴ: 背景が薄く、ロゴが十分に読める場合
- 白背景付きロゴ: 背景が濃い、複雑、またはロゴが沈む場合
- 配置候補: 左上, 右上, 右下, 左下
- 配置ルール: 人物の顔、重要な品物、図解ラベル、キャプションを邪魔しない上部または下部の余白に小さく配置する。
- 理由: Google画像検索、Pinterest、無断転載先で画像が単体流通したときのブランド帰属表示。

## 品質チェック

- アイキャッチまたはアイキャッチ合成用素材の指定がありません。自動補完はしません。
- 本文画像の枚数は適正範囲です。
- 画像生成AIに文字、日本語ラベル、ロゴ、透かし、看板を描かせない。
- 日本語ラベルがある図解は、画像生成AIに文字を任せずレイアウト生成で作る。
- 図解は抽象的な線や図形だけにせず、サンプルのような人物・品物・実家の場面を含むイラスト図解ベースで作る。
- アイキャッチのロゴとタイトルはCanvaで人間が最終合成する。
- ロゴ必須対象: アイキャッチ完成版, Canva仕上げ画像。
- 本文画像・本文図解のロゴ: 本文画像・本文図解はブランド帰属表示としてロゴ必須。背景が薄い場合は透過ロゴ、濃い・複雑な場合は薄い白背景付きロゴを、上部または下部の余白に小さく配置する。
- 暗い遺品整理、ゴミ屋敷、高額査定広告の印象を避ける。
- imagegenの生成候補は `/private/tmp/seiribu-image-work/sellable-disused-items` に置き、採用画像だけ `seiribu-editorial/assets/images/sellable-disused-items` に移す。
- 公開用フォルダに残った候補や旧版は `seiribu-editorial/scripts/clean_image_assets.py --article sellable-disused-items --dry-run` で確認してから退避する。
