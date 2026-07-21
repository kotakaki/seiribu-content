# 画像制作プラン: 【実家の片付け】兄弟で押し付け合いに？「自分ばかり」を防ぐ分担術と解決策

## 記事情報

- 記事ファイル: `drafts/siblings-share.md`
- スラッグ: `siblings-share`
- メインKW: 実家 片付け 兄弟 (関連: 兄弟 押し付け合い, 自分ばかり, トラブル)
- 出力モード: standard（記事内のCMS画像指定をすべて展開する標準モード。アイキャッチ素材1件と本文画像・図解4件を基本にする）
- アイキャッチ仕上げ: Canva手動仕上げ
- Canvaテンプレ: https://canva.link/mqlqak3adj01g1i（任意・手動微調整）
- ロゴ: `seiribu-editorial/assets/images/brand/seiribu-logo.png`
- ロゴ必須対象: アイキャッチ完成版, Canva仕上げ画像, 本文画像, 本文図解
- 本文画像のロゴ: 本文画像・本文図解はブランド帰属表示としてロゴ必須。背景が薄い場合は透過ロゴ、濃い・複雑な場合は薄い白背景付きロゴを、上部または下部の余白に小さく配置する。
- 画像生成ツール: imagegen
- 図解レイアウトツール: imagegen complete illustrated infographic with model-native short Japanese text + logo overlay
- 生成候補の一時置き場: `/private/tmp/seiribu-image-work/siblings-share`
- 採用画像の公開用置き場: `seiribu-editorial/assets/images/siblings-share`
- 画像掃除スクリプト: `seiribu-editorial/scripts/clean_image_assets.py`

## 判定サマリー

| No | 用途 | 制作方法 | 最終サイズ | 生成時の比率 | ファイル名 | 設置位置 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | アイキャッチ素材 | 画像生成素材 + Canva手動仕上げ | 1200 x 675 | 16:9 | `siblings-share-eyecatch.png` | アイキャッチ合成用素材 |
| 2 | 記事内イメージ | 画像生成素材 + ブランド帰属ロゴ合成 | 1200 x 675 | 16:9 | `siblings-share-inline-01.png` | 本文中のCMSブリーフ位置 |
| 3 | 記事内図解_scene | 画像生成素材 + ブランド帰属ロゴ合成 | 1200 x 675 | 16:9 | `siblings-share-inline-options.png` | 本文中のCMSブリーフ位置 |
| 4 | 記事内イメージ | 画像生成素材 + ブランド帰属ロゴ合成 | 1200 x 675 | 16:9 | `siblings-share-inline-options-2.png` | 本文中のCMSブリーフ位置 |

## 制作ブリーフ

### 1. アイキャッチ素材

- ファイル名: `siblings-share-eyecatch.png`
- WordPress画像タイトル: 実家の片付けを一人で押し付けられて不満を抱えるイメージ
- ALT: 実家の片付けを一人で押し付けられて不満を抱えるイメージ
- 最終サイズ: 1200 x 675
- 生成時の比率: 16:9
- 制作方法: 画像生成素材 + Canva手動仕上げ
- 設置位置: アイキャッチ合成用素材
- キャプション候補: なし

#### 制作意図

- 目的: 実家の片付けで兄弟間で不満を感じている人に向けた記事であることを一目で伝える
- 読者に伝えたい感情: 未指定
- 入れたい要素: 実家で一人で片付けをしている人物（疲れた表情）
- 避けたい表現: ゴミ屋敷感

#### 生成プロンプト / レイアウト仕様

Create an eyecatch cutout asset for the Seiribu article '【実家の片付け】兄弟で押し付け合いに？「自分ばかり」を防ぐ分担術と解決策'. Aspect ratio: 16:9. Style: warm flat editorial illustration cutout, high-quality 2D vector art, single coherent subject, clean silhouette, easy to remove background. Transparent background if possible; if transparency is not available, use a single flat light background that is easy to remove. Do not include a room, wall, floor, cast shadow, title area, logo area, or decorative frame. Main subject: 実家で一人で片付けをしている人物（疲れた表情）. Purpose: 実家の片付けで兄弟間で不満を感じている人に向けた記事であることを一目で伝える. Tone: 日本の実家らしさ、読者が状況を想像しやすい生活感、明るく清潔、不安を煽らない、買取業者っぽくしすぎない、捨てるより確認する・分けるを見せる. Must avoid: no text, no letters, no numbers, no Japanese characters, no English words, no labels, no logo, no watermark, no signage, no speech bubbles. Also avoid: ゴミ屋敷感. Do not reuse the composition, character placement, object placement, or background concept from any existing Seiribu article image.

#### アイキャッチCanva仕上げ

