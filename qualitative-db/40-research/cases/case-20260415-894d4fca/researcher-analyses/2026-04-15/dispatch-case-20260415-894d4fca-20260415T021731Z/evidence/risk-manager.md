---
type: evidence_map
case_key: case-20260415-894d4fca
dispatch_id: dispatch-case-20260415-894d4fca-20260415T021731Z
research_run_id: d9488839-5348-438a-955c-ce9898505e22
analysis_date: 2026-04-15
persona: risk-manager
domain: politics
subdomain: surveillance-law
entity: united-states
topic: fisa-section-702-reauthorized-before-it-expires
question: "FISA Section 702 reauthorized before it expires?"
driver: operational-risk
date_created: 2026-04-15
agent: Orchestrator
status: draft
confidence: medium
conflict_status: mild-interpretive
action_relevance: high
related_entities: ["united-states"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: ["contract-interpretation-risk"]
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260415-894d4fca/researcher-analyses/2026-04-15/dispatch-case-20260415-894d4fca-20260415T021731Z/personas/risk-manager.md"]
tags: ["evidence-map", "fisa", "section-702", "contract-interpretation"]
---

# Summary
This is primarily a contract-interpretation and source-of-truth reliability case, not a fresh legislative handicapping case, if the market wording is read literally.

## Question being evaluated
Will the market resolve Yes because Section 702 has already been reauthorized by qualifying legislation before the April 19, 2026 deadline?

## Current lean
Lean Yes very strongly, with the main residual risk coming from interpretation or settlement handling rather than congressional nonperformance.

## Prior / starting view
Starting baseline was the market price of 78.5%, which already implied likely success but still meaningful failure risk.

## Evidence supporting the claim
- Polymarket market text explicitly says qualifying legislation includes Public Law 118-49.
  - Source: market-text source note.
  - Why it matters causally: if a named Public Law qualifies, the pass-both-chambers-and-become-law conditions are already met.
  - Direct or indirect: direct contract evidence.
  - Weight: very high.
- Market text gives Congress.gov / official U.S. government information as primary resolution sources.
  - Why it matters: points to official verification rather than speculative interpretation.
  - Direct or indirect: direct contract evidence.
  - Weight: high.
- Contextual statutory history indicates Section 702 was extended in 2024.
  - Source: Public Law 118-49 context note.
  - Why it matters: makes the named Public Law inclusion substantively plausible rather than obviously mistaken.
  - Direct or indirect: indirect/contextual.
  - Weight: medium.

## Evidence against the claim
- Direct independent access to Congress.gov was blocked during this run, so the official tracker could not be fetched live.
  - Why it matters causally: leaves a small but real verification gap on the governing source-of-truth surface.
  - Direct or indirect: direct process limitation.
  - Weight: medium.
- The market is still trading around 78.5% rather than near certainty.
  - Why it matters: either market participants are under-reading the contract, or there is real ambiguity about whether the named Public Law counts as intended.
  - Direct or indirect: indirect confidence signal.
  - Weight: medium.
- Multi-condition contracts can fail operationally through wording errors, source mismatches, or later clarification.
  - Why it matters: downside may come from settlement mechanics rather than substance.
  - Direct or indirect: indirect mechanism risk.
  - Weight: medium.

## Ambiguous or mixed evidence
- The market’s pointer to H.R. 22 on Congress.gov is consistent with an official tracker, but without live access it is unclear whether that tracker cleanly shows the relevant enacted law in a way that removes all ambiguity.

## Conflict between inputs
- The main disagreement is interpretive and weighting-based.
- Literal contract reading points to near-settlement.
- Market pricing implies participants still assign nontrivial uncertainty.
- The best resolving evidence would be direct official confirmation from Congress.gov that Public Law 118-49 is the qualifying enacted reauthorization referenced by the market.

## Key assumptions
- Public Law 118-49 is a genuine qualifying reauthorization under the contract.
- No later official clarification narrows the contract to future legislation only.

## Key uncertainties
- Whether any source-of-truth ambiguity remains on Congress.gov despite the market wording.
- Whether operational settlement behavior can deviate from the most literal reading.

## Disconfirming signals to watch
- Official source showing Public Law 118-49 does not qualify.
- Market clarification excluding prior enacted law.
- Credible legal reporting identifying a mismatch between the market wording and the actual statute.

## What would increase confidence
- Direct successful fetch or manual review of the Congress.gov H.R. 22 tracker confirming the enacted qualifying law status.
- A platform clarification explicitly stating that Public Law 118-49 already satisfies the contract.

## Net update logic
The biggest update versus the raw market price comes from reading the market text literally. That text appears to collapse most ordinary political timing risk. What remains is mostly operational and interpretive fragility, so the estimate moves above the market but not to 100%.

## Suggested downstream use
- forecast update
- orchestrator synthesis input
- decision-maker review focused on contract interpretation and settlement mechanics rather than congressional whip count