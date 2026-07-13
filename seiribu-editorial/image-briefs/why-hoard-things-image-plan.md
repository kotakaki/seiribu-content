# 画像制作プラン: 物を捨てられない男性の心理とは？夫や父親に多い5つの理由と家族の接し方

## 記事情報

- 記事ファイル: `seiribu-editorial/drafts/why-hoard-things-rewrite.md`
- スラッグ: `why-hoard-things`
- メインKW: 物を捨てられない 心理 / 物を捨てられない 男 心理
- 出力モード: light（初回制作をアイキャッチ系1件と本文画像1件までに絞る軽量モード）
- 標準仕上げ: ローカル合成（Pillow）
- Canvaテンプレ: https://canva.link/mqlqak3adj01g1i（任意・手動微調整）
- ロゴ: `seiribu-editorial/assets/images/brand/seiribu-logo.png`
- ロゴ必須対象: アイキャッチ完成版, Canva仕上げ画像
- 本文画像のロゴ: 本文画像・本文図解は標準ではロゴなし。明示依頼やテンプレ上のブランド表記が必要な場合だけ、後工程で小さく配置する。
- 画像生成ツール: imagegen
- 図解レイアウトツール: visualize / Pillow / SVG
- 生成候補の一時置き場: `/private/tmp/seiribu-image-work/why-hoard-things`
- 採用画像の公開用置き場: `seiribu-editorial/assets/images/why-hoard-things`
- 画像掃除スクリプト: `seiribu-editorial/scripts/clean_image_assets.py`

## 判定サマリー

| No | 用途 | 制作方法 | 最終サイズ | 生成時の比率 | ファイル名 | 設置位置 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | アイキャッチ素材 | 画像生成素材 + 背景透過（ローカル合成で仕上げ） | 1200 x 675 | 16:9 | `why-hoard-things-eyecatch-material.png` | アイキャッチ合成用素材 |
| 2 | 記事内図解 | Pillow、SVG、または任意のCanva手動微調整など、文字とレイアウトを制御できる方法で作る | 1200 x 675 | 16:9 | `why-hoard-things-inline-psychology.png` | 本文中のCMSブリーフ位置 |

## 保留した画像

| 用途 | ファイル名 | 保留理由 |
| --- | --- | --- |
| 記事内イメージ | `why-hoard-things-inline-male-memory.png` | lightモードでは本文画像を1件までに絞ります。必要なら --mode standard で出力します。 |
| 記事内図解 | `why-hoard-things-inline-spectrum.png` | lightモードでは本文画像を1件までに絞ります。必要なら --mode standard で出力します。 |
| 記事内図解 | `why-hoard-things-inline-ng-ok.png` | lightモードでは本文画像を1件までに絞ります。必要なら --mode standard で出力します。 |

## 制作ブリーフ

### 1. アイキャッチ素材

- ファイル名: `why-hoard-things-eyecatch-material.png`
- WordPress画像タイトル: 物を捨てられない父親と寄り添う家族のイラスト
- ALT: 物を捨てられない父親と寄り添う家族のイラスト
- 最終サイズ: 1200 x 675
- 生成時の比率: 16:9
- 制作方法: 画像生成素材 + 背景透過（ローカル合成で仕上げ）
- 設置位置: アイキャッチ合成用素材
- キャプション候補: なし

#### 制作意図

- 目的: 記事のファーストインプレッション。SNSシェア時のサムネイル
- 読者に伝えたい感情: 「うちの家族もこうだ」という共感＋「理由がわかるかも」という期待
- 入れたい要素: 50〜60代の親、30代の子世代、古い本棚・思い出の品々（※背景は描かず、人物の周りに小物を配置する）
- 避けたい表現: 画像内へのテキスト（文字）の生成、背景の描画、ゴミ屋敷、汚部屋、散らかり放題の極端な描写、暗いトーン、孤独感

#### 生成プロンプト / レイアウト仕様

Text-free Seiribu eyecatch cutout asset. Aspect ratio: 16:9. Style: warm flat editorial illustration cutout, high-quality 2D vector art, single coherent subject, clean silhouette, easy to remove background. Subject: 50〜60代の親、30代の子世代、古い本棚・思い出の品々（※背景は描かず、人物の周りに小物を配置する）. Purpose: 記事のファーストインプレッション。SNSシェア時のサムネイル. Tone: 日本の実家らしさ、読者が状況を想像しやすい生活感、明るく清潔、不安を煽らない、買取業者っぽくしすぎない、捨てるより確認する・分けるを見せる. Transparent background, or single flat light background for easy removal. No room, wall, floor, shadow, title area, logo area, frame. Avoid: no text, no letters, no numbers, no Japanese characters, no English words, no labels, no logo, no watermark, no signage, no speech bubbles; 画像内へのテキスト（文字）の生成、背景の描画、ゴミ屋敷、汚部屋、散らかり放題の極端な描写、暗いトーン、孤独感. Do not reuse composition, character placement, object placement, or background concept from existing Seiribu article images.

