# 画像制作プラン: 不用品回収と買取の違い｜実家の片付けではどちらを先に使う？

## 記事情報

- 記事ファイル: `drafts/buying-or-collecting.md`
- スラッグ: `buying-or-collecting`
- メインKW: 不用品回収 買取 違い
- 出力モード: standard（記事内のCMS画像指定をすべて展開する標準モード。アイキャッチ素材1件と本文画像・図解4件を基本にする）
- アイキャッチ仕上げ: Canva手動仕上げ
- Canvaテンプレ: https://canva.link/mqlqak3adj01g1i（任意・手動微調整）
- ロゴ: `seiribu-editorial/assets/images/brand/seiribu-logo.png`
- ロゴ必須対象: アイキャッチ完成版, Canva仕上げ画像, 本文画像, 本文図解
- 本文画像のロゴ: 本文画像・本文図解はブランド帰属表示としてロゴ必須。背景が薄い場合は透過ロゴ、濃い・複雑な場合は薄い白背景付きロゴを、上部または下部の余白に小さく配置する。
- 画像生成ツール: imagegen
- 図解レイアウトツール: imagegen illustration base + Pillow / SVG / Canva label and logo overlay
- 生成候補の一時置き場: `/private/tmp/seiribu-image-work/buying-or-collecting`
- 採用画像の公開用置き場: `seiribu-editorial/assets/images/buying-or-collecting`
- 画像掃除スクリプト: `seiribu-editorial/scripts/clean_image_assets.py`

## 判定サマリー

| No | 用途 | 制作方法 | 最終サイズ | 生成時の比率 | ファイル名 | 設置位置 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | アイキャッチ素材 | 画像生成素材 + Canva手動仕上げ | 1200 x 675 | 16:9 | `buying-or-collecting-eyecatch.png` | アイキャッチ合成用素材 |
| 2 | 記事内図解 | 画像生成でサンプルのようなイラスト図解ベースを作り、Pillow、SVG、またはCanvaで短いラベルとロゴを正確に合成する | 1200 x 675 | 16:9 | `buying-or-collecting-inline-flow.png` | 本文中のCMSブリーフ位置 |
| 3 | 写真風素材 | 写真風生成素材 | 1200 x 675 | 16:9 | `buying-or-collecting-photo.png` | 本文中のCMSブリーフ位置 |
| 4 | 記事内イメージ | 画像生成素材 + ブランド帰属ロゴ合成 | 1200 x 675 | 16:9 | `buying-or-collecting-inline-three-boxes.png` | 本文中のCMSブリーフ位置 |
| 5 | 記事内図解 | 画像生成でサンプルのようなイラスト図解ベースを作り、Pillow、SVG、またはCanvaで短いラベルとロゴを正確に合成する | 1200 x 675 | 16:9 | `buying-or-collecting-inline-steps.png` | 本文中のCMSブリーフ位置 |

## 制作ブリーフ

### 1. アイキャッチ素材

- ファイル名: `buying-or-collecting-eyecatch.png`
- WordPress画像タイトル: 不用品回収と買取の違いと実家の片付けでの基本の順番を示すイラスト
- ALT: 不用品回収と買取の違いと実家の片付けでの基本の順番を示すイラスト
- 最終サイズ: 1200 x 675
- 生成時の比率: 16:9
- 制作方法: 画像生成素材 + Canva手動仕上げ
- 設置位置: アイキャッチ合成用素材
- キャプション候補: なし

#### 制作意図

- 目的: 不用品回収と買取の違い、基本の順番を視覚的に伝える
- 読者に伝えたい感情: 順番を決めればスムーズに進み、見落としを減らせるという安心感
- 入れたい要素: 古いカメラや着物を査定する様子（買取）、段ボールや古い家具を運ぶ様子（回収）
- 避けたい表現: 画像内へのテキスト（文字）の生成（※情景イラストのため）、複雑すぎる背景

#### 生成プロンプト / レイアウト仕様