- 仕上げ方法: Canva手動仕上げ
- タイトル: 【実家の片付け】兄弟で押し付け合いに？
- サブタイトル: 「自分ばかり」を防ぐ分担術と解決策
- 出力サイズ: 1200 x 675
- 出力ファイル: `siblings-share-eyecatch-branded.png`
- ロゴ: `seiribu-editorial/assets/images/brand/seiribu-logo.png`
- ロゴ必須: はい
- ロゴ位置: 左上
- ロゴ配置ルール: 生成AI素材にはロゴを描かせない。アイキャッチ完成版はCanvaで人間が仕上げる。本文画像・本文図解はCodex側でブランド帰属ロゴを必ず合成する。背景が薄い場合は透過ロゴ、濃い・複雑な場合は薄い白背景付きロゴを使い、人物の顔、重要な品物、図解ラベルを邪魔しない余白に配置する。
- Canvaの扱い: アイキャッチ完成版はCanvaで人間がタイトル、サブタイトル、ロゴ、Canva専用フォントを手動合成する。

#### Canva仕上げ

- 状態: optional_manual
- テンプレートURL: https://canva.link/mqlqak3adj01g1i
- タイトル: 【実家の片付け】兄弟で押し付け合いに？
- サブタイトル: 「自分ばかり」を防ぐ分担術と解決策
- ロゴ: `seiribu-editorial/assets/images/brand/seiribu-logo.png`
- ロゴ必須: はい
- ロゴ位置: 左上
- ロゴ配置ルール: 生成AI素材にはロゴを描かせない。アイキャッチ完成版はCanvaで人間が仕上げる。本文画像・本文図解はCodex側でブランド帰属ロゴを必ず合成する。背景が薄い場合は透過ロゴ、濃い・複雑な場合は薄い白背景付きロゴを使い、人物の顔、重要な品物、図解ラベルを邪魔しない余白に配置する。
- 見出しフォント: UDモトヤアポロ 太字
- サブタイトルフォント: Noto Sans JP Regular

### 2. 記事内イメージ

- ファイル名: `siblings-share-inline-01.png`
- WordPress画像タイトル: 一人で実家の片付けを背負い込み疲労している様子
- ALT: 一人で実家の片付けを背負い込み疲労している様子
- 最終サイズ: 1200 x 675
- 生成時の比率: 16:9
- 制作方法: 画像生成素材 + ブランド帰属ロゴ合成
- 設置位置: 本文中のCMSブリーフ位置
- キャプション候補: どうして自分ばかりがこんなに大変な思いをしなければならないのか、と理不尽に感じるのは当然のことです。

#### 制作意図

- 目的: 一人で片付けを背負い込む理不尽さと疲労感を読者に共感させる
- 読者に伝えたい感情: 共感、孤独感からの解放
- 入れたい要素: 実家で段ボールや袋に囲まれ、一人で疲れて座り込んでいる人物
- 避けたい表現: ゴミ屋敷のようなひどい汚れ、暗すぎる絶望感

#### 生成プロンプト / レイアウト仕様

Create a warm text-free editorial illustration for the Seiribu article '【実家の片付け】兄弟で押し付け合いに？「自分ばかり」を防ぐ分担術と解決策'. Aspect ratio: 16:9. Style: warm watercolor-like editorial illustration, high-quality Japanese picture-book style, soft natural colors, realistic household objects, contemporary Japanese everyday home, clean but lived-in. Main visual: 実家で段ボールや袋に囲まれ、一人で疲れて座り込んでいる人物. Purpose: 一人で片付けを背負い込む理不尽さと疲労感を読者に共感させる. Tone: 日本の実家らしさ、読者が状況を想像しやすい生活感、明るく清潔、不安を煽らない、買取業者っぽくしすぎない、捨てるより確認する・分けるを見せる. Must avoid: no text, no letters, no numbers, no Japanese characters, no English words, no labels, no logo, no watermark, no signage, no speech bubbles. Also avoid: ゴミ屋敷のようなひどい汚れ、暗すぎる絶望感.

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

- ファイル名: `siblings-share-inline-options.png`
- WordPress画像タイトル: 片付けの負担を「作業・費用・連絡」に分ける図解
- ALT: 片付けの負担を「作業・費用・連絡」に分ける図解
- 最終サイズ: 1200 x 675
- 生成時の比率: 16:9
- 制作方法: 画像生成素材 + ブランド帰属ロゴ合成
- 設置位置: 本文中のCMSブリーフ位置
- キャプション候補: 負担を3つに分けて考えることで、それぞれができる形で関わりやすくなります。

#### 制作意図

- 目的: 片付けの負担を3つに切り分ける考え方を視覚的に示す
- 読者に伝えたい感情: 未指定
- 入れたい要素: 負担の切り分け（作業、費用、連絡）を示す3つの枠とアイコン
- 避けたい表現: 抽象的すぎる線や丸だけの図形

