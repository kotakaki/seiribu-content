# 画像制作プラン: 実家の片付けが進まない！母親が「片付けられない・逆ギレする」理由と対処法

## 記事情報

- 記事ファイル: `seiribu-editorial/drafts/untidy-mother.md`
- スラッグ: `untidy-mother`
- メインKW: 実家 片付け 母親 片付けられない (関連: 母親 捨てるの嫌がる 逆ギレ)
- 出力モード: standard（記事内のCMS画像指定をすべて展開する標準モード。アイキャッチ素材1件と本文画像・図解4件を基本にする）
- アイキャッチ仕上げ: Canva手動仕上げ
- Canvaテンプレ: https://canva.link/mqlqak3adj01g1i（任意・手動微調整）
- ロゴ: `seiribu-editorial/assets/images/brand/seiribu-logo.png`
- ロゴ必須対象: アイキャッチ完成版, Canva仕上げ画像
- 本文画像のロゴ: 本文画像・本文図解はブランド帰属表示としてロゴ必須。背景が薄い場合は透過ロゴ、濃い・複雑な場合は薄い白背景付きロゴを、上部または下部の余白に小さく配置する。
- 画像生成ツール: imagegen
- 図解レイアウトツール: imagegen illustration base + Pillow / SVG / Canva label and logo overlay
- 生成候補の一時置き場: `/private/tmp/seiribu-image-work/untidy-mother`
- 採用画像の公開用置き場: `seiribu-editorial/assets/images/untidy-mother`
- 画像掃除スクリプト: `seiribu-editorial/scripts/clean_image_assets.py`

## 判定サマリー

| No | 用途 | 制作方法 | 最終サイズ | 生成時の比率 | ファイル名 | 設置位置 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | アイキャッチ素材 | 画像生成素材 + Canva手動仕上げ | 1200 x 675 | 16:9 | `untidy-mother-eyecatch.png` | アイキャッチ合成用素材 |
| 2 | 記事内イメージ | 画像生成素材 + ブランド帰属ロゴ合成 | 1200 x 675 | 16:9 | `untidy-mother-inline-01.png` | 本文中のCMSブリーフ位置 |
| 3 | 記事内イメージ | 画像生成素材 + ブランド帰属ロゴ合成 | 1200 x 675 | 16:9 | `untidy-mother-inline-02.png` | 本文中のCMSブリーフ位置 |
| 4 | 記事内イメージ | 画像生成素材 + ブランド帰属ロゴ合成 | 1200 x 675 | 16:9 | `untidy-mother-inline-male-memory.png` | 本文中のCMSブリーフ位置 |
| 5 | 記事内イメージ | 画像生成素材 + ブランド帰属ロゴ合成 | 1200 x 675 | 16:9 | `untidy-mother-inline-04.png` | 本文中のCMSブリーフ位置 |

## 制作ブリーフ

### 1. アイキャッチ素材

- ファイル名: `untidy-mother-eyecatch.png`
- WordPress画像タイトル: 片付けで逆ギレする母親と困る子供
- ALT: 片付けで逆ギレする母親と困る子供
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

Create an eyecatch cutout asset for the Seiribu article '実家の片付けが進まない！母親が「片付けられない・逆ギレする」理由と対処法'. Aspect ratio: 16:9. Style: warm flat editorial illustration cutout, high-quality 2D vector art, single coherent subject, clean silhouette, easy to remove background. Transparent background if possible; if transparency is not available, use a single flat light background that is easy to remove. Do not include a room, wall, floor, cast shadow, title area, logo area, or decorative frame. Main subject: 記事内容に合う人物と物. Purpose: . Tone: 日本の実家らしさ、読者が状況を想像しやすい生活感、明るく清潔、不安を煽らない、買取業者っぽくしすぎない、捨てるより確認する・分けるを見せる. Must avoid: no text, no letters, no numbers, no Japanese characters, no English words, no labels, no logo, no watermark, no signage, no speech bubbles. Also avoid: ゴミ屋敷のような汚さ、暗い遺品整理の雰囲気、札束や高額査定の強調、不用品回収業者だけを推す広告感、既存記事と同じ構図や素材の使い回し、ミニマリスト風の真っ白な部屋、ロゴが見出し・人物の顔・重要な品物を邪魔する配置、抽象的な線、丸、四角、矢印だけで構成された低品質な図解、無料素材風の薄いアイコン図解. Do not reuse the composition, character placement, object placement, or background concept from any existing Seiribu article image.

