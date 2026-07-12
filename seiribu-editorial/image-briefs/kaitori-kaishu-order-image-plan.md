# 画像制作プラン: 実家の不用品は「買取」と「回収」どちらが先？損しない処分の順番

## 記事情報

- 記事ファイル: `seiribu-editorial/drafts/kaitori-kaishu-order.md`
- スラッグ: `kaitori-kaishu-order`
- メインKW: 不用品 買取 回収 どっち, 実家 不用品 買取 回収
- 標準仕上げ: ローカル合成（Pillow）
- Canvaテンプレ: https://canva.link/mqlqak3adj01g1i（任意・手動微調整）
- ロゴ: `seiribu-editorial/assets/images/brand/seiribu-logo.png`
- 完成版ロゴ必須: はい

## 判定サマリー

| No | 用途 | 制作方法 | 最終サイズ | 生成時の比率 | ファイル名 | 設置位置 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | アイキャッチ素材 | 画像生成素材 + 背景透過（ローカル合成で仕上げ） | 1536 x 1024 | 3:2 | `kaitori-kaishu-order-eyecatch.png` | アイキャッチ合成用素材 |
| 2 | 記事内イメージ | 画像生成素材 | 1200 x 800 | 3:2 | `kaitori-kaishu-order-inline-inline-01.png` | 本文中のCMSブリーフ位置 |
| 3 | 記事内イメージ | 画像生成素材 | 1200 x 800 | 3:2 | `kaitori-kaishu-order-inline-male-memory.png` | 本文中のCMSブリーフ位置 |

## 制作ブリーフ

### 1. アイキャッチ素材

- ファイル名: `kaitori-kaishu-order-eyecatch.png`
- WordPress画像タイトル: 買取と回収の正しい順番を示すイラスト
- ALT: 買取と回収の正しい順番を示すイラスト
- 最終サイズ: 1536 x 1024
- 生成時の比率: 3:2
- 制作方法: 画像生成素材 + 背景透過（ローカル合成で仕上げ）
- 設置位置: アイキャッチ合成用素材
- キャプション候補: なし

#### 制作意図

- 目的: 買取と回収の正しい順番を視覚的に伝える
- 読者に伝えたい感情: 順番さえ守ればスムーズに進むという安心感、賢い選択
- 入れたい要素: 古いカメラや着物（買取）、段ボールや古い家具（回収）
- 避けたい表現: 画像内へのテキスト（文字）の生成、背景の描画

#### 生成プロンプト / レイアウト仕様

Create an eyecatch cutout asset for the Seiribu article '実家の不用品は「買取」と「回収」どちらが先？損しない処分の順番'. Aspect ratio: 3:2. Style: warm flat editorial illustration cutout, high-quality 2D vector art, single coherent subject, clean silhouette, easy to remove background. Transparent background if possible; if transparency is not available, use a single flat light background that is easy to remove. Do not include a room, wall, floor, cast shadow, title area, logo area, or decorative frame. Main subject: 古いカメラや着物（買取）、段ボールや古い家具（回収）. Purpose: 買取と回収の正しい順番を視覚的に伝える. Tone: 日本の実家らしさ、読者が状況を想像しやすい生活感、明るく清潔、不安を煽らない、買取業者っぽくしすぎない、捨てるより確認する・分けるを見せる. Must avoid: no text, no letters, no numbers, no Japanese characters, no English words, no labels, no logo, no watermark, no signage, no speech bubbles. Also avoid: 画像内へのテキスト（文字）の生成、背景の描画. Do not reuse the composition, character placement, object placement, or background concept from any existing Seiribu article image.

#### ローカル合成

- 合成スクリプト: `seiribu-editorial/scripts/compose_eyecatch.py`
- タイトル: 実家の不用品 買取と回収どちらが先？
- サブタイトル: 損しない処分の順番
- 出力サイズ: 1200 x 630
- 出力ファイル: `kaitori-kaishu-order-eyecatch-branded.png`
- ロゴ: `seiribu-editorial/assets/images/brand/seiribu-logo.png`
- ロゴ必須: はい
- ロゴ位置: 左上
- ロゴ配置ルール: 生成AI素材にはロゴを描かせない。標準ではPillowのローカル合成で、完成版にはセイリ部ロゴを必ず小さなブランド署名として配置する。
- Canvaの扱い: 任意の手動微調整。Canva API連携を本番前提にしない。

#### Canva任意微調整

- 状態: optional_manual
- テンプレートURL: https://canva.link/mqlqak3adj01g1i
- タイトル: 実家の不用品 買取と回収どちらが先？
- サブタイトル: 損しない処分の順番
- ロゴ: `seiribu-editorial/assets/images/brand/seiribu-logo.png`
- ロゴ必須: はい
- ロゴ位置: 左上
- ロゴ配置ルール: 生成AI素材にはロゴを描かせない。標準ではPillowのローカル合成で、完成版にはセイリ部ロゴを必ず小さなブランド署名として配置する。
- 見出しフォント: UDモトヤアポロ 太字
- サブタイトルフォント: Noto Sans JP Regular

