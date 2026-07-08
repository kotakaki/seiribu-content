# seiribu-editorial

セイリ部向けのコンテンツ制作エージェント用リポジトリです。

この作業場は、Codexに記事を無制限に量産させるためではなく、編集部の判断を助けるための仕組みです。企画、構成、下書き、チェック、内部リンク案までを整理し、公開前には必ず人間が確認します。

## 基本フロー

```text
Search Console CSV
  -> キーワード抽出
  -> 記事企画
  -> 構成作成
  -> 下書き作成
  -> ファクトチェック・表現チェック
  -> 内部リンク・CTA設計
  -> WordPress下書き投入
  -> 人間レビュー
  -> 公開
```

## ディレクトリ

- `data/`: Search Console、サイトマップ、アフィリエイト情報などの入力データ
- `strategy/`: サイト方針、カテゴリ、内部リンク、収益ページ、カレンダー
- `templates/`: 企画、構成、下書き、レビュー用テンプレート
- `briefs/`: 記事企画
- `drafts/`: 下書き
- `reviewed/`: 人間レビュー後の原稿
- `scripts/`: 補助スクリプト
- `reports/`: キーワード機会、重複、週次レビューなどのレポート

## まず読む戦略資料

- `strategy/zero-one-validation-plan.md`: ゼロイチ検証の方針。心理・家族の悩み系ロングテールを入口にする判断をまとめています。
- `strategy/content-production-workflow.md`: 記事制作のフェーズ停止ルール。主力記事はH2ごとに作ります。
- `strategy/categories.md`: カテゴリ、ピラー、カテゴリページnoindex方針。
- `reports/article-lineup-rewrite-plan.md`: 全記事のリライト優先順位。
- `reports/minimum-foundation-workplan.md`: 最低限の棚と記事を整える工数管理。

## 最初の使い方

1. `data/search-console/queries.csv` にSearch ConsoleのクエリCSVを置きます。
2. `strategy/site-concept.md` と `strategy/categories.md` を必要に応じて更新します。
3. `python3 scripts/score_keywords.py` でキーワード候補をレポート化します。
4. `templates/article-brief.md` を使って `briefs/` に記事企画を作ります。
5. `templates/article-draft.md` を使って `drafts/` に下書きを作ります。
6. `python3 scripts/check_article.py drafts/ファイル名.md` で禁止表現などを確認します。

## 重要ルール

- 公開は人間が行います。
- 実体験がないのに体験談として書きません。
- 根拠のない相場金額や買取保証を書きません。
- アフィリエイト誘導より、読者の判断を優先します。
