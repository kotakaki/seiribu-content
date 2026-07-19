# 画像制作プラン: 一人っ子の実家の片付けはどう進める？親との話し合いと準備

## 記事情報

- 記事ファイル: `seiribu-editorial/drafts/only-child.md`
- スラッグ: `only-child`
- メインKW: 一人っ子 実家 片付け
- 出力モード: standard（記事内のCMS画像指定をすべて展開する標準モード。アイキャッチ素材1件と本文画像・図解4件を基本にする）
- アイキャッチ仕上げ: Canva手動仕上げ
- Canvaテンプレ: https://canva.link/mqlqak3adj01g1i（任意・手動微調整）
- ロゴ: `seiribu-editorial/assets/images/brand/seiribu-logo.png`
- ロゴ必須対象: アイキャッチ完成版, Canva仕上げ画像
- 本文画像のロゴ: 本文画像・本文図解はブランド帰属表示としてロゴ必須。背景が薄い場合は透過ロゴ、濃い・複雑な場合は薄い白背景付きロゴを、上部または下部の余白に小さく配置する。
- 画像生成ツール: imagegen
- 図解レイアウトツール: imagegen illustration base + Pillow / SVG / Canva label and logo overlay
- 生成候補の一時置き場: `/private/tmp/seiribu-image-work/only-child`
- 採用画像の公開用置き場: `seiribu-editorial/assets/images/only-child`
- 画像掃除スクリプト: `seiribu-editorial/scripts/clean_image_assets.py`

## 判定サマリー

| No | 用途 | 制作方法 | 最終サイズ | 生成時の比率 | ファイル名 | 設置位置 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | アイキャッチ素材 | 画像生成素材 + Canva手動仕上げ | 1200 x 675 | 16:9 | `only-child-eyecatch.png` | アイキャッチ合成用素材 |
| 2 | 記事内イメージ | 画像生成素材 + ブランド帰属ロゴ合成 | 1200 x 675 | 16:9 | `only-child-inline-01.png` | 本文中のCMSブリーフ位置 |
| 3 | 記事内イメージ | 画像生成素材 + ブランド帰属ロゴ合成 | 1200 x 675 | 16:9 | `only-child-conflict-trap.png` | 本文中のCMSブリーフ位置 |
| 4 | 記事内図解 | 画像生成でサンプルのようなイラスト図解ベースを作り、Pillow、SVG、またはCanvaで短いラベルとロゴを正確に合成する | 1200 x 675 | 16:9 | `only-child-two-professionals.png` | 本文中のCMSブリーフ位置 |
| 5 | 記事内図解 | 画像生成でサンプルのようなイラスト図解ベースを作り、Pillow、SVG、またはCanvaで短いラベルとロゴを正確に合成する | 1200 x 675 | 16:9 | `only-child-3steps-flow.png` | 本文中のCMSブリーフ位置 |
| 6 | 記事内図解 | 画像生成でサンプルのようなイラスト図解ベースを作り、Pillow、SVG、またはCanvaで短いラベルとロゴを正確に合成する | 1200 x 675 | 16:9 | `only-child-inline-options.png` | 本文中のCMSブリーフ位置 |
| 7 | 記事内図解 | 画像生成でサンプルのようなイラスト図解ベースを作り、Pillow、SVG、またはCanvaで短いラベルとロゴを正確に合成する | 1200 x 675 | 16:9 | `only-child-inline-steps.png` | 本文中のCMSブリーフ位置 |

## 制作ブリーフ

### 1. アイキャッチ素材

- ファイル名: `only-child-eyecatch.png`
- WordPress画像タイトル: 一人っ子の実家の片付け負担をプロの力で減らすイメージ
- ALT: 一人っ子の実家の片付け負担をプロの力で減らすイメージ
- 最終サイズ: 1200 x 675
- 生成時の比率: 16:9
- 制作方法: 画像生成素材 + Canva手動仕上げ
- 設置位置: アイキャッチ合成用素材
- キャプション候補: なし

#### 制作意図

- 目的: 未指定
- 読者に伝えたい感情: 未指定
- 入れたい要素: 未指定
- 避けたい表現: 未指定

#### 生成プロンプト / レイアウト仕様

