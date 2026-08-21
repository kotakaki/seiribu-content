# 画像制作プラン: 実家の片付けはどこから？売る・残す・処分の順番と揉めない進め方

## 記事情報

- 記事ファイル: `drafts/pillars/home-cleanout-clean.md`
- スラッグ: `home-cleanout`
- メインKW: 実家片付け どこから
- 出力モード: standard（記事内のCMS画像指定をすべて展開する標準モード。アイキャッチ素材1件と本文画像・図解4件を基本にする）
- アイキャッチ仕上げ: Canva手動仕上げ
- Canvaテンプレ: https://canva.link/mqlqak3adj01g1i（任意・手動微調整）
- ロゴ: `seiribu-editorial/assets/images/brand/seiribu-logo.png`
- ロゴ必須対象: アイキャッチ完成版, Canva仕上げ画像, 本文画像, 本文図解
- 本文画像のロゴ: 本文画像・本文図解はブランド帰属表示としてロゴ必須。背景が薄い場合は透過ロゴ、濃い・複雑な場合は薄い白背景付きロゴを、上部または下部の余白に小さく配置する。
- 画像生成ツール: imagegen
- 図解レイアウトツール: imagegen complete illustrated infographic with model-native short Japanese text + logo overlay
- 生成候補の一時置き場: `/private/tmp/seiribu-image-work/home-cleanout`
- 採用画像の公開用置き場: `seiribu-editorial/assets/images/home-cleanout`
- 画像掃除スクリプト: `seiribu-editorial/scripts/clean_image_assets.py`

## 判定サマリー

| No | 用途 | 制作方法 | 最終サイズ | 生成時の比率 | ファイル名 | 設置位置 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | アイキャッチ素材 | 画像生成素材 + Canva手動仕上げ | 1200 x 675 | 16:9 | `home-cleanout-eyecatch-cutout.png` | H1直下 |
| 2 | 記事内図解_slide | 画像生成素材 + ブランド帰属ロゴ合成 | 1200 x 675 | 16:9 | `home-cleanout-inline-steps.png` | H2「実家の片付けはどこから始める？効率的な順番」の直下 |
| 3 | 記事内図解_slide | 画像生成素材 + ブランド帰属ロゴ合成 | 1200 x 675 | 16:9 | `home-cleanout-inline-three-boxes.png` | H3「ステップ4」内の解説直下 |
| 4 | 記事内図解_scene | 画像生成素材 + ブランド帰属ロゴ合成 | 1200 x 675 | 16:9 | `home-cleanout-inline-principles.png` | H2「実家の片付けで挫折しないための3つの鉄則」の直下 |
| 5 | 記事内イメージ | 画像生成素材 + ブランド帰属ロゴ合成 | 1200 x 675 | 16:9 | `home-cleanout-inline-ng-ok.png` | H2「仕分けた荷物はどうする？」の直下 |

## 制作ブリーフ

### 1. アイキャッチ素材

- ファイル名: `home-cleanout-eyecatch-cutout.png`
- WordPress画像タイトル: 実家の片付けはどこから始めるか
- ALT: 実家の片付けはどこから始めるか
- 最終サイズ: 1200 x 675
- 生成時の比率: 16:9
- 制作方法: 画像生成素材 + Canva手動仕上げ
- 設置位置: H1直下
- キャプション候補: なし

#### 制作意図

- 目的: 記事の第一印象。実家の片付けに悩む読者が「これなら自分にもできそう」と安心感を持てるようにする
- 読者に伝えたい感情: 安心感、解決への期待感
- 入れたい要素: 実家の和室やリビング、いくつかの段ボール箱、片付けをしている親子（温かみのある後ろ姿や手元など）
- 避けたい表現: 暗い遺品整理感、ゴミ屋敷感、疲労困憊している様子

#### 生成プロンプト / レイアウト仕様

