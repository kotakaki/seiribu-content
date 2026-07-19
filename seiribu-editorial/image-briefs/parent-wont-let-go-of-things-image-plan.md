# 画像制作プラン: 親が物を捨てさせてくれないときの話し方｜実家整理で揉めない進め方

## 記事情報

- 記事ファイル: `seiribu-editorial/drafts/parent-wont-let-go-of-things.md`
- スラッグ: `parent-wont-let-go-of-things`
- メインKW: 親が物を捨てさせてくれない
- 出力モード: standard（記事内のCMS画像指定をすべて展開する標準モード。アイキャッチ素材1件と本文画像・図解4件を基本にする）
- アイキャッチ仕上げ: Canva手動仕上げ
- Canvaテンプレ: https://canva.link/mqlqak3adj01g1i（任意・手動微調整）
- ロゴ: `seiribu-editorial/assets/images/brand/seiribu-logo.png`
- ロゴ必須対象: アイキャッチ完成版, Canva仕上げ画像
- 本文画像のロゴ: 本文画像・本文図解はブランド帰属表示としてロゴ必須。背景が薄い場合は透過ロゴ、濃い・複雑な場合は薄い白背景付きロゴを、上部または下部の余白に小さく配置する。
- 画像生成ツール: imagegen
- 図解レイアウトツール: imagegen illustration base + Pillow / SVG / Canva label and logo overlay
- 生成候補の一時置き場: `/private/tmp/seiribu-image-work/parent-wont-let-go-of-things`
- 採用画像の公開用置き場: `seiribu-editorial/assets/images/parent-wont-let-go-of-things`
- 画像掃除スクリプト: `seiribu-editorial/scripts/clean_image_assets.py`

## 判定サマリー

| No | 用途 | 制作方法 | 最終サイズ | 生成時の比率 | ファイル名 | 設置位置 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | アイキャッチ素材 | 画像生成素材 + Canva手動仕上げ | 1200 x 675 | 16:9 | `parent-wont-let-go-of-things-eyecatch-cutout.png` | アイキャッチ合成用素材 |
| 2 | 記事内イメージ | 画像生成素材 + ブランド帰属ロゴ合成 | 1200 x 675 | 16:9 | `parent-wont-let-go-of-things-inline-02.png` | 本文中のCMSブリーフ位置 |
| 3 | 記事内図解 | 画像生成でサンプルのようなイラスト図解ベースを作り、Pillow、SVG、またはCanvaで短いラベルとロゴを正確に合成する | 1200 x 675 | 16:9 | `parent-wont-let-go-of-things-inline-03.png` | 本文中のCMSブリーフ位置 |
| 4 | 記事内図解 | 画像生成でサンプルのようなイラスト図解ベースを作り、Pillow、SVG、またはCanvaで短いラベルとロゴを正確に合成する | 1200 x 675 | 16:9 | `parent-wont-let-go-of-things-inline-ng-ok.png` | 本文中のCMSブリーフ位置 |

## 制作ブリーフ

### 1. アイキャッチ素材

- ファイル名: `parent-wont-let-go-of-things-eyecatch-cutout.png`
- WordPress画像タイトル: 親が物を捨てさせてくれない悩みを解決する
- ALT: 親が物を捨てさせてくれない悩みを解決する
- 最終サイズ: 1200 x 675
- 生成時の比率: 16:9
- 制作方法: 画像生成素材 + Canva手動仕上げ
- 設置位置: アイキャッチ合成用素材
- キャプション候補: なし（アイキャッチのため）

#### 制作意図

- 目的: 親が物を手放してくれず困っている状況に共感しつつ、解決の希望を持たせる。
- 読者に伝えたい感情: 実家整理の悩みに寄り添い、平和な解決策がここにあるという安心感。
- 入れたい要素: 40〜50代の子どもが、たくさんの荷物に囲まれた実家の部屋で少し困った表情をしつつも、解決のヒント（チェックリストやスマホ）を見つけてホッとしている情景。
- 避けたい表現: 過度に怒っている、または悲壮感のあるネガティブすぎる表現。

