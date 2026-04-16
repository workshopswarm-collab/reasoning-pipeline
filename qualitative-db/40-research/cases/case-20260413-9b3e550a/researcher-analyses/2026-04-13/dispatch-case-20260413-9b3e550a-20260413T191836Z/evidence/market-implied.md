---
type: evidence_map
case_key: case-20260413-9b3e550a
dispatch_id: dispatch-case-20260413-9b3e550a-20260413T191836Z
research_run_id: 444b3ddc-9ba6-4860-a774-d0e69cefa84b
analysis_date: 2026-04-13
persona: market-implied
domain: politics
subdomain: elections
entity:
topic: bulgarian-parliamentary-election-third-place
question: "Will We Continue the Change – Democratic Bulgaria (PP–DB) finish third in the 2026 Bulgarian parliamentary election?"
driver: elections
date_created: 2026-04-13
agent: orchestrator
status: draft
confidence: medium
conflict_status: moderate
action_relevance: high
related_entities: []
related_drivers: ["elections"]
proposed_entities: ["pp-db", "revival", "dps", "central-election-commission-of-bulgaria"]
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["market-implied-finding"]
tags: ["evidence-map", "bulgaria", "elections", "pp-db"]
---

# Summary

Visible public evidence supports PP–DB as a serious contender for third place, but does not cleanly support a near-lock interpretation. The market appears to be pricing a stronger ranking stability than the accessible contextual evidence alone demonstrates.

## Question being evaluated

Will We Continue the Change – Democratic Bulgaria (PP–DB) finish third in the 2026 Bulgarian parliamentary election?

## Current lean

Lean yes, but at materially lower confidence than the market price implies.

## Prior / starting view

Starting from the market, the natural prior is that PP–DB has become the most likely third-place finisher and that dispersed information may justify confidence above a simple public-poll reading.

## Evidence supporting the claim

- **Polymarket current price baseline (assignment context: 0.78)**
  - Why it matters causally: the market itself is aggregating trader beliefs and potentially non-obvious local or tacit information.
  - Direct or indirect: indirect.
  - Weight: medium.

- **Politico Poll of Polls puts PP–DB in a tight cluster around mid-teens behind GERB**
  - Why it matters causally: if GERB is clearly first and PP–DB is not clearly second, third place becomes a live and plausible landing spot.
  - Direct or indirect: indirect/contextual.
  - Weight: medium.

- **Outgoing parliamentary baseline still has PP–DB among the top national blocs**
  - Why it matters causally: PP–DB has enough established support to remain in the top tier rather than risk falling far below third.
  - Direct or indirect: indirect/contextual.
  - Weight: low to medium.

## Evidence against the claim

- **The accessible poll aggregation does not clearly show PP–DB running third rather than second**
  - Why it matters causally: a three-way cluster means exact third is noisy, and a 0.78 price may overstate certainty.
  - Direct or indirect: indirect/contextual.
  - Weight: high.

- **Seat conversion can differ from vote shares, but no strong public seat model was verified here**
  - Why it matters causally: without district-level seat modelling, confidence in exact rank should be capped.
  - Direct or indirect: indirect.
  - Weight: medium.

- **Coalition treatment could matter if PP–DB structure changes before the election**
  - Why it matters causally: the contract has a dissolution clause tied to the constituent party with the largest pre-election seat count, creating an additional interpretation risk.
  - Direct or indirect: direct contract risk.
  - Weight: low to medium.

## Ambiguous or mixed evidence

- The market may know more than the accessible public pages show, especially if recent Bulgarian-language polling, district information, or trader flow is not visible here.
- The same polling cluster that makes third plausible also keeps second plausible, so it cuts both ways.

## Conflict between inputs

- Main disagreement is **weighting-based and timing-based**.
- The market appears to weight PP–DB's chance of landing specifically third much more heavily than the accessible contextual evidence supports.
- Better late-cycle Bulgarian polls or seat models would help resolve this.

## Key assumptions

- Current public polling snapshots are broadly representative.
- No major coalition rupture or reporting reinterpretation occurs before election day.
- The market is not simply stale or overconfident relative to the public evidence floor.

## Key uncertainties

- Exact latest Bulgarian polling and seat-model distribution.
- Whether recent local information materially favors a third-place finish over second.
- How coalition-dissolution contingencies would matter in practice if party structure changes.

## Disconfirming signals to watch

- New polls moving PP–DB clearly into second.
- New polls moving PP–DB clearly below both Revival and DPS, which would increase confidence in third.
- Any coalition or ballot-structure changes affecting contract interpretation.

## What would increase confidence

- A high-quality late poll average showing PP–DB consistently centered in third.
- District/seat analysis showing PP–DB's vote efficiency maps more cleanly to third than second.
- Direct accessible confirmation from official election scheduling/reporting sources without scraping issues.

## Net update logic

The market prior remains valuable: PP–DB is obviously not a fringe answer. But after checking the contract and accessible contextual sources, the public evidence looks more like "PP–DB is one of the most plausible third-place outcomes" than "PP–DB should be nearly 80%." That moves the final estimate down from the market while still keeping PP–DB as the modal single outcome.

## Suggested downstream use

- Orchestrator synthesis input.
- Decision-maker review.
- Follow-up investigation focused on better Bulgarian polling / seat conversion evidence if a sharper number is needed.