#### 生成プロンプト / レイアウト仕様

Create an illustrated infographic diagram for a Seiribu article. Aspect ratio: 16:9. Style: warm flat editorial illustration diagram with simple scene panels, soft colors, no photorealism, no realistic lighting, no camera perspective. Content to show as a structured infographic diagram: 負担の切り分け（作業、費用、連絡）を示す3つの枠とアイコン. Layout: Use a clean, solid background (e.g., white or light beige). Structure the information using bordered boxes for each step and connecting arrows. Do NOT create full-bleed comic panels or edge-to-edge full-screen scenes. Keep ample negative space. It is perfectly fine to use spot illustrations of characters and items inside the diagram boxes. Do not create empty placeholder boxes, dotted rectangles, blank logo slots, or unused label cards. Render only the short Japanese labels explicitly implied by the brief, naturally, as part of the generated infographic. Do not specify a font; let the image model choose a clean natural label style. Purpose: 片付けの負担を3つに切り分ける考え方を視覚的に示す. Must avoid: no logo, no watermark, no signage, no speech bubbles, no garbled Japanese, no random extra labels, no font specification. Also avoid: 抽象的すぎる線や丸だけの図形. Do not create full-screen immersive scenes or manga layouts. Do not create abstract line art only. Leave quiet margin space for a small Seiribu brand logo overlay. ロゴ: 本文画像・本文図解はブランド帰属表示としてロゴ必須。背景が薄い場合は透過ロゴ、濃い・複雑な場合は薄い白背景付きロゴを、上部または下部の余白に小さく配置する。

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

- ファイル名: `siblings-share-inline-options-2.png`
- WordPress画像タイトル: プロの業者に任せて実家がスムーズに片付く様子
- ALT: プロの業者に任せて実家がスムーズに片付く様子
- 最終サイズ: 1200 x 675
- 生成時の比率: 16:9
- 制作方法: 画像生成素材 + ブランド帰属ロゴ合成
- 設置位置: 本文中のCMSブリーフ位置
- キャプション候補: 専門業者を入れると、作業量や費用を家族で共有しやすくなります。

#### 制作意図

- 目的: プロの業者が介入することで、家族で話し合いがまとまりやすくなる様子を伝える
- 読者に伝えたい感情: 安心感、解決への希望
- 入れたい要素: 清潔感のある制服を着た業者と、ホッとした表情で見守る家族
- 避けたい表現: 札束の強調、高額請求の恐怖感、乱暴な作業風景

#### 生成プロンプト / レイアウト仕様

Create a warm text-free editorial illustration for the Seiribu article '【実家の片付け】兄弟で押し付け合いに？「自分ばかり」を防ぐ分担術と解決策'. Aspect ratio: 16:9. Style: warm watercolor-like editorial illustration, high-quality Japanese picture-book style, soft natural colors, realistic household objects, contemporary Japanese everyday home, clean but lived-in. Main visual: 清潔感のある制服を着た業者と、ホッとした表情で見守る家族. Purpose: プロの業者が介入することで、家族で話し合いがまとまりやすくなる様子を伝える. Tone: 日本の実家らしさ、読者が状況を想像しやすい生活感、明るく清潔、不安を煽らない、買取業者っぽくしすぎない、捨てるより確認する・分けるを見せる. Must avoid: no text, no letters, no numbers, no Japanese characters, no English words, no labels, no logo, no watermark, no signage, no speech bubbles. Also avoid: 札束の強調、高額請求の恐怖感、乱暴な作業風景.

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
- 本文画像の枚数は適正範囲です。
- 画像生成AIに文字、日本語ラベル、ロゴ、透かし、看板を描かせない。
- 日本語ラベルがある図解は、画像生成AIに文字を任せずレイアウト生成で作る。
- 図解は抽象的な線や図形だけにせず、サンプルのような人物・品物・実家の場面を含むイラスト図解ベースで作る。
- アイキャッチのロゴとタイトルはCanvaで人間が最終合成する。
- ロゴ必須対象: アイキャッチ完成版, Canva仕上げ画像, 本文画像, 本文図解。
- 本文画像・本文図解のロゴ: 本文画像・本文図解はブランド帰属表示としてロゴ必須。背景が薄い場合は透過ロゴ、濃い・複雑な場合は薄い白背景付きロゴを、上部または下部の余白に小さく配置する。
- 暗い遺品整理、ゴミ屋敷、高額査定広告の印象を避ける。
- imagegenの生成候補は `/private/tmp/seiribu-image-work/siblings-share` に置き、採用画像だけ `seiribu-editorial/assets/images/siblings-share` に移す。
- 公開用フォルダに残った候補や旧版は `seiribu-editorial/scripts/clean_image_assets.py --article siblings-share --dry-run` で確認してから退避する。
