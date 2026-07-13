# 画像制作プラン: 実家の片付けが進まない！物を捨てない母親が逆ギレする理由と対処法

## 記事情報

- 記事ファイル: `seiribu-editorial/drafts/untidy-mother.md`
- スラッグ: `untidy-mother`
- メインKW: 実家 片付け 母親 片付けられない (関連: 母親 捨てるの嫌がる 逆ギレ)
- 標準仕上げ: ローカル合成（Pillow）
- Canvaテンプレ: https://canva.link/mqlqak3adj01g1i（任意・手動微調整）
- ロゴ: `seiribu-editorial/assets/images/brand/seiribu-logo.png`
- 完成版ロゴ必須: はい

## 判定サマリー

| No | 用途 | 制作方法 | 最終サイズ | 生成時の比率 | ファイル名 | 設置位置 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | アイキャッチ素材 | 画像生成素材 + 背景透過（ローカル合成で仕上げ） | 1536 x 1024 | 3:2 | `untidy-mother-eyecatch.png` | アイキャッチ合成用素材 |
| 2 | 記事内イメージ | 画像生成素材 | 1200 x 800 | 3:2 | `untidy-mother-inline-psychology.png` | 本文中のCMSブリーフ位置 |
| 3 | 記事内イメージ | 画像生成素材 | 1200 x 800 | 3:2 | `untidy-mother-inline-inline-02.png` | 本文中のCMSブリーフ位置 |

## 制作ブリーフ

### 1. アイキャッチ素材

- ファイル名: `untidy-mother-eyecatch.png`
- WordPress画像タイトル: 片付けで逆ギレする母親と困る子供
- ALT: 片付けで逆ギレする母親と困る子供
- 最終サイズ: 1536 x 1024
- 生成時の比率: 3:2
- 制作方法: 画像生成素材 + 背景透過（ローカル合成で仕上げ）
- 設置位置: アイキャッチ合成用素材
- キャプション候補: なし

#### 制作意図

- 目的: 実家の片付けで対立する親子と、第三者の介入による解決の期待感を示すため
- 読者に伝えたい感情: 親子の対立のリアルさと、解決に向けた前向きな気持ち
- 入れたい要素: 高齢の母親、悩む子供世代、段ボールや散らかった小物
- 避けたい表現: 画像内へのテキスト（文字）の生成、背景の描画、深刻すぎる殺伐とした雰囲気

#### 生成プロンプト / レイアウト仕様

Create an eyecatch cutout asset for the Seiribu article '実家の片付けが進まない！物を捨てない母親が逆ギレする理由と対処法'. Aspect ratio: 3:2. Style: warm flat editorial illustration cutout, high-quality 2D vector art, single coherent subject, clean silhouette, easy to remove background. Transparent background if possible; if transparency is not available, use a single flat light background that is easy to remove. Do not include a room, wall, floor, cast shadow, title area, logo area, or decorative frame. Main subject: 高齢の母親、悩む子供世代、段ボールや散らかった小物. Purpose: 実家の片付けで対立する親子と、第三者の介入による解決の期待感を示すため. Tone: 日本の実家らしさ、読者が状況を想像しやすい生活感、明るく清潔、不安を煽らない、買取業者っぽくしすぎない、捨てるより確認する・分けるを見せる. Must avoid: no text, no letters, no numbers, no Japanese characters, no English words, no labels, no logo, no watermark, no signage, no speech bubbles. Also avoid: 画像内へのテキスト（文字）の生成、背景の描画、深刻すぎる殺伐とした雰囲気. Do not reuse the composition, character placement, object placement, or background concept from any existing Seiribu article image.

#### ローカル合成

- 合成スクリプト: `seiribu-editorial/scripts/compose_eyecatch.py`
- タイトル: （※画像内には生成せず合成時に追加）
- サブタイトル: （※同上）
- 出力サイズ: 1200 x 630
- 出力ファイル: `untidy-mother-eyecatch-branded.png`
- ロゴ: `seiribu-editorial/assets/images/brand/seiribu-logo.png`
- ロゴ必須: はい
- ロゴ位置: 左上
- ロゴ配置ルール: 生成AI素材にはロゴを描かせない。標準ではPillowのローカル合成で、完成版にはセイリ部ロゴを必ず小さなブランド署名として配置する。
- Canvaの扱い: 任意の手動微調整。Canva API連携を本番前提にしない。

#### Canva任意微調整

- 状態: optional_manual
- テンプレートURL: https://canva.link/mqlqak3adj01g1i
- タイトル: （※画像内には生成せず合成時に追加）
- サブタイトル: （※同上）
- ロゴ: `seiribu-editorial/assets/images/brand/seiribu-logo.png`
- ロゴ必須: はい
- ロゴ位置: 左上
- ロゴ配置ルール: 生成AI素材にはロゴを描かせない。標準ではPillowのローカル合成で、完成版にはセイリ部ロゴを必ず小さなブランド署名として配置する。
- 見出しフォント: UDモトヤアポロ 太字
- サブタイトルフォント: Noto Sans JP Regular

