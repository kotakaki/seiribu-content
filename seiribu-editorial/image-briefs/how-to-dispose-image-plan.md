# 画像制作プラン: 実家の不用品を安く処分する方法｜粗大ごみ・持ち込み・回収業者の使い分け

## 記事情報

- 記事ファイル: `seiribu-editorial/drafts/how-to-dispose.md`
- スラッグ: `how-to-dispose`
- メインKW: 実家 不用品 処分 安く
- 出力モード: standard（記事内のCMS画像指定をすべて展開する標準モード。アイキャッチ素材1件と本文画像・図解4件を基本にする）
- アイキャッチ仕上げ: Canva手動仕上げ
- Canvaテンプレ: https://canva.link/mqlqak3adj01g1i（任意・手動微調整）
- ロゴ: `seiribu-editorial/assets/images/brand/seiribu-logo.png`
- ロゴ必須対象: アイキャッチ完成版, Canva仕上げ画像
- 本文画像のロゴ: 本文画像・本文図解はブランド帰属表示としてロゴ必須。背景が薄い場合は透過ロゴ、濃い・複雑な場合は薄い白背景付きロゴを、上部または下部の余白に小さく配置する。
- 画像生成ツール: imagegen
- 図解レイアウトツール: imagegen illustration base + Pillow / SVG / Canva label and logo overlay
- 生成候補の一時置き場: `/private/tmp/seiribu-image-work/how-to-dispose`
- 採用画像の公開用置き場: `seiribu-editorial/assets/images/how-to-dispose`
- 画像掃除スクリプト: `seiribu-editorial/scripts/clean_image_assets.py`

## 判定サマリー

| No | 用途 | 制作方法 | 最終サイズ | 生成時の比率 | ファイル名 | 設置位置 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | アイキャッチ素材 | 画像生成素材 + Canva手動仕上げ | 1200 x 675 | 16:9 | `how-to-dispose-eyecatch-material.png` | アイキャッチ合成用素材 |
| 2 | 記事内図解 | 画像生成でサンプルのようなイラスト図解ベースを作り、Pillow、SVG、またはCanvaで短いラベルとロゴを正確に合成する | 1200 x 675 | 16:9 | `how-to-dispose-inline-options.png` | H2「実家の不用品を安く処分するための3つの基本手順」の直下 |
| 3 | 記事内図解 | 画像生成でサンプルのようなイラスト図解ベースを作り、Pillow、SVG、またはCanvaで短いラベルとロゴを正確に合成する | 1200 x 675 | 16:9 | `how-to-dispose-inline-options-2.png` | H2「不用品を手放す4つの方法（費用と手間の比較）」の直下（比較表の上） |
| 4 | 記事内イメージ | 画像生成素材 + ブランド帰属ロゴ合成 | 1200 x 675 | 16:9 | `how-to-dispose-inline-psychology.png` | H2「「自力」と「業者」の境界線は？どこからプロに任せるべきか」の直下 |

## 制作ブリーフ

### 1. アイキャッチ素材

- ファイル名: `how-to-dispose-eyecatch-material.png`
- WordPress画像タイトル: 実家の不用品を安く処分する方法を検討している様子
- ALT: 実家の不用品を安く処分する方法を検討している様子
- 最終サイズ: 1200 x 675
- 生成時の比率: 16:9
- 制作方法: 画像生成素材 + Canva手動仕上げ
- 設置位置: アイキャッチ合成用素材
- キャプション候補: なし

#### 制作意図

- 目的: 読者の「大型家具や大量のゴミをどうやって捨てればいいか途方に暮れている」というリアルな悩みに深く共感し、解決策への期待を持たせる
- 読者に伝えたい感情: 自力では動かせない粗大ごみや使い物にならない大量のガラクタを前に、費用と手間の壁を感じて途方に暮れているリアルな悩みへの共感
- 入れたい要素: 子世代（30〜40代）、古いタンス、壊れた家電や大量のガラクタ（※背景は描かず小物として配置）
- 避けたい表現: 画像内へのテキスト（文字）の生成、背景の描画、お札が舞うような過度な「安さ」の強調、特殊清掃レベルの極端な汚部屋

