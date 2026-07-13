# 画像制作プラン: 実家の不用品を安く処分する方法｜粗大ごみ・持ち込み・回収業者の使い分け

## 記事情報

- 記事ファイル: `seiribu-editorial/drafts/how-to-dispose.md`
- スラッグ: `how-to-dispose`
- メインKW: 実家 不用品 処分 安く
- 出力モード: light（初回制作をアイキャッチ系1件と本文画像1件までに絞る軽量モード）
- 標準仕上げ: ローカル合成（Pillow）
- Canvaテンプレ: https://canva.link/mqlqak3adj01g1i（任意・手動微調整）
- ロゴ: `seiribu-editorial/assets/images/brand/seiribu-logo.png`
- ロゴ必須対象: アイキャッチ完成版, Canva仕上げ画像
- 本文画像のロゴ: 本文画像・本文図解は標準ではロゴなし。明示依頼やテンプレ上のブランド表記が必要な場合だけ、後工程で小さく配置する。
- 画像生成ツール: imagegen
- 図解レイアウトツール: visualize / Pillow / SVG
- 生成候補の一時置き場: `/private/tmp/seiribu-image-work/how-to-dispose`
- 採用画像の公開用置き場: `seiribu-editorial/assets/images/how-to-dispose`
- 画像掃除スクリプト: `seiribu-editorial/scripts/clean_image_assets.py`

## 判定サマリー

| No | 用途 | 制作方法 | 最終サイズ | 生成時の比率 | ファイル名 | 設置位置 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | アイキャッチ素材 | 画像生成素材 + 背景透過（ローカル合成で仕上げ） | 1200 x 675 | 16:9 | `how-to-dispose-eyecatch-material.png` | アイキャッチ合成用素材 |
| 2 | 記事内図解 | Pillow、SVG、または任意のCanva手動微調整など、文字とレイアウトを制御できる方法で作る | 1200 x 675 | 16:9 | `how-to-dispose-inline-options.png` | H2「実家の不用品を安く処分するための3つの基本手順」の直下 |

## 保留した画像

| 用途 | ファイル名 | 保留理由 |
| --- | --- | --- |
| 記事内図解 | `how-to-dispose-inline-options-2.png` | lightモードでは本文画像を1件までに絞ります。必要なら --mode standard で出力します。 |
| 記事内イメージ | `how-to-dispose-inline-psychology.png` | lightモードでは本文画像を1件までに絞ります。必要なら --mode standard で出力します。 |

## 制作ブリーフ

### 1. アイキャッチ素材

- ファイル名: `how-to-dispose-eyecatch-material.png`
- WordPress画像タイトル: 実家の不用品を安く処分する方法を検討している様子
- ALT: 実家の不用品を安く処分する方法を検討している様子
- 最終サイズ: 1200 x 675
- 生成時の比率: 16:9
- 制作方法: 画像生成素材 + 背景透過（ローカル合成で仕上げ）
- 設置位置: アイキャッチ合成用素材
- キャプション候補: なし

#### 制作意図

- 目的: 読者の「大型家具や大量のゴミをどうやって捨てればいいか途方に暮れている」というリアルな悩みに深く共感し、解決策への期待を持たせる
- 読者に伝えたい感情: 自力では動かせない粗大ごみや使い物にならない大量のガラクタを前に、費用と手間の壁を感じて途方に暮れているリアルな悩みへの共感
- 入れたい要素: 子世代（30〜40代）、古いタンス、壊れた家電や大量のガラクタ（※背景は描かず小物として配置）
- 避けたい表現: 画像内へのテキスト（文字）の生成、背景の描画、お札が舞うような過度な「安さ」の強調、特殊清掃レベルの極端な汚部屋

#### 生成プロンプト / レイアウト仕様

