# 画像制作プラン: ミニマリストに向いている性格とは？物を減らせる人・捨てすぎる人の違い

## 記事情報

- 記事ファイル: `seiribu-editorial/drafts/minimalist-personality.md`
- スラッグ: `minimalist-personality`
- メインKW: ミニマリスト 性格
- 出力モード: standard（記事内のCMS画像指定をすべて展開する標準モード。アイキャッチ素材1件と本文画像・図解4件を基本にする）
- アイキャッチ仕上げ: Canva手動仕上げ
- Canvaテンプレ: https://canva.link/mqlqak3adj01g1i（任意・手動微調整）
- ロゴ: `seiribu-editorial/assets/images/brand/seiribu-logo.png`
- ロゴ必須対象: アイキャッチ完成版, Canva仕上げ画像, 本文画像, 本文図解
- 本文画像のロゴ: 本文画像・本文図解はブランド帰属表示としてロゴ必須。背景が薄い場合は透過ロゴ、濃い・複雑な場合は薄い白背景付きロゴを、上部または下部の余白に小さく配置する。
- 画像生成ツール: imagegen
- 図解レイアウトツール: imagegen complete illustrated infographic with model-native short Japanese text + logo overlay
- 生成候補の一時置き場: `/private/tmp/seiribu-image-work/minimalist-personality`
- 採用画像の公開用置き場: `seiribu-editorial/assets/images/minimalist-personality`
- 画像掃除スクリプト: `seiribu-editorial/scripts/clean_image_assets.py`

## 判定サマリー

| No | 用途 | 制作方法 | 最終サイズ | 生成時の比率 | ファイル名 | 設置位置 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | アイキャッチ素材 | 画像生成素材 + Canva手動仕上げ | 1200 x 675 | 16:9 | `minimalist-personality-eyecatch.png` | アイキャッチ合成用素材 |
| 2 | 記事内イメージ | 画像生成素材 + ブランド帰属ロゴ合成 | 1200 x 675 | 16:9 | `minimalist-personality-inline-01.png` | 本文中のCMSブリーフ位置 |
| 3 | 記事内図解_scene | 画像生成素材 + ブランド帰属ロゴ合成 | 1200 x 675 | 16:9 | `minimalist-personality-inline-options.png` | 本文中のCMSブリーフ位置 |
| 4 | 記事内イメージ | 画像生成素材 + ブランド帰属ロゴ合成 | 1200 x 675 | 16:9 | `minimalist-personality-inline-03.png` | 本文中のCMSブリーフ位置 |
| 5 | 記事内イメージ | 画像生成素材 + ブランド帰属ロゴ合成 | 1200 x 675 | 16:9 | `minimalist-personality-inline-three-boxes.png` | 本文中のCMSブリーフ位置 |

## 制作ブリーフ

### 1. アイキャッチ素材

- ファイル名: `minimalist-personality-eyecatch.png`
- WordPress画像タイトル: 物を減らせる人と捨てられない人の性格の違いと整理のコツ
- ALT: 物を減らせる人と捨てられない人の性格の違いと整理のコツ
- 最終サイズ: 1200 x 675
- 生成時の比率: 16:9
- 制作方法: 画像生成素材 + Canva手動仕上げ
- 設置位置: アイキャッチ合成用素材
- キャプション候補: なし

#### 制作意図

- 目的: 記事の顔として、物を減らす考え方と性格の違いを視覚的に伝える
- 読者に伝えたい感情: 極端にならず、自分に合ったペースで整理しようという安心感
- 入れたい要素: 少し悩んでいるが前向きな表情の人物、3つに分けられたダンボール箱
- 避けたい表現: 画像内へのテキスト（文字）の生成、背景の描画、過剰に何もない殺風景な部屋

#### 生成プロンプト / レイアウト仕様

