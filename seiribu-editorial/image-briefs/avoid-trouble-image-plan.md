# 画像制作プラン: 実家の親を守る！訪問買取（押し買い）のトラブル手口とクーリングオフの全知識

## 記事情報

- 記事ファイル: `seiribu-editorial/drafts/avoid-trouble.md`
- スラッグ: `avoid-trouble`
- メインKW: 訪問買取 トラブル
- 出力モード: standard（記事内のCMS画像指定をすべて展開する標準モード。アイキャッチ素材1件と本文画像・図解4件を基本にする）
- アイキャッチ仕上げ: Canva手動仕上げ
- Canvaテンプレ: https://canva.link/mqlqak3adj01g1i（任意・手動微調整）
- ロゴ: `seiribu-editorial/assets/images/brand/seiribu-logo.png`
- ロゴ必須対象: アイキャッチ完成版, Canva仕上げ画像
- 本文画像のロゴ: 本文画像・本文図解はブランド帰属表示としてロゴ必須。背景が薄い場合は透過ロゴ、濃い・複雑な場合は薄い白背景付きロゴを、上部または下部の余白に小さく配置する。
- 画像生成ツール: imagegen
- 図解レイアウトツール: imagegen illustration base + Pillow / SVG / Canva label and logo overlay
- 生成候補の一時置き場: `/private/tmp/seiribu-image-work/avoid-trouble`
- 採用画像の公開用置き場: `seiribu-editorial/assets/images/avoid-trouble`
- 画像掃除スクリプト: `seiribu-editorial/scripts/clean_image_assets.py`

## 判定サマリー

| No | 用途 | 制作方法 | 最終サイズ | 生成時の比率 | ファイル名 | 設置位置 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | アイキャッチ素材 | 画像生成素材 + Canva手動仕上げ | 1200 x 675 | 16:9 | `avoid-trouble-eyecatch.png` | アイキャッチ合成用素材 |
| 2 | 記事内図解 | 画像生成でサンプルのようなイラスト図解ベースを作り、Pillow、SVG、またはCanvaで短いラベルとロゴを正確に合成する | 1200 x 675 | 16:9 | `avoid-trouble-inline-01.png` | 本文中のCMSブリーフ位置 |
| 3 | 記事内イメージ | 画像生成素材 + ブランド帰属ロゴ合成 | 1200 x 675 | 16:9 | `avoid-trouble-inline-02.png` | 本文中のCMSブリーフ位置 |
| 4 | 記事内図解 | 画像生成でサンプルのようなイラスト図解ベースを作り、Pillow、SVG、またはCanvaで短いラベルとロゴを正確に合成する | 1200 x 675 | 16:9 | `avoid-trouble-inline-03.png` | 本文中のCMSブリーフ位置 |

## 制作ブリーフ

### 1. アイキャッチ素材

- ファイル名: `avoid-trouble-eyecatch.png`
- WordPress画像タイトル: 訪問買取トラブル対策のアイキャッチ
- ALT: 訪問買取トラブル対策のアイキャッチ
- 最終サイズ: 1200 x 675
- 生成時の比率: 16:9
- 制作方法: 画像生成素材 + Canva手動仕上げ
- 設置位置: アイキャッチ合成用素材
- キャプション候補: なし

#### 制作意図

- 目的: 実家の親を悪質業者から守るという「防衛・安心感」を伝える
- 読者に伝えたい感情: 親が騙されないか心配（不安）→ 対策を知って安心したい
- 入れたい要素: 悪質業者をシャットアウトする盾や、実家のドアをしっかり閉めている情景
- 避けたい表現: 画像内へのテキスト（文字）の生成、背景の描画、過度に恐怖を煽るホラー調、血、ドクロなどの表現

#### 生成プロンプト / レイアウト仕様

Create an eyecatch cutout asset for the Seiribu article '実家の親を守る！訪問買取（押し買い）のトラブル手口とクーリングオフの全知識'. Aspect ratio: 16:9. Style: warm flat editorial illustration cutout, high-quality 2D vector art, single coherent subject, clean silhouette, easy to remove background. Transparent background if possible; if transparency is not available, use a single flat light background that is easy to remove. Do not include a room, wall, floor, cast shadow, title area, logo area, or decorative frame. Main subject: 悪質業者をシャットアウトする盾や、実家のドアをしっかり閉めている情景. Purpose: 実家の親を悪質業者から守るという「防衛・安心感」を伝える. Tone: 日本の実家らしさ、読者が状況を想像しやすい生活感、明るく清潔、不安を煽らない、買取業者っぽくしすぎない、捨てるより確認する・分けるを見せる. Must avoid: no text, no letters, no numbers, no Japanese characters, no English words, no labels, no logo, no watermark, no signage, no speech bubbles. Also avoid: 画像内へのテキスト（文字）の生成、背景の描画、過度に恐怖を煽るホラー調、血、ドクロなどの表現. Do not reuse the composition, character placement, object placement, or background concept from any existing Seiribu article image.