#### 生成プロンプト / レイアウト仕様

Create an eyecatch cutout asset for the Seiribu article '実家の不用品を安く処分する方法｜粗大ごみ・持ち込み・回収業者の使い分け'. Aspect ratio: 16:9. Style: warm flat editorial illustration cutout, high-quality 2D vector art, single coherent subject, clean silhouette, easy to remove background. Transparent background if possible; if transparency is not available, use a single flat light background that is easy to remove. Do not include a room, wall, floor, cast shadow, title area, logo area, or decorative frame. Main subject: 子世代（30〜40代）、古いタンス、壊れた家電や大量のガラクタ（※背景は描かず小物として配置）. Purpose: 読者の「大型家具や大量のゴミをどうやって捨てればいいか途方に暮れている」というリアルな悩みに深く共感し、解決策への期待を持たせる. Tone: 日本の実家らしさ、読者が状況を想像しやすい生活感、明るく清潔、不安を煽らない、買取業者っぽくしすぎない、捨てるより確認する・分けるを見せる. Must avoid: no text, no letters, no numbers, no Japanese characters, no English words, no labels, no logo, no watermark, no signage, no speech bubbles. Also avoid: 画像内へのテキスト（文字）の生成、背景の描画、お札が舞うような過度な「安さ」の強調、特殊清掃レベルの極端な汚部屋. Do not reuse the composition, character placement, object placement, or background concept from any existing Seiribu article image.

#### アイキャッチCanva仕上げ

- 仕上げ方法: Canva手動仕上げ
- タイトル: 実家の不用品を安く処分する方法（※画像内には生成せず合成時に追加）
- サブタイトル: 粗大ごみ・持ち込み・回収業者の費用比較（※同上）
- 出力サイズ: 1200 x 675
- 出力ファイル: `how-to-dispose-eyecatch-branded.png`
- ロゴ: `seiribu-editorial/assets/images/brand/seiribu-logo.png`
- ロゴ必須: はい
- ロゴ位置: 左上
- ロゴ配置ルール: 生成AI素材にはロゴを描かせない。アイキャッチ完成版はCanvaで人間が仕上げる。本文画像・本文図解はCodex側でブランド帰属ロゴを必ず合成する。背景が薄い場合は透過ロゴ、濃い・複雑な場合は薄い白背景付きロゴを使い、人物の顔、重要な品物、図解ラベルを邪魔しない余白に配置する。
- Canvaの扱い: アイキャッチ完成版はCanvaで人間がタイトル、サブタイトル、ロゴ、Canva専用フォントを手動合成する。

#### Canva仕上げ

- 状態: optional_manual
- テンプレートURL: https://canva.link/mqlqak3adj01g1i
- タイトル: 実家の不用品を安く処分する方法（※画像内には生成せず合成時に追加）
- サブタイトル: 粗大ごみ・持ち込み・回収業者の費用比較（※同上）
- ロゴ: `seiribu-editorial/assets/images/brand/seiribu-logo.png`
- ロゴ必須: はい
- ロゴ位置: 左上
- ロゴ配置ルール: 生成AI素材にはロゴを描かせない。アイキャッチ完成版はCanvaで人間が仕上げる。本文画像・本文図解はCodex側でブランド帰属ロゴを必ず合成する。背景が薄い場合は透過ロゴ、濃い・複雑な場合は薄い白背景付きロゴを使い、人物の顔、重要な品物、図解ラベルを邪魔しない余白に配置する。
- 見出しフォント: UDモトヤアポロ 太字
- サブタイトルフォント: Noto Sans JP Regular

### 2. 記事内図解

