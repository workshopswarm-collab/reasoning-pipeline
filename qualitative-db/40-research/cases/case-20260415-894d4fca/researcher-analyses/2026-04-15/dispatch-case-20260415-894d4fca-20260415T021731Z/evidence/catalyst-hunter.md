---
type: evidence_map
case_key: case-20260415-894d4fca
dispatch_id: dispatch-case-20260415-894d4fca-20260415T021731Z
research_run_id: 808d1adb-6d17-4c03-8675-f6e2c3ed253e
analysis_date: 2026-04-15
persona: catalyst-hunter
domain: politics
subdomain: surveillance-policy
entity: united-states
topic: fisa-section-702-reauthorized-before-it-expires
question: "FISA Section 702 reauthorized before it expires?"
driver:
date_created: 2026-04-15
agent: Orchestrator
status: draft
confidence: medium
conflict_status: active
action_relevance: high
related_entities: ["united-states"]
related_drivers: []
proposed_entities: ["congress-gov-house-bill-22", "house-permanent-select-committee-on-intelligence", "senate-judiciary-committee"]
proposed_drivers: ["legislative-timing-risk", "bicameral-coordination-risk"]
upstream_inputs: []
downstream_uses: []
tags: ["fisa", "section-702", "evidence-map", "catalyst"]
---

# Summary

The evidence nets to a modest Yes lean, but only because the strongest available live catalyst is an official push for a clean extension; absent that catalyst, deadline and coalition risk would push the case lower.

## Question being evaluated

Will legislation reauthorizing FISA Title VII including Section 702 pass both chambers and become law by April 19, 2026, 11:59 PM ET / before the underlying April 20, 2026 sunset effectively bites?

## Current lean

Lean Yes, but with meaningful deadline fragility.

## Prior / starting view

Starting expectation was that a critical national-security authority would usually be favored for extension, but the case was immediately limited by contract wording requiring enacted law by a specific near-term deadline.

## Evidence supporting the claim

- House Intelligence Chair Crawford said on March 19 that the President sought an 18-month clean extension and that he was working with House leadership, the ranking member, and Judiciary Chair Jordan to support it.
  - Source: case source note on Crawford statement.
  - Why it matters: this is the clearest explicit late-stage catalyst path.
  - Direct or indirect: direct on legislative intent/signaling.
  - Weight: high.

- Brookings notes Section 702 is a critical authority and that the prior reauthorization in 2024 already preserved a path to revisit it in 2026 rather than let it disappear without another fight.
  - Source: Brookings source note.
  - Why it matters: strong structural reason for Congress to avoid outright lapse.
  - Direct or indirect: indirect/contextual.
  - Weight: medium.

## Evidence against the claim

- Brookings also describes the reauthorization path as unclear and politically difficult for both parties because reform fights over U.S.-person queries and surveillance scope remain unresolved.
  - Source: Brookings source note.
  - Why it matters: coalition management, not substantive merit, is the main failure mode.
  - Direct or indirect: contextual but highly relevant.
  - Weight: high.

- The market contract is narrow: a Yes needs bicameral passage and enactment by a specific deadline, not just broad expectation, committee support, or plausible eventual renewal.
  - Source: market description and assignment prompt.
  - Why it matters: timing slippage alone can resolve No.
  - Direct or indirect: direct contract interpretation.
  - Weight: high.

## Ambiguous or mixed evidence

- Advocacy resources from Brennan Center show organized opposition and ongoing reform pressure. This cuts against a smooth clean extension, but opposition alone does not prove Congress will fail to extend under deadline pressure.

## Conflict between inputs

- The main conflict is not factual but timing-based and weighting-based.
- Official political signaling says there is an active extension push.
- Policy/context sources say the path remains politically difficult and contested.
- The missing evidence that would resolve the conflict is a real bill vehicle, floor schedule, or bicameral leadership commitment.

## Key assumptions

- If action occurs, it will likely be via a simple extension vehicle rather than a fully renegotiated reform package.
- Leadership still views lapse as too costly relative to a short extension.

## Key uncertainties

- Whether a legislative vehicle is active and viable right now.
- Whether the Senate would clear a late extension quickly.
- Whether civil-liberties and judiciary objections can delay action past the deadline even if eventual reauthorization remains likely.

## Disconfirming signals to watch

- No announced floor action as the deadline nears.
- Public signs of a Senate or House blockade.
- Shift from extension rhetoric to managing a lapse.

## What would increase confidence

- Congress.gov showing active movement on the named bill or another clear vehicle.
- Public statements from Senate leadership or key committees endorsing a deadline extension path.
- Reporting that both chambers have aligned on a clean or near-clean short-term bill.

## Net update logic

The initial national-security base rate pointed toward extension, but the contract’s strict timing requirement pulled that down. Crawford’s official statement pulled it back above even odds by identifying an actual near-term catalyst path. Contextual evidence from Brookings and civil-liberties sources prevented a higher estimate because the coalition and process risk still look real.

## Suggested downstream use

- orchestrator synthesis input
- forecast update
- follow-up investigation focused on live bill movement and floor schedule