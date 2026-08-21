# 画像制作プラン: 実家の片付けを一人っ子はどう進める？親と揉めずに自力で乗り切る手順

## 記事情報

- 記事ファイル: `drafts/only-child.md`
- スラッグ: `only-child`
- メインKW: 一人っ子 実家 片付け
- 出力モード: standard（記事内のCMS画像指定をすべて展開する標準モード。アイキャッチ素材1件と本文画像・図解4件を基本にする）
- アイキャッチ仕上げ: Canva手動仕上げ
- Canvaテンプレ: https://canva.link/mqlqak3adj01g1i（任意・手動微調整）
- ロゴ: `seiribu-editorial/assets/images/brand/seiribu-logo.png`
- ロゴ必須対象: アイキャッチ完成版, Canva仕上げ画像, 本文画像, 本文図解
- 本文画像のロゴ: 本文画像・本文図解はブランド帰属表示としてロゴ必須。背景が薄い場合は透過ロゴ、濃い・複雑な場合は薄い白背景付きロゴを、上部または下部の余白に小さく配置する。
- 画像生成ツール: imagegen
- 図解レイアウトツール: imagegen complete illustrated infographic with model-native short Japanese text + logo overlay
- 生成候補の一時置き場: `/private/tmp/seiribu-image-work/only-child`
- 採用画像の公開用置き場: `seiribu-editorial/assets/images/only-child`
- 画像掃除スクリプト: `seiribu-editorial/scripts/clean_image_assets.py`

## 判定サマリー

| No | 用途 | 制作方法 | 最終サイズ | 生成時の比率 | ファイル名 | 設置位置 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | アイキャッチ素材 | 画像生成素材 + Canva手動仕上げ | 1200 x 675 | 16:9 | `only-child-eyecatch.png` | アイキャッチ合成用素材 |
| 2 | 記事内イメージ | 画像生成素材 + ブランド帰属ロゴ合成 | 1200 x 675 | 16:9 | `only-child-inline-steps.png` | 本文中のCMSブリーフ位置 |
| 3 | 記事内図解_scene | 画像生成素材 + ブランド帰属ロゴ合成 | 1200 x 675 | 16:9 | `only-child-inline-options.png` | 本文中のCMSブリーフ位置 |
| 4 | 記事内イメージ | 画像生成素材 + ブランド帰属ロゴ合成 | 1200 x 675 | 16:9 | `only-child-inline-ng-ok.png` | 本文中のCMSブリーフ位置 |
| 5 | 記事内図解_slide | 画像生成素材 + ブランド帰属ロゴ合成 | 1200 x 675 | 16:9 | `only-child-inline-options-2.png` | 本文中のCMSブリーフ位置 |

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

- 目的: 記事の第一印象。一人で抱え込まずに済むという安心感
- 読者に伝えたい感情: 安心感、解決への期待感
- 入れたい要素: 片付けに悩む人と、サポートする業者や相談窓口のイメージ
- 避けたい表現: 画像内へのテキスト（文字）の生成、背景の描画

#### 生成プロンプト / レイアウト仕様

Create an eyecatch cutout asset for the Seiribu article '実家の片付けを一人っ子はどう進める？親と揉めずに自力で乗り切る手順'. Aspect ratio: 16:9. Style: warm flat editorial illustration cutout, high-quality 2D vector art, single coherent subject, clean silhouette, easy to remove background. Transparent background if possible; if transparency is not available, use a single flat light background that is easy to remove. Do not include a room, wall, floor, cast shadow, title area, logo area, or decorative frame. Main subject: 片付けに悩む人と、サポートする業者や相談窓口のイメージ. Purpose: 記事の第一印象。一人で抱え込まずに済むという安心感. Tone: 読者がパッと見て意味がわかる視覚的なわかりやすさ、情報を整理して伝えるクリーンなインフォグラフィック調、清潔感と信頼感、不安を煽らない、買取業者っぽくしすぎない、過度な感情の押し売りをしないスマートな解説. Must avoid: no logo, no watermark, no signage, no messy background scribbles. Also avoid: 画像内へのテキスト（文字）の生成、背景の描画. Do not reuse the composition, character placement, object placement, or background concept from any existing Seiribu article image.

#### アイキャッチCanva仕上げ

- 仕上げ方法: Canva手動仕上げ
- タイトル: 実家の片付けを一人っ子はどう進める？
- サブタイトル: 親と揉めずに自力で乗り切る手順
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
- タイトル: 実家の片付けを一人っ子はどう進める？
- サブタイトル: 親と揉めずに自力で乗り切る手順
- ロゴ: `seiribu-editorial/assets/images/brand/seiribu-logo.png`
- ロゴ必須: はい
- ロゴ位置: 左上
- ロゴ配置ルール: 生成AI素材にはロゴを描かせない。アイキャッチ完成版はCanvaで人間が仕上げる。本文画像・本文図解はCodex側でブランド帰属ロゴを必ず合成する。背景が薄い場合は透過ロゴ、濃い・複雑な場合は薄い白背景付きロゴを使い、人物の顔、重要な品物、図解ラベルを邪魔しない余白に配置する。
- 見出しフォント: UDモトヤアポロ 太字
- サブタイトルフォント: Noto Sans JP Regular

