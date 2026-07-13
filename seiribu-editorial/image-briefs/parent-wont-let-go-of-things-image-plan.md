# 画像制作プラン: 実家の片付けで親が捨てさせてくれない！対立を避けてプロを頼る「賢い」対処法

## 記事情報

- 記事ファイル: `seiribu-editorial/drafts/parent-wont-let-go-of-things.md`
- スラッグ: `parent-wont-let-go-of-things`
- メインKW: 親が物を捨てさせてくれない
- 出力モード: light（初回制作をアイキャッチ系1件と本文画像1件までに絞る軽量モード）
- 標準仕上げ: ローカル合成（Pillow）
- Canvaテンプレ: https://canva.link/mqlqak3adj01g1i（任意・手動微調整）
- ロゴ: `seiribu-editorial/assets/images/brand/seiribu-logo.png`
- ロゴ必須対象: アイキャッチ完成版, Canva仕上げ画像
- 本文画像のロゴ: 本文画像・本文図解は標準ではロゴなし。明示依頼やテンプレ上のブランド表記が必要な場合だけ、後工程で小さく配置する。
- 画像生成ツール: imagegen
- 図解レイアウトツール: visualize / Pillow / SVG
- 生成候補の一時置き場: `/private/tmp/seiribu-image-work/parent-wont-let-go-of-things`
- 採用画像の公開用置き場: `seiribu-editorial/assets/images/parent-wont-let-go-of-things`
- 画像掃除スクリプト: `seiribu-editorial/scripts/clean_image_assets.py`

## 判定サマリー

| No | 用途 | 制作方法 | 最終サイズ | 生成時の比率 | ファイル名 | 設置位置 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | アイキャッチ素材 | 画像生成素材 + 背景透過（ローカル合成で仕上げ） | 1200 x 675 | 16:9 | `eyecatch-parent-wont-let-go.png` | アイキャッチ合成用素材 |
| 2 | 記事内イメージ | 画像生成素材 | 1200 x 675 | 16:9 | `parent-wont-let-go-of-things-inline-three-boxes.png` | 本文中のCMSブリーフ位置 |

## 保留した画像

| 用途 | ファイル名 | 保留理由 |
| --- | --- | --- |
| 記事内イメージ | `parent-wont-let-go-of-things-inline-02.png` | lightモードでは本文画像を1件までに絞ります。必要なら --mode standard で出力します。 |
| 記事内図解 | `parent-wont-let-go-of-things-inline-options.png` | lightモードでは本文画像を1件までに絞ります。必要なら --mode standard で出力します。 |

## 制作ブリーフ

### 1. アイキャッチ素材

- ファイル名: `eyecatch-parent-wont-let-go.png`
- WordPress画像タイトル: 実家の片付けで親が捨てさせてくれない時の対処法
- ALT: 実家の片付けで親が捨てさせてくれない時の対処法
- 最終サイズ: 1200 x 675
- 生成時の比率: 16:9
- 制作方法: 画像生成素材 + 背景透過（ローカル合成で仕上げ）
- 設置位置: アイキャッチ合成用素材
- キャプション候補: なし

#### 制作意図

- 目的: 記事の顔として、「プロを頼ることで親との対立を避けられる」という解決策と安心感を伝える。
- 読者に伝えたい感情: 安心感、実務的な解決策があるという希望。
- 入れたい要素: 実家の散らかった部屋に立つ親と子ども、その間に立って笑顔で場を和ませるプロの査定士。
- 避けたい表現: 画像内へのテキスト（文字）の生成、背景の描画（合成しやすいよう白または透過）。

#### 生成プロンプト / レイアウト仕様

Text-free Seiribu eyecatch cutout asset. Aspect ratio: 16:9. Style: warm flat editorial illustration cutout, high-quality 2D vector art, single coherent subject, clean silhouette, easy to remove background. Subject: 実家の散らかった部屋に立つ親と子ども、その間に立って笑顔で場を和ませるプロの査定士。. Purpose: 記事の顔として、「プロを頼ることで親との対立を避けられる」という解決策と安心感を伝える。. Tone: 日本の実家らしさ、読者が状況を想像しやすい生活感、明るく清潔、不安を煽らない、買取業者っぽくしすぎない、捨てるより確認する・分けるを見せる. Transparent background, or single flat light background for easy removal. No room, wall, floor, shadow, title area, logo area, frame. Avoid: no text, no letters, no numbers, no Japanese characters, no English words, no labels, no logo, no watermark, no signage, no speech bubbles; 画像内へのテキスト（文字）の生成、背景の描画（合成しやすいよう白または透過）。. Do not reuse composition, character placement, object placement, or background concept from existing Seiribu article images.