#### アイキャッチCanva仕上げ

- 仕上げ方法: Canva手動仕上げ
- タイトル: 実家の親を守る！訪問買取トラブル対策
- サブタイトル: 押し買いの手口とクーリングオフ
- 出力サイズ: 1200 x 675
- 出力ファイル: `avoid-trouble-eyecatch-branded.png`
- ロゴ: `seiribu-editorial/assets/images/brand/seiribu-logo.png`
- ロゴ必須: はい
- ロゴ位置: 左上
- ロゴ配置ルール: 生成AI素材にはロゴを描かせない。アイキャッチ完成版はCanvaで人間が仕上げる。本文画像・本文図解はCodex側でブランド帰属ロゴを必ず合成する。背景が薄い場合は透過ロゴ、濃い・複雑な場合は薄い白背景付きロゴを使い、人物の顔、重要な品物、図解ラベルを邪魔しない余白に配置する。
- Canvaの扱い: アイキャッチ完成版はCanvaで人間がタイトル、サブタイトル、ロゴ、Canva専用フォントを手動合成する。

#### Canva仕上げ

- 状態: optional_manual
- テンプレートURL: https://canva.link/mqlqak3adj01g1i
- タイトル: 実家の親を守る！訪問買取トラブル対策
- サブタイトル: 押し買いの手口とクーリングオフ
- ロゴ: `seiribu-editorial/assets/images/brand/seiribu-logo.png`
- ロゴ必須: はい
- ロゴ位置: 左上
- ロゴ配置ルール: 生成AI素材にはロゴを描かせない。アイキャッチ完成版はCanvaで人間が仕上げる。本文画像・本文図解はCodex側でブランド帰属ロゴを必ず合成する。背景が薄い場合は透過ロゴ、濃い・複雑な場合は薄い白背景付きロゴを使い、人物の顔、重要な品物、図解ラベルを邪魔しない余白に配置する。
- 見出しフォント: UDモトヤアポロ 太字
- サブタイトルフォント: Noto Sans JP Regular

### 2. 記事内図解

- ファイル名: `avoid-trouble-inline-01.png`
- WordPress画像タイトル: 押し買いの典型的な3つの手口
- ALT: 押し買いの典型的な3つの手口
- 最終サイズ: 1200 x 675
- 生成時の比率: 16:9
- 制作方法: 画像生成でサンプルのようなイラスト図解ベースを作り、Pillow、SVG、またはCanvaで短いラベルとロゴを正確に合成する
- 設置位置: 本文中のCMSブリーフ位置
- キャプション候補: なし

#### 制作意図

- 目的: 「押し買い」の典型的な3つの手口を視覚的に理解させる
- 読者に伝えたい感情: なるほど、こういう手口があるのかという理解と警戒心
- 入れたい要素: 不用品と言いながら貴金属を狙う、居座って帰らない、契約書を渡さないという3つのシーンをアイコンやイラストで表現
- 避けたい表現: 文字の詰め込みすぎ（短いラベルは積極的に使用する）、複雑すぎるフローチャート

#### 生成プロンプト / レイアウト仕様

Create a text-free illustrated diagram base for a Seiribu article. Aspect ratio: 16:9. Style: warm Japanese picture-book style illustrated diagram, scene-based panels with people, household items, rooms, boxes, kimono, books, cameras or other concrete objects, not abstract line art, not plain geometric shapes. Content to show as warm scene-based panels or a comparison illustration: 不用品と言いながら貴金属を狙う、居座って帰らない、契約書を渡さないという3つのシーンをアイコンやイラストで表現. Purpose: 「押し買い」の典型的な3つの手口を視覚的に理解させる. Must avoid: no text, no letters, no numbers, no Japanese characters, no English words, no labels, no logo, no watermark, no signage, no speech bubbles. Also avoid: 文字の詰め込みすぎ（短いラベルは積極的に使用する）、複雑すぎるフローチャート. Do not create abstract line art, a generic flowchart, wireframe boxes, plain circles, arrows-only diagrams, or free-icon-style graphics. Use concrete scenes with people, household items, rooms, boxes, kimono, books, cameras, documents, or other article-specific objects. Do not include readable text, Japanese labels, numbers, logo, watermark, signage, or speech bubbles in the generated image; short Japanese labels and captions will be added later with Pillow, SVG, or Canva. Leave quiet margin space for a small Seiribu brand logo overlay. ロゴ: 本文画像・本文図解はブランド帰属表示としてロゴ必須。背景が薄い場合は透過ロゴ、濃い・複雑な場合は薄い白背景付きロゴを、上部または下部の余白に小さく配置する。

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

- ファイル名: `avoid-trouble-inline-02.png`
- WordPress画像タイトル: 訪問買取業者に困惑する高齢者の親
- ALT: 訪問買取業者に困惑する高齢者の親
- 最終サイズ: 1200 x 675
- 生成時の比率: 16:9
- 制作方法: 画像生成素材 + ブランド帰属ロゴ合成
- 設置位置: 本文中のCMSブリーフ位置
- キャプション候補: なし