Create an eyecatch cutout asset for the Seiribu article '不用品回収と買取の違い｜実家の片付けではどちらを先に使う？'. Aspect ratio: 16:9. Style: warm flat editorial illustration cutout, high-quality 2D vector art, single coherent subject, clean silhouette, easy to remove background. Transparent background if possible; if transparency is not available, use a single flat light background that is easy to remove. Do not include a room, wall, floor, cast shadow, title area, logo area, or decorative frame. Main subject: 古いカメラや着物を査定する様子（買取）、段ボールや古い家具を運ぶ様子（回収）. Purpose: 不用品回収と買取の違い、基本の順番を視覚的に伝える. Tone: 日本の実家らしさ、読者が状況を想像しやすい生活感、明るく清潔、不安を煽らない、買取業者っぽくしすぎない、捨てるより確認する・分けるを見せる. Must avoid: no text, no letters, no numbers, no Japanese characters, no English words, no labels, no logo, no watermark, no signage, no speech bubbles. Also avoid: 画像内へのテキスト（文字）の生成（※情景イラストのため）、複雑すぎる背景. Do not reuse the composition, character placement, object placement, or background concept from any existing Seiribu article image.

#### アイキャッチCanva仕上げ

- 仕上げ方法: Canva手動仕上げ
- タイトル: 不用品回収と買取の違い
- サブタイトル: 実家の片付けではどちらが先？
- 出力サイズ: 1200 x 675
- 出力ファイル: `buying-or-collecting-eyecatch-branded.png`
- ロゴ: `seiribu-editorial/assets/images/brand/seiribu-logo.png`
- ロゴ必須: はい
- ロゴ位置: 左上
- ロゴ配置ルール: 生成AI素材にはロゴを描かせない。アイキャッチ完成版はCanvaで人間が仕上げる。本文画像・本文図解はCodex側でブランド帰属ロゴを必ず合成する。背景が薄い場合は透過ロゴ、濃い・複雑な場合は薄い白背景付きロゴを使い、人物の顔、重要な品物、図解ラベルを邪魔しない余白に配置する。
- Canvaの扱い: アイキャッチ完成版はCanvaで人間がタイトル、サブタイトル、ロゴ、Canva専用フォントを手動合成する。

#### Canva仕上げ

- 状態: optional_manual
- テンプレートURL: https://canva.link/mqlqak3adj01g1i
- タイトル: 不用品回収と買取の違い
- サブタイトル: 実家の片付けではどちらが先？
- ロゴ: `seiribu-editorial/assets/images/brand/seiribu-logo.png`
- ロゴ必須: はい
- ロゴ位置: 左上
- ロゴ配置ルール: 生成AI素材にはロゴを描かせない。アイキャッチ完成版はCanvaで人間が仕上げる。本文画像・本文図解はCodex側でブランド帰属ロゴを必ず合成する。背景が薄い場合は透過ロゴ、濃い・複雑な場合は薄い白背景付きロゴを使い、人物の顔、重要な品物、図解ラベルを邪魔しない余白に配置する。
- 見出しフォント: UDモトヤアポロ 太字
- サブタイトルフォント: Noto Sans JP Regular

### 2. 記事内図解

- ファイル名: `buying-or-collecting-inline-flow.png`
- WordPress画像タイトル: 不用品回収と買取のお金の流れの違い
- ALT: 不用品回収と買取のお金の流れの違い
- 最終サイズ: 1200 x 675
- 生成時の比率: 16:9
- 制作方法: 画像生成でサンプルのようなイラスト図解ベースを作り、Pillow、SVG、またはCanvaで短いラベルとロゴを正確に合成する
- 設置位置: 本文中のCMSブリーフ位置
- キャプション候補: 不用品回収は「払う」、買取は「もらう」という正反対のサービスです。

#### 制作意図

- 目的: 不用品回収と買取のお金の流れの違い（払う vs もらう）を視覚的に整理し、お金の流れが真逆であることを納得させる
- 読者に伝えたい感情: サービスの性質が全く異なることへの理解と納得感
- 入れたい要素: 左右に分割されたシンプルな図解。左側（不用品回収）は40〜50代の子供世代が作業スタッフにお金を「支払う（払う）」矢印、右側（買取）は査定員からお金を「受け取る（もらう）」矢印を描く。
- 避けたい表現: 文字の詰め込みすぎ（短いラベルは積極的に使用する）