Text-free Seiribu eyecatch cutout asset. Aspect ratio: 16:9. Style: warm flat editorial illustration cutout, high-quality 2D vector art, single coherent subject, clean silhouette, easy to remove background. Subject: 子世代（30〜40代）、古いタンス、壊れた家電や大量のガラクタ（※背景は描かず小物として配置）. Purpose: 読者の「大型家具や大量のゴミをどうやって捨てればいいか途方に暮れている」というリアルな悩みに深く共感し、解決策への期待を持たせる. Tone: 日本の実家らしさ、読者が状況を想像しやすい生活感、明るく清潔、不安を煽らない、買取業者っぽくしすぎない、捨てるより確認する・分けるを見せる. Transparent background, or single flat light background for easy removal. No room, wall, floor, shadow, title area, logo area, frame. Avoid: no text, no letters, no numbers, no Japanese characters, no English words, no labels, no logo, no watermark, no signage, no speech bubbles; 画像内へのテキスト（文字）の生成、背景の描画、お札が舞うような過度な「安さ」の強調、特殊清掃レベルの極端な汚部屋. Do not reuse composition, character placement, object placement, or background concept from existing Seiribu article images.

#### ローカル合成

- 合成スクリプト: `seiribu-editorial/scripts/compose_eyecatch.py`
- タイトル: 実家の不用品を安く処分する方法（※画像内には生成せず合成時に追加）
- サブタイトル: 粗大ごみ・持ち込み・回収業者の費用比較（※同上）
- 出力サイズ: 1200 x 675
- 出力ファイル: `how-to-dispose-eyecatch-branded.png`
- ロゴ: `seiribu-editorial/assets/images/brand/seiribu-logo.png`
- ロゴ必須: はい
- ロゴ位置: 左上
- ロゴ配置ルール: 生成AI素材にはロゴを描かせない。アイキャッチ完成版とCanva仕上げ画像では、ローカル合成または手動調整でセイリ部ロゴを小さなブランド署名として配置する。本文画像・本文図解は標準ではロゴなしで軽く保つ。
- Canvaの扱い: 任意の手動微調整。Canva API連携を本番前提にしない。

### 2. 記事内図解

- ファイル名: `how-to-dispose-inline-options.png`
- WordPress画像タイトル: 実家の不用品処分費用を安く抑える3つの手順
- ALT: 実家の不用品処分費用を安く抑える3つの手順（売る、家庭ごみ、不用品回収）
- 最終サイズ: 1200 x 675
- 生成時の比率: 16:9
- 制作方法: Pillow、SVG、または任意のCanva手動微調整など、文字とレイアウトを制御できる方法で作る
- 設置位置: H2「実家の不用品を安く処分するための3つの基本手順」の直下
- キャプション候補: 売る・自力で捨てる手順を挟むことで、業者への依頼費用を最小化できます。

#### 制作意図

- 目的: 費用を最小化する処分手順の「漏斗（ファネル）」構造を視覚的に理解させる
- 読者に伝えたい感情: 未指定
- 入れたい要素: 逆三角形（漏斗）の図、3つのステップ名とアイコン、下に行くほど荷物量が減っていく表現
- 避けたい表現: 「捨てる」を推奨するようなポジティブすぎる表現、ゴミ箱に何でも捨てるイラスト

#### 生成プロンプト / レイアウト仕様

画像生成AIには渡さない。1200 x 675 / 16:9 の図解として、Pillow・SVG・Canvaなどで制作。内容: 逆三角形（漏斗）の図、3つのステップ名とアイコン、下に行くほど荷物量が減っていく表現。目的: 費用を最小化する処分手順の「漏斗（ファネル）」構造を視覚的に理解させる。日本語ラベル、表、矢印、比較軸は後工程で正確に配置する。ロゴ: 本文画像・本文図解は標準ではロゴなし。明示依頼やテンプレ上のブランド表記が必要な場合だけ、後工程で小さく配置する。

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
- imagegenの生成候補は `/private/tmp/seiribu-image-work/how-to-dispose` に置き、採用画像だけ `seiribu-editorial/assets/images/how-to-dispose` に移す。
- 公開用フォルダに残った候補や旧版は `seiribu-editorial/scripts/clean_image_assets.py --article how-to-dispose --dry-run` で確認してから退避する。