#### ローカル合成

- 合成スクリプト: `seiribu-editorial/scripts/compose_eyecatch.py`
- タイトル: 物を捨てられない男性の心理とは？（※画像内には生成せず、後からCanvaで追加する想定）
- サブタイトル: 夫や父親に多い理由と接し方（※同上）
- 出力サイズ: 1200 x 675
- 出力ファイル: `why-hoard-things-eyecatch-branded.png`
- ロゴ: `seiribu-editorial/assets/images/brand/seiribu-logo.png`
- ロゴ必須: はい
- ロゴ位置: 左上
- ロゴ配置ルール: 生成AI素材にはロゴを描かせない。アイキャッチ完成版とCanva仕上げ画像では、ローカル合成または手動調整でセイリ部ロゴを小さなブランド署名として配置する。本文画像・本文図解は標準ではロゴなしで軽く保つ。
- Canvaの扱い: 任意の手動微調整。Canva API連携を本番前提にしない。

### 2. 記事内図解

- ファイル名: `why-hoard-things-inline-psychology.png`
- WordPress画像タイトル: 物を捨てられない男性の心理に隠された5つの理由の概念図
- ALT: 物を捨てられない男性の心理に隠された5つの理由の概念図
- 最終サイズ: 1200 x 675
- 生成時の比率: 16:9
- 制作方法: Pillow、SVG、または任意のCanva手動微調整など、文字とレイアウトを制御できる方法で作る
- 設置位置: 本文中のCMSブリーフ位置
- キャプション候補: 物を捨てられない心理は、1つの原因ではなく複数のメカニズムが絡み合っている

#### 制作意図

- 目的: 5つの心理パターンを俯瞰し、記事の全体像を掴ませる
- 読者に伝えたい感情: 「父親や夫が捨てられないのには、こんなに複雑な理由があるんだ」という納得感
- 入れたい要素: ①損失回避バイアス（「捨てたら損するかも」）②拡張自己（「物は自分の一部」）③アニミズム的思考（「物に魂が宿る」）④判断疲れ（「決める気力がない」）⑤孤独感・不安（「物に囲まれると安心」）を中心の「物を捨てられない」から放射状に配置
- 避けたい表現: 学術論文のような堅苦しいダイアグラム、ネガティブな色使い

#### 生成プロンプト / レイアウト仕様

画像生成AIには渡さない。1200 x 675 / 16:9 の図解として、Pillow・SVG・Canvaなどで制作。内容: ①損失回避バイアス（「捨てたら損するかも」）②拡張自己（「物は自分の一部」）③アニミズム的思考（「物に魂が宿る」）④判断疲れ（「決める気力がない」）⑤孤独感・不安（「物に囲まれると安心」）を中心の「物を捨てられない」から放射状に配置。目的: 5つの心理パターンを俯瞰し、記事の全体像を掴ませる。日本語ラベル、表、矢印、比較軸は後工程で正確に配置する。ロゴ: 本文画像・本文図解は標準ではロゴなし。明示依頼やテンプレ上のブランド表記が必要な場合だけ、後工程で小さく配置する。

## 品質チェック

- ローカル合成で仕上げるためのアイキャッチ素材指定を利用しています。
- 本文画像はlightモードの初回範囲です。追加画像は保留分から必要に応じて選びます。
- lightモードのため、初回制作は2件に絞り、3件を保留しました。
- 画像生成AIに文字、日本語ラベル、ロゴ、透かし、看板を描かせない。
- 日本語ラベルがある図解は、画像生成AIに文字を任せずレイアウト生成で作る。
- アイキャッチのロゴとタイトルは標準ではローカル合成（Pillow）、必要に応じてSVGやCanvaの手動微調整で配置する。
- ロゴ必須対象: アイキャッチ完成版, Canva仕上げ画像。
- 本文画像・本文図解のロゴ: 本文画像・本文図解は標準ではロゴなし。明示依頼やテンプレ上のブランド表記が必要な場合だけ、後工程で小さく配置する。
- 暗い遺品整理、ゴミ屋敷、高額査定広告の印象を避ける。
- imagegenの生成候補は `/private/tmp/seiribu-image-work/why-hoard-things` に置き、採用画像だけ `seiribu-editorial/assets/images/why-hoard-things` に移す。
- 公開用フォルダに残った候補や旧版は `seiribu-editorial/scripts/clean_image_assets.py --article why-hoard-things --dry-run` で確認してから退避する。
