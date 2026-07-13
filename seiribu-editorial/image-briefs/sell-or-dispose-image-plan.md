# 画像制作プラン: 買取不可だったものはどうする？売れない理由と処分方法

## 記事情報

- 記事ファイル: `seiribu-editorial/drafts/pillars/sell-or-dispose-clean.md`
- スラッグ: `sell-or-dispose`
- メインKW: 買取不可 処分
- 出力モード: light（初回制作をアイキャッチ系1件と本文画像1件までに絞る軽量モード）
- 標準仕上げ: ローカル合成（Pillow）
- Canvaテンプレ: https://canva.link/mqlqak3adj01g1i（任意・手動微調整）
- ロゴ: `seiribu-editorial/assets/images/brand/seiribu-logo.png`
- ロゴ必須対象: アイキャッチ完成版, Canva仕上げ画像
- 本文画像のロゴ: 本文画像・本文図解は標準ではロゴなし。明示依頼やテンプレ上のブランド表記が必要な場合だけ、後工程で小さく配置する。
- 画像生成ツール: imagegen
- 図解レイアウトツール: visualize / Pillow / SVG
- 生成候補の一時置き場: `/private/tmp/seiribu-image-work/sell-or-dispose`
- 採用画像の公開用置き場: `seiribu-editorial/assets/images/sell-or-dispose`
- 画像掃除スクリプト: `seiribu-editorial/scripts/clean_image_assets.py`

## 判定サマリー

| No | 用途 | 制作方法 | 最終サイズ | 生成時の比率 | ファイル名 | 設置位置 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | アイキャッチ | 背景なし画像生成素材 + ローカル合成（Pillow） | 1200 x 675 | 16:9 | `sell-or-dispose-eyecatch.webp` | アイキャッチ |
| 2 | 記事内イメージ | 画像生成素材 | 1200 x 675 | 16:9 | `sell-or-dispose-inline-three-boxes.png` | 本文中のCMSブリーフ位置 |

## 保留した画像

| 用途 | ファイル名 | 保留理由 |
| --- | --- | --- |
| 記事内イメージ | `sell-or-dispose-inline-three-boxes-2.png` | lightモードでは本文画像を1件までに絞ります。必要なら --mode standard で出力します。 |

## 制作ブリーフ

### 1. アイキャッチ

- ファイル名: `sell-or-dispose-eyecatch.webp`
- WordPress画像タイトル: 買取不可だった不用品の処分方法と売れない理由
- ALT: 買取不可だった不用品の処分方法と売れない理由
- 最終サイズ: 1200 x 675
- 生成時の比率: 16:9
- 制作方法: 背景なし画像生成素材 + ローカル合成（Pillow）
- 設置位置: アイキャッチ
- キャプション候補: なし

#### 制作意図

- 目的: 読者が「買取不可になっても、ちゃんと次の手があるんだ」と安心できるような表紙
- 読者に伝えたい感情: 買取不可に対する落胆の解消と、前向きな片付けへのモチベーション
- 入れたい要素: 買取業者に見送られた後、残った段ボール箱や古着を前に「さて、次はどうやって手放そうか」と前向きに考えている家族（親子）の後ろ姿や横顔
- 避けたい表現: 暗く絶望している姿、ゴミ屋敷のような汚い部屋、買取業者の悪目立ち

#### 生成プロンプト / レイアウト仕様

Text-free Seiribu eyecatch cutout material for '買取不可だったものはどうする？売れない理由と処分方法'. Aspect ratio: 16:9. Style: warm flat editorial illustration cutout, high-quality 2D vector art, single coherent subject, clean silhouette, easy to remove background. Main visual: 買取業者に見送られた後、残った段ボール箱や古着を前に「さて、次はどうやって手放そうか」と前向きに考えている家族（親子）の後ろ姿や横顔. Purpose: 読者が「買取不可になっても、ちゃんと次の手があるんだ」と安心できるような表紙. Tone: 日本の実家らしさ、読者が状況を想像しやすい生活感、明るく清潔、不安を煽らない、買取業者っぽくしすぎない、捨てるより確認する・分けるを見せる. Transparent background, or single flat light background for easy removal. No room, wall, floor, shadow, title area, logo area, frame. This background-free material will be finished later with the local Seiribu Pillow compositor. Avoid: no text, no letters, no numbers, no Japanese characters, no English words, no labels, no logo, no watermark, no signage, no speech bubbles; 暗く絶望している姿、ゴミ屋敷のような汚い部屋、買取業者の悪目立ち. Do not reuse composition, character placement, object placement, or background concept from existing Seiribu article images.

