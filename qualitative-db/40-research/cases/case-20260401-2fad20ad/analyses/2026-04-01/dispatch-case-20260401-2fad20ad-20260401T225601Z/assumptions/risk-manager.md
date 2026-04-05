---
type: assumption_note
domain: culture
subdomain: streaming
entity: War Machine
topic: case-20260401-2fad20ad | risk-manager
question: Will "War Machine" be the #2 global Netflix movie this week?
driver: operational-risk
date_created: 2026-04-01
agent: risk-manager
status: active
certainty: medium
importance: high
time_horizon: immediate
related_entities: [Netflix, War Machine]
related_drivers: [operational-risk, media-narratives, seasonality]
upstream_inputs: [qualitative-db/40-research/cases/case-20260401-2fad20ad/source-notes/case-20260401-2fad20ad-risk-manager-netflix-top10-page.md, qualitative-db/40-research/cases/case-20260401-2fad20ad/source-notes/case-20260401-2fad20ad-risk-manager-war-machine-page.md]
downstream_uses: [qualitative-db/40-research/cases/case-20260401-2fad20ad/analyses/2026-04-01/dispatch-case-20260401-2fad20ad-20260401T225601Z/personas/risk-manager.md, qualitative-db/40-research/cases/case-20260401-2fad20ad/analyses/2026-04-01/dispatch-case-20260401-2fad20ad-20260401T225601Z/evidence/risk-manager.md]
tags: [assumption-note, case-20260401-2fad20ad, risk-manager, netflix, extraction-risk]
legacy_imported: true
legacy_original_path: qualitative-db/40-research/assumption-notes/case-20260401-2fad20ad-risk-manager-assumptions.md
legacy_original_note_kind: assumption
imported_by: legacy_40_research_backfill
import_batch: 20260405T225345Z
case_key: case-20260401-2fad20ad
dispatch_id: dispatch-case-20260401-2fad20ad-20260401T225601Z
analysis_date: 2026-04-01
persona: risk-manager
---

# Assumption

The visible #2 row on Netflix's official 3/23/26-3/29/26 global English movies chart corresponds to War Machine, and the remaining ambiguity is caused by page-extraction limitations rather than true title/rank uncertainty.

## Why this assumption matters

The market is already priced at 95.85%, so almost all residual probability mass sits on exactly this mapping question. If the assumption is wrong, the market is badly overpriced; if it is right, the market is basically correct.

## What this assumption supports

- A high-probability yes view on War Machine as #2.
- A judgment that remaining uncertainty is mainly operational/extraction risk rather than competitive ranking risk.

## Evidence or logic behind the assumption

- Netflix's official Top 10 page shows the exact relevant weekly window and a clearly defined #2 slot at 10.3M views.
- The same page prominently links to War Machine in the set of most-watched movie links.
- War Machine has a current official Tudum page with March 2026 coverage, consistent with a live charting title.
- The observed #2 to #3 gap is large, making "close-call" ranking risk look small relative to identity/extraction risk.

## What would falsify it

- A direct rendering of the Netflix chart showing a different movie name at #2 for 3/23/26-3/29/26.
- Netflix updating the chart with War Machine at #3 or lower.
- Official market-resolution text or a clearer scrape showing that the War Machine-linked title is not the #2 row.

## Early warning signs

- Any independent scrape or screenshot pairing 10.3M with a different title.
- Evidence that the Top 10 page mixes multiple title links outside the ranked rows, making the War Machine link non-diagnostic.
- A late chart correction from Netflix.

## What changes if this assumption fails

The probability should collapse sharply, because the current pro case is built mostly on the official chart plus inferred title mapping. If mapping fails, the thesis is not "slightly wrong"; it is probably wrong on the core resolution fact.

## Notes that depend on this assumption

- qualitative-db/40-research/cases/case-20260401-2fad20ad/analyses/2026-04-01/dispatch-case-20260401-2fad20ad-20260401T225601Z/personas/risk-manager.md
- qualitative-db/40-research/cases/case-20260401-2fad20ad/analyses/2026-04-01/dispatch-case-20260401-2fad20ad-20260401T225601Z/evidence/risk-manager.md