- ファイル名: `how-to-dispose-inline-options.png`
- WordPress画像タイトル: 実家の不用品処分費用を安く抑える3つの手順
- ALT: 実家の不用品処分費用を安く抑える3つの手順（売る、家庭ごみ、不用品回収）
- 最終サイズ: 1200 x 675
- 生成時の比率: 16:9
- 制作方法: 画像生成でサンプルのようなイラスト図解ベースを作り、Pillow、SVG、またはCanvaで短いラベルとロゴを正確に合成する
- 設置位置: H2「実家の不用品を安く処分するための3つの基本手順」の直下
- キャプション候補: 売る・自力で捨てる手順を挟むことで、業者への依頼費用を最小化できます。

#### 制作意図

- 目的: 費用を最小化する処分手順の「漏斗（ファネル）」構造を視覚的に理解させる
- 読者に伝えたい感情: 未指定
- 入れたい要素: 逆三角形（漏斗）の図、3つのステップ名とアイコン、下に行くほど荷物量が減っていく表現
- 避けたい表現: 「捨てる」を推奨するようなポジティブすぎる表現、ゴミ箱に何でも捨てるイラスト

#### 生成プロンプト / レイアウト仕様

Create a text-free illustrated diagram base for a Seiribu article. Aspect ratio: 16:9. Style: warm Japanese picture-book style illustrated diagram, scene-based panels with people, household items, rooms, boxes, kimono, books, cameras or other concrete objects, not abstract line art, not plain geometric shapes. Content to show as warm scene-based panels or a comparison illustration: 逆三角形（漏斗）の図、3つのステップ名とアイコン、下に行くほど荷物量が減っていく表現. Purpose: 費用を最小化する処分手順の「漏斗（ファネル）」構造を視覚的に理解させる. Must avoid: no text, no letters, no numbers, no Japanese characters, no English words, no labels, no logo, no watermark, no signage, no speech bubbles. Also avoid: 「捨てる」を推奨するようなポジティブすぎる表現、ゴミ箱に何でも捨てるイラスト. Do not create abstract line art, a generic flowchart, wireframe boxes, plain circles, arrows-only diagrams, or free-icon-style graphics. Use concrete scenes with people, household items, rooms, boxes, kimono, books, cameras, documents, or other article-specific objects. Do not include readable text, Japanese labels, numbers, logo, watermark, signage, or speech bubbles in the generated image; short Japanese labels and captions will be added later with Pillow, SVG, or Canva. Leave quiet margin space for a small Seiribu brand logo overlay. ロゴ: 本文画像・本文図解はブランド帰属表示としてロゴ必須。背景が薄い場合は透過ロゴ、濃い・複雑な場合は薄い白背景付きロゴを、上部または下部の余白に小さく配置する。

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

- ファイル名: `how-to-dispose-inline-options-2.png`
- WordPress画像タイトル: 不用品を手放す4つの方法の費用と手間の比較マトリクス
- ALT: 不用品を手放す4つの方法の費用と手間の比較マトリクス
- 最終サイズ: 1200 x 675
- 生成時の比率: 16:9
- 制作方法: 画像生成でサンプルのようなイラスト図解ベースを作り、Pillow、SVG、またはCanvaで短いラベルとロゴを正確に合成する
- 設置位置: H2「不用品を手放す4つの方法（費用と手間の比較）」の直下（比較表の上）
- キャプション候補: それぞれの方法の「費用」と「手間」のバランスを知り、状況に合わせて使い分けましょう。

#### 制作意図

- 目的: 4つの処分方法の特徴を「費用と手間」の2軸で直感的に比較させる
- 読者に伝えたい感情: 未指定
- 入れたい要素: 縦軸（手間がかかる〜手間なし）、横軸（費用が安い〜高い）の2軸マトリクス。4つの方法（持ち込み、粗大ごみ、ジモティー等、回収業者）の配置
- 避けたい表現: 不用品回収業者だけを過剰に目立たせる（アフィリエイト誘導に見える）表現

#### 生成プロンプト / レイアウト仕様

