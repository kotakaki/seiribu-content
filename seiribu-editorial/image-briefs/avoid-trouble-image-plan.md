# 画像制作プラン: 実家の親を守る！訪問買取（押し買い）のトラブル手口とクーリングオフの全知識

## 記事情報

- 記事ファイル: `seiribu-editorial/drafts/avoid-trouble.md`
- スラッグ: `avoid-trouble`
- メインKW: 訪問買取 トラブル
- 標準仕上げ: ローカル合成（Pillow）
- Canvaテンプレ: https://canva.link/mqlqak3adj01g1i（任意・手動微調整）
- ロゴ: `seiribu-editorial/assets/images/brand/seiribu-logo.png`
- 完成版ロゴ必須: はい

## 判定サマリー

| No | 用途 | 制作方法 | 最終サイズ | 生成時の比率 | ファイル名 | 設置位置 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | アイキャッチ素材 | 画像生成素材 + 背景透過（ローカル合成で仕上げ） | 1536 x 1024 | 3:2 | `avoid-trouble-eyecatch.png` | アイキャッチ合成用素材 |
| 2 | 記事内図解 | Pillow、SVG、または任意のCanva手動微調整など、文字とレイアウトを制御できる方法で作る | 1200 x 800 | 3:2 | `avoid-trouble-inline-inline-01.png` | 本文中のCMSブリーフ位置 |
| 3 | 記事内イメージ | 画像生成素材 | 1200 x 800 | 3:2 | `avoid-trouble-inline-inline-02.png` | 本文中のCMSブリーフ位置 |
| 4 | 記事内図解 | Pillow、SVG、または任意のCanva手動微調整など、文字とレイアウトを制御できる方法で作る | 1200 x 800 | 3:2 | `avoid-trouble-inline-inline-03.png` | 本文中のCMSブリーフ位置 |

## 制作ブリーフ

### 1. アイキャッチ素材

- ファイル名: `avoid-trouble-eyecatch.png`
- WordPress画像タイトル: 訪問買取トラブル対策のアイキャッチ
- ALT: 訪問買取トラブル対策のアイキャッチ
- 最終サイズ: 1536 x 1024
- 生成時の比率: 3:2
- 制作方法: 画像生成素材 + 背景透過（ローカル合成で仕上げ）
- 設置位置: アイキャッチ合成用素材
- キャプション候補: なし

#### 制作意図

- 目的: 実家の親を悪質業者から守るという「防衛・安心感」を伝える
- 読者に伝えたい感情: 親が騙されないか心配（不安）→ 対策を知って安心したい
- 入れたい要素: 悪質業者をシャットアウトする盾や、実家のドアをしっかり閉めている情景
- 避けたい表現: 画像内へのテキスト（文字）の生成、背景の描画、過度に恐怖を煽るホラー調、血、ドクロなどの表現

#### 生成プロンプト / レイアウト仕様

Create an eyecatch cutout asset for the Seiribu article '実家の親を守る！訪問買取（押し買い）のトラブル手口とクーリングオフの全知識'. Aspect ratio: 3:2. Style: warm flat editorial illustration cutout, high-quality 2D vector art, single coherent subject, clean silhouette, easy to remove background. Transparent background if possible; if transparency is not available, use a single flat light background that is easy to remove. Do not include a room, wall, floor, cast shadow, title area, logo area, or decorative frame. Main subject: 悪質業者をシャットアウトする盾や、実家のドアをしっかり閉めている情景. Purpose: 実家の親を悪質業者から守るという「防衛・安心感」を伝える. Tone: 日本の実家らしさ、読者が状況を想像しやすい生活感、明るく清潔、不安を煽らない、買取業者っぽくしすぎない、捨てるより確認する・分けるを見せる. Must avoid: no text, no letters, no numbers, no Japanese characters, no English words, no labels, no logo, no watermark, no signage, no speech bubbles. Also avoid: 画像内へのテキスト（文字）の生成、背景の描画、過度に恐怖を煽るホラー調、血、ドクロなどの表現. Do not reuse the composition, character placement, object placement, or background concept from any existing Seiribu article image.

#### ローカル合成

- 合成スクリプト: `seiribu-editorial/scripts/compose_eyecatch.py`
- タイトル: 実家の親を守る！訪問買取トラブル対策
- サブタイトル: 押し買いの手口とクーリングオフ
- 出力サイズ: 1200 x 630
- 出力ファイル: `avoid-trouble-eyecatch-branded.png`
- ロゴ: `seiribu-editorial/assets/images/brand/seiribu-logo.png`
- ロゴ必須: はい
- ロゴ位置: 左上
- ロゴ配置ルール: 生成AI素材にはロゴを描かせない。標準ではPillowのローカル合成で、完成版にはセイリ部ロゴを必ず小さなブランド署名として配置する。
- Canvaの扱い: 任意の手動微調整。Canva API連携を本番前提にしない。

#### Canva任意微調整

- 状態: optional_manual
- テンプレートURL: https://canva.link/mqlqak3adj01g1i
- タイトル: 実家の親を守る！訪問買取トラブル対策
- サブタイトル: 押し買いの手口とクーリングオフ
- ロゴ: `seiribu-editorial/assets/images/brand/seiribu-logo.png`
- ロゴ必須: はい
- ロゴ位置: 左上
- ロゴ配置ルール: 生成AI素材にはロゴを描かせない。標準ではPillowのローカル合成で、完成版にはセイリ部ロゴを必ず小さなブランド署名として配置する。
- 見出しフォント: UDモトヤアポロ 太字
- サブタイトルフォント: Noto Sans JP Regular

### 2. 記事内図解