Create an eyecatch cutout asset for the Seiribu article '一人っ子の実家の片付けはどう進める？親との話し合いと準備'. Aspect ratio: 16:9. Style: warm flat editorial illustration cutout, high-quality 2D vector art, single coherent subject, clean silhouette, easy to remove background. Transparent background if possible; if transparency is not available, use a single flat light background that is easy to remove. Do not include a room, wall, floor, cast shadow, title area, logo area, or decorative frame. Main subject: 記事内容に合う人物と物. Purpose: . Tone: 日本の実家らしさ、読者が状況を想像しやすい生活感、明るく清潔、不安を煽らない、買取業者っぽくしすぎない、捨てるより確認する・分けるを見せる. Must avoid: no text, no letters, no numbers, no Japanese characters, no English words, no labels, no logo, no watermark, no signage, no speech bubbles. Also avoid: ゴミ屋敷のような汚さ、暗い遺品整理の雰囲気、札束や高額査定の強調、不用品回収業者だけを推す広告感、既存記事と同じ構図や素材の使い回し、ミニマリスト風の真っ白な部屋、ロゴが見出し・人物の顔・重要な品物を邪魔する配置、抽象的な線、丸、四角、矢印だけで構成された低品質な図解、無料素材風の薄いアイコン図解. Do not reuse the composition, character placement, object placement, or background concept from any existing Seiribu article image.

#### アイキャッチCanva仕上げ

- 仕上げ方法: Canva手動仕上げ
- タイトル: 一人っ子の実家の片付けはどう進める？
- サブタイトル: 親との話し合いと準備
- 出力サイズ: 1200 x 675
- 出力ファイル: `only-child-eyecatch-branded.png`
- ロゴ: `seiribu-editorial/assets/images/brand/seiribu-logo.png`
- ロゴ必須: はい
- ロゴ位置: 左上
- ロゴ配置ルール: 生成AI素材にはロゴを描かせない。アイキャッチ完成版はCanvaで人間が仕上げる。本文画像・本文図解はCodex側でブランド帰属ロゴを必ず合成する。背景が薄い場合は透過ロゴ、濃い・複雑な場合は薄い白背景付きロゴを使い、人物の顔、重要な品物、図解ラベルを邪魔しない余白に配置する。
- Canvaの扱い: アイキャッチ完成版はCanvaで人間がタイトル、サブタイトル、ロゴ、Canva専用フォントを手動合成する。

#### Canva仕上げ

- 状態: optional_manual
- テンプレートURL: https://canva.link/mqlqak3adj01g1i
- タイトル: 一人っ子の実家の片付けはどう進める？
- サブタイトル: 親との話し合いと準備
- ロゴ: `seiribu-editorial/assets/images/brand/seiribu-logo.png`
- ロゴ必須: はい
- ロゴ位置: 左上
- ロゴ配置ルール: 生成AI素材にはロゴを描かせない。アイキャッチ完成版はCanvaで人間が仕上げる。本文画像・本文図解はCodex側でブランド帰属ロゴを必ず合成する。背景が薄い場合は透過ロゴ、濃い・複雑な場合は薄い白背景付きロゴを使い、人物の顔、重要な品物、図解ラベルを邪魔しない余白に配置する。
- 見出しフォント: UDモトヤアポロ 太字
- サブタイトルフォント: Noto Sans JP Regular

### 2. 記事内イメージ

- ファイル名: `only-child-inline-01.png`
- WordPress画像タイトル: 一人で実家の片付けの負担を抱え込む一人っ子のイメージ
- ALT: 一人で実家の片付けの負担を抱え込む一人っ子のイメージ
- 最終サイズ: 1200 x 675
- 生成時の比率: 16:9
- 制作方法: 画像生成素材 + ブランド帰属ロゴ合成
- 設置位置: 本文中のCMSブリーフ位置
- キャプション候補: 一人っ子の場合、実家の片付けの精神的・肉体的な負担がすべて一人に集中してしまいます。

#### 制作意図

- 目的: 未指定
- 読者に伝えたい感情: 未指定
- 入れたい要素: 未指定
- 避けたい表現: 未指定

#### 生成プロンプト / レイアウト仕様