#### 生成プロンプト / レイアウト仕様

Create an eyecatch cutout asset for the Seiribu article '親が物を捨てさせてくれないときの話し方｜実家整理で揉めない進め方'. Aspect ratio: 16:9. Style: warm flat editorial illustration cutout, high-quality 2D vector art, single coherent subject, clean silhouette, easy to remove background. Transparent background if possible; if transparency is not available, use a single flat light background that is easy to remove. Do not include a room, wall, floor, cast shadow, title area, logo area, or decorative frame. Main subject: 40〜50代の子どもが、たくさんの荷物に囲まれた実家の部屋で少し困った表情をしつつも、解決のヒント（チェックリストやスマホ）を見つけてホッとしている情景。. Purpose: 親が物を手放してくれず困っている状況に共感しつつ、解決の希望を持たせる。. Tone: 日本の実家らしさ、読者が状況を想像しやすい生活感、明るく清潔、不安を煽らない、買取業者っぽくしすぎない、捨てるより確認する・分けるを見せる. Must avoid: no text, no letters, no numbers, no Japanese characters, no English words, no labels, no logo, no watermark, no signage, no speech bubbles. Also avoid: 過度に怒っている、または悲壮感のあるネガティブすぎる表現。. Do not reuse the composition, character placement, object placement, or background concept from any existing Seiribu article image.

#### アイキャッチCanva仕上げ

- 仕上げ方法: Canva手動仕上げ
- タイトル: 親が物を捨てさせてくれないときの話し方｜実家整理
- サブタイトル: で揉めない進め方
- 出力サイズ: 1200 x 675
- 出力ファイル: `parent-wont-let-go-of-things-eyecatch-branded.png`
- ロゴ: `seiribu-editorial/assets/images/brand/seiribu-logo.png`
- ロゴ必須: はい
- ロゴ位置: 左上
- ロゴ配置ルール: 生成AI素材にはロゴを描かせない。アイキャッチ完成版はCanvaで人間が仕上げる。本文画像・本文図解はCodex側でブランド帰属ロゴを必ず合成する。背景が薄い場合は透過ロゴ、濃い・複雑な場合は薄い白背景付きロゴを使い、人物の顔、重要な品物、図解ラベルを邪魔しない余白に配置する。
- Canvaの扱い: アイキャッチ完成版はCanvaで人間がタイトル、サブタイトル、ロゴ、Canva専用フォントを手動合成する。

#### Canva仕上げ

- 状態: optional_manual
- テンプレートURL: https://canva.link/mqlqak3adj01g1i
- タイトル: 親が物を捨てさせてくれないときの話し方｜実家整理
- サブタイトル: で揉めない進め方
- ロゴ: `seiribu-editorial/assets/images/brand/seiribu-logo.png`
- ロゴ必須: はい
- ロゴ位置: 左上
- ロゴ配置ルール: 生成AI素材にはロゴを描かせない。アイキャッチ完成版はCanvaで人間が仕上げる。本文画像・本文図解はCodex側でブランド帰属ロゴを必ず合成する。背景が薄い場合は透過ロゴ、濃い・複雑な場合は薄い白背景付きロゴを使い、人物の顔、重要な品物、図解ラベルを邪魔しない余白に配置する。
- 見出しフォント: UDモトヤアポロ 太字
- サブタイトルフォント: Noto Sans JP Regular

### 2. 記事内イメージ

- ファイル名: `parent-wont-let-go-of-things-inline-02.png`
- WordPress画像タイトル: 物を捨てようと説得する子どもと意固地になる親
- ALT: 物を捨てようと説得する子どもと意固地になる親
- 最終サイズ: 1200 x 675
- 生成時の比率: 16:9
- 制作方法: 画像生成素材 + ブランド帰属ロゴ合成
- 設置位置: 本文中のCMSブリーフ位置
- キャプション候補: 親を理詰めで説得しようとするほど、相手は心を閉ざしてしまいます。