#### アイキャッチCanva仕上げ

- 仕上げ方法: Canva手動仕上げ
- タイトル: 実家の片付けが進まない！母親が「片付けられない・
- サブタイトル: 逆ギレする」理由と対処法
- 出力サイズ: 1200 x 675
- 出力ファイル: `untidy-mother-eyecatch-branded.png`
- ロゴ: `seiribu-editorial/assets/images/brand/seiribu-logo.png`
- ロゴ必須: はい
- ロゴ位置: 左上
- ロゴ配置ルール: 生成AI素材にはロゴを描かせない。アイキャッチ完成版はCanvaで人間が仕上げる。本文画像・本文図解はCodex側でブランド帰属ロゴを必ず合成する。背景が薄い場合は透過ロゴ、濃い・複雑な場合は薄い白背景付きロゴを使い、人物の顔、重要な品物、図解ラベルを邪魔しない余白に配置する。
- Canvaの扱い: アイキャッチ完成版はCanvaで人間がタイトル、サブタイトル、ロゴ、Canva専用フォントを手動合成する。

#### Canva仕上げ

- 状態: optional_manual
- テンプレートURL: https://canva.link/mqlqak3adj01g1i
- タイトル: 実家の片付けが進まない！母親が「片付けられない・
- サブタイトル: 逆ギレする」理由と対処法
- ロゴ: `seiribu-editorial/assets/images/brand/seiribu-logo.png`
- ロゴ必須: はい
- ロゴ位置: 左上
- ロゴ配置ルール: 生成AI素材にはロゴを描かせない。アイキャッチ完成版はCanvaで人間が仕上げる。本文画像・本文図解はCodex側でブランド帰属ロゴを必ず合成する。背景が薄い場合は透過ロゴ、濃い・複雑な場合は薄い白背景付きロゴを使い、人物の顔、重要な品物、図解ラベルを邪魔しない余白に配置する。
- 見出しフォント: UDモトヤアポロ 太字
- サブタイトルフォント: Noto Sans JP Regular

### 2. 記事内イメージ

- ファイル名: `untidy-mother-inline-01.png`
- WordPress画像タイトル: 片付けられずに悩む高齢の母親
- ALT: 片付けられずに悩む高齢の母親
- 最終サイズ: 1200 x 675
- 生成時の比率: 16:9
- 制作方法: 画像生成素材 + ブランド帰属ロゴ合成
- 設置位置: 本文中のCMSブリーフ位置
- キャプション候補: 逆ギレの裏には、母親なりの葛藤と不安が隠れています。

#### 制作意図

- 目的: 未指定
- 読者に伝えたい感情: 未指定
- 入れたい要素: 未指定
- 避けたい表現: 未指定

#### 生成プロンプト / レイアウト仕様

