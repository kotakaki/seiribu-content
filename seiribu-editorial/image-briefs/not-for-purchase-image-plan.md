# 画像制作プラン: 「買取基準に満たない」＝偽物？査定員が言わない本当の理由と3つの対策

## 記事情報

- 記事ファイル: `seiribu-editorial/drafts/not-for-purchase.md`
- スラッグ: `not-for-purchase`
- メインKW: 買取基準に満たない 偽物
- 出力モード: standard（記事内のCMS画像指定をすべて展開する標準モード。アイキャッチ素材1件と本文画像・図解4件を基本にする）
- アイキャッチ仕上げ: Canva手動仕上げ
- Canvaテンプレ: https://canva.link/mqlqak3adj01g1i（任意・手動微調整）
- ロゴ: `seiribu-editorial/assets/images/brand/seiribu-logo.png`
- ロゴ必須対象: アイキャッチ完成版, Canva仕上げ画像
- 本文画像のロゴ: 本文画像・本文図解はブランド帰属表示としてロゴ必須。背景が薄い場合は透過ロゴ、濃い・複雑な場合は薄い白背景付きロゴを、上部または下部の余白に小さく配置する。
- 画像生成ツール: imagegen
- 図解レイアウトツール: imagegen illustration base + Pillow / SVG / Canva label and logo overlay
- 生成候補の一時置き場: `/private/tmp/seiribu-image-work/not-for-purchase`
- 採用画像の公開用置き場: `seiribu-editorial/assets/images/not-for-purchase`
- 画像掃除スクリプト: `seiribu-editorial/scripts/clean_image_assets.py`

## 判定サマリー

| No | 用途 | 制作方法 | 最終サイズ | 生成時の比率 | ファイル名 | 設置位置 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | アイキャッチ素材 | 画像生成素材 + Canva手動仕上げ | 1200 x 675 | 16:9 | `not-for-purchase_eyecatch.png` | アイキャッチ合成用素材 |
| 2 | 記事内図解 | 画像生成でサンプルのようなイラスト図解ベースを作り、Pillow、SVG、またはCanvaで短いラベルとロゴを正確に合成する | 1200 x 675 | 16:9 | `not-for-purchase-inline-reasons.png` | 本文中のCMSブリーフ位置 |
| 3 | 記事内イメージ | 画像生成素材 + ブランド帰属ロゴ合成 | 1200 x 675 | 16:9 | `not-for-purchase-inline-reasons-2.png` | 本文中のCMSブリーフ位置 |
| 4 | 記事内イメージ | 画像生成素材 + ブランド帰属ロゴ合成 | 1200 x 675 | 16:9 | `not-for-purchase-inline-checklist.png` | 本文中のCMSブリーフ位置 |

## 制作ブリーフ

### 1. アイキャッチ素材

- ファイル名: `not-for-purchase_eyecatch.png`
- WordPress画像タイトル: 買取基準に満たないと言われて戸惑う女性のイラスト
- ALT: 買取基準に満たないと言われて戸惑う女性のイラスト
- 最終サイズ: 1200 x 675
- 生成時の比率: 16:9
- 制作方法: 画像生成素材 + Canva手動仕上げ
- 設置位置: アイキャッチ合成用素材
- キャプション候補: なし

#### 制作意図

- 目的: 記事の顔として「買取を断られて戸惑う様子」を視覚化する
- 読者に伝えたい感情: 共感（「あるある、断られてどうしようってなるよね」という寄り添い）
- 入れたい要素: 少し困り顔の女性、ブランド品らしいバッグや時計
- 避けたい表現: 画像内へのテキスト（文字）の生成、背景の描画、過度にショックを受けている（泣いている等）ネガティブすぎる表現

#### 生成プロンプト / レイアウト仕様