#### 生成プロンプト / レイアウト仕様

Create an illustrated infographic diagram for a Seiribu article. Aspect ratio: 16:9. Style: simple warm Japanese editorial infographic, light cream background, rounded bordered panels, sparse spot illustrations of people and household items, clean arrows, ample negative space, easy to scan, not full-scene manga, not abstract line art. Content to show as a structured infographic diagram: 左右に分割されたシンプルな図解。左側（不用品回収）は40〜50代の子供世代が作業スタッフにお金を「支払う（払う）」矢印、右側（買取）は査定員からお金を「受け取る（もらう）」矢印を描く。. Layout: Use a clean, solid background (e.g., white or light beige). Structure the information using bordered boxes for each step and connecting arrows. Do NOT create full-bleed comic panels or edge-to-edge full-screen scenes. Keep ample negative space. It is perfectly fine to use spot illustrations of characters and items inside the diagram boxes. Do not create empty placeholder boxes, dotted rectangles, blank logo slots, or unused label cards. Render only the short Japanese labels explicitly implied by the brief, naturally, as part of the generated infographic. Do not specify a font; let the image model choose a clean natural label style. Purpose: 不用品回収と買取のお金の流れの違い（払う vs もらう）を視覚的に整理し、お金の流れが真逆であることを納得させる. Must avoid: no logo, no watermark, no signage, no speech bubbles, no garbled Japanese, no random extra labels, no font specification. Also avoid: 文字の詰め込みすぎ（短いラベルは積極的に使用する）. Do not create full-screen immersive scenes or manga layouts. Do not create abstract line art only. Leave quiet margin space for a small Seiribu brand logo overlay. ロゴ: 本文画像・本文図解はブランド帰属表示としてロゴ必須。背景が薄い場合は透過ロゴ、濃い・複雑な場合は薄い白背景付きロゴを、上部または下部の余白に小さく配置する。

#### ブランド帰属ロゴ

- ロゴ必須: はい
- ロゴ: `seiribu-editorial/assets/images/brand/seiribu-logo.png`
- 表示モード: auto
- 透過ロゴ: 背景が薄く、ロゴが十分に読める場合
- 白背景付きロゴ: 背景が濃い、複雑、またはロゴが沈む場合
- 配置候補: 左上, 右上, 右下, 左下
- 配置ルール: 人物の顔、重要な品物、図解ラベル、キャプションを邪魔しない上部または下部の余白に小さく配置する。
- 理由: Google画像検索、Pinterest、無断転載先で画像が単体流通したときのブランド帰属表示。

### 3. 写真風素材

- ファイル名: `buying-or-collecting-photo.png`
- WordPress画像タイトル: 査定対象になる物をゴミとして処分してしまうリスク
- ALT: 査定対象になる物をゴミとして処分してしまうリスク
- 最終サイズ: 1200 x 675
- 生成時の比率: 16:9
- 制作方法: 写真風生成素材
- 設置位置: 本文中のCMSブリーフ位置
- キャプション候補: 専門知識がないと、査定対象になる物まで処分対象として扱われてしまうことも。

#### 制作意図

- 目的: 「査定対象になる物をゴミとして捨ててしまうリスク」を視覚的に伝える
- 読者に伝えたい感情: もったいない、見落としたくないという警戒心
- 入れたい要素: アンティークの時計や年代物のフィルムカメラが、無造作にゴミ袋の束と一緒に床に置かれているリアルな様子（人物は不要、物だけで状況を伝える）
- 避けたい表現: 暗すぎるゴミ屋敷感、ホラー感、広告のフリー素材感

#### 生成プロンプト / レイアウト仕様