Create an eyecatch cutout asset for the Seiribu article '実家の片付けはどこから？売る・残す・処分の順番と揉めない進め方'. Aspect ratio: 16:9. Style: warm flat editorial illustration cutout, high-quality 2D vector art, single coherent subject, clean silhouette, easy to remove background. Transparent background if possible; if transparency is not available, use a single flat light background that is easy to remove. Do not include a room, wall, floor, cast shadow, title area, logo area, or decorative frame. Main subject: 実家の和室やリビング、いくつかの段ボール箱、片付けをしている親子（温かみのある後ろ姿や手元など）. Purpose: 記事の第一印象。実家の片付けに悩む読者が「これなら自分にもできそう」と安心感を持てるようにする. Tone: 日本の実家らしさ、読者が状況を想像しやすい生活感、明るく清潔、不安を煽らない、買取業者っぽくしすぎない、捨てるより確認する・分けるを見せる. Must avoid: no text, no letters, no numbers, no Japanese characters, no English words, no labels, no logo, no watermark, no signage, no speech bubbles. Also avoid: 暗い遺品整理感、ゴミ屋敷感、疲労困憊している様子. Do not reuse the composition, character placement, object placement, or background concept from any existing Seiribu article image.

#### アイキャッチCanva仕上げ

- 仕上げ方法: Canva手動仕上げ
- タイトル: 実家の片付けはどこから？
- サブタイトル: 売る・残す・処分の順番と揉めない進め方
- 出力サイズ: 1200 x 675
- 出力ファイル: `home-cleanout-eyecatch-branded.png`
- ロゴ: `seiribu-editorial/assets/images/brand/seiribu-logo.png`
- ロゴ必須: はい
- ロゴ位置: 左上
- ロゴ配置ルール: 生成AI素材にはロゴを描かせない。アイキャッチ完成版はCanvaで人間が仕上げる。本文画像・本文図解はCodex側でブランド帰属ロゴを必ず合成する。背景が薄い場合は透過ロゴ、濃い・複雑な場合は薄い白背景付きロゴを使い、人物の顔、重要な品物、図解ラベルを邪魔しない余白に配置する。
- Canvaの扱い: アイキャッチ完成版はCanvaで人間がタイトル、サブタイトル、ロゴ、Canva専用フォントを手動合成する。

#### Canva仕上げ

- 状態: optional_manual
- テンプレートURL: https://canva.link/mqlqak3adj01g1i
- タイトル: 実家の片付けはどこから？
- サブタイトル: 売る・残す・処分の順番と揉めない進め方
- ロゴ: `seiribu-editorial/assets/images/brand/seiribu-logo.png`
- ロゴ必須: はい
- ロゴ位置: 左上
- ロゴ配置ルール: 生成AI素材にはロゴを描かせない。アイキャッチ完成版はCanvaで人間が仕上げる。本文画像・本文図解はCodex側でブランド帰属ロゴを必ず合成する。背景が薄い場合は透過ロゴ、濃い・複雑な場合は薄い白背景付きロゴを使い、人物の顔、重要な品物、図解ラベルを邪魔しない余白に配置する。
- 見出しフォント: UDモトヤアポロ 太字
- サブタイトルフォント: Noto Sans JP Regular

### 2. 記事内図解_slide

- ファイル名: `home-cleanout-inline-steps.png`
- WordPress画像タイトル: 実家の片付けを効率よく進める4つのステップ
- ALT: 実家の片付けを効率よく進める（どこから始めるか）4つのステップ
- 最終サイズ: 1200 x 675
- 生成時の比率: 16:9
- 制作方法: 画像生成素材 + ブランド帰属ロゴ合成
- 設置位置: H2「実家の片付けはどこから始める？効率的な順番」の直下
- キャプション候補: 判断に迷わない小さな場所から始めて、成功体験を積みましょう

#### 制作意図

- 目的: 片付けのハードルを下げ、簡単な場所から始めればよいことを視覚的に伝える
- 読者に伝えたい感情: 安心感、前向きな気持ち
- 入れたい要素: 「1. 自分の物・ゴミ」→「2. 玄関・洗面所」→「3. リビング・台所」→「4. 収納・趣味品」の横型フロー。各ステップに小さなアイコン
- 避けたい表現: 作業の辛さを連想させるような暗い色合い、複雑すぎる図形

#### 生成プロンプト / レイアウト仕様

Create a simple 16:9 Japanese slide-style infographic.

Style:
simple slide-style flat 2D vector infographic, icon-based diagram, clean presentation slide, light cream background, rounded cards, simple arrows, large readable Japanese labels, limited warm colors, minimal icon-like people only if necessary, no photorealism, no realistic lighting, no camera perspective, no detailed room scene

