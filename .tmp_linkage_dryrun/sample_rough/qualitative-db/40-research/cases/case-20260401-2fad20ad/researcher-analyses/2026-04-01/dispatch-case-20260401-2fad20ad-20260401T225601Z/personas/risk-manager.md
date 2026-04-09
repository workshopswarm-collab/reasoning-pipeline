---
type: agent_finding
domain: culture
subdomain: streaming
entity:
topic: "case-20260401-2fad20ad | risk-manager"
question: "Will \"War Machine\" be the #2 global Netflix movie this week?"
driver: operational-risk
date_created: 2026-04-01
agent: risk-manager
stance: agree-but-slightly-less-confident-than-market
certainty: medium
importance: high
novelty: low
time_horizon: immediate
related_entities: ["netflix"]
related_drivers: ["operational-risk", "seasonality", "media-narratives"]
proposed_entities: ["War Machine"]
proposed_drivers: []
upstream_inputs: ["qualitative-db/40-research/cases/case-20260401-2fad20ad/researcher-source-notes/case-20260401-2fad20ad-risk-manager-netflix-top10-page.md", "qualitative-db/40-research/cases/case-20260401-2fad20ad/researcher-source-notes/case-20260401-2fad20ad-risk-manager-war-machine-page.md", "qualitative-db/40-research/cases/case-20260401-2fad20ad/researcher-analyses/2026-04-01/dispatch-case-20260401-2fad20ad-20260401T225601Z/assumptions/risk-manager.md", "qualitative-db/40-research/cases/case-20260401-2fad20ad/researcher-analyses/2026-04-01/dispatch-case-20260401-2fad20ad-20260401T225601Z/evidence/risk-manager.md"]
downstream_uses: []
tags: ["agent-finding", "case-20260401-2fad20ad", "risk-manager", "netflix", "war-machine"]
legacy_imported: true
legacy_original_path: qualitative-db/40-research/agent-findings/risk-manager/case-20260401-2fad20ad-will-war-machine-be-the-2-global-netflix-movie-this-week-794.md
legacy_original_note_kind: persona
imported_by: legacy_40_research_backfill
import_batch: 20260405T225345Z
case_key: case-20260401-2fad20ad
dispatch_id: dispatch-case-20260401-2fad20ad-20260401T225601Z
analysis_date: 2026-04-01
persona: risk-manager
---

# Claim

War Machine is still very likely to resolve as the #2 global Netflix movie for the relevant week, but the remaining risk is concentrated in title-to-row mapping and official-page extraction rather than in the competitive ranking itself. My estimate is **91%**, versus the market-implied **95.85%** from the current price of 0.9585.

## Implication for the question

I **roughly agree** with the market's direction but think the market is embedding almost-complete confidence when the auditable evidence available in this run is a little weaker than that. The official Netflix Top 10 page for 3/23/26 - 3/29/26 shows a clear #2 slot at **10.3M views**, well ahead of #3 at **7.9M views**, and also links to War Machine. That makes a yes resolution the dominant outcome. But because the readable extraction does not cleanly print the title names alongside the rank rows, I keep a non-trivial residual chance that the #2 row belongs to another movie or that a late official clarification changes the mapping.

## Supporting evidence

- Netflix's own Tudum Top 10 page is live for the exact relevant weekly window and shows the #2 row at 10.3M views, with a sizable 2.4M gap over #3.
- The same official page includes a direct War Machine title link.
- War Machine has a current official Tudum page with March 2026 editorial coverage, consistent with an active release in the relevant chart window.
- If War Machine is indeed the #2 row, the gap to #3 is large enough that normal small data noise is unlikely to matter.

## Counterpoints

- The strongest counterpoint is **not** a rival-title thesis; it is an **evidence-quality problem**. The readable extraction of the official page drops or obscures the title names next to the rank rows.
- The War Machine title page confirms the object but does not independently confirm rank.
- At 95.85%, the market is pricing only about 4.15% residual uncertainty. That seems a bit too low given the evidence here still requires a mapping inference.

## Key assumptions

- The 10.3M #2 row on the official chart is War Machine.
- Netflix will not materially revise the published chart after the relevant update.
- The market resolves against the official chart as published, not against a malformed or incomplete rendering artifact.

## Why this is decision-relevant

This is mostly a **confidence calibration** call. The market direction is probably right, but the downside if the mapping assumption fails is discontinuous: the thesis is not slightly weakened, it is largely wrong. So the right risk-manager posture is to stay yes-leaning while refusing to round a partially inferred official-source reading up to near-certainty.

## What would falsify this interpretation

- A direct official rendering or screenshot showing another title at #2 for 3/23/26 - 3/29/26.
- Netflix revising the chart and moving War Machine below #2.
- Any clearer official extraction showing that War Machine is present on the page but not attached to the #2 row.

## Recommended follow-up

- If available, capture one cleaner direct rendering or screenshot of the official Netflix chart pairing War Machine with the #2 row.
- If no cleaner extraction is available, this note is already sufficient to justify a high-probability yes with an explicit haircut for operational/extraction risk rather than for substantive ranking competition.