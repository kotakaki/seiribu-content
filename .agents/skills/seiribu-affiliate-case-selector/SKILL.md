---
name: seiribu-affiliate-case-selector
description: "セイリ部のASP/アフィリエイト広告案件を、読者適合、成果地点、否認リスク、提携状況、記事導線で評価し、主力/条件付き主力/テスト/保留/非推奨に仕分ける。バイセル、専門買取、回収案件のCTA選定、ASP条件の照合、Notion案件台帳の更新、掲載前の案件確認で使う。"
---

# Seiribu Affiliate Case Selector

## Purpose

Use this skill to decide what a program should do inside Seiribu: main CTA, conditional comparison, limited test, hold, or non-fit. Treat affiliate data as editorial infrastructure. Reader benefit comes first; reward amount must never become a reader-facing recommendation.

The current operating baseline is [references/program-baseline-2026-08-07.md](references/program-baseline-2026-08-07.md). It is a dated default, not proof of current terms.

## Freshness And Evidence

Use this order for a publication decision:

1. Current ASP screen, terms, program detail, or downloadable conversion-target list supplied by the user.
2. Current official advertiser LP and official terms.
3. The dated program baseline and the latest Seiribu research report.
4. Notion or older working notes.

Keep two facts separate:

- An official site saying it handles an item does **not** prove that the affiliate program pays for that item, method, or LP.
- A user-provided ASP condition is the best available conversion evidence, but it expires when the program or link changes.

Never infer `提携済み` from an old note. When sources conflict, record `要確認`, preserve both source dates, and do not publish the link until the ASP state is confirmed.

## Extract Before Judging

Capture these fields for every program:

- `広告案件`, `ASP`, `プログラムID`, `確認日`, `提携状態`.
- `単価`, `EPC`, `確定率`, `再訪問期間`, `成果確定目安`, and whether tax treatment is known.
- `成果地点`: Web申込, 電話確認, 査定完了, 本査定完了, 作業完了, or 成約.
- `申込経路`: Web, 電話, LINE, LP限定, or call tracking only.
- `成果対象`: eligible item, age, person type, region, and purchase method.
- `否認条件`: repeat, unreachable, cancellation, low appraisal, target exclusion, incomplete data, trademark SEO, or copied content.
- `広告表現制限`: wording, testimonials, image assets, campaign claims, and experience-article restrictions.

For a changing condition, keep the source URL or ASP screenshot date next to the value. Do not copy a conversion condition into article copy unless it is useful to the reader and directly confirmed.

## Seiribu Fit

Good fits:

- Supports `捨てる前に、売れるか確認。`.
- Helps readers make a calm `売る・残す・捨てる` decision during実家整理, 遺品整理, or生前整理.
- Appears after a believable value-check moment: valuable-looking items, a specialist category, difficult transport, or too many items to sort alone.

Weak fits:

- B2B-only, narrow-area, phone-only, or distant-conversion conditions that the article cannot explain naturally.
- Pure disposal before the reader has had a chance to check value.
- A program that needs claims such as "必ず高く売れる" or "何でも買い取れる".

## Decision Labels

Use one label and one priority.

| Label | Meaning |
| --- | --- |
| `主力` | Current partnership and conditions are verified; strong reader fit; safe primary CTA. |
| `条件付き主力` | Strong fit, but only for a matching item, LP, region, or confirmed condition. |
| `テスト` | Useful but narrow, distant conversion, unknown approval quality, or limited area. |
| `保留` | Needs partnership, current-condition check, or a matching article. |
| `非推奨` | Structural reader mismatch or unacceptable denial/trust risk. |
| `対象外` | The article and program do not overlap. |

`優先度`: `S` build or test soon, `A` strong next candidate, `B` limited test, `C` shelf, `D` low priority.

## Routing Defaults

Apply these only after the current ASP check. See the baseline for the reasoning and caveats.

| Reader situation | First route | Optional second route | Do not do |
| --- | --- | --- | --- |
| 実家の混在品を価値確認したい | バイセル | - | Use one generic LP across every item article. |
| 着物を品目特化で売りたい | バイセル | - | Split early traffic between multiple kimono programs or attract excluded clothing with a blanket "着物なら何でも" claim. |
| ブランド、時計、宝石、貴金属、毛皮 | ブラリバ for specialist intent | バイセル for genuinely mixed items | Treat broad miscellaneous goods as high-value items. |
| 絵画、掛軸、茶道具、作家物、骨董 | 獏 | 日晃堂 or a separate-group comparison | Present group-related services as three independent competitors. |
| カメラ、楽器、オーディオ | Current specialist program | バイセル only when the exact成果対象 is verified | Assume the broad program pays because its public site accepts the item. |
| 値段がつきそうにない、家を空にしたい | Disposal or municipal guidance after the value check | - | Force a purchase CTA. |