Important:
This must look like a simple slide diagram, not a photo, not a realistic scene, not watercolor, not manga, not a full room illustration. Use minimal icon-like people only if needed. No realistic lighting, no camera perspective, no detailed faces.

Content:
片付けのハードルを下げ、簡単な場所から始めればよいことを視覚的に伝える

Layout:
Clean presentation layout with cards and arrows.

Use only these Japanese labels:
「1. 自分の物・ゴミ」→「2. 玄関・洗面所」→「3. リビング・台所」→「4. 収納・趣味品」の横型フロー。各ステップに小さなアイコン

Avoid:
no extra text, no garbled Japanese, no logo, no watermark, no speech bubbles, no money unless explicitly required, no truck unless explicitly required, no sales scene, no logo, no watermark, no signage, no speech bubbles, no garbled Japanese, no random extra labels, no font specification. 作業の辛さを連想させるような暗い色合い、複雑すぎる図形.
Leave a quiet corner for a small Seiribu brand logo overlay.

#### ブランド帰属ロゴ

- ロゴ必須: はい
- ロゴ: `seiribu-editorial/assets/images/brand/seiribu-logo.png`
- 表示モード: auto
- 透過ロゴ: 背景が薄く、ロゴが十分に読める場合
- 白背景付きロゴ: 背景が濃い、複雑、またはロゴが沈む場合
- 配置候補: 左上, 右上, 右下, 左下
- 配置ルール: 人物の顔、重要な品物、図解ラベル、キャプションを邪魔しない上部または下部の余白に小さく配置する。
- 理由: Google画像検索、Pinterest、無断転載先で画像が単体流通したときのブランド帰属表示。

### 3. 記事内図解_slide

- ファイル名: `home-cleanout-inline-three-boxes.png`
- WordPress画像タイトル: 実家の荷物を「売れる物」「家族に確認」「処分」の3箱に仕分けるイメージ図
- ALT: 実家の荷物を「売れる物」「家族に確認」「処分」の3箱に仕分けるイメージ図
- 最終サイズ: 1200 x 675
- 生成時の比率: 16:9
- 制作方法: 画像生成素材 + ブランド帰属ロゴ合成
- 設置位置: H3「ステップ4」内の解説直下
- キャプション候補: 「捨てる・捨てない」で迷ったら、まずはこの3つの箱に分けてみましょう

#### 制作意図

- 目的: 実家の荷物をシンプルに3箱に分類すればよいと伝えること
- 読者に伝えたい感情: 納得感、作業のシンプルさへの安堵
- 入れたい要素: 3つの段ボール箱（緑・黄・グレーなどで色分け）。「売れる物」「家族に確認」「処分」のラベル。それぞれの箱の上に代表的な品物アイコン
- 避けたい表現: 乱雑にゴミが詰め込まれたような不潔な表現

#### 生成プロンプト / レイアウト仕様

Create a simple 16:9 Japanese slide-style infographic.

Style:
simple slide-style flat 2D vector infographic, icon-based diagram, clean presentation slide, light cream background, rounded cards, simple arrows, large readable Japanese labels, limited warm colors, minimal icon-like people only if necessary, no photorealism, no realistic lighting, no camera perspective, no detailed room scene

Important:
This must look like a simple slide diagram, not a photo, not a realistic scene, not watercolor, not manga, not a full room illustration. Use minimal icon-like people only if needed. No realistic lighting, no camera perspective, no detailed faces.

Content:
実家の荷物をシンプルに3箱に分類すればよいと伝えること

Layout:
Clean presentation layout with cards and arrows.

Use only these Japanese labels:
3つの段ボール箱（緑・黄・グレーなどで色分け）。「売れる物」「家族に確認」「処分」のラベル。それぞれの箱の上に代表的な品物アイコン

Avoid:
no extra text, no garbled Japanese, no logo, no watermark, no speech bubbles, no money unless explicitly required, no truck unless explicitly required, no sales scene, no logo, no watermark, no signage, no speech bubbles, no garbled Japanese, no random extra labels, no font specification. 乱雑にゴミが詰め込まれたような不潔な表現.
Leave a quiet corner for a small Seiribu brand logo overlay.

#### ブランド帰属ロゴ

