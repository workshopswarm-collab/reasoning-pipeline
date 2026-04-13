---
type: evidence_map
case_key: case-20260413-9c835dfe
dispatch_id: dispatch-case-20260413-9c835dfe-20260413T162509Z
research_run_id: 24097620-9e3a-4275-9a52-82cc98ae4c72
analysis_date: 2026-04-13
persona: catalyst-hunter
domain: crypto
subdomain: corporate-bitcoin-treasury
entity: bitcoin
topic: "MicroStrategy/Strategy >1000 BTC announcement April 7-13"
question: "Did Strategy announce a purchase of more than 1000 BTC during April 7-13, 2026?"
driver: reliability
date_created: 2026-04-13
agent: Orchestrator
status: draft
confidence: high
conflict_status: low
action_relevance: high
related_entities: ["bitcoin"]
related_drivers: ["reliability"]
proposed_entities: ["Strategy Inc", "Michael Saylor"]
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260413-9c835dfe/researcher-analyses/2026-04-13/dispatch-case-20260413-9c835dfe-20260413T162509Z/personas/catalyst-hunter.md"]
tags: ["official-source", "timing", "evidence-netting"]
---

# Summary

The evidence nets to a strong YES because an official Strategy-owned source posted a same-day April 13 disclosure for 13,927 BTC, with the main residual uncertainty being source-of-truth interpretation rather than event occurrence.

## Question being evaluated

Did MicroStrategy/Strategy announce a purchase of more than 1000 BTC between April 7 and April 13, 2026 inclusive?

## Current lean

YES, with high confidence.

## Prior / starting view

The market price of 0.96 implied the market already expected a YES outcome, likely because Strategy often posts bitcoin purchase updates on Monday mornings.

## Evidence supporting the claim

- Official Strategy purchases page updated with an April 13, 2026 row showing `13,927 BTC` and linked 8-K.
  - Source: `researcher-source-notes/2026-04-13-catalyst-hunter-strategy-purchases-page.md`
  - Why it matters causally: directly satisfies both size and timing if counted as official company information.
  - Direct vs indirect: direct.
  - Weight: very high.

- Same row contains company social copy stating `@Strategy has acquired 13,927 BTC ... As of 4/12/2026 ...`.
  - Source: same note.
  - Why it matters causally: confirms the company framed the event as an acquisition announcement on April 13.
  - Direct vs indirect: direct.
  - Weight: high.

- Historical company press archive shows bitcoin purchases are routinely announced on official Strategy channels.
  - Source: `researcher-source-notes/2026-04-13-catalyst-hunter-strategy-press-pattern.md`
  - Why it matters causally: reduces the chance that the purchases page is some unofficial or purely archival surface.
  - Direct vs indirect: indirect/contextual.
  - Weight: medium.

## Evidence against the claim

- The contract says resolution will be based on official information from MicroStrategy or Michael Saylor, which leaves a small interpretation risk if a reviewer demanded a narrower announcement surface than the purchases page plus linked 8-K.
  - Why it matters causally: this is the only realistic path to a false negative after the April 13 post.
  - Direct vs indirect: rule/interpretation risk.
  - Weight: low-to-medium.

## Ambiguous or mixed evidence

- The purchases may have been made before April 7, but the contract explicitly says announcement timing governs regardless of purchase timing. This is potentially confusing but not actually adverse if rules are followed literally.

## Conflict between inputs

No material factual conflict found. The main issue is wording interpretation, not conflicting evidence.

## Key assumptions

- The official Strategy purchases page and linked 8-K qualify as official company information for resolution.
- The April 13 publication occurred inside the ET market window.

## Key uncertainties

- Whether Polymarket adjudicators require a distinct press release or Michael Saylor post even when the company site/8-K already discloses the purchase.

## Disconfirming signals to watch

- Official correction or withdrawal of the April 13 purchase entry.
- Resolution guidance excluding the purchases page/8-K from accepted announcement surfaces.

## What would increase confidence

- Direct text extraction from the linked 8-K or a same-day Strategy/Michael Saylor post repeating the 13,927 BTC figure.
- Market comments or resolver guidance explicitly confirming the purchases page counts.

## Net update logic

The market was already near-certain YES at 96%, and the official April 13 company update is strong enough to justify moving to near-settled YES. Residual uncertainty comes almost entirely from source-of-truth interpretation, not from whether a qualifying >1000 BTC announcement happened.

## Suggested downstream use

Use as forecast update and orchestrator synthesis input; minimal further follow-up unless source-of-truth interpretation becomes disputed.