### 2. 記事内イメージ

- ファイル名: `only-child-inline-steps.png`
- WordPress画像タイトル: 一人っ子でも無理なく実家の片付けを進めるイメージ
- ALT: 一人っ子でも無理なく実家の片付けを進めるイメージ
- 最終サイズ: 1200 x 675
- 生成時の比率: 16:9
- 制作方法: 画像生成素材 + ブランド帰属ロゴ合成
- 設置位置: 本文中のCMSブリーフ位置
- キャプション候補: 家全体を一気に片付けようとせず、まずは小さな場所から親のペースに合わせて進めるのが失敗しないコツです。

#### 制作意図

- 目的: 一人っ子でも少しずつ安全に進められるという安心感を視覚的に伝える
- 読者に伝えたい感情: 安心感、これならできそうという前向きな気持ち
- 入れたい要素: 実家の洗面所や玄関などの小さなスペースで、親と子が穏やかに話し合いながら物を整理している温かいイラスト
- 避けたい表現: 画像内へのテキスト（文字）の生成、作業の辛さを連想させるような暗い色合い、家全体が散らかっている表現

#### 生成プロンプト / レイアウト仕様

Create a warm text-free editorial illustration for the Seiribu article '実家の片付けを一人っ子はどう進める？親と揉めずに自力で乗り切る手順'. Aspect ratio: 16:9. Style: high-quality Japanese editorial illustration, utilizing varied art styles (e.g., soft watercolor, modern flat vector, pastel, clean line art) to avoid visual repetition, soft natural colors, realistic household objects, contemporary Japanese everyday home, clean but lived-in. Main visual: 実家の洗面所や玄関などの小さなスペースで、親と子が穏やかに話し合いながら物を整理している温かいイラスト. Purpose: 一人っ子でも少しずつ安全に進められるという安心感を視覚的に伝える. Tone: 読者がパッと見て意味がわかる視覚的なわかりやすさ、情報を整理して伝えるクリーンなインフォグラフィック調、清潔感と信頼感、不安を煽らない、買取業者っぽくしすぎない、過度な感情の押し売りをしないスマートな解説. Must avoid: no logo, no watermark, no signage, no messy background scribbles. Also avoid: 画像内へのテキスト（文字）の生成、作業の辛さを連想させるような暗い色合い、家全体が散らかっている表現.

#### ブランド帰属ロゴ

- ロゴ必須: はい
- ロゴ: `seiribu-editorial/assets/images/brand/seiribu-logo.png`
- 表示モード: auto
- 透過ロゴ: 背景が薄く、ロゴが十分に読める場合
- 白背景付きロゴ: 背景が濃い、複雑、またはロゴが沈む場合
- 配置候補: 左上, 右上, 右下, 左下
- 配置ルール: 人物の顔、重要な品物、図解ラベル、キャプションを邪魔しない上部または下部の余白に小さく配置する。
- 理由: Google画像検索、Pinterest、無断転載先で画像が単体流通したときのブランド帰属表示。

### 3. 記事内図解_scene

- ファイル名: `only-child-inline-options.png`
- WordPress画像タイトル: 一人っ子が実家の片付けで抱える3つの過酷な重圧
- ALT: 一人っ子が実家の片付けで抱える3つの過酷な重圧（決断・対立・費用）
- 最終サイズ: 1200 x 675
- 生成時の比率: 16:9
- 制作方法: 画像生成素材 + ブランド帰属ロゴ合成
- 設置位置: 本文中のCMSブリーフ位置
- キャプション候補: 一人っ子の片付けは、決断・作業・費用の負担がすべて一人に集中する過酷な構造になっています。

#### 制作意図

- 目的: 一人っ子が抱える3つの特有の重圧を視覚化し、読者に「自分だけが辛いわけではない」と共感してもらう
- 読者に伝えたい感情: 共感、孤独感からの解放
- 入れたい要素: 3つの重圧（決断の責任、親との対立、費用の負担）をそれぞれ四角い枠線のボックスに整理し、中央の一人っ子に矢印が向かうような構造のインフォグラフィック
- 避けたい表現: 過度に絶望感を煽る暗い色合い、解読不能な長文テキスト

#### 生成プロンプト / レイアウト仕様