Create a bright realistic editorial photo-style visual for the Seiribu article '不用品回収と買取の違い｜実家の片付けではどちらを先に使う？'. Aspect ratio: 16:9. Style: bright realistic editorial photo, natural daylight, clean lived-in Japanese home, not gritty, not luxury advertising, not dramatic. Main visual: アンティークの時計や年代物のフィルムカメラが、無造作にゴミ袋の束と一緒に床に置かれているリアルな様子（人物は不要、物だけで状況を伝える）. Purpose: 「査定対象になる物をゴミとして捨ててしまうリスク」を視覚的に伝える. Tone: 日本の実家らしさ、読者が状況を想像しやすい生活感、明るく清潔、不安を煽らない、買取業者っぽくしすぎない、捨てるより確認する・分けるを見せる. Must avoid: no text, no letters, no numbers, no Japanese characters, no English words, no labels, no logo, no watermark, no signage, no speech bubbles. Also avoid: 暗すぎるゴミ屋敷感、ホラー感、広告のフリー素材感.

#### ブランド帰属ロゴ

- ロゴ必須: はい
- ロゴ: `seiribu-editorial/assets/images/brand/seiribu-logo.png`
- 表示モード: auto
- 透過ロゴ: 背景が薄く、ロゴが十分に読める場合
- 白背景付きロゴ: 背景が濃い、複雑、またはロゴが沈む場合
- 配置候補: 左上, 右上, 右下, 左下
- 配置ルール: 人物の顔、重要な品物、図解ラベル、キャプションを邪魔しない上部または下部の余白に小さく配置する。
- 理由: Google画像検索、Pinterest、無断転載先で画像が単体流通したときのブランド帰属表示。

### 4. 記事内イメージ

- ファイル名: `buying-or-collecting-inline-three-boxes.png`
- WordPress画像タイトル: 売るものと捨てるものを仕分ける親子の様子
- ALT: 売るものと捨てるものを仕分ける親子の様子
- 最終サイズ: 1200 x 675
- 生成時の比率: 16:9
- 制作方法: 画像生成素材 + ブランド帰属ロゴ合成
- 設置位置: 本文中のCMSブリーフ位置
- キャプション候補: 古いから価値がないと自己判断せず、まずは査定対象になるか確認しましょう。

#### 制作意図

- 目的: 実家の片付けで親子が協力しながら「売るもの」「捨てるもの」を仕分けする温かい様子を描く
- 読者に伝えたい感情: 親と一緒に協力して整理を進められるという前向きな感情
- 入れたい要素: 70〜80代の親と、40〜50代の子供世代が並んで座り、古いアルバムやカメラ、時計などを手に取りながら、笑顔で話し合っている様子。
- 避けたい表現: 画像内へのテキスト（文字）の生成（※情景イラストのため）、散らかりすぎた暗い部屋

#### 生成プロンプト / レイアウト仕様

Create a warm text-free editorial illustration for the Seiribu article '不用品回収と買取の違い｜実家の片付けではどちらを先に使う？'. Aspect ratio: 16:9. Style: warm watercolor-like editorial illustration, high-quality Japanese picture-book style, soft natural colors, realistic household objects, contemporary Japanese everyday home, clean but lived-in. Main visual: 70〜80代の親と、40〜50代の子供世代が並んで座り、古いアルバムやカメラ、時計などを手に取りながら、笑顔で話し合っている様子。. Purpose: 実家の片付けで親子が協力しながら「売るもの」「捨てるもの」を仕分けする温かい様子を描く. Tone: 日本の実家らしさ、読者が状況を想像しやすい生活感、明るく清潔、不安を煽らない、買取業者っぽくしすぎない、捨てるより確認する・分けるを見せる. Must avoid: no text, no letters, no numbers, no Japanese characters, no English words, no labels, no logo, no watermark, no signage, no speech bubbles. Also avoid: 画像内へのテキスト（文字）の生成（※情景イラストのため）、散らかりすぎた暗い部屋.

#### ブランド帰属ロゴ

- ロゴ必須: はい
- ロゴ: `seiribu-editorial/assets/images/brand/seiribu-logo.png`
- 表示モード: auto
- 透過ロゴ: 背景が薄く、ロゴが十分に読める場合
- 白背景付きロゴ: 背景が濃い、複雑、またはロゴが沈む場合
- 配置候補: 左上, 右上, 右下, 左下
- 配置ルール: 人物の顔、重要な品物、図解ラベル、キャプションを邪魔しない上部または下部の余白に小さく配置する。
- 理由: Google画像検索、Pinterest、無断転載先で画像が単体流通したときのブランド帰属表示。

