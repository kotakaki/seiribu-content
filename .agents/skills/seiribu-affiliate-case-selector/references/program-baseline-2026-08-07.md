# Seiribu Program Baseline

- Updated: 2026-08-07
- Purpose: default routing for affiliate case selection. This is not a substitute for the current ASP program detail.
- Decision rule: a service's official item list proves consumer availability only. Use current ASP data to decide whether the item, LP, and application path can produce an affiliate conversion.

## Evidence Status

| Source | Date | How to use it |
| --- | --- | --- |
| `reports/visit-purchase-official-web-research-2026-07-29.md` | 2026-07-29 | Latest repository-wide ASP/official research baseline. Recheck its program conditions in the ASP before placement. |
| User-provided program notes | 2026-08-07 | Useful for program strategy and risk flags. Exact rates, rewards, review figures, and terms require current ASP or official-source confirmation before publication. |
| Official provider pages checked in this update | 2026-08-07 | Use for current service names, consumer-facing methods, and group relationships; not affiliate eligibility. |

## Current Program Matrix

| Program | Default decision | Best use | Hard gate |
| --- | --- | --- | --- |
| バイセル | 条件付き主力 / S | Mixed household items and verified item-specific pages. | Verify current conversion target, path, and matching LP/creative. |
| ハッピープライス（旧GoodDeal） | 保留 / C | No published use. | Do not place in articles, comparison tables, or CTA slots. Reconsider only through a user-approved controlled test after current ASP verification. |
| 福ちゃん | 保留 / A | Candidate for focused kimono articles and service-anxiety contexts after approval. | Partnership status conflicts across repository notes. Confirm ASP status and item exclusions first. |
| ブラリバ | 主力 / S after routine ASP check | Brand bags, watches, jewellery, precious metals, fur. | Confirm link conditions and supported application path. |
| 美術品買取専門店獏 | 主力 / S after routine ASP check | Art, hanging scrolls, tea utensils, antiques, artist-made ceramics. | Confirm current appraisal/amount conditions. |
| 日晃堂 | 条件付き主力 / A | Specialist comparison for antiques and art. | Use an independent-group comparison option when comparison framing matters. |
| ニーゴ・リユース | 条件付き主力 / A | Mixed camera, instrument, and audio collections. | Check service area and current target category. |
| カメラの買取屋さん、楽器の買取屋さん、オーディオの買取屋さん | 提携優先 / A | Single-category specialist articles. | Apply and confirm before planning a primary CTA. |
| ウリドキ | 提携優先 / A | One high-value item where the reader wants a comparison. | Do not use for whole-house mixed-item clean-outs. |
| 不用品回収・遺品整理 | 後段導線 | Items with no realistic value or a home that must be cleared. | Complete the value-check branch first and verify disposal permissions. |

## Program Notes

### バイセル

- The latest repository ASP snapshot is 2026-07-29: AccessTrade program `761701`, partnership recorded as active, CVR `0.65%`, approval `88.40%`, and category-level rewards. These are snapshot values, not evergreen settings.
- Treat the confirmed reward list as a starting point only. Download and inspect the current target-list CSV before using a category that has no current explicit target.
- Official site checked 2026-08-07 lists Web/phone contact, visit/store/mail purchase methods, 24-hour phone reception, and a broad item list. Its 4,800万点 and 180種類 figures are dated by the provider to 2015-2025 and 2026-03 respectively; do not reuse them in an article without checking the current official page.
- The July research records restrictions including no blanket purchase claim, no unapproved appraisal experience, and special care for old assets, negative-trademark SEO, and item/method claims. Current ASP terms override that record.

Sources:

- `reports/visit-purchase-official-web-research-2026-07-29.md`
- https://buysell-kaitori.com/

### ハッピープライス（旧GoodDeal）

- Officially renamed from GoodDeal to ハッピープライス on 2026-02-03; the notice says the operating company and service content did not change.
- Status: `保留 / C`. Do not use it in published articles, comparison tables, or CTA slots.
- Rationale: the current reader benefit does not outweigh the explanation cost against バイセル for mixed items and specialist routes for high-value brand items. The high reward and distant `本査定完了` condition are not reasons to create a reader-facing recommendation.
- Reconsider only through a user-approved controlled test after confirming the current ASP conditions and a distinct reader benefit that existing routes cannot supply.

Sources:

- `reports/visit-purchase-official-web-research-2026-07-29.md`
- https://happyprice.jp/info/happy-price/
- https://happyprice.jp/

### 福ちゃん

- Official pages checked 2026-08-07 show free visit appraisal, item additions during a visit, customer cancellation, and a women's-staff program. The women's program is limited by customer conditions, area, scheduling, and application route.
- Current repository records conflict: a 2026-07-11 summary says some 福ちゃん programs are active, while the later research and user-provided data describe item-specific applications or an unpartnered state. Treat all partnership fields as `要確認` until the actual ASP program page is checked.
- User-provided figures suggest the kimono program may be a high-potential test. Do not elevate it on EPC or approval rate alone. First confirm approval, the current eligible-item/exclusion list, conversion point, and word restrictions; then test one or two focused kimono pages.
- The service relationship with バイセル is material in comparison content. Do not frame 福ちゃん, バイセル, and 日晃堂 as capital-independent competitors.

Sources:

- `reports/visit-purchase-official-web-research-2026-07-29.md`
- `reports/affiliate-all-programs-summary-2026-07-11.md`
- https://www.fuku-chan.info/shuccho/
- https://www.fuku-chan.info/shuccho/ladies_plan/

### Specialist Defaults

- Use ブラリバ for brand-led intent, rather than making a broad mixed-item program look like a specialist.
- Use 獏 for art, hanging scrolls, tea utensils, antique ceramics, and artist-made items. Use 日晃堂 as a specialist alternative, with a separate-group option in comparisons.
- Use a current specialist program for camera, instrument, and audio articles. A broad provider's public item list is not enough to prove affiliate eligibility.

Sources:

- https://brandrevalue.com/purchase/shuccho
- https://www.baku-art.co.jp/

## Group Relationship

BuySell Technologies states that, from October 2024, Rextholdings joined its group and has subsidiaries including REGATE (買取福ちゃん) and 日晃堂. Services can still differ in method and audience fit, but comparison copy must not hide this relationship.

Source: https://buysell-technologies.com/strategy/ma/

## Measurement Rule

Use this sequence for every new primary CTA:

1. Confirm partnership, accepted item, conversion point, application path, LP, and restrictions in the current ASP.
2. Publish the CTA only in a matching article and start an observation record.
3. Track CTA impression, click, application, approval, denial reason, approved revenue, and the article/item cluster.
4. After at least 10 occurrences and one full confirmation period, compare `approved revenue per 1,000 sessions` with like-for-like article groups.
5. Keep, expand, reduce, or stop based on own data and reader fit. Do not compare raw EPC or approval rates between ASPs without aligning the date range, denominator, and tax treatment.

## Do Not Use As Published Facts Without Fresh Evidence

- Current reward amount, EPC, CVR, approval rate, and partnership status.
- Store count, employee count, cumulative purchase count, item-count claims, and campaign promotions.
- Third-party review averages, review-count claims, or anecdotal appraisal outcomes.
- Statements that a particular general item is eligible, profitable, or likely to receive a price.
