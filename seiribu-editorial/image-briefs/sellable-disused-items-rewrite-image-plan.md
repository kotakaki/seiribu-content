# 画像制作プラン: 実家の片付けで売れるものは？捨てる前に整理したい品物と確認ポイント

## 記事情報

- 記事ファイル: `seiribu-editorial/drafts/pillars/sellable-disused-items-rewrite.md`
- スラッグ: `sellable-disused-items-rewrite`
- メインKW: 未設定
- 出力モード: light（初回制作をアイキャッチ系1件と本文画像1件までに絞る軽量モード）
- 標準仕上げ: ローカル合成（Pillow）
- Canvaテンプレ: https://canva.link/mqlqak3adj01g1i（任意・手動微調整）
- ロゴ: `seiribu-editorial/assets/images/brand/seiribu-logo.png`
- ロゴ必須対象: アイキャッチ完成版, Canva仕上げ画像
- 本文画像のロゴ: 本文画像・本文図解は標準ではロゴなし。明示依頼やテンプレ上のブランド表記が必要な場合だけ、後工程で小さく配置する。
- 画像生成ツール: imagegen
- 図解レイアウトツール: visualize / Pillow / SVG
- 生成候補の一時置き場: `/private/tmp/seiribu-image-work/sellable-disused-items-rewrite`
- 採用画像の公開用置き場: `seiribu-editorial/assets/images/sellable-disused-items-rewrite`
- 画像掃除スクリプト: `seiribu-editorial/scripts/clean_image_assets.py`

## 判定サマリー

| No | 用途 | 制作方法 | 最終サイズ | 生成時の比率 | ファイル名 | 設置位置 |
| --- | --- | --- | --- | --- | --- | --- |

## 制作ブリーフ

## 品質チェック

- アイキャッチまたはアイキャッチ合成用素材の指定がありません。自動補完はしません。
- 本文画像が少なめです。ピラー記事では図解をもう1枚検討してください。
- lightモードですが、保留対象はありません。
- 画像生成AIに文字、日本語ラベル、ロゴ、透かし、看板を描かせない。
- 日本語ラベルがある図解は、画像生成AIに文字を任せずレイアウト生成で作る。
- アイキャッチのロゴとタイトルは標準ではローカル合成（Pillow）、必要に応じてSVGやCanvaの手動微調整で配置する。
- ロゴ必須対象: アイキャッチ完成版, Canva仕上げ画像。
- 本文画像・本文図解のロゴ: 本文画像・本文図解は標準ではロゴなし。明示依頼やテンプレ上のブランド表記が必要な場合だけ、後工程で小さく配置する。
- 暗い遺品整理、ゴミ屋敷、高額査定広告の印象を避ける。
- imagegenの生成候補は `/private/tmp/seiribu-image-work/sellable-disused-items-rewrite` に置き、採用画像だけ `seiribu-editorial/assets/images/sellable-disused-items-rewrite` に移す。
- 公開用フォルダに残った候補や旧版は `seiribu-editorial/scripts/clean_image_assets.py --article sellable-disused-items-rewrite --dry-run` で確認してから退避する。
