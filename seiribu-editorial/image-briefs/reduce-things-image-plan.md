# 画像制作プラン: 物を減らすと楽になる理由｜何から始める？無理なく続ける整理のコツ

## 記事情報

- 記事ファイル: `seiribu-editorial/drafts/reduce-things.md`
- スラッグ: `reduce-things`
- メインKW: 物を減らすと楽になる
- 出力モード: standard（記事内のCMS画像指定をすべて展開する標準モード。アイキャッチ素材1件と本文画像・図解4件を基本にする）
- アイキャッチ仕上げ: Canva手動仕上げ
- Canvaテンプレ: https://canva.link/mqlqak3adj01g1i（任意・手動微調整）
- ロゴ: `seiribu-editorial/assets/images/brand/seiribu-logo.png`
- ロゴ必須対象: アイキャッチ完成版, Canva仕上げ画像, 本文画像, 本文図解
- 本文画像のロゴ: 本文画像・本文図解はブランド帰属表示としてロゴ必須。背景が薄い場合は透過ロゴ、濃い・複雑な場合は薄い白背景付きロゴを、上部または下部の余白に小さく配置する。
- 画像生成ツール: imagegen
- 図解レイアウトツール: imagegen complete illustrated infographic with model-native short Japanese text + logo overlay
- 生成候補の一時置き場: `/private/tmp/seiribu-image-work/reduce-things`
- 採用画像の公開用置き場: `seiribu-editorial/assets/images/reduce-things`
- 画像掃除スクリプト: `seiribu-editorial/scripts/clean_image_assets.py`

## 判定サマリー

| No | 用途 | 制作方法 | 最終サイズ | 生成時の比率 | ファイル名 | 設置位置 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | アイキャッチ | 画像生成素材 + Canva手動仕上げ | 1200 x 675 | 16:9 | `reduce-things-eyecatch-branded.png` | アイキャッチ |
| 2 | 記事内図解_scene | 画像生成素材 + ブランド帰属ロゴ合成 | 1200 x 675 | 16:9 | `reduce-things-inline-01.png` | 本文中のCMSブリーフ位置 |
| 3 | 記事内図解_slide | 画像生成素材 + ブランド帰属ロゴ合成 | 1200 x 675 | 16:9 | `reduce-things-inline-options.png` | 本文中のCMSブリーフ位置 |
| 4 | 記事内イメージ | 画像生成素材 + ブランド帰属ロゴ合成 | 1200 x 675 | 16:9 | `reduce-things-inline-three-boxes.png` | 本文中のCMSブリーフ位置 |
| 5 | 記事内イメージ | 画像生成素材 + ブランド帰属ロゴ合成 | 1200 x 675 | 16:9 | `reduce-things-inline-ng-ok.png` | 本文中のCMSブリーフ位置 |

## 制作ブリーフ

### 1. アイキャッチ

- ファイル名: `reduce-things-eyecatch-branded.png`
- WordPress画像タイトル: 物を減らすには何から始めるかを考えながら小さな場所から整理する人
- ALT: 物を減らすには何から始めるかを考えながら小さな場所から整理する人
- 最終サイズ: 1200 x 675
- 生成時の比率: 16:9
- 制作方法: 画像生成素材 + Canva手動仕上げ
- 設置位置: アイキャッチ
- キャプション候補: なし

#### 制作意図

- 目的: 「物を減らすと楽になる」「何から始めるか」をひと目で伝える
- 読者に伝えたい感情: 未指定
- 入れたい要素: 未指定
- 避けたい表現: 極端なミニマリスト部屋、ゴミ屋敷、過度に暗い表情、札束や高額査定の強調

#### 生成プロンプト / レイアウト仕様

Create a text-free background-free eyecatch illustration material for the Seiribu article '物を減らすと楽になる理由｜何から始める？無理なく続ける整理のコツ'. Aspect ratio: 16:9. Style: warm flat editorial illustration cutout, high-quality 2D vector art, single coherent subject, clean silhouette, easy to remove background. Transparent background if possible; if transparency is not available, use a single flat light background that is easy to remove. Do not include a room, wall, floor, cast shadow, title area, logo area, decorative frame, placeholder card, or text panel. This background-free material will be finished later in the manual Canva eyecatch template. Main visual: 記事内容に合う人物と物. Purpose: 「物を減らすと楽になる」「何から始めるか」をひと目で伝える. Tone: 日本の実家らしさ、読者が状況を想像しやすい生活感、明るく清潔、不安を煽らない、買取業者っぽくしすぎない、捨てるより確認する・分けるを見せる. Must avoid: no text, no letters, no numbers, no Japanese characters, no English words, no labels, no logo, no watermark, no signage, no speech bubbles. Also avoid: 極端なミニマリスト部屋、ゴミ屋敷、過度に暗い表情、札束や高額査定の強調. Do not reuse the composition, character placement, object placement, or background concept from any existing Seiribu article image.