Create a warm text-free editorial illustration for the Seiribu article '実家の片付けが進まない！母親が「片付けられない・逆ギレする」理由と対処法'. Aspect ratio: 16:9. Style: warm watercolor-like editorial illustration, high-quality Japanese picture-book style, soft natural colors, realistic household objects, contemporary Japanese everyday home, clean but lived-in. Main visual: 記事内容に合う人物と物. Purpose: . Tone: 日本の実家らしさ、読者が状況を想像しやすい生活感、明るく清潔、不安を煽らない、買取業者っぽくしすぎない、捨てるより確認する・分けるを見せる. Must avoid: no text, no letters, no numbers, no Japanese characters, no English words, no labels, no logo, no watermark, no signage, no speech bubbles. Also avoid: ゴミ屋敷のような汚さ、暗い遺品整理の雰囲気、札束や高額査定の強調、不用品回収業者だけを推す広告感、既存記事と同じ構図や素材の使い回し、ミニマリスト風の真っ白な部屋、ロゴが見出し・人物の顔・重要な品物を邪魔する配置、抽象的な線、丸、四角、矢印だけで構成された低品質な図解、無料素材風の薄いアイコン図解.

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

- ファイル名: `untidy-mother-inline-02.png`
- WordPress画像タイトル: 娘が勝手にゴミ袋に物を入れようとして、母親が怒って止めている様子
- ALT: 娘が勝手にゴミ袋に物を入れようとして、母親が怒って止めている様子
- 最終サイズ: 1200 x 675
- 生成時の比率: 16:9
- 制作方法: 画像生成素材 + ブランド帰属ロゴ合成
- 設置位置: 本文中のCMSブリーフ位置
- キャプション候補: 良かれと思った行動が、かえって母親の心を閉ざしてしまうことも。

#### 制作意図

- 目的: 未指定
- 読者に伝えたい感情: 未指定
- 入れたい要素: 未指定
- 避けたい表現: 未指定

#### 生成プロンプト / レイアウト仕様

Create a warm text-free editorial illustration for the Seiribu article '実家の片付けが進まない！母親が「片付けられない・逆ギレする」理由と対処法'. Aspect ratio: 16:9. Style: warm watercolor-like editorial illustration, high-quality Japanese picture-book style, soft natural colors, realistic household objects, contemporary Japanese everyday home, clean but lived-in. Main visual: 記事内容に合う人物と物. Purpose: . Tone: 日本の実家らしさ、読者が状況を想像しやすい生活感、明るく清潔、不安を煽らない、買取業者っぽくしすぎない、捨てるより確認する・分けるを見せる. Must avoid: no text, no letters, no numbers, no Japanese characters, no English words, no labels, no logo, no watermark, no signage, no speech bubbles. Also avoid: ゴミ屋敷のような汚さ、暗い遺品整理の雰囲気、札束や高額査定の強調、不用品回収業者だけを推す広告感、既存記事と同じ構図や素材の使い回し、ミニマリスト風の真っ白な部屋、ロゴが見出し・人物の顔・重要な品物を邪魔する配置、抽象的な線、丸、四角、矢印だけで構成された低品質な図解、無料素材風の薄いアイコン図解.

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

- ファイル名: `untidy-mother-inline-male-memory.png`
- WordPress画像タイトル: 娘が母親に寄り添い、アルバムを見ながら優しく片付けの提案をしている様子
- ALT: 娘が母親に寄り添い、アルバムを見ながら優しく片付けの提案をしている様子
- 最終サイズ: 1200 x 675
- 生成時の比率: 16:9
- 制作方法: 画像生成素材 + ブランド帰属ロゴ合成
- 設置位置: 本文中のCMSブリーフ位置
- キャプション候補: 無理に捨てるのではなく、安全と思い出を大切にするアプローチが成功の鍵です。

#### 制作意図

- 目的: 未指定
- 読者に伝えたい感情: 未指定
- 入れたい要素: 未指定
- 避けたい表現: 未指定

#### 生成プロンプト / レイアウト仕様

