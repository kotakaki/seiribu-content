# 画像制作プラン: 一人っ子の実家の片付けはどう進める？親との話し合いと準備

## 記事情報

- 記事ファイル: `seiribu-editorial/drafts/only-child.md`
- スラッグ: `only-child`
- メインKW: 一人っ子 実家 片付け
- 標準仕上げ: ローカル合成（Pillow）
- Canvaテンプレ: https://canva.link/mqlqak3adj01g1i（任意・手動微調整）
- ロゴ: `seiribu-editorial/assets/images/brand/seiribu-logo.png`
- 完成版ロゴ必須: はい

## 判定サマリー

| No | 用途 | 制作方法 | 最終サイズ | 生成時の比率 | ファイル名 | 設置位置 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | アイキャッチ素材 | 画像生成素材 + 背景透過（ローカル合成で仕上げ） | 1536 x 1024 | 3:2 | `only-child-eyecatch.png` | アイキャッチ合成用素材 |
| 2 | 記事内イメージ | 画像生成素材 | 1200 x 800 | 3:2 | `only-child-inline-psychology.png` | 本文中のCMSブリーフ位置 |
| 3 | 記事内イメージ | 画像生成素材 | 1200 x 800 | 3:2 | `only-child-conflict-trap.png` | 本文中のCMSブリーフ位置 |
| 4 | 記事内図解 | Pillow、SVG、または任意のCanva手動微調整など、文字とレイアウトを制御できる方法で作る | 1200 x 800 | 3:2 | `only-child-two-professionals.png` | 本文中のCMSブリーフ位置 |
| 5 | 記事内図解 | Pillow、SVG、または任意のCanva手動微調整など、文字とレイアウトを制御できる方法で作る | 1200 x 800 | 3:2 | `only-child-3steps-flow.png` | 本文中のCMSブリーフ位置 |

## 制作ブリーフ

### 1. アイキャッチ素材

- ファイル名: `only-child-eyecatch.png`
- WordPress画像タイトル: 一人っ子の実家の片付け負担をプロの力で減らすイメージ
- ALT: 一人っ子の実家の片付け負担をプロの力で減らすイメージ
- 最終サイズ: 1536 x 1024
- 生成時の比率: 3:2
- 制作方法: 画像生成素材 + 背景透過（ローカル合成で仕上げ）
- 設置位置: アイキャッチ合成用素材
- キャプション候補: なし

#### 制作意図

- 目的: 記事の顔として「一人っ子が抱える孤独なプレッシャー」と「プロに頼る解決策」を直感的に伝える
- 読者に伝えたい感情: 孤独感への共感と、解決への希望
- 入れたい要素: 悩む男女（40〜50代）、段ボールや古い家具、エプロンや制服を着た業者スタッフ、明るい光
- 避けたい表現: 画像内へのテキスト（文字）の生成、背景の描画、過度なホラーテイスト

#### 生成プロンプト / レイアウト仕様

Create an eyecatch cutout asset for the Seiribu article '一人っ子の実家の片付けはどう進める？親との話し合いと準備'. Aspect ratio: 3:2. Style: warm flat editorial illustration cutout, high-quality 2D vector art, single coherent subject, clean silhouette, easy to remove background. Transparent background if possible; if transparency is not available, use a single flat light background that is easy to remove. Do not include a room, wall, floor, cast shadow, title area, logo area, or decorative frame. Main subject: 悩む男女（40〜50代）、段ボールや古い家具、エプロンや制服を着た業者スタッフ、明るい光. Purpose: 記事の顔として「一人っ子が抱える孤独なプレッシャー」と「プロに頼る解決策」を直感的に伝える. Tone: 日本の実家らしさ、読者が状況を想像しやすい生活感、明るく清潔、不安を煽らない、買取業者っぽくしすぎない、捨てるより確認する・分けるを見せる. Must avoid: no text, no letters, no numbers, no Japanese characters, no English words, no labels, no logo, no watermark, no signage, no speech bubbles. Also avoid: 画像内へのテキスト（文字）の生成、背景の描画、過度なホラーテイスト. Do not reuse the composition, character placement, object placement, or background concept from any existing Seiribu article image.

#### ローカル合成

- 合成スクリプト: `seiribu-editorial/scripts/compose_eyecatch.py`
- タイトル: 一人っ子の実家の片付けはどう進める？親との話し合いと準備（※画像内には生成せず合成時に追加）
- サブタイトル: 100%の負担を抱え込まないためのプロ活用術（※同上）
- 出力サイズ: 1200 x 630
- 出力ファイル: `only-child-eyecatch-branded.png`
- ロゴ: `seiribu-editorial/assets/images/brand/seiribu-logo.png`
- ロゴ必須: はい
- ロゴ位置: 左上
- ロゴ配置ルール: 生成AI素材にはロゴを描かせない。標準ではPillowのローカル合成で、完成版にはセイリ部ロゴを必ず小さなブランド署名として配置する。
- Canvaの扱い: 任意の手動微調整。Canva API連携を本番前提にしない。