#### アイキャッチCanva仕上げ

- 仕上げ方法: Canva手動仕上げ
- タイトル: 物を減らすと楽になる理由｜何から始める？
- サブタイトル: 無理なく続ける整理のコツ
- 出力サイズ: 1200 x 675
- 出力ファイル: `reduce-things-eyecatch-branded.png`
- ロゴ: `seiribu-editorial/assets/images/brand/seiribu-logo.png`
- ロゴ必須: はい
- ロゴ位置: 左上
- ロゴ配置ルール: 生成AI素材にはロゴを描かせない。アイキャッチ完成版はCanvaで人間が仕上げる。本文画像・本文図解はCodex側でブランド帰属ロゴを必ず合成する。背景が薄い場合は透過ロゴ、濃い・複雑な場合は薄い白背景付きロゴを使い、人物の顔、重要な品物、図解ラベルを邪魔しない余白に配置する。
- Canvaの扱い: アイキャッチ完成版はCanvaで人間がタイトル、サブタイトル、ロゴ、Canva専用フォントを手動合成する。

#### Canva仕上げ

- 状態: optional_manual
- テンプレートURL: https://canva.link/mqlqak3adj01g1i
- タイトル: 物を減らすと楽になる理由｜何から始める？
- サブタイトル: 無理なく続ける整理のコツ
- ロゴ: `seiribu-editorial/assets/images/brand/seiribu-logo.png`
- ロゴ必須: はい
- ロゴ位置: 左上
- ロゴ配置ルール: 生成AI素材にはロゴを描かせない。アイキャッチ完成版はCanvaで人間が仕上げる。本文画像・本文図解はCodex側でブランド帰属ロゴを必ず合成する。背景が薄い場合は透過ロゴ、濃い・複雑な場合は薄い白背景付きロゴを使い、人物の顔、重要な品物、図解ラベルを邪魔しない余白に配置する。
- 見出しフォント: UDモトヤアポロ 太字
- サブタイトルフォント: Noto Sans JP Regular

### 2. 記事内図解_scene

- ファイル名: `reduce-things-inline-01.png`
- WordPress画像タイトル: 物を減らすことで探し物や掃除の時間が減るメリットの図解
- ALT: 物を減らすことで探し物や掃除の時間が減るメリットの図解
- 最終サイズ: 1200 x 675
- 生成時の比率: 16:9
- 制作方法: 画像生成素材 + ブランド帰属ロゴ合成
- 設置位置: 本文中のCMSブリーフ位置
- キャプション候補: 物が減ると、掃除や探し物の時間が大きく減ります

#### 制作意図

- 目的: 物を減らすことで、探し物や掃除の前の「物をどかす作業」が減り、心にゆとりが生まれることを図解する
- 読者に伝えたい感情: 物が少ないとこんなに楽なんだ、という納得感と期待感
- 入れたい要素: スッキリした部屋で探し物をせず笑顔で出かける様子と、散らかった部屋で焦って探し物をする様子の対比図解。短いテキストラベルあり。
- 避けたい表現: 画像内への大量の文字生成、極端なミニマリスト部屋

#### 生成プロンプト / レイアウト仕様

Create an illustrated infographic diagram for a Seiribu article. Aspect ratio: 16:9. Style: high-quality editorial illustration diagram with simple scene panels, utilizing varied art styles (e.g., flat vector, watercolor, pastel, modern line art) to avoid visual repetition, soft colors, no photorealism, no realistic lighting, no camera perspective. Content to show as a structured infographic diagram: スッキリした部屋で探し物をせず笑顔で出かける様子と、散らかった部屋で焦って探し物をする様子の対比図解。短いテキストラベルあり。. Layout: Use a clean, solid background (e.g., white or light beige). Structure the information using bordered boxes for each step and connecting arrows. Do NOT create full-bleed comic panels or edge-to-edge full-screen scenes. Keep ample negative space. It is perfectly fine to use spot illustrations of characters and items inside the diagram boxes. Do not create empty placeholder boxes, dotted rectangles, blank logo slots, or unused label cards. Render only the short Japanese labels explicitly implied by the brief, naturally, as part of the generated infographic. Do not specify a font; let the image model choose a clean natural label style. Purpose: 物を減らすことで、探し物や掃除の前の「物をどかす作業」が減り、心にゆとりが生まれることを図解する. Must avoid: no logo, no watermark, no signage, no speech bubbles, no garbled Japanese, no random extra labels, no font specification. Also avoid: 画像内への大量の文字生成、極端なミニマリスト部屋. Do not create full-screen immersive scenes or manga layouts. Do not create abstract line art only. Leave quiet margin space for a small Seiribu brand logo overlay. ロゴ: 本文画像・本文図解はブランド帰属表示としてロゴ必須。背景が薄い場合は透過ロゴ、濃い・複雑な場合は薄い白背景付きロゴを、上部または下部の余白に小さく配置する。

