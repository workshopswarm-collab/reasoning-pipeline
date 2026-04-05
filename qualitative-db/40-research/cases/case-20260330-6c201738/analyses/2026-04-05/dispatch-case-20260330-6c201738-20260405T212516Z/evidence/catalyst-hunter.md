---
type: evidence_map
case_key: case-20260330-6c201738
dispatch_id: dispatch-case-20260330-6c201738-20260405T212516Z
research_run_id: 70885244-3ed7-4285-ac14-ec9cb33f7e77
analysis_date: 2026-04-05
persona: catalyst-hunter
domain: trade-policy
subdomain: tariffs
entity: united-states-china-trade
topic: case-20260330-6c201738 | catalyst-hunter
question: Will the U.S. tariff rate on China be between 5% and 15% on March 31, 2026?
driver: official-order-timing
date_created: 2026-04-05
agent: Orchestrator
status: complete
confidence: medium
conflict_status: interpretive-conflict
action_relevance: high
related_entities: [china, united-states, white-house, ustr]
related_drivers: [official-order-timing, paused-vs-in-effect-orders, tariff-stack-calculation, source-hierarchy]
upstream_inputs: []
downstream_uses: [orchestrator-synthesis]
tags: [catalyst-hunter, evidence-map, tariffs, timing]
---

# Summary

The market’s likely repricing path is driven by a short list of concrete official catalysts, not by generic tariff commentary. Current official materials point to a China-wide tariff stack above 15%, but the market can still move if later official action or implementation changes collapse that stack to a single 10% layer by the March 31, 2026 checkpoint.

## Question being evaluated

Whether the U.S. general tariff rate on China, as defined by the contract, will be between 5% and 15% on March 31, 2026 at 12:00 PM ET.

## Current lean

Current lean is **No**, with the main catalyst-sensitive caveat that later official rollback or legal/implementation displacement could still move the market into the bracket.

## Prior / starting view

Starting view: the market price near 95.9% Yes implied that traders were probably anchoring on a simple 10% general-tariff story. That looked plausible as a timing prior, but required verification against the official action chain.

## Evidence supporting the claim

- **Catalyst path to Yes exists via future rollback or legal displacement.**
  - Source / note reference: Tax Foundation contextual summary cited in existing case artifacts; variant-view finding and current source note.
  - Why it matters causally: if broad China-specific layers do not survive to March 31, 2026, the stack could fall into the bracket.
  - Direct or indirect: indirect/contextual.
  - Weight: medium.

- **Market price suggests many participants already expect only a single broad 10% layer to matter.**
  - Source / note reference: current_price 0.959 and market context.
  - Why it matters causally: repricing could be violent if official guidance either confirms or refutes that simplification.
  - Direct or indirect: indirect.
  - Weight: low-medium.

## Evidence against the claim

- **Official reciprocal-tariff chain leaves a 10% PRC reciprocal layer in effect through November 10, 2026.**
  - Source / note reference: White House May 12, Aug. 11, and Nov. 4, 2025 orders; catalyst source note.
  - Why it matters causally: this alone is a broad China-wide layer still live at the checkpoint.
  - Direct or indirect: direct.
  - Weight: high.

- **Official synthetic-opioid PRC duty was reduced to 10%, not removed, effective November 10, 2025.**
  - Source / note reference: White House Mar. 3 and Nov. 4, 2025 orders; catalyst source note.
  - Why it matters causally: this creates a second broad China-wide layer that likely keeps the stack above 15%.
  - Direct or indirect: direct.
  - Weight: high.

- **Contract wording supports additive logic and excludes only paused / not-yet-effective / item-specific measures.**
  - Source / note reference: Polymarket contract surface.
  - Why it matters causally: additive logic makes a 10% + 10% stack resolve outside the band.
  - Direct or indirect: direct contextual.
  - Weight: high.

## Ambiguous or mixed evidence

- **Resolver interpretation risk.** The contract strongly suggests additive treatment, but the market may be assuming only one broad layer counts.
- **Future legal status risk.** Legal defeats or administrative replacement could matter a lot, but only if they change what is actually in effect by noon ET on March 31, 2026.

## Conflict between inputs

- Disagreement is mostly **interpretive and timing-based**, not factual.
- One camp treats the market as basically a 10% universal/general-rate question.
- The stronger official-chain reading treats it as a stacked general-rate question where two China-wide 10% layers can coexist.
- Evidence that would resolve this: a later official summary, implementation notice, HTSUS guidance, or explicit resolver clarification stating the operative China general tariff stack at the checkpoint.

## Key assumptions

- Both the reciprocal 10% and synthetic-opioid 10% qualify as general China-wide tariffs.
- No later official action eliminates one of the layers before the checkpoint.
- “In effect” is determined by actual operative official status, not rhetorical announcements.

## Key uncertainties

- Whether a future White House/USTR action changes one or both broad China-wide layers.
- Whether a controlling legal or customs implementation development changes the in-effect stack.
- Whether Polymarket resolution practice applies additive logic exactly as the contract example suggests.

## Disconfirming signals to watch

- Official action removing or pausing one broad China-wide 10% layer.
- Official implementation guidance showing the relevant general China tariff is only 10%.
- Credible consensus reporting near resolution, tied to official sources, saying China-specific layers are no longer in effect.

## What would increase confidence

- Near-resolution White House/USTR confirmation of the operative China tariff stack.
- Customs / HTSUS implementation material matching the two-layer reading.
- Explicit resolver or market clarification on additive treatment of multiple general China-wide tariffs.

## Net update logic

The main update from the starting market view is that the official chronology makes the market’s simple 10% story look incomplete. What mattered most was not headline pause coverage but the explicit effective-date chain showing that two 10% China-wide layers plausibly coexisted. I downweighted generic tariff headlines because this contract is about what is actually in effect at a specific timestamp, not sentiment or announced intentions.

## Suggested downstream use

Use this as an **orchestrator synthesis input** and as a guide for near-resolution monitoring. The practical watchlist is narrow: later official action, implementation guidance, or legal displacement that changes which broad China-wide tariffs are operative at noon ET on March 31, 2026.