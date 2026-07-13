# 画像制作プラン: 実家の片付けで売れるもの一覧｜捨てる前に確認する品物と整理手順

## 記事情報

- 記事ファイル: `seiribu-editorial/drafts/pillars/sellable-disused-items-rewrite-v2.md`
- スラッグ: `sellable-disused-items`
- メインKW: 実家 片付け 売れるもの
- 出力モード: light（初回制作をアイキャッチ系1件と本文画像1件までに絞る軽量モード）
- 標準仕上げ: ローカル合成（Pillow）
- Canvaテンプレ: https://canva.link/mqlqak3adj01g1i（任意・手動微調整）
- ロゴ: `seiribu-editorial/assets/images/brand/seiribu-logo.png`
- ロゴ必須対象: アイキャッチ完成版, Canva仕上げ画像
- 本文画像のロゴ: 本文画像・本文図解は標準ではロゴなし。明示依頼やテンプレ上のブランド表記が必要な場合だけ、後工程で小さく配置する。
- 画像生成ツール: imagegen
- 図解レイアウトツール: visualize / Pillow / SVG
- 生成候補の一時置き場: `/private/tmp/seiribu-image-work/sellable-disused-items`
- 採用画像の公開用置き場: `seiribu-editorial/assets/images/sellable-disused-items`
- 画像掃除スクリプト: `seiribu-editorial/scripts/clean_image_assets.py`

## 判定サマリー

| No | 用途 | 制作方法 | 最終サイズ | 生成時の比率 | ファイル名 | 設置位置 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 記事内イメージ | 画像生成素材 | 1200 x 675 | 16:9 | `sellable-disused-items-inline-01.png` | 導入文の直後（最初のH2の上） |

## 保留した画像

| 用途 | ファイル名 | 保留理由 |
| --- | --- | --- |
| 記事内図解 | `sellable-disused-items-inline-three-boxes.png` | lightモードでは本文画像を1件までに絞ります。必要なら --mode standard で出力します。 |

## 制作ブリーフ

### 1. 記事内イメージ

- ファイル名: `sellable-disused-items-inline-01.png`
- WordPress画像タイトル: 実家の片付けで出てきた古い本やカメラ、レコード、ブランド品を親子で確認している様子
- ALT: 実家の片付けで出てきた古い本やカメラ、レコード、ブランド品を親子で確認している様子
- 最終サイズ: 1200 x 675
- 生成時の比率: 16:9
- 制作方法: 画像生成素材
- 設置位置: 導入文の直後（最初のH2の上）
- キャプション候補: 実家には、捨ててしまうにはもったいない品物がたくさん眠っています。

#### 制作意図

- 目的: 実家の片付けで出てきた様々な「売れるかもしれない物」を確認している様子をイメージさせる
- 読者に伝えたい感情: 未指定
- 入れたい要素: 親子（40代の子と70代の親）、段ボール、カメラ、レコード、ブランド品
- 避けたい表現: 暗い雰囲気、ゴミ屋敷のような散らかりすぎた部屋

#### 生成プロンプト / レイアウト仕様

Warm text-free Seiribu editorial illustration for '実家の片付けで売れるもの一覧｜捨てる前に確認する品物と整理手順'. Aspect ratio: 16:9. Style: warm flat editorial illustration, high-quality 2D vector art, soft shapes, minimal or no outlines, gentle natural colors, contemporary Japanese everyday home, clean but lived-in. Main visual: 親子（40代の子と70代の親）、段ボール、カメラ、レコード、ブランド品. Purpose: 実家の片付けで出てきた様々な「売れるかもしれない物」を確認している様子をイメージさせる. Tone: 日本の実家らしさ、読者が状況を想像しやすい生活感、明るく清潔、不安を煽らない、買取業者っぽくしすぎない、捨てるより確認する・分けるを見せる. Avoid: no text, no letters, no numbers, no Japanese characters, no English words, no labels, no logo, no watermark, no signage, no speech bubbles; 暗い雰囲気、ゴミ屋敷のような散らかりすぎた部屋. Do not reuse composition, character placement, object placement, or background concept from existing Seiribu article images.

## 品質チェック

- アイキャッチまたはアイキャッチ合成用素材の指定がありません。自動補完はしません。
- 本文画像はlightモードの初回範囲です。追加画像は保留分から必要に応じて選びます。
- lightモードのため、初回制作は1件に絞り、1件を保留しました。
- 画像生成AIに文字、日本語ラベル、ロゴ、透かし、看板を描かせない。
- 日本語ラベルがある図解は、画像生成AIに文字を任せずレイアウト生成で作る。
- アイキャッチのロゴとタイトルは標準ではローカル合成（Pillow）、必要に応じてSVGやCanvaの手動微調整で配置する。
- ロゴ必須対象: アイキャッチ完成版, Canva仕上げ画像。
- 本文画像・本文図解のロゴ: 本文画像・本文図解は標準ではロゴなし。明示依頼やテンプレ上のブランド表記が必要な場合だけ、後工程で小さく配置する。
- 暗い遺品整理、ゴミ屋敷、高額査定広告の印象を避ける。
- imagegenの生成候補は `/private/tmp/seiribu-image-work/sellable-disused-items` に置き、採用画像だけ `seiribu-editorial/assets/images/sellable-disused-items` に移す。
- 公開用フォルダに残った候補や旧版は `seiribu-editorial/scripts/clean_image_assets.py --article sellable-disused-items --dry-run` で確認してから退避する。
