# 画像制作プラン: 買取不可だったものはどうする？売れない理由と処分方法

## 記事情報

- 記事ファイル: `seiribu-editorial/drafts/pillars/sell-or-dispose-clean.md`
- スラッグ: `sell-or-dispose`
- メインKW: 買取不可 処分
- 標準仕上げ: ローカル合成（Pillow）
- Canvaテンプレ: https://canva.link/mqlqak3adj01g1i（任意・手動微調整）
- ロゴ: `seiribu-editorial/assets/images/brand/seiribu-logo.png`
- 完成版ロゴ必須: はい

## 判定サマリー

| No | 用途 | 制作方法 | 最終サイズ | 生成時の比率 | ファイル名 | 設置位置 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | アイキャッチ | 画像生成素材 + ローカル合成（Pillow） | 1200 x 630 | 16:9 | `sell-or-dispose-eyecatch.webp` | アイキャッチ |
| 2 | 記事内イメージ | 画像生成素材 | 1200 x 800 | 3:2 | `sell-or-dispose-inline-three-boxes.png` | 本文中のCMSブリーフ位置 |
| 3 | 記事内イメージ | 画像生成素材 | 1200 x 800 | 3:2 | `sell-or-dispose-inline-three-boxes-2.png` | 本文中のCMSブリーフ位置 |

## 制作ブリーフ

### 1. アイキャッチ

- ファイル名: `sell-or-dispose-eyecatch.webp`
- WordPress画像タイトル: 買取不可だった不用品の処分方法と売れない理由
- ALT: 買取不可だった不用品の処分方法と売れない理由
- 最終サイズ: 1200 x 630
- 生成時の比率: 16:9
- 制作方法: 画像生成素材 + ローカル合成（Pillow）
- 設置位置: アイキャッチ
- キャプション候補: なし

#### 制作意図

- 目的: 読者が「買取不可になっても、ちゃんと次の手があるんだ」と安心できるような表紙
- 読者に伝えたい感情: 買取不可に対する落胆の解消と、前向きな片付けへのモチベーション
- 入れたい要素: 買取業者に見送られた後、残った段ボール箱や古着を前に「さて、次はどうやって手放そうか」と前向きに考えている家族（親子）の後ろ姿や横顔
- 避けたい表現: 暗く絶望している姿、ゴミ屋敷のような汚い部屋、買取業者の悪目立ち

#### 生成プロンプト / レイアウト仕様

Create a text-free eyecatch background and subject illustration for the Seiribu article '買取不可だったものはどうする？売れない理由と処分方法'. Aspect ratio: 16:9. Style: warm flat editorial illustration, high-quality 2D vector art, soft shapes, minimal or no outlines, gentle natural colors, contemporary Japanese everyday home, clean but lived-in. This image will be finished later with the local Seiribu Pillow compositor, so leave calm uncluttered space for a title and logo to be added later, but do not draw any placeholder cards or panels with text. Composition: タイトル・サブタイトル・ロゴをローカル合成で載せる前提で、上部に余白を残し、下部から中央に人物や実家の物を配置するブランド型素材. Main visual: 買取業者に見送られた後、残った段ボール箱や古着を前に「さて、次はどうやって手放そうか」と前向きに考えている家族（親子）の後ろ姿や横顔. Purpose: 読者が「買取不可になっても、ちゃんと次の手があるんだ」と安心できるような表紙. Tone: 日本の実家らしさ、読者が状況を想像しやすい生活感、明るく清潔、不安を煽らない、買取業者っぽくしすぎない、捨てるより確認する・分けるを見せる. Must avoid: no text, no letters, no numbers, no Japanese characters, no English words, no labels, no logo, no watermark, no signage, no speech bubbles. Also avoid: 暗く絶望している姿、ゴミ屋敷のような汚い部屋、買取業者の悪目立ち. Do not reuse the composition, character placement, object placement, or background concept from any existing Seiribu article image.

#### ローカル合成

- 合成スクリプト: `seiribu-editorial/scripts/compose_eyecatch.py`
- タイトル: 買取不可だったものはどうする？
- サブタイトル: 売れない理由と処分方法
- 出力サイズ: 1200 x 630
- 出力ファイル: `sell-or-dispose-eyecatch.webp`
- ロゴ: `seiribu-editorial/assets/images/brand/seiribu-logo.png`
- ロゴ必須: はい
- ロゴ位置: 左上
- ロゴ配置ルール: 生成AI素材にはロゴを描かせない。標準ではPillowのローカル合成で、完成版にはセイリ部ロゴを必ず小さなブランド署名として配置する。
- Canvaの扱い: 任意の手動微調整。Canva API連携を本番前提にしない。

#### Canva任意微調整

- 状態: optional_manual
- テンプレートURL: https://canva.link/mqlqak3adj01g1i
- タイトル: 買取不可だったものはどうする？
- サブタイトル: 売れない理由と処分方法
- ロゴ: `seiribu-editorial/assets/images/brand/seiribu-logo.png`
- ロゴ必須: はい
- ロゴ位置: 左上
- ロゴ配置ルール: 生成AI素材にはロゴを描かせない。標準ではPillowのローカル合成で、完成版にはセイリ部ロゴを必ず小さなブランド署名として配置する。
- 見出しフォント: UDモトヤアポロ 太字
- サブタイトルフォント: Noto Sans JP Regular