Create a warm text-free editorial illustration for the Seiribu article '一人っ子の実家の片付けはどう進める？親との話し合いと準備'. Aspect ratio: 16:9. Style: warm watercolor-like editorial illustration, high-quality Japanese picture-book style, soft natural colors, realistic household objects, contemporary Japanese everyday home, clean but lived-in. Main visual: 記事内容に合う人物と物. Purpose: . Tone: 日本の実家らしさ、読者が状況を想像しやすい生活感、明るく清潔、不安を煽らない、買取業者っぽくしすぎない、捨てるより確認する・分けるを見せる. Must avoid: no text, no letters, no numbers, no Japanese characters, no English words, no labels, no logo, no watermark, no signage, no speech bubbles. Also avoid: ゴミ屋敷のような汚さ、暗い遺品整理の雰囲気、札束や高額査定の強調、不用品回収業者だけを推す広告感、既存記事と同じ構図や素材の使い回し、ミニマリスト風の真っ白な部屋、ロゴが見出し・人物の顔・重要な品物を邪魔する配置、抽象的な線、丸、四角、矢印だけで構成された低品質な図解、無料素材風の薄いアイコン図解.

#### ブランド帰属ロゴ

- ロゴ必須: はい
- ロゴ: `seiribu-editorial/assets/images/brand/seiribu-logo.png`
- 表示モード: auto
- 透過ロゴ: 背景が薄く、ロゴが十分に読める場合
- 白背景付きロゴ: 背景が濃い、複雑、またはロゴが沈む場合
- 配置候補: 左上, 右上, 右下, 左下
- 配置ルール: 人物の顔、重要な品物、図解ラベル、キャプションを邪魔しない上部または下部の余白に小さく配置する。
- 理由: Google画像検索、Pinterest、無断転載先で画像が単体流通したときのブランド帰属表示。

### 3. 記事内イメージ

- ファイル名: `only-child-conflict-trap.png`
- WordPress画像タイトル: 片付けを巡って親と1対1で対立してしまう一人っ子のイメージ
- ALT: 片付けを巡って親と1対1で対立してしまう一人っ子のイメージ
- 最終サイズ: 1200 x 675
- 生成時の比率: 16:9
- 制作方法: 画像生成素材 + ブランド帰属ロゴ合成
- 設置位置: 本文中のCMSブリーフ位置
- キャプション候補: 「捨てる・捨てない」で親と1対1で向き合うと、逃げ場のない対立構造に陥ってしまいます。

#### 制作意図

- 目的: 未指定
- 読者に伝えたい感情: 未指定
- 入れたい要素: 未指定
- 避けたい表現: 未指定

#### 生成プロンプト / レイアウト仕様

Create a warm text-free editorial illustration for the Seiribu article '一人っ子の実家の片付けはどう進める？親との話し合いと準備'. Aspect ratio: 16:9. Style: warm watercolor-like editorial illustration, high-quality Japanese picture-book style, soft natural colors, realistic household objects, contemporary Japanese everyday home, clean but lived-in. Main visual: 記事内容に合う人物と物. Purpose: . Tone: 日本の実家らしさ、読者が状況を想像しやすい生活感、明るく清潔、不安を煽らない、買取業者っぽくしすぎない、捨てるより確認する・分けるを見せる. Must avoid: no text, no letters, no numbers, no Japanese characters, no English words, no labels, no logo, no watermark, no signage, no speech bubbles. Also avoid: ゴミ屋敷のような汚さ、暗い遺品整理の雰囲気、札束や高額査定の強調、不用品回収業者だけを推す広告感、既存記事と同じ構図や素材の使い回し、ミニマリスト風の真っ白な部屋、ロゴが見出し・人物の顔・重要な品物を邪魔する配置、抽象的な線、丸、四角、矢印だけで構成された低品質な図解、無料素材風の薄いアイコン図解.

#### ブランド帰属ロゴ

- ロゴ必須: はい
- ロゴ: `seiribu-editorial/assets/images/brand/seiribu-logo.png`
- 表示モード: auto
- 透過ロゴ: 背景が薄く、ロゴが十分に読める場合
- 白背景付きロゴ: 背景が濃い、複雑、またはロゴが沈む場合
- 配置候補: 左上, 右上, 右下, 左下
- 配置ルール: 人物の顔、重要な品物、図解ラベル、キャプションを邪魔しない上部または下部の余白に小さく配置する。
- 理由: Google画像検索、Pinterest、無断転載先で画像が単体流通したときのブランド帰属表示。

### 4. 記事内図解

- ファイル名: `only-child-two-professionals.png`
- WordPress画像タイトル: 一人っ子が味方につけるべき2種類のプロ
- ALT: 一人っ子が味方につけるべき2種類のプロ（出張買取業者と不用品回収業者）
- 最終サイズ: 1200 x 675
- 生成時の比率: 16:9
- 制作方法: 画像生成でサンプルのようなイラスト図解ベースを作り、Pillow、SVG、またはCanvaで短いラベルとロゴを正確に合成する
- 設置位置: 本文中のCMSブリーフ位置
- キャプション候補: 一人っ子の負担を劇的に減らすためには、価値を見極める「買取業者」とゴミを一掃する「回収業者」の使い分けが必須です。