#### ブランド帰属ロゴ

- ロゴ必須: はい
- ロゴ: `seiribu-editorial/assets/images/brand/seiribu-logo.png`
- 表示モード: auto
- 透過ロゴ: 背景が薄く、ロゴが十分に読める場合
- 白背景付きロゴ: 背景が濃い、複雑、またはロゴが沈む場合
- 配置候補: 左上, 右上, 右下, 左下
- 配置ルール: 人物の顔、重要な品物、図解ラベル、キャプションを邪魔しない上部または下部の余白に小さく配置する。
- 理由: Google画像検索、Pinterest、無断転載先で画像が単体流通したときのブランド帰属表示。

### 3. 記事内図解_slide

- ファイル名: `reduce-things-inline-options.png`
- WordPress画像タイトル: 捨てるか残すかだけでなく、売る・譲る・保留を加えた5つの選択肢
- ALT: 捨てるか残すかだけでなく、売る・譲る・保留を加えた5つの選択肢
- 最終サイズ: 1200 x 675
- 生成時の比率: 16:9
- 制作方法: 画像生成素材 + ブランド帰属ロゴ合成
- 設置位置: 本文中のCMSブリーフ位置
- キャプション候補: 捨てる以外の選択肢を持つと、判断が楽になります

#### 制作意図

- 目的: 捨てるか残すかの二択ではなく、「売る」「譲る」「保留」という選択肢があることを伝える
- 読者に伝えたい感情: 「全部捨てなくてもいいんだ」という安心感
- 入れたい要素: 中央の品物から、「残す」「売る」「譲る」「保留」「処分」の5つの矢印が伸びる構造的な図解。
- 避けたい表現: 画像内への大量のテキスト、複雑すぎるフローチャート

#### 生成プロンプト / レイアウト仕様

Create a simple 16:9 Japanese slide-style infographic.

Style:
simple slide-style flat 2D vector infographic, icon-based diagram, clean presentation slide, light cream background, rounded cards, simple arrows, large readable Japanese labels, limited warm colors, minimal icon-like people only if necessary, no photorealism, no realistic lighting, no camera perspective, no detailed room scene

Important:
This must look like a simple slide diagram, not a photo, not a realistic scene, not watercolor, not manga, not a full room illustration. Use minimal icon-like people only if needed. No realistic lighting, no camera perspective, no detailed faces.

Content:
捨てるか残すかの二択ではなく、「売る」「譲る」「保留」という選択肢があることを伝える

Layout:
Clean presentation layout with cards and arrows.

Use only these Japanese labels:
中央の品物から、「残す」「売る」「譲る」「保留」「処分」の5つの矢印が伸びる構造的な図解。

Avoid:
no extra text, no garbled Japanese, no logo, no watermark, no speech bubbles, no money unless explicitly required, no truck unless explicitly required, no sales scene, no logo, no watermark, no signage, no speech bubbles, no garbled Japanese, no random extra labels, no font specification. 画像内への大量のテキスト、複雑すぎるフローチャート.
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

### 4. 記事内イメージ

- ファイル名: `reduce-things-inline-three-boxes.png`
- WordPress画像タイトル: まずは財布など小さな場所から物を減らす様子
- ALT: まずは財布など小さな場所から物を減らす様子
- 最終サイズ: 1200 x 675
- 生成時の比率: 16:9
- 制作方法: 画像生成素材 + ブランド帰属ロゴ合成
- 設置位置: 本文中のCMSブリーフ位置
- キャプション候補: まずは15分で終わる小さな場所から始めましょう

#### 制作意図

- 目的: 小さな場所（財布や洗面所）から片付けを始めることで得られる小さな達成感を伝える
- 読者に伝えたい感情: これなら私にもできそう、という気軽さと前向きな気持ち
- 入れたい要素: 財布の中の不要なレシートをゴミ箱に捨てて、スッキリした財布を見て少し笑顔になっている様子。
- 避けたい表現: 部屋全体を大掛かりに掃除している様子

#### 生成プロンプト / レイアウト仕様

Create a warm text-free editorial illustration for the Seiribu article '物を減らすと楽になる理由｜何から始める？無理なく続ける整理のコツ'. Aspect ratio: 16:9. Style: high-quality Japanese editorial illustration, utilizing varied art styles (e.g., soft watercolor, modern flat vector, pastel, clean line art) to avoid visual repetition, soft natural colors, realistic household objects, contemporary Japanese everyday home, clean but lived-in. Main visual: 財布の中の不要なレシートをゴミ箱に捨てて、スッキリした財布を見て少し笑顔になっている様子。. Purpose: 小さな場所（財布や洗面所）から片付けを始めることで得られる小さな達成感を伝える. Tone: 日本の実家らしさ、読者が状況を想像しやすい生活感、明るく清潔、不安を煽らない、買取業者っぽくしすぎない、捨てるより確認する・分けるを見せる. Must avoid: no text, no letters, no numbers, no Japanese characters, no English words, no labels, no logo, no watermark, no signage, no speech bubbles. Also avoid: 部屋全体を大掛かりに掃除している様子.