### 5. 記事内図解

- ファイル名: `buying-or-collecting-inline-steps.png`
- WordPress画像タイトル: 実家の不用品を無駄なく片付ける順番のフローチャート
- ALT: 実家の不用品を無駄なく片付ける順番のフローチャート
- 最終サイズ: 1200 x 675
- 生成時の比率: 16:9
- 制作方法: 画像生成でサンプルのようなイラスト図解ベースを作り、Pillow、SVG、またはCanvaで短いラベルとロゴを正確に合成する
- 設置位置: 本文中のCMSブリーフ位置
- キャプション候補: 残すものを分けた後、買取で価値を確認してから処分を進めると、見落としを減らしやすくなります。

#### 制作意図

- 目的: 実家の不用品整理における正しい手順（残す→売る→処分する）を視覚的なフローチャートで分かりやすく伝える
- 読者に伝えたい感情: 順番を守れば費用や手間の無駄がなくなり、安心して進められるという確信
- 入れたい要素: スッキリした背景に、枠線つきのボックスを並べたインフォグラフィック風レイアウト。Step 1:「残す」アルバムを手にする様子。Step 2:「売る」古いカメラを査定員に見せる様子。Step 3:「処分する」壊れたテレビをスタッフが運ぶ様子。各ステップが矢印でつながれている。
- 避けたい表現: 全画面に広がる漫画のようなコマ割り、複雑な背景（文字説明のラベルなどを図表内にしっかり入れるため、余白を確保する）

#### 生成プロンプト / レイアウト仕様

Create an illustrated infographic diagram for a Seiribu article. Aspect ratio: 16:9. Style: simple warm Japanese editorial infographic, light cream background, rounded bordered panels, sparse spot illustrations of people and household items, clean arrows, ample negative space, easy to scan, not full-scene manga, not abstract line art. Content to show as a structured infographic diagram: スッキリした背景に、枠線つきのボックスを並べたインフォグラフィック風レイアウト。Step 1:「残す」アルバムを手にする様子。Step 2:「売る」古いカメラを査定員に見せる様子。Step 3:「処分する」壊れたテレビをスタッフが運ぶ様子。各ステップが矢印でつながれている。. Layout: Use a clean, solid background (e.g., white or light beige). Structure the information using bordered boxes for each step and connecting arrows. Do NOT create full-bleed comic panels or edge-to-edge full-screen scenes. Keep ample negative space. It is perfectly fine to use spot illustrations of characters and items inside the diagram boxes. Do not create empty placeholder boxes, dotted rectangles, blank logo slots, or unused label cards. Render only the short Japanese labels explicitly implied by the brief, naturally, as part of the generated infographic. Do not specify a font; let the image model choose a clean natural label style. Purpose: 実家の不用品整理における正しい手順（残す→売る→処分する）を視覚的なフローチャートで分かりやすく伝える. Must avoid: no logo, no watermark, no signage, no speech bubbles, no garbled Japanese, no random extra labels, no font specification. Also avoid: 全画面に広がる漫画のようなコマ割り、複雑な背景（文字説明のラベルなどを図表内にしっかり入れるため、余白を確保する）. Do not create full-screen immersive scenes or manga layouts. Do not create abstract line art only. Leave quiet margin space for a small Seiribu brand logo overlay. ロゴ: 本文画像・本文図解はブランド帰属表示としてロゴ必須。背景が薄い場合は透過ロゴ、濃い・複雑な場合は薄い白背景付きロゴを、上部または下部の余白に小さく配置する。

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
- imagegenの生成候補は `/private/tmp/seiribu-image-work/buying-or-collecting` に置き、採用画像だけ `seiribu-editorial/assets/images/buying-or-collecting` に移す。
- 公開用フォルダに残った候補や旧版は `seiribu-editorial/scripts/clean_image_assets.py --article buying-or-collecting --dry-run` で確認してから退避する。