Create a text-free illustrated diagram base for a Seiribu article. Aspect ratio: 16:9. Style: warm Japanese picture-book style illustrated diagram, scene-based panels with people, household items, rooms, boxes, kimono, books, cameras or other concrete objects, not abstract line art, not plain geometric shapes. Content to show as warm scene-based panels or a comparison illustration: 縦軸（手間がかかる〜手間なし）、横軸（費用が安い〜高い）の2軸マトリクス。4つの方法（持ち込み、粗大ごみ、ジモティー等、回収業者）の配置. Purpose: 4つの処分方法の特徴を「費用と手間」の2軸で直感的に比較させる. Must avoid: no text, no letters, no numbers, no Japanese characters, no English words, no labels, no logo, no watermark, no signage, no speech bubbles. Also avoid: 不用品回収業者だけを過剰に目立たせる（アフィリエイト誘導に見える）表現. Do not create abstract line art, a generic flowchart, wireframe boxes, plain circles, arrows-only diagrams, or free-icon-style graphics. Use concrete scenes with people, household items, rooms, boxes, kimono, books, cameras, documents, or other article-specific objects. Do not include readable text, Japanese labels, numbers, logo, watermark, signage, or speech bubbles in the generated image; short Japanese labels and captions will be added later with Pillow, SVG, or Canva. Leave quiet margin space for a small Seiribu brand logo overlay. ロゴ: 本文画像・本文図解はブランド帰属表示としてロゴ必須。背景が薄い場合は透過ロゴ、濃い・複雑な場合は薄い白背景付きロゴを、上部または下部の余白に小さく配置する。

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

- ファイル名: `how-to-dispose-inline-psychology.png`
- WordPress画像タイトル: 自力で大型家具を運び出そうとして限界を感じている様子のイラスト
- ALT: 自力で大型家具を運び出そうとして限界を感じている様子のイラスト
- 最終サイズ: 1200 x 675
- 生成時の比率: 16:9
- 制作方法: 画像生成素材 + ブランド帰属ロゴ合成
- 設置位置: H2「「自力」と「業者」の境界線は？どこからプロに任せるべきか」の直下
- キャプション候補: 無理をして自力で進めると、かえって危険や思わぬ出費を伴うケースがあります。

#### 制作意図

- 目的: 自力処分の限界（体力・時間・手間の壁）を視覚的に伝え、プロに頼むことへの心理的ハードルを下げる
- 読者に伝えたい感情: 「無理して自分で全部やらなくていいんだ」「プロに頼むのも賢い選択だ」という共感と安堵
- 入れたい要素: 未指定
- 避けたい表現: 図表やチェックボックスなどのB2B的な硬い表現、ケガをして血が出ているなどの過激な表現、文字の合成

#### 生成プロンプト / レイアウト仕様

Create a warm text-free editorial illustration for the Seiribu article '実家の不用品を安く処分する方法｜粗大ごみ・持ち込み・回収業者の使い分け'. Aspect ratio: 16:9. Style: warm watercolor-like editorial illustration, high-quality Japanese picture-book style, soft natural colors, realistic household objects, contemporary Japanese everyday home, clean but lived-in. Main visual: 記事内容に合う人物と物. Purpose: 自力処分の限界（体力・時間・手間の壁）を視覚的に伝え、プロに頼むことへの心理的ハードルを下げる. Tone: 日本の実家らしさ、読者が状況を想像しやすい生活感、明るく清潔、不安を煽らない、買取業者っぽくしすぎない、捨てるより確認する・分けるを見せる. Must avoid: no text, no letters, no numbers, no Japanese characters, no English words, no labels, no logo, no watermark, no signage, no speech bubbles. Also avoid: 図表やチェックボックスなどのB2B的な硬い表現、ケガをして血が出ているなどの過激な表現、文字の合成.

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
- imagegenの生成候補は `/private/tmp/seiribu-image-work/how-to-dispose` に置き、採用画像だけ `seiribu-editorial/assets/images/how-to-dispose` に移す。
- 公開用フォルダに残った候補や旧版は `seiribu-editorial/scripts/clean_image_assets.py --article how-to-dispose --dry-run` で確認してから退避する。
