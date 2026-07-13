# 画像制作プラン: avoid-trouble（訪問買取トラブル・クーリングオフ）

`image-engine.md` の最新ルール（`--mode light`、アスペクト比 16:9）に基づき、画像制作プランを最新版として再構築しました。
初回は「アイキャッチ用素材」と「H2-2直下の情景イラスト」の2点を生成対象としています。

## 1. アイキャッチ用素材 - [生成対象]
- **仕様**: `1200 x 675` / `16:9` / 文字なし・背景イラストのみ
- **目的**: 実家の親を悪質業者から守るという「防衛・安心感」を伝える
- **画像生成用プロンプト (Prompt)**:
  `A high-quality flat vector illustration of a modern Japanese house entrance. An elderly Japanese couple is safely inside, closing their front door securely against a shadowy, suspicious salesperson figure outside. A glowing shield motif is subtly incorporated to convey safety and defense. Clean and modern flat art style, soft and reassuring colors, no text, no letters, no logos. Aspect ratio 16:9.`
- **NG表現**: 文字の混入、過度に恐怖を煽るホラー調（血やドクロ等）、ロゴの混入
- **後工程**: 生成後、`seiribu-editorial/scripts/compose_eyecatch.py` 等を用いて見出し文字（実家の親を守る！訪問買取トラブル対策）とサブタイトル（押し買いの手口とクーリングオフ）、セイリ部ロゴをローカル合成します。

## 2. 記事内イメージ: 業者に強く言われて困惑する高齢者 - [生成対象]
- **配置先**: 第2H2（親世代の心理）直下
- **仕様**: `1200 x 675` / `16:9` / 文字なし
- **画像生成用プロンプト (Prompt)**:
  `A clean flat vector illustration of an elderly Japanese person looking anxious and bewildered in their living room. An aggressive salesperson in a suit is leaning forward, pressuring them. The room has some cardboard boxes and old belongings. The color palette is slightly muted to convey a sense of pressure but not overly dark or scary. Minimalist and empathetic style, no text, no logos. Aspect ratio 16:9.`
- **NG表現**: 文字の混入、高齢者を認知症のように極端に描くこと、ホラーテイスト

---

## 3. 記事内図解 1: 「押し買い」の典型的な3つの手口 - [保留 (lightモード)]
- **配置先**: 第1H2直下
- **仕様**: `1200 x 675` / `16:9` / 図解
- **状態**: `--mode light` のため今回は保留。
- **備考**: 画像生成AIで直接出力せず、PillowやSVG等を用いて「不用品と言いながら貴金属を狙う」「居座って帰らない」「契約書を渡さない」という3つのシーンをアイコンやイラストで表現・レイアウトして制作する予定です。

## 4. 記事内図解 2: クーリングオフの条件（8日間） - [保留 (lightモード)]
- **配置先**: 第3H2直下
- **仕様**: `1200 x 675` / `16:9` / 図解
- **状態**: `--mode light` のため今回は保留。
- **備考**: クーリングオフの8日間を強調するカレンダーと、対象品目・対象外品目の簡単な対比図をPillowやSVG等でレイアウトします。
