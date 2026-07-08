---
name: seiribu-seo-editor
description: Use when planning, rewriting, reviewing, or drafting Seiribu editorial SEO articles, especially for search-intent checks, topic-cluster boundaries, pillar/cluster design, H2 role labeling, phased article production, and preventing article drafts from drifting into adjacent or unrelated topics.
---

# Seiribu SEO Editor

Use this skill as the execution gate for Seiribu article work. The goal is not to generate more text; the goal is to keep each article aligned with its search intent, topic cluster, and editorial role.

## Non-Negotiable Behavior

- Start article-production responses with `【現在実行中のフェーズ: PHASE X】`.
- Output only the current phase. Do not write body copy during planning or outline phases.
- Save article artifacts to the appropriate `briefs/` or `drafts/` file. In chat, report only the file path, concise summary, checks, and confirmation question.
- Do not paste full outlines, intros, H2 sections, FAQ, or final drafts into chat unless the user explicitly asks to view them in chat.
- Stop every phase with a confirmation question. Do not self-advance.
- Before writing body copy, fix the search intent, topic-cluster boundary, and H2 role labels.
- If an existing draft lacks a frozen design or appears to drift, run a boundary audit before polishing.
- Treat "required elements" as placement requirements, not as permission to expand every adjacent topic.

## Minimum Gate

For any article creation, rewrite, or structural review, output this gate before body copy:

```md
【現在実行中のフェーズ: PHASE 0】
KW:
検索意図:
主トピック:
同一クラスタ:
隣接クラスタ:
別トピッククラスタ:
扱わないこと:
本文前に注意すること:

この前提で記事企画へ進めてよいですか？
```

Do not omit this gate for pillar articles, existing traffic articles, revenue-adjacent articles, or normal item articles. For tiny fixes such as typo correction, one internal link insertion, or local wording cleanup, skip the gate only if the search intent and structure are not affected.

## Topic Boundary Rules

Classify every topic before outlining:

| Class | Meaning | Treatment |
| --- | --- | --- |
| 主トピック | The article's core search intent | Write thickly |
| 同一クラスタ | Direct child/supporting article | Link strongly, summarize briefly if needed |
| 隣接クラスタ | Related but not the article's job | Mention lightly or link |
| 別トピッククラスタ | Different cluster | Do not H2; at most one note/link |
| 扱わないこと | Dilutes intent or causes cannibalization | Exclude |

For each H2, assign one role:

| Role | Treatment |
| --- | --- |
| 主役 | Core section; can be detailed |
| 補助 | Helps the reader judge the core topic; keep moderate |
| 導線 | Sends reader to another article; keep short |
| 注意書き | Prevents mistakes; one paragraph/table row |
| 削除候補 | Remove from outline |

If a section is "導線" or "注意書き", do not turn it into a complete standalone article.

## Seiribu Editorial Defaults

- Core message: `捨てる前に、売れるか確認。`
- Audience: adults sorting a parent's home, old belongings, hobby goods, collections, and disposal decisions.
- Tone: polite `です・ます`, gentle but not sugary, plain enough for middle-school readers.
- Avoid hard claims: use `売れる可能性があります`, `査定対象になることがあります`, `買取が難しいこともあります`.
- Never claim guaranteed high prices, guaranteed purchase, any-condition purchase, urgent loss framing, fake firsthand experience, or unsupported market prices.
- Human review and final publishing decision remain required.

## Phase Flow

### PHASE 0: Search Intent And Boundary

Use the Minimum Gate. For rewrites, also inspect the existing draft's current role, likely drift, and missing/out-of-scope boundaries.

Stop: `この前提で記事企画へ進めてよいですか？`

### PHASE 1: Brief

Output:

- Target KW
- Reader
- Search intent
- Reader anxiety
- Article role
- Topic boundary table
- Internal-link candidates by class
- Production mode

Do not write body copy.

Save the brief to `briefs/` or the active draft file. Chat should only summarize the saved brief and ask for approval.

Stop: `この企画で見出し構成へ進めてよいですか？`

### PHASE 2: Outline

Output:

- H1 and title options
- Meta description
- H2/H3 outline
- What each H2 answers
- H2 role label
- Required tables/checklists/FAQ candidates
- Internal links and CTA
- Image/ALT candidates

After approval, save a frozen design in the draft file as an HTML comment containing: search intent, main topic, out-of-scope topics, H2 role labels, and internal-link intent.

Stop: `この構成で導入文制作へ進めてよいですか？`

### PHASE 3: Intro

Write only the intro. Include reader situation, anxiety, article conclusion, and what the article clarifies. Do not repeat H2-1.

Save the intro to the draft file. Chat should not paste the full intro unless requested.

Stop: `この導入文でH2ごとの本文作成へ進めてよいですか？`

### PHASE 4: H2 Body

Write one H2 at a time. Before writing, check its role label:

- 主役: answer directly and include enough detail.
- 補助: keep scoped to the main topic.
- 導線: summarize and link out.
- 注意書き: keep to one paragraph or a small table row.
- 削除候補: do not write; explain why it should be removed.

Save the H2 body to the draft file. Chat should report the edited H2, role label, and any checks.

Stop: `このH2の内容で次のH2へ進めてよいですか？`

### PHASE 5: Final Adjustment

Check:

- The title and body match.
- The opening answers search intent quickly.
- H2s do not duplicate or expand into other clusters.
- Required elements are present at the right depth.
- Internal links are natural and classified.
- Affiliate pressure is not too strong.
- Unsupported claims and banned expressions are absent.
- `human_review_required: true` remains.

Stop: `この内容をWordPress下書き化してよいですか？`

## Common Seiribu Failure Modes

- Filling every H2 equally instead of respecting H2 roles.
- Treating adjacent clusters as if they are children of the pillar.
- Expanding family-conflict content inside a "sellable items" pillar.
- Expanding disposal details inside a "sellable items" pillar.
- Letting required elements become full sections when a table row or link is enough.
- Polishing a drifting draft instead of first re-setting the boundary.