Create an illustrated infographic diagram for a Seiribu article. Aspect ratio: 16:9. Style: high-quality editorial illustration diagram with simple scene panels, utilizing varied art styles (e.g., flat vector, watercolor, pastel, modern line art) to avoid visual repetition, soft colors, no photorealism, no realistic lighting, no camera perspective. Content to show as a structured infographic diagram: 3つの重圧（決断の責任、親との対立、費用の負担）をそれぞれ四角い枠線のボックスに整理し、中央の一人っ子に矢印が向かうような構造のインフォグラフィック. Layout: Use a clean, solid background (e.g., white or light beige). Structure the information using bordered boxes for each step and connecting arrows. Do NOT create full-bleed comic panels or edge-to-edge full-screen scenes. Keep ample negative space. It is perfectly fine to use spot illustrations of characters and items inside the diagram boxes. Do not create empty placeholder boxes, dotted rectangles, blank logo slots, or unused label cards. Typography: Render the provided Japanese labels clearly, boldly, and accurately as part of the diagram. Do not use scribbles or fake text. Do not specify a font; let the image model choose a clean natural label style. Purpose: 一人っ子が抱える3つの特有の重圧を視覚化し、読者に「自分だけが辛いわけではない」と共感してもらう. Must avoid: no logo, no watermark, no signage, no messy background scribbles, no messy placeholder scribbles, no font specification. Also avoid: 過度に絶望感を煽る暗い色合い、解読不能な長文テキスト. Do not create full-screen immersive scenes or manga layouts. Do not create abstract line art only. Leave quiet margin space for a small Seiribu brand logo overlay. ロゴ: 本文画像・本文図解はブランド帰属表示としてロゴ必須。背景が薄い場合は透過ロゴ、濃い・複雑な場合は薄い白背景付きロゴを、上部または下部の余白に小さく配置する。

#### ブランド帰属ロゴ

- ロゴ必須: はい
- ロゴ: `seiribu-editorial/assets/images/brand/seiribu-logo.png`
- 表示モード: auto
- 透過ロゴ: 背景が薄く、ロゴが十分に読める場合
- 白背景付きロゴ: 背景が濃い、複雑、またはロゴが沈む場合
- 配置候補: 左上, 右上, 右下, 左下
- 配置ルール: 人物の顔、重要な品物、図解ラベル、キャプションを邪魔しない上部または下部の余白に小さく配置する。
- 理由: Google画像検索、Pinterest、無断転載先で画像が単体流通したときのブランド帰属表示。

### 4. 記事内イメージ

- ファイル名: `only-child-inline-ng-ok.png`
- WordPress画像タイトル: 親の気持ちを尊重しながら実家の片付けについて話し合う様子
- ALT: 親の気持ちを尊重しながら実家の片付けについて話し合う様子
- 最終サイズ: 1200 x 675
- 生成時の比率: 16:9
- 制作方法: 画像生成素材 + ブランド帰属ロゴ合成
- 設置位置: 本文中のCMSブリーフ位置
- キャプション候補: 実家はあくまで親のテリトリーです。勝手に捨てるのではなく、親の思い出話に耳を傾ける余裕を持つことが、結果的に片付けの近道になります。

#### 制作意図

- 目的: 「捨てる」と強要せず、親の気持ちに寄り添う対話の重要性を伝える
- 読者に伝えたい感情: 親への理解、優しい声かけへの気づき
- 入れたい要素: 実家の居間で、子どもが親の昔のアルバムや思い出の品を一緒に見ながら、笑顔で穏やかに話を聞いている情景
- 避けたい表現: 親と子が険悪な表情で言い争っているネガティブな表現、画像内へのテキスト（文字）の生成

#### 生成プロンプト / レイアウト仕様

Create a warm text-free editorial illustration for the Seiribu article '実家の片付けを一人っ子はどう進める？親と揉めずに自力で乗り切る手順'. Aspect ratio: 16:9. Style: high-quality Japanese editorial illustration, utilizing varied art styles (e.g., soft watercolor, modern flat vector, pastel, clean line art) to avoid visual repetition, soft natural colors, realistic household objects, contemporary Japanese everyday home, clean but lived-in. Main visual: 実家の居間で、子どもが親の昔のアルバムや思い出の品を一緒に見ながら、笑顔で穏やかに話を聞いている情景. Purpose: 「捨てる」と強要せず、親の気持ちに寄り添う対話の重要性を伝える. Tone: 読者がパッと見て意味がわかる視覚的なわかりやすさ、情報を整理して伝えるクリーンなインフォグラフィック調、清潔感と信頼感、不安を煽らない、買取業者っぽくしすぎない、過度な感情の押し売りをしないスマートな解説. Must avoid: no logo, no watermark, no signage, no messy background scribbles. Also avoid: 親と子が険悪な表情で言い争っているネガティブな表現、画像内へのテキスト（文字）の生成.