Create an eyecatch cutout asset for the Seiribu article 'ミニマリストに向いている性格とは？物を減らせる人・捨てすぎる人の違い'. Aspect ratio: 16:9. Style: warm flat editorial illustration cutout, high-quality 2D vector art, single coherent subject, clean silhouette, easy to remove background. Transparent background if possible; if transparency is not available, use a single flat light background that is easy to remove. Do not include a room, wall, floor, cast shadow, title area, logo area, or decorative frame. Main subject: 少し悩んでいるが前向きな表情の人物、3つに分けられたダンボール箱. Purpose: 記事の顔として、物を減らす考え方と性格の違いを視覚的に伝える. Tone: 日本の実家らしさ、読者が状況を想像しやすい生活感、明るく清潔、不安を煽らない、買取業者っぽくしすぎない、捨てるより確認する・分けるを見せる. Must avoid: no text, no letters, no numbers, no Japanese characters, no English words, no labels, no logo, no watermark, no signage, no speech bubbles. Also avoid: 画像内へのテキスト（文字）の生成、背景の描画、過剰に何もない殺風景な部屋. Do not reuse the composition, character placement, object placement, or background concept from any existing Seiribu article image.

#### アイキャッチCanva仕上げ

- 仕上げ方法: Canva手動仕上げ
- タイトル: （※画像内には生成せず合成時に追加）
- サブタイトル: （※同上）
- 出力サイズ: 1200 x 675
- 出力ファイル: `minimalist-personality-eyecatch-branded.png`
- ロゴ: `seiribu-editorial/assets/images/brand/seiribu-logo.png`
- ロゴ必須: はい
- ロゴ位置: 左上
- ロゴ配置ルール: 生成AI素材にはロゴを描かせない。アイキャッチ完成版はCanvaで人間が仕上げる。本文画像・本文図解はCodex側でブランド帰属ロゴを必ず合成する。背景が薄い場合は透過ロゴ、濃い・複雑な場合は薄い白背景付きロゴを使い、人物の顔、重要な品物、図解ラベルを邪魔しない余白に配置する。
- Canvaの扱い: アイキャッチ完成版はCanvaで人間がタイトル、サブタイトル、ロゴ、Canva専用フォントを手動合成する。

#### Canva仕上げ

- 状態: optional_manual
- テンプレートURL: https://canva.link/mqlqak3adj01g1i
- タイトル: （※画像内には生成せず合成時に追加）
- サブタイトル: （※同上）
- ロゴ: `seiribu-editorial/assets/images/brand/seiribu-logo.png`
- ロゴ必須: はい
- ロゴ位置: 左上
- ロゴ配置ルール: 生成AI素材にはロゴを描かせない。アイキャッチ完成版はCanvaで人間が仕上げる。本文画像・本文図解はCodex側でブランド帰属ロゴを必ず合成する。背景が薄い場合は透過ロゴ、濃い・複雑な場合は薄い白背景付きロゴを使い、人物の顔、重要な品物、図解ラベルを邪魔しない余白に配置する。
- 見出しフォント: UDモトヤアポロ 太字
- サブタイトルフォント: Noto Sans JP Regular

### 2. 記事内イメージ

- ファイル名: `minimalist-personality-inline-01.png`
- WordPress画像タイトル: 綺麗な部屋に憧れつつも自分には無理だと悩む様子
- ALT: 綺麗な部屋に憧れつつも自分には無理だと悩む様子
- 最終サイズ: 1200 x 675
- 生成時の比率: 16:9
- 制作方法: 画像生成素材 + ブランド帰属ロゴ合成
- 設置位置: 本文中のCMSブリーフ位置
- キャプション候補: なし

#### 制作意図

- 目的: ミニマリストに対する憧れと自分には無理だというギャップを表現する
- 読者に伝えたい感情: 私と同じように悩んでいる人がいるんだという共感
- 入れたい要素: SNSや雑誌の「何もない綺麗な部屋」の写真を見ながら、自分の少し物が多い部屋を見渡してため息をついている人物。
- 避けたい表現: 画像内へのテキスト（文字）の生成、絶望感の強すぎる表現

#### 生成プロンプト / レイアウト仕様