### 2. 記事内イメージ

- ファイル名: `kaitori-kaishu-order-inline-inline-01.png`
- WordPress画像タイトル: 価値あるものをゴミとして処分してしまうリスク
- ALT: 価値あるものをゴミとして処分してしまうリスク
- 最終サイズ: 1200 x 800
- 生成時の比率: 3:2
- 制作方法: 画像生成素材
- 設置位置: 本文中のCMSブリーフ位置
- キャプション候補: 専門知識がないと、価値あるものまでゴミとして扱われてしまうことも。

#### 制作意図

- 目的: 「価値あるものをゴミとして捨ててしまうリスク」を視覚的に伝える
- 読者に伝えたい感情: もったいない、損をしたくないという警戒心
- 入れたい要素: アンティークの時計や年代物のカメラが、ただのガラクタとしてゴミ袋に入れられようとしている様子に、慌てる人のイラスト
- 避けたい表現: 画像内へのテキスト（文字）の生成

#### 生成プロンプト / レイアウト仕様

Create a warm text-free editorial illustration for the Seiribu article '実家の不用品は「買取」と「回収」どちらが先？損しない処分の順番'. Aspect ratio: 3:2. Style: warm flat editorial illustration, high-quality 2D vector art, soft shapes, minimal or no outlines, gentle natural colors, contemporary Japanese everyday home, clean but lived-in. Main visual: アンティークの時計や年代物のカメラが、ただのガラクタとしてゴミ袋に入れられようとしている様子に、慌てる人のイラスト. Purpose: 「価値あるものをゴミとして捨ててしまうリスク」を視覚的に伝える. Tone: 日本の実家らしさ、読者が状況を想像しやすい生活感、明るく清潔、不安を煽らない、買取業者っぽくしすぎない、捨てるより確認する・分けるを見せる. Must avoid: no text, no letters, no numbers, no Japanese characters, no English words, no labels, no logo, no watermark, no signage, no speech bubbles. Also avoid: 画像内へのテキスト（文字）の生成.

### 3. 記事内イメージ

- ファイル名: `kaitori-kaishu-order-inline-male-memory.png`
- WordPress画像タイトル: 親の気持ちに寄り添った実家の買取査定
- ALT: 親の気持ちに寄り添った実家の買取査定
- 最終サイズ: 1200 x 800
- 生成時の比率: 3:2
- 制作方法: 画像生成素材
- 設置位置: 本文中のCMSブリーフ位置
- キャプション候補: 大切な思い出の品も、価値をわかってくれる人になら安心して手放せます。

#### 制作意図

- 目的: 親の気持ちに寄り添った片付けの成功イメージを伝える
- 読者に伝えたい感情: 安心感、ポジティブな気持ち、親孝行
- 入れたい要素: 査定員が古いカメラや着物を丁寧に扱い、それを見て親が安心したように微笑んでいるイラスト
- 避けたい表現: 画像内へのテキスト（文字）の生成

#### 生成プロンプト / レイアウト仕様

Create a warm text-free editorial illustration for the Seiribu article '実家の不用品は「買取」と「回収」どちらが先？損しない処分の順番'. Aspect ratio: 3:2. Style: warm flat editorial illustration, high-quality 2D vector art, soft shapes, minimal or no outlines, gentle natural colors, contemporary Japanese everyday home, clean but lived-in. Main visual: 査定員が古いカメラや着物を丁寧に扱い、それを見て親が安心したように微笑んでいるイラスト. Purpose: 親の気持ちに寄り添った片付けの成功イメージを伝える. Tone: 日本の実家らしさ、読者が状況を想像しやすい生活感、明るく清潔、不安を煽らない、買取業者っぽくしすぎない、捨てるより確認する・分けるを見せる. Must avoid: no text, no letters, no numbers, no Japanese characters, no English words, no labels, no logo, no watermark, no signage, no speech bubbles. Also avoid: 画像内へのテキスト（文字）の生成.

## 品質チェック

- ローカル合成で仕上げるためのアイキャッチ素材指定を利用しています。
- 本文画像の枚数は適正範囲です。
- 画像生成AIに文字、日本語ラベル、ロゴ、透かし、看板を描かせない。
- 日本語ラベルがある図解は、画像生成AIに文字を任せずレイアウト生成で作る。
- ロゴとタイトルは標準ではローカル合成（Pillow）、必要に応じてSVGやCanvaの手動微調整で配置する。
- アイキャッチ完成版と本文図解完成版では、セイリ部ロゴを必ず小さなブランド署名として配置する。
- 暗い遺品整理、ゴミ屋敷、高額査定広告の印象を避ける。