- ロゴ必須: はい
- ロゴ: `seiribu-editorial/assets/images/brand/seiribu-logo.png`
- 表示モード: auto
- 透過ロゴ: 背景が薄く、ロゴが十分に読める場合
- 白背景付きロゴ: 背景が濃い、複雑、またはロゴが沈む場合
- 配置候補: 左上, 右上, 右下, 左下
- 配置ルール: 人物の顔、重要な品物、図解ラベル、キャプションを邪魔しない上部または下部の余白に小さく配置する。
- 理由: Google画像検索、Pinterest、無断転載先で画像が単体流通したときのブランド帰属表示。

### 4. 記事内図解_scene

- ファイル名: `home-cleanout-inline-principles.png`
- WordPress画像タイトル: 実家の片付けを失敗しないための3つの鉄則
- ALT: 実家の片付けを失敗しないための3つの鉄則
- 最終サイズ: 1200 x 675
- 生成時の比率: 16:9
- 制作方法: 画像生成素材 + ブランド帰属ロゴ合成
- 設置位置: H2「実家の片付けで挫折しないための3つの鉄則」の直下
- キャプション候補: この3つを最初に家族で共有するだけで、片付けはスムーズに進みます

#### 制作意図

- 目的: 読者に「この3つの鉄則さえ守れば失敗しない」と安心感を持たせること
- 読者に伝えたい感情: 安心感、家族と向き合う覚悟
- 入れたい要素: 「1.勝手に捨てない」「2.一人で抱え込まない」「3.売る・残す・処分で仕分ける」の3つの原則と、温かみのあるシンプルなアイコン（握手、複数人の家族、3つの箱など）
- 避けたい表現: 禁止マーク（❌）など、読者を過度に萎縮させる表現

#### 生成プロンプト / レイアウト仕様

Create an illustrated infographic diagram for a Seiribu article. Aspect ratio: 16:9. Style: high-quality editorial illustration diagram with simple scene panels, utilizing varied art styles (e.g., flat vector, watercolor, pastel, modern line art) to avoid visual repetition, soft colors, no photorealism, no realistic lighting, no camera perspective. Content to show as a structured infographic diagram: 「1.勝手に捨てない」「2.一人で抱え込まない」「3.売る・残す・処分で仕分ける」の3つの原則と、温かみのあるシンプルなアイコン（握手、複数人の家族、3つの箱など）. Layout: Use a clean, solid background (e.g., white or light beige). Structure the information using bordered boxes for each step and connecting arrows. Do NOT create full-bleed comic panels or edge-to-edge full-screen scenes. Keep ample negative space. It is perfectly fine to use spot illustrations of characters and items inside the diagram boxes. Do not create empty placeholder boxes, dotted rectangles, blank logo slots, or unused label cards. Render only the short Japanese labels explicitly implied by the brief, naturally, as part of the generated infographic. Do not specify a font; let the image model choose a clean natural label style. Purpose: 読者に「この3つの鉄則さえ守れば失敗しない」と安心感を持たせること. Must avoid: no logo, no watermark, no signage, no speech bubbles, no garbled Japanese, no random extra labels, no font specification. Also avoid: 禁止マーク（❌）など、読者を過度に萎縮させる表現. Do not create full-screen immersive scenes or manga layouts. Do not create abstract line art only. Leave quiet margin space for a small Seiribu brand logo overlay. ロゴ: 本文画像・本文図解はブランド帰属表示としてロゴ必須。背景が薄い場合は透過ロゴ、濃い・複雑な場合は薄い白背景付きロゴを、上部または下部の余白に小さく配置する。

#### ブランド帰属ロゴ

- ロゴ必須: はい
- ロゴ: `seiribu-editorial/assets/images/brand/seiribu-logo.png`
- 表示モード: auto
- 透過ロゴ: 背景が薄く、ロゴが十分に読める場合
- 白背景付きロゴ: 背景が濃い、複雑、またはロゴが沈む場合
- 配置候補: 左上, 右上, 右下, 左下
- 配置ルール: 人物の顔、重要な品物、図解ラベル、キャプションを邪魔しない上部または下部の余白に小さく配置する。
- 理由: Google画像検索、Pinterest、無断転載先で画像が単体流通したときのブランド帰属表示。

### 5. 記事内イメージ

