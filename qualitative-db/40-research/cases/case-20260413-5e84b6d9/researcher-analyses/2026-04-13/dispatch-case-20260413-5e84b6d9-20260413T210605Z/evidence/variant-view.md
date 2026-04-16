---
type: evidence_map
case_key: case-20260413-5e84b6d9
dispatch_id: dispatch-case-20260413-5e84b6d9-20260413T210605Z
research_run_id: fe467b5d-c0cc-4490-91a7-c348d0908e1f
analysis_date: 2026-04-13
persona: variant-view
domain: politics
subdomain: bulgaria
topic: next-prime-minister-of-bulgaria
question: "Will Rumen Radev be the next prime minister of Bulgaria after the 2026 parliamentary election?"
driver: elections
date_created: 2026-04-13
agent: Orchestrator
status: draft
confidence: medium
conflict_status: moderate
action_relevance: high
related_entities: []
related_drivers: ["elections", "governance"]
proposed_entities: ["ruman-radev", "bulgarian-presidency"]
proposed_drivers: ["coalition-formation-fragility"]
upstream_inputs: []
downstream_uses: []
tags: ["evidence-netting", "resolution", "variant-view"]
entity:
---

# Summary
The variant case is that the market is too confident because it is pricing Radev’s centrality in Bulgarian politics more than the narrower event of being the first qualifying post-election sworn-in prime minister.

## Question being evaluated
Will Rumen Radev be the next individual officially sworn in as Prime Minister of Bulgaria following the April 19, 2026 parliamentary election, excluding caretaker/interim PMs and with “Other” if no one qualifies by March 31, 2027 11:59 PM ET?

## Current lean
Lean no / below-market on Radev despite his apparent frontrunner status.

## Prior / starting view
Initial baseline was that a 90% market price likely reflected very strong public reporting in favor of Radev.

## Evidence supporting the claim
- Market participants appear to view Radev as the dominant expected answer; the price itself implies strong consensus. Weight: medium. Directness: indirect.
- Radev is an established national political figure with sufficient stature to be discussed plausibly for the role. Weight: low-to-medium. Directness: contextual.

## Evidence against the claim
- The market contract is narrow: it requires actual formal swearing-in after the election. Weight: high. Directness: direct to resolution.
- Caretaker/interim PM exclusion removes a common low-quality path in unstable parliamentary contexts. Weight: high. Directness: direct to resolution.
- Government formation depends on parliamentary/institutional mechanics rather than name recognition alone. Weight: medium-to-high. Directness: contextual but causally central.
- The fallback to “Other” through March 31, 2027 creates a nontrivial deadlock path that a 90% single-name price may underweight. Weight: medium. Directness: direct to resolution.

## Ambiguous or mixed evidence
- Radev’s political prominence cuts both ways: it raises his plausibility but may also cause markets to over-anchor on him even if coalition arithmetic remains unresolved.

## Conflict between inputs
The main conflict is not factual but weighting-based: consensus pricing appears to treat Radev’s prominence as near-decisive, while the contract and institutions imply meaningful execution risk before a qualifying swearing-in occurs.

## Key assumptions
- There is still meaningful coalition-formation risk.
- No authoritative source currently settles Radev as the already-secured next PM.
- “Other” remains a live tail that should not be collapsed into near-zero.

## Key uncertainties
- Whether there is already broad credible reporting of a Radev coalition path that was not accessible through current fetch tools.
- Whether the market has high-quality local-language information unavailable in the retrieved sources.

## Disconfirming signals to watch
- Official government or parliamentary statements naming Radev as the accepted PM-designate.
- Multiple independent high-credibility reports that coalition negotiations have effectively locked in Radev.

## What would increase confidence
- Direct official Bulgarian government reporting on nomination and swearing-in mechanics.
- Independent wire reporting confirming or denying Radev’s coalition path.
- Better local-language reporting access.

## Net update logic
The market started as the baseline, but the rule wording and institutional mechanism make the near-certainty look too aggressive without stronger direct confirmation. The key update is from “Radev is prominent” to “Radev must actually be the first qualifying sworn-in PM under a contract that excludes caretaker outcomes and tolerates long deadlock.”

## Suggested downstream use
Use as orchestrator synthesis input and resolution-audit support rather than as a stand-alone forecast driver.