Create an eyecatch cutout asset for the Seiribu article '「買取基準に満たない」＝偽物？査定員が言わない本当の理由と3つの対策'. Aspect ratio: 16:9. Style: warm flat editorial illustration cutout, high-quality 2D vector art, single coherent subject, clean silhouette, easy to remove background. Transparent background if possible; if transparency is not available, use a single flat light background that is easy to remove. Do not include a room, wall, floor, cast shadow, title area, logo area, or decorative frame. Main subject: 少し困り顔の女性、ブランド品らしいバッグや時計. Purpose: 記事の顔として「買取を断られて戸惑う様子」を視覚化する. Tone: 日本の実家らしさ、読者が状況を想像しやすい生活感、明るく清潔、不安を煽らない、買取業者っぽくしすぎない、捨てるより確認する・分けるを見せる. Must avoid: no text, no letters, no numbers, no Japanese characters, no English words, no labels, no logo, no watermark, no signage, no speech bubbles. Also avoid: 画像内へのテキスト（文字）の生成、背景の描画、過度にショックを受けている（泣いている等）ネガティブすぎる表現. Do not reuse the composition, character placement, object placement, or background concept from any existing Seiribu article image.

#### アイキャッチCanva仕上げ

- 仕上げ方法: Canva手動仕上げ
- タイトル: （※画像内には生成せず合成時に追加）
- サブタイトル: （※同上）
- 出力サイズ: 1200 x 675
- 出力ファイル: `not-for-purchase-eyecatch-branded.png`
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

### 2. 記事内図解

- ファイル名: `not-for-purchase-inline-reasons.png`
- WordPress画像タイトル: 「買取基準に満たない」という言葉の裏にある2つの理由の図解
- ALT: 「買取基準に満たない」という言葉の裏にある2つの理由の図解
- 最終サイズ: 1200 x 675
- 生成時の比率: 16:9
- 制作方法: 画像生成でサンプルのようなイラスト図解ベースを作り、Pillow、SVG、またはCanvaで短いラベルとロゴを正確に合成する
- 設置位置: 本文中のCMSブリーフ位置
- キャプション候補: 業者がハッキリ理由を言わないのには、業界特有の事情があります

#### 制作意図

- 目的: 「買取基準に満たない」という言葉の裏にある2つの本当の理由を分解して伝える
- 読者に伝えたい感情: 納得感（「なるほど、業界の構造的な事情があるのか」）
- 入れたい要素: 「買取基準に満たない」という吹き出し・バッジを中心に配置し、矢印で2つの理由に分岐する図解。① 法律上、偽物と断言できない ② クレーム回避のための接客用語
- 避けたい表現: 未指定

#### 生成プロンプト / レイアウト仕様

Create a text-free illustrated diagram base for a Seiribu article. Aspect ratio: 16:9. Style: warm Japanese picture-book style illustrated diagram, scene-based panels with people, household items, rooms, boxes, kimono, books, cameras or other concrete objects, not abstract line art, not plain geometric shapes. Content to show as warm scene-based panels or a comparison illustration: 「買取基準に満たない」という吹き出し・バッジを中心に配置し、矢印で2つの理由に分岐する図解。① 法律上、偽物と断言できない ② クレーム回避のための接客用語. Purpose: 「買取基準に満たない」という言葉の裏にある2つの本当の理由を分解して伝える. Must avoid: no text, no letters, no numbers, no Japanese characters, no English words, no labels, no logo, no watermark, no signage, no speech bubbles. Also avoid: ゴミ屋敷のような汚さ、暗い遺品整理の雰囲気、札束や高額査定の強調、不用品回収業者だけを推す広告感、既存記事と同じ構図や素材の使い回し、ミニマリスト風の真っ白な部屋、ロゴが見出し・人物の顔・重要な品物を邪魔する配置、抽象的な線、丸、四角、矢印だけで構成された低品質な図解、無料素材風の薄いアイコン図解. Do not create abstract line art, a generic flowchart, wireframe boxes, plain circles, arrows-only diagrams, or free-icon-style graphics. Use concrete scenes with people, household items, rooms, boxes, kimono, books, cameras, documents, or other article-specific objects. Do not include readable text, Japanese labels, numbers, logo, watermark, signage, or speech bubbles in the generated image; short Japanese labels and captions will be added later with Pillow, SVG, or Canva. Leave quiet margin space for a small Seiribu brand logo overlay. ロゴ: 本文画像・本文図解はブランド帰属表示としてロゴ必須。背景が薄い場合は透過ロゴ、濃い・複雑な場合は薄い白背景付きロゴを、上部または下部の余白に小さく配置する。

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

- ファイル名: `not-for-purchase-inline-reasons-2.png`
- WordPress画像タイトル: 買取を断られる3つのケース
- ALT: 買取を断られる3つのケース（状態不良・在庫過多・対象外）
- 最終サイズ: 1200 x 675
- 生成時の比率: 16:9
- 制作方法: 画像生成素材 + ブランド帰属ロゴ合成
- 設置位置: 本文中のCMSブリーフ位置
- キャプション候補: 本物であっても、お店の事情で買取不可になるケースは多々あります