- ファイル名: `home-cleanout-inline-ng-ok.png`
- WordPress画像タイトル: 仕分けた荷物の次のアクション
- ALT: 仕分けた荷物の次のアクション（売る・保留・処分）
- 最終サイズ: 1200 x 675
- 生成時の比率: 16:9
- 制作方法: 画像生成素材 + ブランド帰属ロゴ合成
- 設置位置: H2「仕分けた荷物はどうする？」の直下
- キャプション候補: 仕分けが終われば、あとはそれぞれの出口に任せるだけです

#### 制作意図

- 目的: 仕分けた後の「売る」「残す」「処分」の次の行動が明確であることを視覚的に伝える
- 読者に伝えたい感情: 安心感、道筋が見えた納得感
- 入れたい要素: 「査定に出す（カメラや古い本）」「保留箱（段ボール）」「不用品回収（ゴミ袋や粗大ゴミ）」の3つの出口を示すイラスト
- 避けたい表現: 高額な札束（現金）の過度な強調、悪徳業者を連想させる表現

#### 生成プロンプト / レイアウト仕様

Create a warm text-free editorial illustration for the Seiribu article '実家の片付けはどこから？売る・残す・処分の順番と揉めない進め方'. Aspect ratio: 16:9. Style: high-quality Japanese editorial illustration, utilizing varied art styles (e.g., soft watercolor, modern flat vector, pastel, clean line art) to avoid visual repetition, soft natural colors, realistic household objects, contemporary Japanese everyday home, clean but lived-in. Main visual: 「査定に出す（カメラや古い本）」「保留箱（段ボール）」「不用品回収（ゴミ袋や粗大ゴミ）」の3つの出口を示すイラスト. Purpose: 仕分けた後の「売る」「残す」「処分」の次の行動が明確であることを視覚的に伝える. Tone: 日本の実家らしさ、読者が状況を想像しやすい生活感、明るく清潔、不安を煽らない、買取業者っぽくしすぎない、捨てるより確認する・分けるを見せる. Must avoid: no text, no letters, no numbers, no Japanese characters, no English words, no labels, no logo, no watermark, no signage, no speech bubbles. Also avoid: 高額な札束（現金）の過度な強調、悪徳業者を連想させる表現.

#### ブランド帰属ロゴ

- ロゴ必須: はい
- ロゴ: `seiribu-editorial/assets/images/brand/seiribu-logo.png`
- 表示モード: auto
- 透過ロゴ: 背景が薄く、ロゴが十分に読める場合
- 白背景付きロゴ: 背景が濃い、複雑、またはロゴが沈む場合
- 配置候補: 左上, 右上, 右下, 左下
- 配置ルール: 人物の顔、重要な品物、図解ラベル、キャプションを邪魔しない上部または下部の余白に小さく配置する。
- 理由: Google画像検索、Pinterest、無断転載先で画像が単体流通したときのブランド帰属表示。

## 品質チェック

- Canvaで仕上げるためのアイキャッチ素材指定を利用しています。
- 本文画像・図解は4枚構成です。記事内の全CMSブリーフを標準制作対象にします。
- 画像生成AIに文字、日本語ラベル、ロゴ、透かし、看板を描かせない。
- 日本語ラベルがある図解は、画像生成AIに文字を任せずレイアウト生成で作る。
- 図解は抽象的な線や図形だけにせず、サンプルのような人物・品物・実家の場面を含むイラスト図解ベースで作る。
- アイキャッチのロゴとタイトルはCanvaで人間が最終合成する。
- ロゴ必須対象: アイキャッチ完成版, Canva仕上げ画像, 本文画像, 本文図解。
- 本文画像・本文図解のロゴ: 本文画像・本文図解はブランド帰属表示としてロゴ必須。背景が薄い場合は透過ロゴ、濃い・複雑な場合は薄い白背景付きロゴを、上部または下部の余白に小さく配置する。
- 暗い遺品整理、ゴミ屋敷、高額査定広告の印象を避ける。
- imagegenの生成候補は `/private/tmp/seiribu-image-work/home-cleanout` に置き、採用画像だけ `seiribu-editorial/assets/images/home-cleanout` に移す。
- 公開用フォルダに残った候補や旧版は `seiribu-editorial/scripts/clean_image_assets.py --article home-cleanout --dry-run` で確認してから退避する。
