# 画像制作プラン: 実家の片付けはどこから？売る・残す・処分の順番と揉めない進め方

## 記事情報

- 記事ファイル: `seiribu-editorial/drafts/pillars/home-cleanout-clean.md`
- スラッグ: `home-cleanout`
- メインKW: 実家片付け どこから
- 出力モード: standard（記事内のCMS画像指定をすべて展開する標準モード。アイキャッチ素材1件と本文画像・図解4件を基本にする）
- アイキャッチ仕上げ: Canva手動仕上げ
- Canvaテンプレ: https://canva.link/mqlqak3adj01g1i（任意・手動微調整）
- ロゴ: `seiribu-editorial/assets/images/brand/seiribu-logo.png`
- ロゴ必須対象: アイキャッチ完成版, Canva仕上げ画像
- 本文画像のロゴ: 本文画像・本文図解はブランド帰属表示としてロゴ必須。背景が薄い場合は透過ロゴ、濃い・複雑な場合は薄い白背景付きロゴを、上部または下部の余白に小さく配置する。
- 画像生成ツール: imagegen
- 図解レイアウトツール: imagegen illustration base + Pillow / SVG / Canva label and logo overlay
- 生成候補の一時置き場: `/private/tmp/seiribu-image-work/home-cleanout`
- 採用画像の公開用置き場: `seiribu-editorial/assets/images/home-cleanout`
- 画像掃除スクリプト: `seiribu-editorial/scripts/clean_image_assets.py`

## 判定サマリー

| No | 用途 | 制作方法 | 最終サイズ | 生成時の比率 | ファイル名 | 設置位置 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 記事内図解 | 画像生成でサンプルのようなイラスト図解ベースを作り、Pillow、SVG、またはCanvaで短いラベルとロゴを正確に合成する | 1200 x 675 | 16:9 | `home-cleanout-inline-principles.png` | H2「実家の片付けで挫折しないための3つの鉄則」の直下 |
| 2 | 記事内図解 | 画像生成でサンプルのようなイラスト図解ベースを作り、Pillow、SVG、またはCanvaで短いラベルとロゴを正確に合成する | 1200 x 675 | 16:9 | `home-cleanout-inline-steps.png` | H2「実家の片付けはどこから始める？効率的な順番」の直下（ステップ1の前） |
| 3 | 記事内図解 | 画像生成でサンプルのようなイラスト図解ベースを作り、Pillow、SVG、またはCanvaで短いラベルとロゴを正確に合成する | 1200 x 675 | 16:9 | `home-cleanout-inline-three-boxes.png` | H3「ステップ4」内の解説直下（3箱仕分けの説明の前） |

## 制作ブリーフ

### 1. 記事内図解

- ファイル名: `home-cleanout-inline-principles.png`
- WordPress画像タイトル: 実家の片付けを失敗しないための3つの鉄則
- ALT: 実家の片付けを失敗しないための3つの鉄則
- 最終サイズ: 1200 x 675
- 生成時の比率: 16:9
- 制作方法: 画像生成でサンプルのようなイラスト図解ベースを作り、Pillow、SVG、またはCanvaで短いラベルとロゴを正確に合成する
- 設置位置: H2「実家の片付けで挫折しないための3つの鉄則」の直下
- キャプション候補: この3つを最初に家族で共有するだけで、片付けはスムーズに進みます

#### 制作意図

- 目的: 読者に「この3つさえ守れば失敗しない」と安心感を持たせること
- 読者に伝えたい感情: 未指定
- 入れたい要素: 3つのルールを並べ、横に温かみのあるシンプルなアイコン（握手、複数人の家族、3つの箱など）
- 避けたい表現: 禁止マーク（❌）など、読者を過度に萎縮させる表現

#### 生成プロンプト / レイアウト仕様