#### 制作意図

- 目的: 親世代の「もったいない精神」と「押しへの弱さ」に共感させる
- 読者に伝えたい感情: うちの親もまさにこれだ…という納得感
- 入れたい要素: 押し入れいっぱいの荷物を前に途方に暮れる高齢者、または業者に強く言われて困惑している高齢者
- 避けたい表現: 画像内へのテキスト（文字）の生成、高齢者を極端に認知症のように描くこと

#### 生成プロンプト / レイアウト仕様

Create a warm text-free editorial illustration for the Seiribu article '実家の親を守る！訪問買取（押し買い）のトラブル手口とクーリングオフの全知識'. Aspect ratio: 16:9. Style: warm watercolor-like editorial illustration, high-quality Japanese picture-book style, soft natural colors, realistic household objects, contemporary Japanese everyday home, clean but lived-in. Main visual: 押し入れいっぱいの荷物を前に途方に暮れる高齢者、または業者に強く言われて困惑している高齢者. Purpose: 親世代の「もったいない精神」と「押しへの弱さ」に共感させる. Tone: 日本の実家らしさ、読者が状況を想像しやすい生活感、明るく清潔、不安を煽らない、買取業者っぽくしすぎない、捨てるより確認する・分けるを見せる. Must avoid: no text, no letters, no numbers, no Japanese characters, no English words, no labels, no logo, no watermark, no signage, no speech bubbles. Also avoid: 画像内へのテキスト（文字）の生成、高齢者を極端に認知症のように描くこと.

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

- ファイル名: `avoid-trouble-inline-03.png`
- WordPress画像タイトル: クーリングオフの8日間と対象外品目
- ALT: クーリングオフの8日間と対象外品目
- 最終サイズ: 1200 x 675
- 生成時の比率: 16:9
- 制作方法: 画像生成でサンプルのようなイラスト図解ベースを作り、Pillow、SVG、またはCanvaで短いラベルとロゴを正確に合成する
- 設置位置: 本文中のCMSブリーフ位置
- キャプション候補: なし

#### 制作意図

- 目的: クーリングオフの条件（8日間・対象外品目）を分かりやすく整理する
- 読者に伝えたい感情: 取り戻せるんだという安心感
- 入れたい要素: カレンダー（8日間を強調）、対象品と対象外品の簡単な対比図
- 避けたい表現: 文字の詰め込みすぎ（短いラベルは積極的に使用する）、法律の専門書のような硬すぎるデザイン

#### 生成プロンプト / レイアウト仕様

Create a text-free illustrated diagram base for a Seiribu article. Aspect ratio: 16:9. Style: warm Japanese picture-book style illustrated diagram, scene-based panels with people, household items, rooms, boxes, kimono, books, cameras or other concrete objects, not abstract line art, not plain geometric shapes. Content to show as warm scene-based panels or a comparison illustration: カレンダー（8日間を強調）、対象品と対象外品の簡単な対比図. Purpose: クーリングオフの条件（8日間・対象外品目）を分かりやすく整理する. Must avoid: no text, no letters, no numbers, no Japanese characters, no English words, no labels, no logo, no watermark, no signage, no speech bubbles. Also avoid: 文字の詰め込みすぎ（短いラベルは積極的に使用する）、法律の専門書のような硬すぎるデザイン. Do not create abstract line art, a generic flowchart, wireframe boxes, plain circles, arrows-only diagrams, or free-icon-style graphics. Use concrete scenes with people, household items, rooms, boxes, kimono, books, cameras, documents, or other article-specific objects. Do not include readable text, Japanese labels, numbers, logo, watermark, signage, or speech bubbles in the generated image; short Japanese labels and captions will be added later with Pillow, SVG, or Canva. Leave quiet margin space for a small Seiribu brand logo overlay. ロゴ: 本文画像・本文図解はブランド帰属表示としてロゴ必須。背景が薄い場合は透過ロゴ、濃い・複雑な場合は薄い白背景付きロゴを、上部または下部の余白に小さく配置する。

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
- ロゴ必須対象: アイキャッチ完成版, Canva仕上げ画像。
- 本文画像・本文図解のロゴ: 本文画像・本文図解はブランド帰属表示としてロゴ必須。背景が薄い場合は透過ロゴ、濃い・複雑な場合は薄い白背景付きロゴを、上部または下部の余白に小さく配置する。
- 暗い遺品整理、ゴミ屋敷、高額査定広告の印象を避ける。
- imagegenの生成候補は `/private/tmp/seiribu-image-work/avoid-trouble` に置き、採用画像だけ `seiribu-editorial/assets/images/avoid-trouble` に移す。
- 公開用フォルダに残った候補や旧版は `seiribu-editorial/scripts/clean_image_assets.py --article avoid-trouble --dry-run` で確認してから退避する。
