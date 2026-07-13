# 画像制作プラン: 【実家の片付け】兄弟で押し付け合いに？「自分ばかり」を防ぐ分担術と解決策

## 記事情報

- 記事ファイル: `seiribu-editorial/drafts/siblings-share.md`
- スラッグ: `siblings-share`
- メインKW: 実家 片付け 兄弟 (関連: 兄弟 押し付け合い, 自分ばかり, トラブル)
- 出力モード: light（初回制作をアイキャッチ系1件と本文画像1件までに絞る軽量モード）
- 標準仕上げ: ローカル合成（Pillow）
- Canvaテンプレ: https://canva.link/mqlqak3adj01g1i（任意・手動微調整）
- ロゴ: `seiribu-editorial/assets/images/brand/seiribu-logo.png`
- ロゴ必須対象: アイキャッチ完成版, Canva仕上げ画像
- 本文画像のロゴ: 本文画像・本文図解は標準ではロゴなし。明示依頼やテンプレ上のブランド表記が必要な場合だけ、後工程で小さく配置する。
- 画像生成ツール: imagegen
- 図解レイアウトツール: visualize / Pillow / SVG
- 生成候補の一時置き場: `/private/tmp/seiribu-image-work/siblings-share`
- 採用画像の公開用置き場: `seiribu-editorial/assets/images/siblings-share`
- 画像掃除スクリプト: `seiribu-editorial/scripts/clean_image_assets.py`

## 判定サマリー

| No | 用途 | 制作方法 | 最終サイズ | 生成時の比率 | ファイル名 | 設置位置 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | アイキャッチ | 背景なし画像生成素材 + ローカル合成（Pillow） | 1200 x 675 | 16:9 | `siblings-share-eyecatch-branded.png` | アイキャッチ |
| 2 | 記事内イメージ | 画像生成素材 | 1200 x 675 | 16:9 | `siblings-share-inline-psychology.png` | 本文中のCMSブリーフ位置 |

## 保留した画像

| 用途 | ファイル名 | 保留理由 |
| --- | --- | --- |
| 記事内図解 | `siblings-share-inline-options.png` | lightモードでは本文画像を1件までに絞ります。必要なら --mode standard で出力します。 |
| 記事内イメージ | `siblings-share-inline-options-2.png` | lightモードでは本文画像を1件までに絞ります。必要なら --mode standard で出力します。 |

## 制作ブリーフ

### 1. アイキャッチ

- ファイル名: `siblings-share-eyecatch-branded.png`
- WordPress画像タイトル: 【実家の片付け】兄弟で押し付け合いに？「自分ばかり」を防ぐ分担術と解決策のアイキャッチ
- ALT: 【実家の片付け】兄弟で押し付け合いに？「自分ばかり」を防ぐ分担術と解決策に関するアイキャッチ
- 最終サイズ: 1200 x 675
- 生成時の比率: 16:9
- 制作方法: 背景なし画像生成素材 + ローカル合成（Pillow）
- 設置位置: アイキャッチ
- キャプション候補: なし

#### 制作意図

- 目的: 未指定
- 読者に伝えたい感情: 未指定
- 入れたい要素: 未指定
- 避けたい表現: 未指定

#### 生成プロンプト / レイアウト仕様

Text-free Seiribu eyecatch cutout material for '【実家の片付け】兄弟で押し付け合いに？「自分ばかり」を防ぐ分担術と解決策'. Aspect ratio: 16:9. Style: warm flat editorial illustration cutout, high-quality 2D vector art, single coherent subject, clean silhouette, easy to remove background. Main visual: 記事内容に合う人物と物. Purpose: . Tone: 日本の実家らしさ、読者が状況を想像しやすい生活感、明るく清潔、不安を煽らない、買取業者っぽくしすぎない、捨てるより確認する・分けるを見せる. Transparent background, or single flat light background for easy removal. No room, wall, floor, shadow, title area, logo area, frame. This background-free material will be finished later with the local Seiribu Pillow compositor. Avoid: no text, no letters, no numbers, no Japanese characters, no English words, no labels, no logo, no watermark, no signage, no speech bubbles; 暗さ、ゴミ屋敷感、高額査定広告感、既存構図の流用. Do not reuse composition, character placement, object placement, or background concept from existing Seiribu article images.

#### ローカル合成