Create a text-free illustrated diagram base for a Seiribu article. Aspect ratio: 16:9. Style: warm Japanese picture-book style illustrated diagram, scene-based panels with people, household items, rooms, boxes, kimono, books, cameras or other concrete objects, not abstract line art, not plain geometric shapes. Content to show as warm scene-based panels or a comparison illustration: 3つのルールを並べ、横に温かみのあるシンプルなアイコン（握手、複数人の家族、3つの箱など）. Purpose: 読者に「この3つさえ守れば失敗しない」と安心感を持たせること. Must avoid: no text, no letters, no numbers, no Japanese characters, no English words, no labels, no logo, no watermark, no signage, no speech bubbles. Also avoid: 禁止マーク（❌）など、読者を過度に萎縮させる表現. Do not create abstract line art, a generic flowchart, wireframe boxes, plain circles, arrows-only diagrams, or free-icon-style graphics. Use concrete scenes with people, household items, rooms, boxes, kimono, books, cameras, documents, or other article-specific objects. Do not include readable text, Japanese labels, numbers, logo, watermark, signage, or speech bubbles in the generated image; short Japanese labels and captions will be added later with Pillow, SVG, or Canva. Leave quiet margin space for a small Seiribu brand logo overlay. ロゴ: 本文画像・本文図解はブランド帰属表示としてロゴ必須。背景が薄い場合は透過ロゴ、濃い・複雑な場合は薄い白背景付きロゴを、上部または下部の余白に小さく配置する。

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

- ファイル名: `home-cleanout-inline-steps.png`
- WordPress画像タイトル: 実家の片付けを効率よく進める4つのステップ
- ALT: 実家の片付けを効率よく進める4つのステップ
- 最終サイズ: 1200 x 675
- 生成時の比率: 16:9
- 制作方法: 画像生成でサンプルのようなイラスト図解ベースを作り、Pillow、SVG、またはCanvaで短いラベルとロゴを正確に合成する
- 設置位置: H2「実家の片付けはどこから始める？効率的な順番」の直下（ステップ1の前）
- キャプション候補: 判断に迷わない小さな場所から始めて、成功体験を積みましょう

#### 制作意図

- 目的: 片付けのハードルを下げ、簡単な場所から始めればよいことを視覚的に伝える
- 読者に伝えたい感情: 未指定
- 入れたい要素: 「1. 話し合い」→「2. 自分の物・ゴミ」→「3. 玄関・洗面所」→「4. リビング・趣味品」の横型フロー。各ステップに小さなアイコン
- 避けたい表現: 作業の辛さを連想させるような暗い色合い

#### 生成プロンプト / レイアウト仕様

Create a text-free illustrated diagram base for a Seiribu article. Aspect ratio: 16:9. Style: warm Japanese picture-book style illustrated diagram, scene-based panels with people, household items, rooms, boxes, kimono, books, cameras or other concrete objects, not abstract line art, not plain geometric shapes. Content to show as warm scene-based panels or a comparison illustration: 「1. 話し合い」→「2. 自分の物・ゴミ」→「3. 玄関・洗面所」→「4. リビング・趣味品」の横型フロー。各ステップに小さなアイコン. Purpose: 片付けのハードルを下げ、簡単な場所から始めればよいことを視覚的に伝える. Must avoid: no text, no letters, no numbers, no Japanese characters, no English words, no labels, no logo, no watermark, no signage, no speech bubbles. Also avoid: 作業の辛さを連想させるような暗い色合い. Do not create abstract line art, a generic flowchart, wireframe boxes, plain circles, arrows-only diagrams, or free-icon-style graphics. Use concrete scenes with people, household items, rooms, boxes, kimono, books, cameras, documents, or other article-specific objects. Do not include readable text, Japanese labels, numbers, logo, watermark, signage, or speech bubbles in the generated image; short Japanese labels and captions will be added later with Pillow, SVG, or Canva. Leave quiet margin space for a small Seiribu brand logo overlay. ロゴ: 本文画像・本文図解はブランド帰属表示としてロゴ必須。背景が薄い場合は透過ロゴ、濃い・複雑な場合は薄い白背景付きロゴを、上部または下部の余白に小さく配置する。