Create a warm text-free editorial illustration for the Seiribu article 'ミニマリストに向いている性格とは？物を減らせる人・捨てすぎる人の違い'. Aspect ratio: 16:9. Style: high-quality Japanese editorial illustration, utilizing varied art styles (e.g., soft watercolor, modern flat vector, pastel, clean line art) to avoid visual repetition, soft natural colors, realistic household objects, contemporary Japanese everyday home, clean but lived-in. Main visual: SNSや雑誌の「何もない綺麗な部屋」の写真を見ながら、自分の少し物が多い部屋を見渡してため息をついている人物。. Purpose: ミニマリストに対する憧れと自分には無理だというギャップを表現する. Tone: 日本の実家らしさ、読者が状況を想像しやすい生活感、明るく清潔、不安を煽らない、買取業者っぽくしすぎない、捨てるより確認する・分けるを見せる. Must avoid: no text, no letters, no numbers, no Japanese characters, no English words, no labels, no logo, no watermark, no signage, no speech bubbles. Also avoid: 画像内へのテキスト（文字）の生成、絶望感の強すぎる表現.

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

- ファイル名: `minimalist-personality-inline-options.png`
- WordPress画像タイトル: 物を減らせる人の判断基準と価値観のフィルター
- ALT: 物を減らせる人の判断基準と価値観のフィルター
- 最終サイズ: 1200 x 675
- 生成時の比率: 16:9
- 制作方法: 画像生成素材 + ブランド帰属ロゴ合成
- 設置位置: 本文中のCMSブリーフ位置
- キャプション候補: なし

#### 制作意図

- 目的: 物を減らせる人の思考回路（判断基準や管理コストへの意識）を視覚的に整理する
- 読者に伝えたい感情: なるほど、ただ捨てるのが好きなわけじゃなく、合理的だから減らせるんだという納得感
- 入れたい要素: 頭の中に「自分軸（価値観）」「管理の手間」「長期的な視点」という3つのフィルターがあり、そこを通った本当に必要な物だけが手元に残る図解表現。
- 避けたい表現: 画像内へのテキスト（文字）の生成

#### 生成プロンプト / レイアウト仕様

Create an illustrated infographic diagram for a Seiribu article. Aspect ratio: 16:9. Style: high-quality editorial illustration diagram with simple scene panels, utilizing varied art styles (e.g., flat vector, watercolor, pastel, modern line art) to avoid visual repetition, soft colors, no photorealism, no realistic lighting, no camera perspective. Content to show as a structured infographic diagram: 頭の中に「自分軸（価値観）」「管理の手間」「長期的な視点」という3つのフィルターがあり、そこを通った本当に必要な物だけが手元に残る図解表現。. Layout: Use a clean, solid background (e.g., white or light beige). Structure the information using bordered boxes for each step and connecting arrows. Do NOT create full-bleed comic panels or edge-to-edge full-screen scenes. Keep ample negative space. It is perfectly fine to use spot illustrations of characters and items inside the diagram boxes. Do not create empty placeholder boxes, dotted rectangles, blank logo slots, or unused label cards. Render only the short Japanese labels explicitly implied by the brief, naturally, as part of the generated infographic. Do not specify a font; let the image model choose a clean natural label style. Purpose: 物を減らせる人の思考回路（判断基準や管理コストへの意識）を視覚的に整理する. Must avoid: no logo, no watermark, no signage, no speech bubbles, no garbled Japanese, no random extra labels, no font specification. Also avoid: 画像内へのテキスト（文字）の生成. Do not create full-screen immersive scenes or manga layouts. Do not create abstract line art only. Leave quiet margin space for a small Seiribu brand logo overlay. ロゴ: 本文画像・本文図解はブランド帰属表示としてロゴ必須。背景が薄い場合は透過ロゴ、濃い・複雑な場合は薄い白背景付きロゴを、上部または下部の余白に小さく配置する。

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

- ファイル名: `minimalist-personality-inline-03.png`
- WordPress画像タイトル: 物を捨てる価値観を家族に押し付けて衝突する様子
- ALT: 物を捨てる価値観を家族に押し付けて衝突する様子
- 最終サイズ: 1200 x 675
- 生成時の比率: 16:9
- 制作方法: 画像生成素材 + ブランド帰属ロゴ合成
- 設置位置: 本文中のCMSブリーフ位置
- キャプション候補: なし

#### 制作意図

- 目的: 自分の価値観を押し付けて家族と衝突する様子を伝える
- 読者に伝えたい感情: こういう押し付けは良くないよね、という共感と反面教師
- 入れたい要素: ゴミ袋を持って「捨てるべき」と主張する人と、自分の大切なものを守ろうとして困惑・反発している家族の対比イラスト。
- 避けたい表現: 画像内へのテキスト（文字）の生成、深刻すぎる暴力的な描写