#### 制作意図

- 目的: 未指定
- 読者に伝えたい感情: 未指定
- 入れたい要素: 未指定
- 避けたい表現: 未指定

#### 生成プロンプト / レイアウト仕様

Create a text-free illustrated diagram base for a Seiribu article. Aspect ratio: 16:9. Style: warm Japanese picture-book style illustrated diagram, scene-based panels with people, household items, rooms, boxes, kimono, books, cameras or other concrete objects, not abstract line art, not plain geometric shapes. Content to show as warm scene-based panels or a comparison illustration: 未指定. Purpose: . Must avoid: no text, no letters, no numbers, no Japanese characters, no English words, no labels, no logo, no watermark, no signage, no speech bubbles. Also avoid: ゴミ屋敷のような汚さ、暗い遺品整理の雰囲気、札束や高額査定の強調、不用品回収業者だけを推す広告感、既存記事と同じ構図や素材の使い回し、ミニマリスト風の真っ白な部屋、ロゴが見出し・人物の顔・重要な品物を邪魔する配置、抽象的な線、丸、四角、矢印だけで構成された低品質な図解、無料素材風の薄いアイコン図解. Do not create abstract line art, a generic flowchart, wireframe boxes, plain circles, arrows-only diagrams, or free-icon-style graphics. Use concrete scenes with people, household items, rooms, boxes, kimono, books, cameras, documents, or other article-specific objects. Do not include readable text, Japanese labels, numbers, logo, watermark, signage, or speech bubbles in the generated image; short Japanese labels and captions will be added later with Pillow, SVG, or Canva. Leave quiet margin space for a small Seiribu brand logo overlay. ロゴ: 本文画像・本文図解はブランド帰属表示としてロゴ必須。背景が薄い場合は透過ロゴ、濃い・複雑な場合は薄い白背景付きロゴを、上部または下部の余白に小さく配置する。

#### ブランド帰属ロゴ

- ロゴ必須: はい
- ロゴ: `seiribu-editorial/assets/images/brand/seiribu-logo.png`
- 表示モード: auto
- 透過ロゴ: 背景が薄く、ロゴが十分に読める場合
- 白背景付きロゴ: 背景が濃い、複雑、またはロゴが沈む場合
- 配置候補: 左上, 右上, 右下, 左下
- 配置ルール: 人物の顔、重要な品物、図解ラベル、キャプションを邪魔しない上部または下部の余白に小さく配置する。
- 理由: Google画像検索、Pinterest、無断転載先で画像が単体流通したときのブランド帰属表示。

### 5. 記事内図解

- ファイル名: `only-child-3steps-flow.png`
- WordPress画像タイトル: 買取の利益で回収費用を相殺する実家の片付け3ステップ
- ALT: 買取の利益で回収費用を相殺する実家の片付け3ステップ
- 最終サイズ: 1200 x 675
- 生成時の比率: 16:9
- 制作方法: 画像生成でサンプルのようなイラスト図解ベースを作り、Pillow、SVG、またはCanvaで短いラベルとロゴを正確に合成する
- 設置位置: 本文中のCMSブリーフ位置
- キャプション候補: 買取で得た現金を処分費用に充てる「相殺」テクニックを使えば、費用の負担は最小限に抑えられます。

#### 制作意図

- 目的: 未指定
- 読者に伝えたい感情: 未指定
- 入れたい要素: 未指定
- 避けたい表現: 未指定

#### 生成プロンプト / レイアウト仕様

