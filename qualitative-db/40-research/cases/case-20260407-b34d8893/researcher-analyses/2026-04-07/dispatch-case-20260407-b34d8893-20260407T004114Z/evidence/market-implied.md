---
type: evidence_map
case_key: case-20260407-b34d8893
dispatch_id: dispatch-case-20260407-b34d8893-20260407T004114Z
research_run_id: 436ed12f-ab89-44dd-bef0-a07429be0fd3
analysis_date: 2026-04-07
persona: market-implied
domain: crypto
subdomain: corporate-bitcoin-treasury
entity:
topic: will-microstrategy-announce-a-bitcoin-purchase-march-31-april-6
question: "Will Microstrategy announce a Bitcoin purchase March 31-April 6?"
driver: sentiment
date_created: 2026-04-07
agent: market-implied
status: draft
confidence: high
conflict_status: low
action_relevance: high
related_entities: []
related_drivers: ["sentiment"]
proposed_entities: ["strategy"]
proposed_drivers: []
upstream_inputs: []
downstream_uses: []
tags: ["official-source", "resolution-check", "direct-company-announcement"]
---

# Summary

This evidence map is simple because one direct official source appears to settle the market, while the remaining uncertainty is mainly technical around timing/interpretation rather than substantive.

## Question being evaluated

Will Microstrategy announce a Bitcoin purchase March 31-April 6?

## Current lean

Strong Yes lean, effectively near-certain.

## Prior / starting view

Starting view was that a 94.85% market price likely reflected traders expecting the usual weekly Strategy BTC announcement cadence, but it still needed direct official confirmation because the market is date-bounded and source-bounded.

## Evidence supporting the claim

- **Official Strategy purchases page shows April 2026 acquisition entry**  
  - Source: `2026-04-07-market-implied-strategy-purchases-and-8k.md`  
  - Why it matters causally: this is the exact type of official company announcement contemplated by the rules.  
  - Direct or indirect: direct.  
  - Weight: very high.

- **Linked Form 8-K artifact on the official page**  
  - Source: same source note.  
  - Why it matters causally: reduces risk that the webpage is merely informal social copy; anchors the announcement to a formal filing workflow.  
  - Direct or indirect: direct/verification.  
  - Weight: high.

- **Market structure/context**  
  - Source: Polymarket market page and assignment context.  
  - Why it matters causally: extreme price already implied traders expected official confirmation and that expectation proved correct.  
  - Direct or indirect: indirect/contextual.  
  - Weight: moderate.

## Evidence against the claim

- **Residual timestamp ambiguity**  
  - Why it matters causally: if the official posting somehow occurred after the eligible ET cutoff, a seemingly valid announcement could still miss the window.  
  - Direct or indirect: indirect/technical.  
  - Weight: low.

## Ambiguous or mixed evidence

- The Polymarket rendered page showed 100% in fetched FAQ text while assignment metadata listed current_price 0.9485. That discrepancy is not resolution-relevant; it only shows the public page text can lag or round differently.

## Conflict between inputs

No meaningful factual conflict found. The only real issue is technical caution about exact publication timing, not competing evidence about whether Strategy announced a purchase.

## Key assumptions

- The official Strategy purchases page counts as valid official information under the market rules.
- The April 6 posting occurred within the eligible market window.

## Key uncertainties

- Exact publication timestamp in ET for the webpage / filing surface.

## Disconfirming signals to watch

- Official correction or retraction.
- Evidence that the posting time missed the cutoff.
- Resolution guidance excluding the purchases page despite the market description referencing it.

## What would increase confidence

- A clearly timestamped official Strategy or Michael Saylor post matching the purchases page.
- Direct inspection of the linked 8-K timestamp if needed.

## Net update logic

The market started at an extreme Yes price because traders appeared to expect the routine weekly Strategy BTC announcement. After direct official website verification, the case moved from "market probably right" to "market right for the simple reason that the official announcement is already there." The remaining uncertainty is too small to justify a material discount.

## Suggested downstream use

Use as direct synthesis input and as audit trail showing why this low-difficulty, source-bounded case could be finished decisively after one authoritative verification plus one contextual/market pass.