#### ブランド帰属ロゴ

- ロゴ必須: はい
- ロゴ: `seiribu-editorial/assets/images/brand/seiribu-logo.png`
- 表示モード: auto
- 透過ロゴ: 背景が薄く、ロゴが十分に読める場合
- 白背景付きロゴ: 背景が濃い、複雑、またはロゴが沈む場合
- 配置候補: 左上, 右上, 右下, 左下
- 配置ルール: 人物の顔、重要な品物、図解ラベル、キャプションを邪魔しない上部または下部の余白に小さく配置する。
- 理由: Google画像検索、Pinterest、無断転載先で画像が単体流通したときのブランド帰属表示。

### 5. 記事内図解_slide

- ファイル名: `only-child-inline-options-2.png`
- WordPress画像タイトル: 出張買取と不用品回収を使い分けて一人っ子の片付け負担を減らす方法
- ALT: 出張買取と不用品回収を使い分けて一人っ子の片付け負担を減らす方法
- 最終サイズ: 1200 x 675
- 生成時の比率: 16:9
- 制作方法: 画像生成素材 + ブランド帰属ロゴ合成
- 設置位置: 本文中のCMSブリーフ位置
- キャプション候補: 価値あるものを買取に出して費用を相殺し、肉体労働は回収業者に任せるのが、一人っ子が潰れないための「逃げ道」です。

#### 制作意図

- 目的: 出張買取と不用品回収を使い分けることで負担が減る仕組みを図解する
- 読者に伝えたい感情: 解決への道筋が見えた安心感、賢い選択をしているという自信
- 入れたい要素: 「出張買取（価値ある物→軍資金）」と「不用品回収（ゴミ→丸投げ処分）」の2つのルートを左右に配置し、下部の「一人っ子の負担減」につながるフローチャート風の図解
- 避けたい表現: 高級感だけが強い買取業者風のデザイン、札束の直接的な描写、抽象的すぎる図形だけのデザイン

#### 生成プロンプト / レイアウト仕様

Create a simple 16:9 Japanese slide-style infographic.

Style:
simple slide-style flat 2D vector infographic, icon-based diagram, clean presentation slide, light cream background, rounded cards, simple arrows, large readable Japanese labels, limited warm colors, minimal icon-like people only if necessary, no photorealism, no realistic lighting, no camera perspective, no detailed room scene

Important:
This must look like a simple slide diagram, not a photo, not a realistic scene, not watercolor, not manga, not a full room illustration. Use minimal icon-like people only if needed. No realistic lighting, no camera perspective, no detailed faces.

Content:
出張買取と不用品回収を使い分けることで負担が減る仕組みを図解する

Layout:
Clean presentation layout with cards and arrows.

Typography Instruction:
Render the following Japanese labels clearly and beautifully as integral parts of the infographic:
「出張買取（価値ある物→軍資金）」と「不用品回収（ゴミ→丸投げ処分）」の2つのルートを左右に配置し、下部の「一人っ子の負担減」につながるフローチャート風の図解

Avoid:
no logo, no watermark, no money unless explicitly required, no truck unless explicitly required, no sales scene, no logo, no watermark, no signage, no messy background scribbles, no messy placeholder scribbles, no font specification. 高級感だけが強い買取業者風のデザイン、札束の直接的な描写、抽象的すぎる図形だけのデザイン.
Leave a quiet corner for a small Seiribu brand logo overlay.

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
- 本文画像・図解は4枚構成です。記事内の全CMSブリーフを標準制作対象にします。
- 画像生成AIにロゴ、透かし、看板を描かせない（文字やラベルは積極的に描かせる）。
- 日本語ラベルがある図解は、指定されたテキストが美しく統合されたインフォグラフィックになるようプロンプトで指示する。
- 図解は抽象的な線や図形だけにせず、サンプルのような人物・品物・実家の場面を含むイラスト図解ベースで作る。
- アイキャッチのロゴとタイトルはCanvaで人間が最終合成する。
- ロゴ必須対象: アイキャッチ完成版, Canva仕上げ画像, 本文画像, 本文図解。
- 本文画像・本文図解のロゴ: 本文画像・本文図解はブランド帰属表示としてロゴ必須。背景が薄い場合は透過ロゴ、濃い・複雑な場合は薄い白背景付きロゴを、上部または下部の余白に小さく配置する。
- 暗い遺品整理、ゴミ屋敷、高額査定広告の印象を避ける。
- imagegenの生成候補は `/private/tmp/seiribu-image-work/only-child` に置き、採用画像だけ `seiribu-editorial/assets/images/only-child` に移す。
- 公開用フォルダに残った候補や旧版は `seiribu-editorial/scripts/clean_image_assets.py --article only-child --dry-run` で確認してから退避する。