#### ブランド帰属ロゴ

- ロゴ必須: はい
- ロゴ: `seiribu-editorial/assets/images/brand/seiribu-logo.png`
- 表示モード: auto
- 透過ロゴ: 背景が薄く、ロゴが十分に読める場合
- 白背景付きロゴ: 背景が濃い、複雑、またはロゴが沈む場合
- 配置候補: 左上, 右上, 右下, 左下
- 配置ルール: 人物の顔、重要な品物、図解ラベル、キャプションを邪魔しない上部または下部の余白に小さく配置する。
- 理由: Google画像検索、Pinterest、無断転載先で画像が単体流通したときのブランド帰属表示。

### 5. 記事内イメージ

- ファイル名: `reduce-things-inline-ng-ok.png`
- WordPress画像タイトル: 実家の片付けで親と一緒に荷物を確認する親子
- ALT: 実家の片付けで親と一緒に荷物を確認する親子
- 最終サイズ: 1200 x 675
- 生成時の比率: 16:9
- 制作方法: 画像生成素材 + ブランド帰属ロゴ合成
- 設置位置: 本文中のCMSブリーフ位置
- キャプション候補: 「捨てる」のではなく「確認する」スタンスで進めましょう

#### 制作意図

- 目的: 親の物を勝手に捨てず、「確認箱」を使って親と一緒に平和に話し合いながら整理を進める情景を伝える
- 読者に伝えたい感情: 親との対立を避け、協力して進められるという安心感
- 入れたい要素: 実家の和室で、親（70代）と子（40代）が和やかに段ボール箱（保留箱・確認箱）の中身を確認している温かい編集イラスト。
- 避けたい表現: 親と子が怒って喧嘩している様子、孤独な遺品整理感

#### 生成プロンプト / レイアウト仕様

Create a warm text-free editorial illustration for the Seiribu article '物を減らすと楽になる理由｜何から始める？無理なく続ける整理のコツ'. Aspect ratio: 16:9. Style: high-quality Japanese editorial illustration, utilizing varied art styles (e.g., soft watercolor, modern flat vector, pastel, clean line art) to avoid visual repetition, soft natural colors, realistic household objects, contemporary Japanese everyday home, clean but lived-in. Main visual: 実家の和室で、親（70代）と子（40代）が和やかに段ボール箱（保留箱・確認箱）の中身を確認している温かい編集イラスト。. Purpose: 親の物を勝手に捨てず、「確認箱」を使って親と一緒に平和に話し合いながら整理を進める情景を伝える. Tone: 日本の実家らしさ、読者が状況を想像しやすい生活感、明るく清潔、不安を煽らない、買取業者っぽくしすぎない、捨てるより確認する・分けるを見せる. Must avoid: no text, no letters, no numbers, no Japanese characters, no English words, no labels, no logo, no watermark, no signage, no speech bubbles. Also avoid: 親と子が怒って喧嘩している様子、孤独な遺品整理感.

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

- 記事内のアイキャッチ指定を利用しています。
- 本文画像・図解は4枚構成です。記事内の全CMSブリーフを標準制作対象にします。
- 画像生成AIに文字、日本語ラベル、ロゴ、透かし、看板を描かせない。
- 日本語ラベルがある図解は、画像生成AIに文字を任せずレイアウト生成で作る。
- 図解は抽象的な線や図形だけにせず、サンプルのような人物・品物・実家の場面を含むイラスト図解ベースで作る。
- アイキャッチのロゴとタイトルはCanvaで人間が最終合成する。
- ロゴ必須対象: アイキャッチ完成版, Canva仕上げ画像, 本文画像, 本文図解。
- 本文画像・本文図解のロゴ: 本文画像・本文図解はブランド帰属表示としてロゴ必須。背景が薄い場合は透過ロゴ、濃い・複雑な場合は薄い白背景付きロゴを、上部または下部の余白に小さく配置する。
- 暗い遺品整理、ゴミ屋敷、高額査定広告の印象を避ける。
- imagegenの生成候補は `/private/tmp/seiribu-image-work/reduce-things` に置き、採用画像だけ `seiribu-editorial/assets/images/reduce-things` に移す。
- 公開用フォルダに残った候補や旧版は `seiribu-editorial/scripts/clean_image_assets.py --article reduce-things --dry-run` で確認してから退避する。