#### 制作意図

- 目的: 偽物以外で断られる3つのケース（状態不良、在庫過多、対象外）を1枚で直感的に伝える
- 読者に伝えたい感情: 安心感（「なんだ、偽物だからってわけじゃないんだ」）
- 入れたい要素: ボロボロのバッグ（状態不良）、山積みの段ボール（在庫過多）、時計専門店の看板とバッグ（対象外）を並べた3分割のイメージイラスト
- 避けたい表現: 画像内へのテキスト（文字）の生成

#### 生成プロンプト / レイアウト仕様

Create a warm text-free editorial illustration for the Seiribu article '「買取基準に満たない」＝偽物？査定員が言わない本当の理由と3つの対策'. Aspect ratio: 16:9. Style: warm watercolor-like editorial illustration, high-quality Japanese picture-book style, soft natural colors, realistic household objects, contemporary Japanese everyday home, clean but lived-in. Main visual: ボロボロのバッグ（状態不良）、山積みの段ボール（在庫過多）、時計専門店の看板とバッグ（対象外）を並べた3分割のイメージイラスト. Purpose: 偽物以外で断られる3つのケース（状態不良、在庫過多、対象外）を1枚で直感的に伝える. Tone: 日本の実家らしさ、読者が状況を想像しやすい生活感、明るく清潔、不安を煽らない、買取業者っぽくしすぎない、捨てるより確認する・分けるを見せる. Must avoid: no text, no letters, no numbers, no Japanese characters, no English words, no labels, no logo, no watermark, no signage, no speech bubbles. Also avoid: 画像内へのテキスト（文字）の生成.

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

- ファイル名: `not-for-purchase-inline-checklist.png`
- WordPress画像タイトル: 虫眼鏡でブランド品のステッチを確認するイラスト
- ALT: 虫眼鏡でブランド品のステッチを確認するイラスト
- 最終サイズ: 1200 x 675
- 生成時の比率: 16:9
- 制作方法: 画像生成素材 + ブランド帰属ロゴ合成
- 設置位置: 本文中のCMSブリーフ位置
- キャプション候補: 付属品の有無や、細部の縫製をチェックしてみましょう

#### 制作意図

- 目的: セルフチェックの具体的なポイントを視覚的にナビゲートする
- 読者に伝えたい感情: 実用性（「自分でも見分けられそう！」という実感）
- 入れたい要素: 虫眼鏡でブランドバッグの縫い目（ステッチ）やロゴ部分を拡大して見ているイラスト
- 避けたい表現: 画像内へのテキスト（文字）の生成、本物のブランドロゴを精巧に描きすぎること（商標リスク回避）

#### 生成プロンプト / レイアウト仕様

Create a warm text-free editorial illustration for the Seiribu article '「買取基準に満たない」＝偽物？査定員が言わない本当の理由と3つの対策'. Aspect ratio: 16:9. Style: warm watercolor-like editorial illustration, high-quality Japanese picture-book style, soft natural colors, realistic household objects, contemporary Japanese everyday home, clean but lived-in. Main visual: 虫眼鏡でブランドバッグの縫い目（ステッチ）やロゴ部分を拡大して見ているイラスト. Purpose: セルフチェックの具体的なポイントを視覚的にナビゲートする. Tone: 日本の実家らしさ、読者が状況を想像しやすい生活感、明るく清潔、不安を煽らない、買取業者っぽくしすぎない、捨てるより確認する・分けるを見せる. Must avoid: no text, no letters, no numbers, no Japanese characters, no English words, no labels, no logo, no watermark, no signage, no speech bubbles. Also avoid: 画像内へのテキスト（文字）の生成、本物のブランドロゴを精巧に描きすぎること（商標リスク回避）.

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
- imagegenの生成候補は `/private/tmp/seiribu-image-work/not-for-purchase` に置き、採用画像だけ `seiribu-editorial/assets/images/not-for-purchase` に移す。
- 公開用フォルダに残った候補や旧版は `seiribu-editorial/scripts/clean_image_assets.py --article not-for-purchase --dry-run` で確認してから退避する。