#### Canva任意微調整

- 状態: optional_manual
- テンプレートURL: https://canva.link/mqlqak3adj01g1i
- タイトル: 一人っ子の実家の片付けはどう進める？親との話し合いと準備（※画像内には生成せず合成時に追加）
- サブタイトル: 100%の負担を抱え込まないためのプロ活用術（※同上）
- ロゴ: `seiribu-editorial/assets/images/brand/seiribu-logo.png`
- ロゴ必須: はい
- ロゴ位置: 左上
- ロゴ配置ルール: 生成AI素材にはロゴを描かせない。標準ではPillowのローカル合成で、完成版にはセイリ部ロゴを必ず小さなブランド署名として配置する。
- 見出しフォント: UDモトヤアポロ 太字
- サブタイトルフォント: Noto Sans JP Regular

### 2. 記事内イメージ

- ファイル名: `only-child-inline-psychology.png`
- WordPress画像タイトル: 一人で実家の片付けの負担を抱え込む一人っ子のイメージ
- ALT: 一人で実家の片付けの負担を抱え込む一人っ子のイメージ
- 最終サイズ: 1200 x 800
- 生成時の比率: 3:2
- 制作方法: 画像生成素材
- 設置位置: 本文中のCMSブリーフ位置
- キャプション候補: なし

#### 制作意図

- 目的: 一人っ子が抱える孤独感とプレッシャーを視覚的に伝える
- 読者に伝えたい感情: 「私だけじゃないんだ」という共感
- 入れたい要素: 山積みの段ボールや古い家具に囲まれた部屋の中央で、ため息をつきながら一人で立ち尽くす人物のイラスト
- 避けたい表現: 画像内へのテキスト（文字）の生成、ホラーテイスト

#### 生成プロンプト / レイアウト仕様

Create a warm text-free editorial illustration for the Seiribu article '一人っ子の実家の片付けはどう進める？親との話し合いと準備'. Aspect ratio: 3:2. Style: warm flat editorial illustration, high-quality 2D vector art, soft shapes, minimal or no outlines, gentle natural colors, contemporary Japanese everyday home, clean but lived-in. Main visual: 山積みの段ボールや古い家具に囲まれた部屋の中央で、ため息をつきながら一人で立ち尽くす人物のイラスト. Purpose: 一人っ子が抱える孤独感とプレッシャーを視覚的に伝える. Tone: 日本の実家らしさ、読者が状況を想像しやすい生活感、明るく清潔、不安を煽らない、買取業者っぽくしすぎない、捨てるより確認する・分けるを見せる. Must avoid: no text, no letters, no numbers, no Japanese characters, no English words, no labels, no logo, no watermark, no signage, no speech bubbles. Also avoid: 画像内へのテキスト（文字）の生成、ホラーテイスト.

### 3. 記事内イメージ

- ファイル名: `only-child-conflict-trap.png`
- WordPress画像タイトル: 片付けを巡って親と1対1で対立してしまう一人っ子のイメージ
- ALT: 片付けを巡って親と1対1で対立してしまう一人っ子のイメージ
- 最終サイズ: 1200 x 800
- 生成時の比率: 3:2
- 制作方法: 画像生成素材
- 設置位置: 本文中のCMSブリーフ位置
- キャプション候補: なし

#### 制作意図

- 目的: 「親を説得しようとして反発される罠」を視覚的に伝える
- 読者に伝えたい感情: あるある感、これやっちゃダメなんだという気づき
- 入れたい要素: 実家で言い争うように向き合う親（不満顔）と子（困り顔）、その間にある古い不用品
- 避けたい表現: 激しい怒りや暴力を連想させる過度なホラーテイスト、文字の生成

#### 生成プロンプト / レイアウト仕様

Create a warm text-free editorial illustration for the Seiribu article '一人っ子の実家の片付けはどう進める？親との話し合いと準備'. Aspect ratio: 3:2. Style: warm flat editorial illustration, high-quality 2D vector art, soft shapes, minimal or no outlines, gentle natural colors, contemporary Japanese everyday home, clean but lived-in. Main visual: 実家で言い争うように向き合う親（不満顔）と子（困り顔）、その間にある古い不用品. Purpose: 「親を説得しようとして反発される罠」を視覚的に伝える. Tone: 日本の実家らしさ、読者が状況を想像しやすい生活感、明るく清潔、不安を煽らない、買取業者っぽくしすぎない、捨てるより確認する・分けるを見せる. Must avoid: no text, no letters, no numbers, no Japanese characters, no English words, no labels, no logo, no watermark, no signage, no speech bubbles. Also avoid: 激しい怒りや暴力を連想させる過度なホラーテイスト、文字の生成.