### 2. 記事内イメージ

- ファイル名: `untidy-mother-inline-psychology.png`
- WordPress画像タイトル: 片付けられずに悩む高齢の母親
- ALT: 片付けられずに悩む高齢の母親
- 最終サイズ: 1200 x 800
- 生成時の比率: 3:2
- 制作方法: 画像生成素材
- 設置位置: 本文中のCMSブリーフ位置
- キャプション候補: 逆ギレの裏には、母親なりの葛藤と不安が隠れています。

#### 制作意図

- 目的: 母親が片付けられない心理的背景を視覚的に伝えるため
- 読者に伝えたい感情: 母親も好きで散らかしているわけではなく、葛藤や不安を抱えているという共感
- 入れたい要素: 物であふれた部屋の中で、捨てる決心がつかず困ったような、あるいは少し寂しそうな表情をしている高齢の母親のイラスト
- 避けたい表現: 画像内へのテキスト（文字）の生成、極端なゴミ屋敷のような不衛生な描写

#### 生成プロンプト / レイアウト仕様

Create a warm text-free editorial illustration for the Seiribu article '実家の片付けが進まない！物を捨てない母親が逆ギレする理由と対処法'. Aspect ratio: 3:2. Style: warm flat editorial illustration, high-quality 2D vector art, soft shapes, minimal or no outlines, gentle natural colors, contemporary Japanese everyday home, clean but lived-in. Main visual: 物であふれた部屋の中で、捨てる決心がつかず困ったような、あるいは少し寂しそうな表情をしている高齢の母親のイラスト. Purpose: 母親が片付けられない心理的背景を視覚的に伝えるため. Tone: 日本の実家らしさ、読者が状況を想像しやすい生活感、明るく清潔、不安を煽らない、買取業者っぽくしすぎない、捨てるより確認する・分けるを見せる. Must avoid: no text, no letters, no numbers, no Japanese characters, no English words, no labels, no logo, no watermark, no signage, no speech bubbles. Also avoid: 画像内へのテキスト（文字）の生成、極端なゴミ屋敷のような不衛生な描写.

### 3. 記事内イメージ

- ファイル名: `untidy-mother-inline-inline-02.png`
- WordPress画像タイトル: 査定員の丁寧な説明に納得する母親
- ALT: 査定員の丁寧な説明に納得する母親
- 最終サイズ: 1200 x 800
- 生成時の比率: 3:2
- 制作方法: 画像生成素材
- 設置位置: 本文中のCMSブリーフ位置
- キャプション候補: 家族の言葉には反発しても、プロの言葉ならすんなり受け入れられることも多いです。

#### 制作意図

- 目的: 第三者（査定員）が介入することで、母親が笑顔で納得して品物を手放している様子を伝えるため
- 読者に伝えたい感情: プロに任せることで、争わず平和的に解決できるという安心感
- 入れたい要素: 査定員（スーツや清潔な制服姿）が和やかに品物を査定し、母親も嬉しそうに頷いている、安心感のあるイラスト
- 避けたい表現: 画像内へのテキスト（文字）の生成、母親が嫌がっている様子

#### 生成プロンプト / レイアウト仕様

Create a warm text-free editorial illustration for the Seiribu article '実家の片付けが進まない！物を捨てない母親が逆ギレする理由と対処法'. Aspect ratio: 3:2. Style: warm flat editorial illustration, high-quality 2D vector art, soft shapes, minimal or no outlines, gentle natural colors, contemporary Japanese everyday home, clean but lived-in. Main visual: 査定員（スーツや清潔な制服姿）が和やかに品物を査定し、母親も嬉しそうに頷いている、安心感のあるイラスト. Purpose: 第三者（査定員）が介入することで、母親が笑顔で納得して品物を手放している様子を伝えるため. Tone: 日本の実家らしさ、読者が状況を想像しやすい生活感、明るく清潔、不安を煽らない、買取業者っぽくしすぎない、捨てるより確認する・分けるを見せる. Must avoid: no text, no letters, no numbers, no Japanese characters, no English words, no labels, no logo, no watermark, no signage, no speech bubbles. Also avoid: 画像内へのテキスト（文字）の生成、母親が嫌がっている様子.

## 品質チェック

- ローカル合成で仕上げるためのアイキャッチ素材指定を利用しています。
- 本文画像の枚数は適正範囲です。
- 画像生成AIに文字、日本語ラベル、ロゴ、透かし、看板を描かせない。
- 日本語ラベルがある図解は、画像生成AIに文字を任せずレイアウト生成で作る。
- ロゴとタイトルは標準ではローカル合成（Pillow）、必要に応じてSVGやCanvaの手動微調整で配置する。
- アイキャッチ完成版と本文図解完成版では、セイリ部ロゴを必ず小さなブランド署名として配置する。
- 暗い遺品整理、ゴミ屋敷、高額査定広告の印象を避ける。