#### ローカル合成

- 合成スクリプト: `seiribu-editorial/scripts/compose_eyecatch.py`
- タイトル: 買取不可だったものはどうする？
- サブタイトル: 売れない理由と処分方法
- 出力サイズ: 1200 x 675
- 出力ファイル: `sell-or-dispose-eyecatch.webp`
- ロゴ: `seiribu-editorial/assets/images/brand/seiribu-logo.png`
- ロゴ必須: はい
- ロゴ位置: 左上
- ロゴ配置ルール: 生成AI素材にはロゴを描かせない。アイキャッチ完成版とCanva仕上げ画像では、ローカル合成または手動調整でセイリ部ロゴを小さなブランド署名として配置する。本文画像・本文図解は標準ではロゴなしで軽く保つ。
- Canvaの扱い: 任意の手動微調整。Canva API連携を本番前提にしない。

### 2. 記事内イメージ

- ファイル名: `sell-or-dispose-inline-three-boxes.png`
- WordPress画像タイトル: 不用品を「自治体・寄付・業者」の3つに仕分けている風景
- ALT: 不用品を「自治体・寄付・業者」の3つに仕分けている風景
- 最終サイズ: 1200 x 675
- 生成時の比率: 16:9
- 制作方法: 画像生成素材
- 設置位置: 本文中のCMSブリーフ位置
- キャプション候補: 状況に合わせて、自分に一番合った手放し方を選びましょう

#### 制作意図

- 目的: 3つの処分方法があることを視覚的に伝え、片付けが前に進むポジティブな印象を与えること
- 読者に伝えたい感情: 選択肢があることの安心感と、「これなら片付けられそう」という前向きな気持ち
- 入れたい要素: 「自治体のゴミ袋」「寄付用の段ボール」「業者に任せる大きな家具」などを、スッキリとした部屋で仕分けている前向きな片付けの風景
- 避けたい表現: 複雑すぎるB2Bのような比較表や、ゴミが散乱している汚い部屋

#### 生成プロンプト / レイアウト仕様

Warm text-free Seiribu editorial illustration for '買取不可だったものはどうする？売れない理由と処分方法'. Aspect ratio: 16:9. Style: warm flat editorial illustration, high-quality 2D vector art, soft shapes, minimal or no outlines, gentle natural colors, contemporary Japanese everyday home, clean but lived-in. Main visual: 「自治体のゴミ袋」「寄付用の段ボール」「業者に任せる大きな家具」などを、スッキリとした部屋で仕分けている前向きな片付けの風景. Purpose: 3つの処分方法があることを視覚的に伝え、片付けが前に進むポジティブな印象を与えること. Tone: 日本の実家らしさ、読者が状況を想像しやすい生活感、明るく清潔、不安を煽らない、買取業者っぽくしすぎない、捨てるより確認する・分けるを見せる. Avoid: no text, no letters, no numbers, no Japanese characters, no English words, no labels, no logo, no watermark, no signage, no speech bubbles; 複雑すぎるB2Bのような比較表や、ゴミが散乱している汚い部屋. Do not reuse composition, character placement, object placement, or background concept from existing Seiribu article images.

## 品質チェック

- 記事内のアイキャッチ指定を利用しています。
- 本文画像はlightモードの初回範囲です。追加画像は保留分から必要に応じて選びます。
- lightモードのため、初回制作は2件に絞り、1件を保留しました。
- 画像生成AIに文字、日本語ラベル、ロゴ、透かし、看板を描かせない。
- 日本語ラベルがある図解は、画像生成AIに文字を任せずレイアウト生成で作る。
- アイキャッチのロゴとタイトルは標準ではローカル合成（Pillow）、必要に応じてSVGやCanvaの手動微調整で配置する。
- ロゴ必須対象: アイキャッチ完成版, Canva仕上げ画像。
- 本文画像・本文図解のロゴ: 本文画像・本文図解は標準ではロゴなし。明示依頼やテンプレ上のブランド表記が必要な場合だけ、後工程で小さく配置する。
- 暗い遺品整理、ゴミ屋敷、高額査定広告の印象を避ける。
- imagegenの生成候補は `/private/tmp/seiribu-image-work/sell-or-dispose` に置き、採用画像だけ `seiribu-editorial/assets/images/sell-or-dispose` に移す。
- 公開用フォルダに残った候補や旧版は `seiribu-editorial/scripts/clean_image_assets.py --article sell-or-dispose --dry-run` で確認してから退避する。