- 合成スクリプト: `seiribu-editorial/scripts/compose_eyecatch.py`
- タイトル: 【実家の片付け】兄弟で押し付け合いに？
- サブタイトル: 「自分ばかり」を防ぐ分担術と解決策
- 出力サイズ: 1200 x 675
- 出力ファイル: `siblings-share-eyecatch-branded.png`
- ロゴ: `seiribu-editorial/assets/images/brand/seiribu-logo.png`
- ロゴ必須: はい
- ロゴ位置: 左上
- ロゴ配置ルール: 生成AI素材にはロゴを描かせない。アイキャッチ完成版とCanva仕上げ画像では、ローカル合成または手動調整でセイリ部ロゴを小さなブランド署名として配置する。本文画像・本文図解は標準ではロゴなしで軽く保つ。
- Canvaの扱い: 任意の手動微調整。Canva API連携を本番前提にしない。

### 2. 記事内イメージ

- ファイル名: `siblings-share-inline-psychology.png`
- WordPress画像タイトル: 一人で実家の片付けを背負い込み疲労している様子
- ALT: 一人で実家の片付けを背負い込み疲労している様子
- 最終サイズ: 1200 x 675
- 生成時の比率: 16:9
- 制作方法: 画像生成素材
- 設置位置: 本文中のCMSブリーフ位置
- キャプション候補: どうして自分ばかりがこんなに大変な思いをしなければならないのか、と理不尽に感じるのは当然のことです。

#### 制作意図

- 目的: 一人で実家の片付けを背負い込み、疲労と孤独感を抱えている様子を伝えるため
- 読者に伝えたい感情: 不公平感、理不尽さ、疲労感への共感
- 入れたい要素: 散らかった実家の居間で、積み上がった段ボールを前に一人でため息をついている女性（または男性）の姿
- 避けたい表現: 画像内へのテキスト（文字）の生成、極端なホラーテイスト

#### 生成プロンプト / レイアウト仕様

Warm text-free Seiribu editorial illustration for '【実家の片付け】兄弟で押し付け合いに？「自分ばかり」を防ぐ分担術と解決策'. Aspect ratio: 16:9. Style: warm flat editorial illustration, high-quality 2D vector art, soft shapes, minimal or no outlines, gentle natural colors, contemporary Japanese everyday home, clean but lived-in. Main visual: 散らかった実家の居間で、積み上がった段ボールを前に一人でため息をついている女性（または男性）の姿. Purpose: 一人で実家の片付けを背負い込み、疲労と孤独感を抱えている様子を伝えるため. Tone: 日本の実家らしさ、読者が状況を想像しやすい生活感、明るく清潔、不安を煽らない、買取業者っぽくしすぎない、捨てるより確認する・分けるを見せる. Avoid: no text, no letters, no numbers, no Japanese characters, no English words, no labels, no logo, no watermark, no signage, no speech bubbles; 画像内へのテキスト（文字）の生成、極端なホラーテイスト. Do not reuse composition, character placement, object placement, or background concept from existing Seiribu article images.

## 品質チェック

- 記事内のアイキャッチ指定を利用しています。
- 本文画像はlightモードの初回範囲です。追加画像は保留分から必要に応じて選びます。
- lightモードのため、初回制作は2件に絞り、2件を保留しました。
- 画像生成AIに文字、日本語ラベル、ロゴ、透かし、看板を描かせない。
- 日本語ラベルがある図解は、画像生成AIに文字を任せずレイアウト生成で作る。
- アイキャッチのロゴとタイトルは標準ではローカル合成（Pillow）、必要に応じてSVGやCanvaの手動微調整で配置する。
- ロゴ必須対象: アイキャッチ完成版, Canva仕上げ画像。
- 本文画像・本文図解のロゴ: 本文画像・本文図解は標準ではロゴなし。明示依頼やテンプレ上のブランド表記が必要な場合だけ、後工程で小さく配置する。
- 暗い遺品整理、ゴミ屋敷、高額査定広告の印象を避ける。
- imagegenの生成候補は `/private/tmp/seiribu-image-work/siblings-share` に置き、採用画像だけ `seiribu-editorial/assets/images/siblings-share` に移す。
- 公開用フォルダに残った候補や旧版は `seiribu-editorial/scripts/clean_image_assets.py --article siblings-share --dry-run` で確認してから退避する。