#### 生成プロンプト / レイアウト仕様

Create a warm text-free editorial illustration for the Seiribu article 'ミニマリストに向いている性格とは？物を減らせる人・捨てすぎる人の違い'. Aspect ratio: 16:9. Style: high-quality Japanese editorial illustration, utilizing varied art styles (e.g., soft watercolor, modern flat vector, pastel, clean line art) to avoid visual repetition, soft natural colors, realistic household objects, contemporary Japanese everyday home, clean but lived-in. Main visual: ゴミ袋を持って「捨てるべき」と主張する人と、自分の大切なものを守ろうとして困惑・反発している家族の対比イラスト。. Purpose: 自分の価値観を押し付けて家族と衝突する様子を伝える. Tone: 日本の実家らしさ、読者が状況を想像しやすい生活感、明るく清潔、不安を煽らない、買取業者っぽくしすぎない、捨てるより確認する・分けるを見せる. Must avoid: no text, no letters, no numbers, no Japanese characters, no English words, no labels, no logo, no watermark, no signage, no speech bubbles. Also avoid: 画像内へのテキスト（文字）の生成、深刻すぎる暴力的な描写.

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

- ファイル名: `minimalist-personality-inline-three-boxes.png`
- WordPress画像タイトル: 売る・残す・処分の3つに仕分ける様子
- ALT: 売る・残す・処分の3つに仕分ける様子
- 最終サイズ: 1200 x 675
- 生成時の比率: 16:9
- 制作方法: 画像生成素材 + ブランド帰属ロゴ合成
- 設置位置: 本文中のCMSブリーフ位置
- キャプション候補: なし

#### 制作意図

- 目的: 売る・残す・処分の3つに分ける具体的な行動をイメージさせる
- 読者に伝えたい感情: これなら自分でもできそうという気軽さと安心感
- 入れたい要素: 目の前の不用品を「売る箱」「残す箱」「処分する箱」の3つの段ボールに仕分けている人物のイラスト。
- 避けたい表現: 画像内へのテキスト（文字）の生成、暗い表情、汚すぎる部屋

#### 生成プロンプト / レイアウト仕様

Create a warm text-free editorial illustration for the Seiribu article 'ミニマリストに向いている性格とは？物を減らせる人・捨てすぎる人の違い'. Aspect ratio: 16:9. Style: high-quality Japanese editorial illustration, utilizing varied art styles (e.g., soft watercolor, modern flat vector, pastel, clean line art) to avoid visual repetition, soft natural colors, realistic household objects, contemporary Japanese everyday home, clean but lived-in. Main visual: 目の前の不用品を「売る箱」「残す箱」「処分する箱」の3つの段ボールに仕分けている人物のイラスト。. Purpose: 売る・残す・処分の3つに分ける具体的な行動をイメージさせる. Tone: 日本の実家らしさ、読者が状況を想像しやすい生活感、明るく清潔、不安を煽らない、買取業者っぽくしすぎない、捨てるより確認する・分けるを見せる. Must avoid: no text, no letters, no numbers, no Japanese characters, no English words, no labels, no logo, no watermark, no signage, no speech bubbles. Also avoid: 画像内へのテキスト（文字）の生成、暗い表情、汚すぎる部屋.

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
- ロゴ必須対象: アイキャッチ完成版, Canva仕上げ画像, 本文画像, 本文図解。
- 本文画像・本文図解のロゴ: 本文画像・本文図解はブランド帰属表示としてロゴ必須。背景が薄い場合は透過ロゴ、濃い・複雑な場合は薄い白背景付きロゴを、上部または下部の余白に小さく配置する。
- 暗い遺品整理、ゴミ屋敷、高額査定広告の印象を避ける。
- imagegenの生成候補は `/private/tmp/seiribu-image-work/minimalist-personality` に置き、採用画像だけ `seiribu-editorial/assets/images/minimalist-personality` に移す。
- 公開用フォルダに残った候補や旧版は `seiribu-editorial/scripts/clean_image_assets.py --article minimalist-personality --dry-run` で確認してから退避する。