Create a text-free illustrated diagram base for a Seiribu article. Aspect ratio: 16:9. Style: warm Japanese picture-book style illustrated diagram, scene-based panels with people, household items, rooms, boxes, kimono, books, cameras or other concrete objects, not abstract line art, not plain geometric shapes. Content to show as warm scene-based panels or a comparison illustration: 未指定. Purpose: . Must avoid: no text, no letters, no numbers, no Japanese characters, no English words, no labels, no logo, no watermark, no signage, no speech bubbles. Also avoid: ゴミ屋敷のような汚さ、暗い遺品整理の雰囲気、札束や高額査定の強調、不用品回収業者だけを推す広告感、既存記事と同じ構図や素材の使い回し、ミニマリスト風の真っ白な部屋、ロゴが見出し・人物の顔・重要な品物を邪魔する配置、抽象的な線、丸、四角、矢印だけで構成された低品質な図解、無料素材風の薄いアイコン図解. Do not create abstract line art, a generic flowchart, wireframe boxes, plain circles, arrows-only diagrams, or free-icon-style graphics. Use concrete scenes with people, household items, rooms, boxes, kimono, books, cameras, documents, or other article-specific objects. Do not include readable text, Japanese labels, numbers, logo, watermark, signage, or speech bubbles in the generated image; short Japanese labels and captions will be added later with Pillow, SVG, or Canva. Leave quiet margin space for a small Seiribu brand logo overlay. ロゴ: 本文画像・本文図解はブランド帰属表示としてロゴ必須。背景が薄い場合は透過ロゴ、濃い・複雑な場合は薄い白背景付きロゴを、上部または下部の余白に小さく配置する。

#### ブランド帰属ロゴ

- ロゴ必須: はい
- ロゴ: `seiribu-editorial/assets/images/brand/seiribu-logo.png`
- 表示モード: auto
- 透過ロゴ: 背景が薄く、ロゴが十分に読める場合
- 白背景付きロゴ: 背景が濃い、複雑、またはロゴが沈む場合
- 配置候補: 左上, 右上, 右下, 左下
- 配置ルール: 人物の顔、重要な品物、図解ラベル、キャプションを邪魔しない上部または下部の余白に小さく配置する。
- 理由: Google画像検索、Pinterest、無断転載先で画像が単体流通したときのブランド帰属表示。

### 6. 記事内図解

- ファイル名: `only-child-inline-options.png`
- WordPress画像タイトル: 実家の片付けステップ1：ゴミ捨てよりも通帳や印鑑などの重要書類の確保を優先する図解
- ALT: 実家の片付けステップ1：ゴミ捨てよりも通帳や印鑑などの重要書類の確保を優先する図解
- 最終サイズ: 1200 x 675
- 生成時の比率: 16:9
- 制作方法: 画像生成でサンプルのようなイラスト図解ベースを作り、Pillow、SVG、またはCanvaで短いラベルとロゴを正確に合成する
- 設置位置: 本文中のCMSブリーフ位置
- キャプション候補: まずはゴミを捨てる手を止め、通帳や権利書など「失うと絶望的な手間がかかる重要書類」の確保を最優先にしましょう。

#### 制作意図

- 目的: 未指定
- 読者に伝えたい感情: 未指定
- 入れたい要素: 未指定
- 避けたい表現: 未指定

#### 生成プロンプト / レイアウト仕様

Create a text-free illustrated diagram base for a Seiribu article. Aspect ratio: 16:9. Style: warm Japanese picture-book style illustrated diagram, scene-based panels with people, household items, rooms, boxes, kimono, books, cameras or other concrete objects, not abstract line art, not plain geometric shapes. Content to show as warm scene-based panels or a comparison illustration: 未指定. Purpose: . Must avoid: no text, no letters, no numbers, no Japanese characters, no English words, no labels, no logo, no watermark, no signage, no speech bubbles. Also avoid: ゴミ屋敷のような汚さ、暗い遺品整理の雰囲気、札束や高額査定の強調、不用品回収業者だけを推す広告感、既存記事と同じ構図や素材の使い回し、ミニマリスト風の真っ白な部屋、ロゴが見出し・人物の顔・重要な品物を邪魔する配置、抽象的な線、丸、四角、矢印だけで構成された低品質な図解、無料素材風の薄いアイコン図解. Do not create abstract line art, a generic flowchart, wireframe boxes, plain circles, arrows-only diagrams, or free-icon-style graphics. Use concrete scenes with people, household items, rooms, boxes, kimono, books, cameras, documents, or other article-specific objects. Do not include readable text, Japanese labels, numbers, logo, watermark, signage, or speech bubbles in the generated image; short Japanese labels and captions will be added later with Pillow, SVG, or Canva. Leave quiet margin space for a small Seiribu brand logo overlay. ロゴ: 本文画像・本文図解はブランド帰属表示としてロゴ必須。背景が薄い場合は透過ロゴ、濃い・複雑な場合は薄い白背景付きロゴを、上部または下部の余白に小さく配置する。

#### ブランド帰属ロゴ