#### ローカル合成

- 合成スクリプト: `seiribu-editorial/scripts/compose_eyecatch.py`
- タイトル: 実家の片付けで親が捨てさせてくれない！対立を避けてプロを頼る賢い対処法
- サブタイトル: 説得を諦めて第三者を味方につける
- 出力サイズ: 1200 x 675
- 出力ファイル: `parent-wont-let-go-of-things-eyecatch-branded.png`
- ロゴ: `seiribu-editorial/assets/images/brand/seiribu-logo.png`
- ロゴ必須: はい
- ロゴ位置: 左上
- ロゴ配置ルール: 生成AI素材にはロゴを描かせない。アイキャッチ完成版とCanva仕上げ画像では、ローカル合成または手動調整でセイリ部ロゴを小さなブランド署名として配置する。本文画像・本文図解は標準ではロゴなしで軽く保つ。
- Canvaの扱い: 任意の手動微調整。Canva API連携を本番前提にしない。

### 2. 記事内イメージ

- ファイル名: `parent-wont-let-go-of-things-inline-three-boxes.png`
- WordPress画像タイトル: 物を捨てたくない親と頭を抱える子ども
- ALT: 物を捨てたくない親と頭を抱える子ども
- 最終サイズ: 1200 x 675
- 生成時の比率: 16:9
- 制作方法: 画像生成素材
- 設置位置: 本文中のCMSブリーフ位置
- キャプション候補: 説得しようとすればするほど、親は防衛本能から意固地になってしまいます。

#### 制作意図

- 目的: 説得しようとすると親が意固地になるという「最大の罠（あるある）」を視覚的に伝えるため。
- 読者に伝えたい感情: 共感（「うちもまさにこの状態だ」という気付き）。
- 入れたい要素: 古い段ボール箱を頑なに守ろうとする高齢の親と、頭を抱えてストレスを感じている子どもの対立シーン。
- 避けたい表現: 画像内へのテキスト（文字）の生成、激怒しすぎている表現。

#### 生成プロンプト / レイアウト仕様

Warm text-free Seiribu editorial illustration for '実家の片付けで親が捨てさせてくれない！対立を避けてプロを頼る「賢い」対処法'. Aspect ratio: 16:9. Style: warm flat editorial illustration, high-quality 2D vector art, soft shapes, minimal or no outlines, gentle natural colors, contemporary Japanese everyday home, clean but lived-in. Main visual: 古い段ボール箱を頑なに守ろうとする高齢の親と、頭を抱えてストレスを感じている子どもの対立シーン。. Purpose: 説得しようとすると親が意固地になるという「最大の罠（あるある）」を視覚的に伝えるため。. Tone: 日本の実家らしさ、読者が状況を想像しやすい生活感、明るく清潔、不安を煽らない、買取業者っぽくしすぎない、捨てるより確認する・分けるを見せる. Avoid: no text, no letters, no numbers, no Japanese characters, no English words, no labels, no logo, no watermark, no signage, no speech bubbles; 画像内へのテキスト（文字）の生成、激怒しすぎている表現。. Do not reuse composition, character placement, object placement, or background concept from existing Seiribu article images.

## 品質チェック

- ローカル合成で仕上げるためのアイキャッチ素材指定を利用しています。
- 本文画像はlightモードの初回範囲です。追加画像は保留分から必要に応じて選びます。
- lightモードのため、初回制作は2件に絞り、2件を保留しました。
- 画像生成AIに文字、日本語ラベル、ロゴ、透かし、看板を描かせない。
- 日本語ラベルがある図解は、画像生成AIに文字を任せずレイアウト生成で作る。
- アイキャッチのロゴとタイトルは標準ではローカル合成（Pillow）、必要に応じてSVGやCanvaの手動微調整で配置する。
- ロゴ必須対象: アイキャッチ完成版, Canva仕上げ画像。
- 本文画像・本文図解のロゴ: 本文画像・本文図解は標準ではロゴなし。明示依頼やテンプレ上のブランド表記が必要な場合だけ、後工程で小さく配置する。
- 暗い遺品整理、ゴミ屋敷、高額査定広告の印象を避ける。
- imagegenの生成候補は `/private/tmp/seiribu-image-work/parent-wont-let-go-of-things` に置き、採用画像だけ `seiribu-editorial/assets/images/parent-wont-let-go-of-things` に移す。
- 公開用フォルダに残った候補や旧版は `seiribu-editorial/scripts/clean_image_assets.py --article parent-wont-let-go-of-things --dry-run` で確認してから退避する。