Create a warm text-free editorial illustration for the Seiribu article '実家の片付けが進まない！母親が「片付けられない・逆ギレする」理由と対処法'. Aspect ratio: 16:9. Style: warm watercolor-like editorial illustration, high-quality Japanese picture-book style, soft natural colors, realistic household objects, contemporary Japanese everyday home, clean but lived-in. Main visual: 記事内容に合う人物と物. Purpose: . Tone: 日本の実家らしさ、読者が状況を想像しやすい生活感、明るく清潔、不安を煽らない、買取業者っぽくしすぎない、捨てるより確認する・分けるを見せる. Must avoid: no text, no letters, no numbers, no Japanese characters, no English words, no labels, no logo, no watermark, no signage, no speech bubbles. Also avoid: ゴミ屋敷のような汚さ、暗い遺品整理の雰囲気、札束や高額査定の強調、不用品回収業者だけを推す広告感、既存記事と同じ構図や素材の使い回し、ミニマリスト風の真っ白な部屋、ロゴが見出し・人物の顔・重要な品物を邪魔する配置、抽象的な線、丸、四角、矢印だけで構成された低品質な図解、無料素材風の薄いアイコン図解.

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

- ファイル名: `untidy-mother-inline-04.png`
- WordPress画像タイトル: 査定員の丁寧な説明に納得する母親
- ALT: 査定員の丁寧な説明に納得する母親
- 最終サイズ: 1200 x 675
- 生成時の比率: 16:9
- 制作方法: 画像生成素材 + ブランド帰属ロゴ合成
- 設置位置: 本文中のCMSブリーフ位置
- キャプション候補: 家族の言葉には反発しても、プロの言葉ならすんなり受け入れられることも多いです。

#### 制作意図

- 目的: 未指定
- 読者に伝えたい感情: 未指定
- 入れたい要素: 未指定
- 避けたい表現: 未指定

#### 生成プロンプト / レイアウト仕様

Create a warm text-free editorial illustration for the Seiribu article '実家の片付けが進まない！母親が「片付けられない・逆ギレする」理由と対処法'. Aspect ratio: 16:9. Style: warm watercolor-like editorial illustration, high-quality Japanese picture-book style, soft natural colors, realistic household objects, contemporary Japanese everyday home, clean but lived-in. Main visual: 記事内容に合う人物と物. Purpose: . Tone: 日本の実家らしさ、読者が状況を想像しやすい生活感、明るく清潔、不安を煽らない、買取業者っぽくしすぎない、捨てるより確認する・分けるを見せる. Must avoid: no text, no letters, no numbers, no Japanese characters, no English words, no labels, no logo, no watermark, no signage, no speech bubbles. Also avoid: ゴミ屋敷のような汚さ、暗い遺品整理の雰囲気、札束や高額査定の強調、不用品回収業者だけを推す広告感、既存記事と同じ構図や素材の使い回し、ミニマリスト風の真っ白な部屋、ロゴが見出し・人物の顔・重要な品物を邪魔する配置、抽象的な線、丸、四角、矢印だけで構成された低品質な図解、無料素材風の薄いアイコン図解.

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
- 画像生成AIに文字、日本語ラベル、ロゴ、透かし、看板を描かせない。
- 日本語ラベルがある図解は、画像生成AIに文字を任せずレイアウト生成で作る。
- 図解は抽象的な線や図形だけにせず、サンプルのような人物・品物・実家の場面を含むイラスト図解ベースで作る。
- アイキャッチのロゴとタイトルはCanvaで人間が最終合成する。
- ロゴ必須対象: アイキャッチ完成版, Canva仕上げ画像。
- 本文画像・本文図解のロゴ: 本文画像・本文図解はブランド帰属表示としてロゴ必須。背景が薄い場合は透過ロゴ、濃い・複雑な場合は薄い白背景付きロゴを、上部または下部の余白に小さく配置する。
- 暗い遺品整理、ゴミ屋敷、高額査定広告の印象を避ける。
- imagegenの生成候補は `/private/tmp/seiribu-image-work/untidy-mother` に置き、採用画像だけ `seiribu-editorial/assets/images/untidy-mother` に移す。
- 公開用フォルダに残った候補や旧版は `seiribu-editorial/scripts/clean_image_assets.py --article untidy-mother --dry-run` で確認してから退避する。