### 2. 記事内イメージ

- ファイル名: `sell-or-dispose-inline-three-boxes.png`
- WordPress画像タイトル: 不用品を「自治体・寄付・業者」の3つに仕分けている風景
- ALT: 不用品を「自治体・寄付・業者」の3つに仕分けている風景
- 最終サイズ: 1200 x 800
- 生成時の比率: 3:2
- 制作方法: 画像生成素材
- 設置位置: 本文中のCMSブリーフ位置
- キャプション候補: 状況に合わせて、自分に一番合った手放し方を選びましょう

#### 制作意図

- 目的: 3つの処分方法があることを視覚的に伝え、片付けが前に進むポジティブな印象を与えること
- 読者に伝えたい感情: 選択肢があることの安心感と、「これなら片付けられそう」という前向きな気持ち
- 入れたい要素: 「自治体のゴミ袋」「寄付用の段ボール」「業者に任せる大きな家具」などを、スッキリとした部屋で仕分けている前向きな片付けの風景
- 避けたい表現: 複雑すぎるB2Bのような比較表や、ゴミが散乱している汚い部屋

#### 生成プロンプト / レイアウト仕様

Create a warm text-free editorial illustration for the Seiribu article '買取不可だったものはどうする？売れない理由と処分方法'. Aspect ratio: 3:2. Style: warm flat editorial illustration, high-quality 2D vector art, soft shapes, minimal or no outlines, gentle natural colors, contemporary Japanese everyday home, clean but lived-in. Main visual: 「自治体のゴミ袋」「寄付用の段ボール」「業者に任せる大きな家具」などを、スッキリとした部屋で仕分けている前向きな片付けの風景. Purpose: 3つの処分方法があることを視覚的に伝え、片付けが前に進むポジティブな印象を与えること. Tone: 日本の実家らしさ、読者が状況を想像しやすい生活感、明るく清潔、不安を煽らない、買取業者っぽくしすぎない、捨てるより確認する・分けるを見せる. Must avoid: no text, no letters, no numbers, no Japanese characters, no English words, no labels, no logo, no watermark, no signage, no speech bubbles. Also avoid: 複雑すぎるB2Bのような比較表や、ゴミが散乱している汚い部屋.

### 3. 記事内イメージ

- ファイル名: `sell-or-dispose-inline-three-boxes-2.png`
- WordPress画像タイトル: 買取を断られても落ち込まず、次のステップへ進む家族のイラスト
- ALT: 買取を断られても落ち込まず、次のステップへ進む家族のイラスト
- 最終サイズ: 1200 x 800
- 生成時の比率: 3:2
- 制作方法: 画像生成素材
- 設置位置: 本文中のCMSブリーフ位置
- キャプション候補: 買取を断られる主な理由は「業者が再販できないから」です。品物のせいではありません。

#### 制作意図

- 目的: 読者に「自分や品物が悪いのではなく、業者のビジネス上の理由で断られる」と納得してもらうこと
- 読者に伝えたい感情: 買取不可だったことへの落胆を和らげ、「無価値なわけじゃないんだ」という安心感
- 入れたい要素: 業者が帰った後、残された荷物（古い着物や箱）を前に、親子がお茶を飲みながら「まあ、しょうがないね」と穏やかに話しているような温かいイラスト
- 避けたい表現: 読者を責めるような表現や、暗く落ち込んでいる絶望的な雰囲気

#### 生成プロンプト / レイアウト仕様

Create a warm text-free editorial illustration for the Seiribu article '買取不可だったものはどうする？売れない理由と処分方法'. Aspect ratio: 3:2. Style: warm flat editorial illustration, high-quality 2D vector art, soft shapes, minimal or no outlines, gentle natural colors, contemporary Japanese everyday home, clean but lived-in. Main visual: 業者が帰った後、残された荷物（古い着物や箱）を前に、親子がお茶を飲みながら「まあ、しょうがないね」と穏やかに話しているような温かいイラスト. Purpose: 読者に「自分や品物が悪いのではなく、業者のビジネス上の理由で断られる」と納得してもらうこと. Tone: 日本の実家らしさ、読者が状況を想像しやすい生活感、明るく清潔、不安を煽らない、買取業者っぽくしすぎない、捨てるより確認する・分けるを見せる. Must avoid: no text, no letters, no numbers, no Japanese characters, no English words, no labels, no logo, no watermark, no signage, no speech bubbles. Also avoid: 読者を責めるような表現や、暗く落ち込んでいる絶望的な雰囲気.

## 品質チェック

- 記事内のアイキャッチ指定を利用しています。
- 本文画像の枚数は適正範囲です。
- 画像生成AIに文字、日本語ラベル、ロゴ、透かし、看板を描かせない。
- 日本語ラベルがある図解は、画像生成AIに文字を任せずレイアウト生成で作る。
- ロゴとタイトルは標準ではローカル合成（Pillow）、必要に応じてSVGやCanvaの手動微調整で配置する。
- アイキャッチ完成版と本文図解完成版では、セイリ部ロゴを必ず小さなブランド署名として配置する。
- 暗い遺品整理、ゴミ屋敷、高額査定広告の印象を避ける。