### 4. 記事内図解

- ファイル名: `only-child-two-professionals.png`
- WordPress画像タイトル: 一人っ子が味方につけるべき2種類のプロ
- ALT: 一人っ子が味方につけるべき2種類のプロ（出張買取業者と不用品回収業者）
- 最終サイズ: 1200 x 800
- 生成時の比率: 3:2
- 制作方法: Pillow、SVG、または任意のCanva手動微調整など、文字とレイアウトを制御できる方法で作る
- 設置位置: 本文中のCMSブリーフ位置
- キャプション候補: なし

#### 制作意図

- 目的: 「価値を判定する買取業者」と「ゴミを一掃する回収業者」の役割の違いを明確にする
- 読者に伝えたい感情: 未指定
- 入れたい要素: 左側に「出張買取業者（価値を査定する）」、右側に「不用品回収業者（一気に搬出する）」の2軸
- 避けたい表現: 未指定

#### 生成プロンプト / レイアウト仕様

画像生成AIには渡さない。Canva、Pillow、SVGなど、文字とレイアウトを制御できる方法で記事内図解を制作する。最終サイズ: 1200 x 800。アスペクト比: 3:2。入れる内容: 左側に「出張買取業者（価値を査定する）」、右側に「不用品回収業者（一気に搬出する）」の2軸。目的: 「価値を判定する買取業者」と「ゴミを一掃する回収業者」の役割の違いを明確にする。避ける表現: ゴミ屋敷のような汚さ、暗い遺品整理の雰囲気、札束や高額査定の強調、不用品回収業者だけを推す広告感、既存記事と同じ構図や素材の使い回し、ミニマリスト風の真っ白な部屋、ロゴが見出し・人物の顔・重要な品物を邪魔する配置。日本語ラベル、表、矢印、比較軸は後工程で正確に配置する。ロゴは右下などの余白に小さく配置し、本文ラベルを邪魔しない。

### 5. 記事内図解

- ファイル名: `only-child-3steps-flow.png`
- WordPress画像タイトル: 買取の利益で回収費用を相殺する実家の片付け3ステップ
- ALT: 買取の利益で回収費用を相殺する実家の片付け3ステップ
- 最終サイズ: 1200 x 800
- 生成時の比率: 3:2
- 制作方法: Pillow、SVG、または任意のCanva手動微調整など、文字とレイアウトを制御できる方法で作る
- 設置位置: 本文中のCMSブリーフ位置
- キャプション候補: なし

#### 制作意図

- 目的: 買取の利益で回収費用を相殺する「片付け3ステップ」の全体像を直感的に理解させる
- 読者に伝えたい感情: 未指定
- 入れたい要素: 1.重要書類の確保 → 2.出張買取（軍資金ゲット） → 3.不用品回収（相殺して安く処分）の流れ
- 避けたい表現: 未指定

#### 生成プロンプト / レイアウト仕様

画像生成AIには渡さない。Canva、Pillow、SVGなど、文字とレイアウトを制御できる方法で記事内図解を制作する。最終サイズ: 1200 x 800。アスペクト比: 3:2。入れる内容: 1.重要書類の確保 → 2.出張買取（軍資金ゲット） → 3.不用品回収（相殺して安く処分）の流れ。目的: 買取の利益で回収費用を相殺する「片付け3ステップ」の全体像を直感的に理解させる。避ける表現: ゴミ屋敷のような汚さ、暗い遺品整理の雰囲気、札束や高額査定の強調、不用品回収業者だけを推す広告感、既存記事と同じ構図や素材の使い回し、ミニマリスト風の真っ白な部屋、ロゴが見出し・人物の顔・重要な品物を邪魔する配置。日本語ラベル、表、矢印、比較軸は後工程で正確に配置する。ロゴは右下などの余白に小さく配置し、本文ラベルを邪魔しない。

## 品質チェック

- ローカル合成で仕上げるためのアイキャッチ素材指定を利用しています。
- 本文画像が多めです。公開時は重要な2〜3枚に絞ることも検討してください。
- 画像生成AIに文字、日本語ラベル、ロゴ、透かし、看板を描かせない。
- 日本語ラベルがある図解は、画像生成AIに文字を任せずレイアウト生成で作る。
- ロゴとタイトルは標準ではローカル合成（Pillow）、必要に応じてSVGやCanvaの手動微調整で配置する。
- アイキャッチ完成版と本文図解完成版では、セイリ部ロゴを必ず小さなブランド署名として配置する。
- 暗い遺品整理、ゴミ屋敷、高額査定広告の印象を避ける。