#### ブランド帰属ロゴ

- ロゴ必須: はい
- ロゴ: `seiribu-editorial/assets/images/brand/seiribu-logo.png`
- 表示モード: auto
- 透過ロゴ: 背景が薄く、ロゴが十分に読める場合
- 白背景付きロゴ: 背景が濃い、複雑、またはロゴが沈む場合
- 配置候補: 左上, 右上, 右下, 左下
- 配置ルール: 人物の顔、重要な品物、図解ラベル、キャプションを邪魔しない上部または下部の余白に小さく配置する。
- 理由: Google画像検索、Pinterest、無断転載先で画像が単体流通したときのブランド帰属表示。

### 3. 記事内図解

- ファイル名: `home-cleanout-inline-three-boxes.png`
- WordPress画像タイトル: 実家の荷物を「売れる物」「家族に確認」「処分」の3箱に仕分けるイメージ図
- ALT: 実家の荷物を「売れる物」「家族に確認」「処分」の3箱に仕分けるイメージ図
- 最終サイズ: 1200 x 675
- 生成時の比率: 16:9
- 制作方法: 画像生成でサンプルのようなイラスト図解ベースを作り、Pillow、SVG、またはCanvaで短いラベルとロゴを正確に合成する
- 設置位置: H3「ステップ4」内の解説直下（3箱仕分けの説明の前）
- キャプション候補: 「捨てる・捨てない」で迷ったら、まずはこの3つの箱に分けてみましょう

#### 制作意図

- 目的: 実家の荷物をシンプルに3つに分類すればよいと伝えること
- 読者に伝えたい感情: 未指定
- 入れたい要素: 3つの段ボール箱（緑・黄・グレーなどで色分け）。それぞれの箱の上に代表的な品物アイコン
- 避けたい表現: 乱雑にゴミが詰め込まれたような不潔な表現

#### 生成プロンプト / レイアウト仕様

Create a text-free illustrated diagram base for a Seiribu article. Aspect ratio: 16:9. Style: warm Japanese picture-book style illustrated diagram, scene-based panels with people, household items, rooms, boxes, kimono, books, cameras or other concrete objects, not abstract line art, not plain geometric shapes. Content to show as warm scene-based panels or a comparison illustration: 3つの段ボール箱（緑・黄・グレーなどで色分け）。それぞれの箱の上に代表的な品物アイコン. Purpose: 実家の荷物をシンプルに3つに分類すればよいと伝えること. Must avoid: no text, no letters, no numbers, no Japanese characters, no English words, no labels, no logo, no watermark, no signage, no speech bubbles. Also avoid: 乱雑にゴミが詰め込まれたような不潔な表現. Do not create abstract line art, a generic flowchart, wireframe boxes, plain circles, arrows-only diagrams, or free-icon-style graphics. Use concrete scenes with people, household items, rooms, boxes, kimono, books, cameras, documents, or other article-specific objects. Do not include readable text, Japanese labels, numbers, logo, watermark, signage, or speech bubbles in the generated image; short Japanese labels and captions will be added later with Pillow, SVG, or Canva. Leave quiet margin space for a small Seiribu brand logo overlay. ロゴ: 本文画像・本文図解はブランド帰属表示としてロゴ必須。背景が薄い場合は透過ロゴ、濃い・複雑な場合は薄い白背景付きロゴを、上部または下部の余白に小さく配置する。

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
- imagegenの生成候補は `/private/tmp/seiribu-image-work/home-cleanout` に置き、採用画像だけ `seiribu-editorial/assets/images/home-cleanout` に移す。
- 公開用フォルダに残った候補や旧版は `seiribu-editorial/scripts/clean_image_assets.py --article home-cleanout --dry-run` で確認してから退避する。