- ファイル名: `avoid-trouble-inline-inline-01.png`
- WordPress画像タイトル: 押し買いの典型的な3つの手口
- ALT: 押し買いの典型的な3つの手口
- 最終サイズ: 1200 x 800
- 生成時の比率: 3:2
- 制作方法: Pillow、SVG、または任意のCanva手動微調整など、文字とレイアウトを制御できる方法で作る
- 設置位置: 本文中のCMSブリーフ位置
- キャプション候補: なし

#### 制作意図

- 目的: 「押し買い」の典型的な3つの手口を視覚的に理解させる
- 読者に伝えたい感情: なるほど、こういう手口があるのかという理解と警戒心
- 入れたい要素: 不用品と言いながら貴金属を狙う、居座って帰らない、契約書を渡さないという3つのシーンをアイコンやイラストで表現
- 避けたい表現: 画像内へのテキスト（文字）の生成、複雑すぎるフローチャート

#### 生成プロンプト / レイアウト仕様

画像生成AIには渡さない。Canva、Pillow、SVGなど、文字とレイアウトを制御できる方法で記事内図解を制作する。最終サイズ: 1200 x 800。アスペクト比: 3:2。入れる内容: 不用品と言いながら貴金属を狙う、居座って帰らない、契約書を渡さないという3つのシーンをアイコンやイラストで表現。目的: 「押し買い」の典型的な3つの手口を視覚的に理解させる。避ける表現: 画像内へのテキスト（文字）の生成、複雑すぎるフローチャート。日本語ラベル、表、矢印、比較軸は後工程で正確に配置する。ロゴは右下などの余白に小さく配置し、本文ラベルを邪魔しない。

### 3. 記事内イメージ

- ファイル名: `avoid-trouble-inline-inline-02.png`
- WordPress画像タイトル: 訪問買取業者に困惑する高齢者の親
- ALT: 訪問買取業者に困惑する高齢者の親
- 最終サイズ: 1200 x 800
- 生成時の比率: 3:2
- 制作方法: 画像生成素材
- 設置位置: 本文中のCMSブリーフ位置
- キャプション候補: なし

#### 制作意図

- 目的: 親世代の「もったいない精神」と「押しへの弱さ」に共感させる
- 読者に伝えたい感情: うちの親もまさにこれだ…という納得感
- 入れたい要素: 押し入れいっぱいの荷物を前に途方に暮れる高齢者、または業者に強く言われて困惑している高齢者
- 避けたい表現: 画像内へのテキスト（文字）の生成、高齢者を極端に認知症のように描くこと

#### 生成プロンプト / レイアウト仕様

Create a warm text-free editorial illustration for the Seiribu article '実家の親を守る！訪問買取（押し買い）のトラブル手口とクーリングオフの全知識'. Aspect ratio: 3:2. Style: warm flat editorial illustration, high-quality 2D vector art, soft shapes, minimal or no outlines, gentle natural colors, contemporary Japanese everyday home, clean but lived-in. Main visual: 押し入れいっぱいの荷物を前に途方に暮れる高齢者、または業者に強く言われて困惑している高齢者. Purpose: 親世代の「もったいない精神」と「押しへの弱さ」に共感させる. Tone: 日本の実家らしさ、読者が状況を想像しやすい生活感、明るく清潔、不安を煽らない、買取業者っぽくしすぎない、捨てるより確認する・分けるを見せる. Must avoid: no text, no letters, no numbers, no Japanese characters, no English words, no labels, no logo, no watermark, no signage, no speech bubbles. Also avoid: 画像内へのテキスト（文字）の生成、高齢者を極端に認知症のように描くこと.

### 4. 記事内図解

- ファイル名: `avoid-trouble-inline-inline-03.png`
- WordPress画像タイトル: クーリングオフの8日間と対象外品目
- ALT: クーリングオフの8日間と対象外品目
- 最終サイズ: 1200 x 800
- 生成時の比率: 3:2
- 制作方法: Pillow、SVG、または任意のCanva手動微調整など、文字とレイアウトを制御できる方法で作る
- 設置位置: 本文中のCMSブリーフ位置
- キャプション候補: なし

#### 制作意図

- 目的: クーリングオフの条件（8日間・対象外品目）を分かりやすく整理する
- 読者に伝えたい感情: 取り戻せるんだという安心感
- 入れたい要素: カレンダー（8日間を強調）、対象品と対象外品の簡単な対比図
- 避けたい表現: 画像内へのテキスト（文字）の生成、法律の専門書のような硬すぎるデザイン

#### 生成プロンプト / レイアウト仕様

画像生成AIには渡さない。Canva、Pillow、SVGなど、文字とレイアウトを制御できる方法で記事内図解を制作する。最終サイズ: 1200 x 800。アスペクト比: 3:2。入れる内容: カレンダー（8日間を強調）、対象品と対象外品の簡単な対比図。目的: クーリングオフの条件（8日間・対象外品目）を分かりやすく整理する。避ける表現: 画像内へのテキスト（文字）の生成、法律の専門書のような硬すぎるデザイン。日本語ラベル、表、矢印、比較軸は後工程で正確に配置する。ロゴは右下などの余白に小さく配置し、本文ラベルを邪魔しない。

## 品質チェック

- ローカル合成で仕上げるためのアイキャッチ素材指定を利用しています。
- 本文画像の枚数は適正範囲です。
- 画像生成AIに文字、日本語ラベル、ロゴ、透かし、看板を描かせない。
- 日本語ラベルがある図解は、画像生成AIに文字を任せずレイアウト生成で作る。
- ロゴとタイトルは標準ではローカル合成（Pillow）、必要に応じてSVGやCanvaの手動微調整で配置する。
- アイキャッチ完成版と本文図解完成版では、セイリ部ロゴを必ず小さなブランド署名として配置する。
- 暗い遺品整理、ゴミ屋敷、高額査定広告の印象を避ける。