For 不用品回収, ゴミ屋敷, 空き家片付け, or遺品整理 services, make the value-check exit explicit before any disposal CTA. Confirm permits or municipal委託 claims from primary sources.

## Case-Specific Gates

### バイセル

- Default: `条件付き主力 / S` for broad value checks and verified eligible categories.
- Use a creative or LP that matches the article's main item. Do not treat the program as a universal fallback for camera, instruments, audio, or any category not confirmed in the current conversion target list.
- Verify the exact conversion point, accepted Web/phone/LINE path, and current restrictions before each placement cycle.
- Never use guaranteed-purchase wording, unapproved experiences, stale campaign assets, or a negative-trademark SEO angle. Follow the current ASP restrictions over this skill.

### ハッピープライス（旧GoodDeal）

- Default: `保留 / C`; current brand name is ハッピープライス.
- Do not use in published articles, comparison tables, or CTA placement. Its reader benefit does not currently outweigh the explanation cost against バイセル and specialist routes.
- Reconsider only after the current ASP conditions are verified, the service has a distinct reader benefit that existing routes cannot supply, and the user explicitly chooses a controlled test.
- Keep free cancellation as a reader right. Never discourage comparison or cancellation to protect approval.

### 福ちゃん

- Default: `保留 / A` until the current ASP partnership and item-specific terms are verified. Repository notes and user-provided data have conflicted on its partnership state.
- Current operating decision: do not place a 福ちゃん CTA in published kimono articles yet. Use バイセル as the sole kimono route while Seiribu builds search traffic and a baseline of own-site results.
- Reconsider a single focused kimono test only after the ASP terms, eligible-item/exclusion list, conversion point, and word restrictions are confirmed on the actual program page. Use broad mixed-item articles for a confirmed broad program instead.
- A women's-staff option is a conditional service feature, not a universal promise. Verify target region, availability, customer conditions, and approved application path at placement.

### Group Relationship

バイセル、福ちゃん、日晃堂 are separately operated services within the BuySell group. A comparison can still be useful, but do not imply that they are capital-independent competitors. When that relationship materially affects a comparison, state it accurately and include at least one separate-group option.

## CTA And Test Rules

1. Put one primary CTA at each reader decision point. Add a second only when it has a distinct reader benefit: specialist expertise, comparison, or region.
2. Match `記事の主品目` -> `広告の成果対象` -> `LP/creative` -> `CTA wording`. One mismatch is enough to downgrade the placement.
3. State the reader-safe next action: `査定対象になるか相談する`, not `必ず売れる`.
4. Do not use user reviews, expected appraisal price, or high reward as the main CTA rationale. Treat third-party review aggregates as investigation leads, not stable proof.
5. Record CTA impressions, clicks, applications, approvals, denials, approved revenue, item category, and application path.
6. Compare programs using own-site `1,000セッション当たりの確定報酬`, not EPC or approval rate alone. Keep tax treatment and measurement period consistent.
7. Do not promote a test to main status until it has at least 10 recorded occurrences and one full confirmation cycle, or enough data to explain why the program is not viable.

## Notion Workflow

When updating the Seiribu案件一覧, use existing properties where possible. Required practical fields are:

| Property | Use |
| --- | --- |
| `推奨方針` / `優先度` | Decision and urgency. |
| `確認日` / `情報源` | Evidence freshness and ASP/official distinction. |
| `提携状態` / `プログラムID` | Current link eligibility. |
| `成果地点` / `成果対象` / `申込経路` | What can actually convert. |
| `否認注意` / `広告表現制限` | Practical publication constraints. |
| `用途` / `次アクション` | Article context and one concrete next action. |
| `テスト指標` | Clicks, applications, approval, revenue, and review date. |

Do not overwrite a conflicting status with confidence. Preserve the latest date and set `要確認` with an action such as `ASP管理画面で提携と成果対象を確認`.

## Output Pattern

Lead with the decision, then show the evidence and one next action.

```markdown
結論: 条件付き主力 / 優先度A
確認日: YYYY-MM-DD
根拠: ASP確認 / 公式LP / 要確認

向いている記事:
- ...

使わない記事:
- ...

否認・表現注意:
- ...

未解決事項:
- ...

次アクション:
- ...
```

For multiple programs, use a compact table with `案件 | 提携状態 | 方針 | 優先度 | 主用途 | 成果地点 | 未解決事項 | 次アクション`.

## Editorial Safety

Use: `売れる可能性があります`, `査定対象になることがあります`, `処分前に確認しておくと安心です`.

Avoid: `必ず売れる`, `絶対に高く売れる`, `なんでも買い取れる`, unverified `使ってみた`, and rankings based only on reward.

Use `seiribu-content-strategy` for article-role decisions, `seiribu-seo-editor` for planning or drafting, and `seiribu-rewrite-manager` for published-article treatment.