#### 制作意図

- 目的: 説得しようとすると親が意固地になるという「最大の罠（あるある）」を視覚的に伝える
- 読者に伝えたい感情: 共感（「うちもまさにこの状態だ」という気付き）
- 入れたい要素: ゴミ袋を持って「捨てたら？」と提案している子世代に対して、親が古い品物を両手で抱え込んで頑なに拒否している情景。
- 避けたい表現: 過度に怒っている、または悲壮感のあるネガティブすぎる表現

#### 生成プロンプト / レイアウト仕様

Create a warm text-free editorial illustration for the Seiribu article '親が物を捨てさせてくれないときの話し方｜実家整理で揉めない進め方'. Aspect ratio: 16:9. Style: warm watercolor-like editorial illustration, high-quality Japanese picture-book style, soft natural colors, realistic household objects, contemporary Japanese everyday home, clean but lived-in. Main visual: ゴミ袋を持って「捨てたら？」と提案している子世代に対して、親が古い品物を両手で抱え込んで頑なに拒否している情景。. Purpose: 説得しようとすると親が意固地になるという「最大の罠（あるある）」を視覚的に伝える. Tone: 日本の実家らしさ、読者が状況を想像しやすい生活感、明るく清潔、不安を煽らない、買取業者っぽくしすぎない、捨てるより確認する・分けるを見せる. Must avoid: no text, no letters, no numbers, no Japanese characters, no English words, no labels, no logo, no watermark, no signage, no speech bubbles. Also avoid: 過度に怒っている、または悲壮感のあるネガティブすぎる表現.

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

- ファイル名: `parent-wont-let-go-of-things-inline-03.png`
- WordPress画像タイトル: 親が納得する角が立たない言い換え術
- ALT: 親が納得する角が立たない言い換え術
- 最終サイズ: 1200 x 675
- 生成時の比率: 16:9
- 制作方法: 画像生成でサンプルのようなイラスト図解ベースを作り、Pillow、SVG、またはCanvaで短いラベルとロゴを正確に合成する
- 設置位置: 本文中のCMSブリーフ位置
- キャプション候補: 目的を「捨てる」から「安全」や「価値の確認」にすり替えるだけで、親の態度は大きく軟化します。

#### 制作意図

- 目的: 「捨てる（対立）」ではなく、「安全確保」や「査定（価値の確認）」に目的をすり替える言い換え術を図解する。
- 読者に伝えたい感情: なるほど、そういう言い方なら揉めないという納得感。
- 入れたい要素: 「× 捨てる（対立）」と「○ 安全確保 / 価値の確認（共感）」の対比を、温かいアイコンや人物イラストを用いてわかりやすく表現した図解。
- 避けたい表現: 文字が多すぎる複雑な図、無機質なビジネス風のグラフ

#### 生成プロンプト / レイアウト仕様

Create a text-free illustrated diagram base for a Seiribu article. Aspect ratio: 16:9. Style: warm Japanese picture-book style illustrated diagram, scene-based panels with people, household items, rooms, boxes, kimono, books, cameras or other concrete objects, not abstract line art, not plain geometric shapes. Content to show as warm scene-based panels or a comparison illustration: 「× 捨てる（対立）」と「○ 安全確保 / 価値の確認（共感）」の対比を、温かいアイコンや人物イラストを用いてわかりやすく表現した図解。. Purpose: 「捨てる（対立）」ではなく、「安全確保」や「査定（価値の確認）」に目的をすり替える言い換え術を図解する。. Must avoid: no text, no letters, no numbers, no Japanese characters, no English words, no labels, no logo, no watermark, no signage, no speech bubbles. Also avoid: 文字が多すぎる複雑な図、無機質なビジネス風のグラフ. Do not create abstract line art, a generic flowchart, wireframe boxes, plain circles, arrows-only diagrams, or free-icon-style graphics. Use concrete scenes with people, household items, rooms, boxes, kimono, books, cameras, documents, or other article-specific objects. Do not include readable text, Japanese labels, numbers, logo, watermark, signage, or speech bubbles in the generated image; short Japanese labels and captions will be added later with Pillow, SVG, or Canva. Leave quiet margin space for a small Seiribu brand logo overlay. ロゴ: 本文画像・本文図解はブランド帰属表示としてロゴ必須。背景が薄い場合は透過ロゴ、濃い・複雑な場合は薄い白背景付きロゴを、上部または下部の余白に小さく配置する。

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