- ロゴ必須: はい
- ロゴ: `seiribu-editorial/assets/images/brand/seiribu-logo.png`
- 表示モード: auto
- 透過ロゴ: 背景が薄く、ロゴが十分に読める場合
- 白背景付きロゴ: 背景が濃い、複雑、またはロゴが沈む場合
- 配置候補: 左上, 右上, 右下, 左下
- 配置ルール: 人物の顔、重要な品物、図解ラベル、キャプションを邪魔しない上部または下部の余白に小さく配置する。
- 理由: Google画像検索、Pinterest、無断転載先で画像が単体流通したときのブランド帰属表示。

### 7. 記事内図解

- ファイル名: `only-child-inline-steps.png`
- WordPress画像タイトル: 実家の片付けステップ2：プロの査定士が親を説得し、買取金を得る図解
- ALT: 実家の片付けステップ2：プロの査定士が親を説得し、買取金（軍資金）を得る図解
- 最終サイズ: 1200 x 675
- 生成時の比率: 16:9
- 制作方法: 画像生成でサンプルのようなイラスト図解ベースを作り、Pillow、SVG、またはCanvaで短いラベルとロゴを正確に合成する
- 設置位置: 本文中のCMSブリーフ位置
- キャプション候補: プロの客観的な査定は親の執着を断ち切り、さらにその後の片付けの「軍資金」を生み出します。

#### 制作意図

- 目的: 未指定
- 読者に伝えたい感情: 未指定
- 入れたい要素: 未指定
- 避けたい表現: 未指定

#### 生成プロンプト / レイアウト仕様

Create a text-free illustrated diagram base for a Seiribu article. Aspect ratio: 16:9. Style: warm Japanese picture-book style illustrated diagram, scene-based panels with people, household items, rooms, boxes, kimono, books, cameras or other concrete objects, not abstract line art, not plain geometric shapes. Content to show as warm scene-based panels or a comparison illustration: 未指定. Purpose: . Must avoid: no text, no letters, no numbers, no Japanese characters, no English words, no labels, no logo, no watermark, no signage, no speech bubbles. Also avoid: ゴミ屋敷のような汚さ、暗い遺品整理の雰囲気、札束や高額査定の強調、不用品回収業者だけを推す広告感、既存記事と同じ構図や素材の使い回し、ミニマリスト風の真っ白な部屋、ロゴが見出し・人物の顔・重要な品物を邪魔する配置、抽象的な線、丸、四角、矢印だけで構成された低品質な図解、無料素材風の薄いアイコン図解. Do not create abstract line art, a generic flowchart, wireframe boxes, plain circles, arrows-only diagrams, or free-icon-style graphics. Use concrete scenes with people, household items, rooms, boxes, kimono, books, cameras, documents, or other article-specific objects. Do not include readable text, Japanese labels, numbers, logo, watermark, signage, or speech bubbles in the generated image; short Japanese labels and captions will be added later with Pillow, SVG, or Canva. Leave quiet margin space for a small Seiribu brand logo overlay. ロゴ: 本文画像・本文図解はブランド帰属表示としてロゴ必須。背景が薄い場合は透過ロゴ、濃い・複雑な場合は薄い白背景付きロゴを、上部または下部の余白に小さく配置する。

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

- Canvaで仕上げるためのアイキャッチ素材指定を利用しています。
- 本文画像が多めです。標準は本文画像・図解4枚です。
- 画像生成AIに文字、日本語ラベル、ロゴ、透かし、看板を描かせない。
- 日本語ラベルがある図解は、画像生成AIに文字を任せずレイアウト生成で作る。
- 図解は抽象的な線や図形だけにせず、サンプルのような人物・品物・実家の場面を含むイラスト図解ベースで作る。
- アイキャッチのロゴとタイトルはCanvaで人間が最終合成する。
- ロゴ必須対象: アイキャッチ完成版, Canva仕上げ画像。
- 本文画像・本文図解のロゴ: 本文画像・本文図解はブランド帰属表示としてロゴ必須。背景が薄い場合は透過ロゴ、濃い・複雑な場合は薄い白背景付きロゴを、上部または下部の余白に小さく配置する。
- 暗い遺品整理、ゴミ屋敷、高額査定広告の印象を避ける。
- imagegenの生成候補は `/private/tmp/seiribu-image-work/only-child` に置き、採用画像だけ `seiribu-editorial/assets/images/only-child` に移す。
- 公開用フォルダに残った候補や旧版は `seiribu-editorial/scripts/clean_image_assets.py --article only-child --dry-run` で確認してから退避する。