- ファイル名: `parent-wont-let-go-of-things-inline-ng-ok.png`
- WordPress画像タイトル: 親の合意を得ながら進める実家の整理ステップ
- ALT: 親の合意を得ながら進める実家の整理ステップ
- 最終サイズ: 1200 x 675
- 生成時の比率: 16:9
- 制作方法: 画像生成でサンプルのようなイラスト図解ベースを作り、Pillow、SVG、またはCanvaで短いラベルとロゴを正確に合成する
- 設置位置: 本文中のCMSブリーフ位置
- キャプション候補: 保留箱や写真確認、第三者による価値確認を活用することで、後々のトラブルを未然に防ぐことができます。

#### 制作意図

- 目的: 勝手に捨てないための「保留箱」「写真確認」「価値確認」という3つのステップをわかりやすく視覚化する。
- 読者に伝えたい感情: 親の意志を尊重しながら進めることの安心感。
- 入れたい要素: 1. 保留箱、2. スマホで写真確認、3. 価値確認の3ステップを並べる。3つ目では、親子が古い品物を前にして、専門家らしき人物に穏やかに相談している。査定士は補助的な存在として小さめに描き、現金や売却の表現は入れない。
- 避けたい表現: 査定士が中央で主役になっている絵、現金、トラック、買取成立といった広告的な業者感。

#### 生成プロンプト / レイアウト仕様

Create a text-free illustrated diagram base for a Seiribu article. Aspect ratio: 16:9. Style: warm Japanese picture-book style illustrated diagram, scene-based panels with people, household items, rooms, boxes, kimono, books, cameras or other concrete objects, not abstract line art, not plain geometric shapes. Content to show as warm scene-based panels or a comparison illustration: 1. 保留箱、2. スマホで写真確認、3. 価値確認の3ステップを並べる。3つ目では、親子が古い品物を前にして、専門家らしき人物に穏やかに相談している。査定士は補助的な存在として小さめに描き、現金や売却の表現は入れない。. Purpose: 勝手に捨てないための「保留箱」「写真確認」「価値確認」という3つのステップをわかりやすく視覚化する。. Must avoid: no text, no letters, no numbers, no Japanese characters, no English words, no labels, no logo, no watermark, no signage, no speech bubbles. Also avoid: 査定士が中央で主役になっている絵、現金、トラック、買取成立といった広告的な業者感。. Do not create abstract line art, a generic flowchart, wireframe boxes, plain circles, arrows-only diagrams, or free-icon-style graphics. Use concrete scenes with people, household items, rooms, boxes, kimono, books, cameras, documents, or other article-specific objects. Do not include readable text, Japanese labels, numbers, logo, watermark, signage, or speech bubbles in the generated image; short Japanese labels and captions will be added later with Pillow, SVG, or Canva. Leave quiet margin space for a small Seiribu brand logo overlay. ロゴ: 本文画像・本文図解はブランド帰属表示としてロゴ必須。背景が薄い場合は透過ロゴ、濃い・複雑な場合は薄い白背景付きロゴを、上部または下部の余白に小さく配置する。

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
- imagegenの生成候補は `/private/tmp/seiribu-image-work/parent-wont-let-go-of-things` に置き、採用画像だけ `seiribu-editorial/assets/images/parent-wont-let-go-of-things` に移す。
- 公開用フォルダに残った候補や旧版は `seiribu-editorial/scripts/clean_image_assets.py --article parent-wont-let-go-of-things --dry-run` で確認してから退避する。
