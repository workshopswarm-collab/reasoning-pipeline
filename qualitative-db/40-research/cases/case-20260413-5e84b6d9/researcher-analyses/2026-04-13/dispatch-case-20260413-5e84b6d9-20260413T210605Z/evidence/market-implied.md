---
type: evidence_map
case_key: case-20260413-5e84b6d9
dispatch_id: dispatch-case-20260413-5e84b6d9-20260413T210605Z
research_run_id: 67c92cab-7846-4dfe-88d4-42ea3dcf61d4
analysis_date: 2026-04-13
persona: market-implied
domain: politics
subdomain: bulgaria
entity:
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
related_drivers: ["elections"]
proposed_entities: ["rumen-radev", "progressive-bulgaria", "andrey-gurov"]
proposed_drivers: []
upstream_inputs: []
downstream_uses: []
tags: ["evidence-map", "bulgaria", "election", "market-implied"]
---

# Summary

The market’s pro-Radev case is understandable but overconfident relative to the public evidence reviewed here.

## Question being evaluated

Will Rumen Radev be the next individual officially sworn in as Prime Minister of Bulgaria after the 2026 parliamentary election, excluding interim or caretaker prime ministers?

## Current lean

Lean yes, but materially below the market price.

## Prior / starting view

Starting baseline was the live market price of 90.35%, treated as an information-rich prior.

## Evidence supporting the claim

- Public election reporting says Radev resigned in January 2026 and formed Progressive Bulgaria to contest the election.
  - Source: Wikipedia election page / summary review.
  - Why it matters: makes the contract outcome at least facially plausible.
  - Direct or indirect: indirect/contextual.
  - Weight: medium.

- Prime minister office is typically tied to parliamentary coalition leadership, so the market may be pricing coalition focal-point status rather than current incumbency.
  - Source: Prime Minister of Bulgaria page.
  - Why it matters: clarifies mechanism.
  - Direct or indirect: contextual.
  - Weight: low-to-medium.

- Contract excludes caretaker prime ministers, and the current government homepage still highlights Prime Minister Andrey Gurov during the caretaker period.
  - Source: Bulgarian government homepage.
  - Why it matters: strengthens the interpretation that current officeholding does not resolve the market.
  - Direct or indirect: direct on current officeholder; indirect on Radev.
  - Weight: medium.

## Evidence against the claim

- No authoritative Bulgarian government or parliament source reviewed here directly says Radev is the probable next sworn PM or confirms a governing coalition path.
  - Why it matters causally: the market is pricing a specific post-election coalition outcome, not just eligibility.
  - Direct or indirect: direct absence of authoritative confirmation.
  - Weight: high.

- The market is at an extreme probability despite a highly contingent parliamentary-coalition process and a rule-sensitive contract.
  - Why it matters causally: extreme pricing requires unusually strong evidence that was not visible in this pass.
  - Direct or indirect: interpretive.
  - Weight: high.

- The election is still pending as of 13 April 2026, so even a leading candidate can fail to become the first sworn non-caretaker PM.
  - Why it matters causally: coalition bargaining and formal swearing-in are separate hurdles.
  - Direct or indirect: direct institutional logic.
  - Weight: high.

## Ambiguous or mixed evidence

- Public web sources describe Radev’s campaign role, but source quality is mixed and could reflect rapidly evolving or contested reporting.
- The market may know more than was visible in this pass, but that informational edge is not auditable from price alone.

## Conflict between inputs

The main conflict is not factual in the narrow sense; it is between market confidence and publicly auditable proof quality. The market says near-certainty. The source set supports plausibility and maybe favoritism, but not near-certainty.

## Key assumptions

- Radev is indeed an active and viable post-election coalition focal point.
- No rival coalition candidate will be sworn first.
- Consensus reporting, if needed for resolution, will align with official Bulgarian government information.

## Key uncertainties

- Registered candidacy and coalition arithmetic from authoritative Bulgarian sources.
- Whether major parties would support or block a Radev-led government.
- Whether a delayed stalemate could push resolution toward another individual or even Other.

## Disconfirming signals to watch

- Official or high-credibility reporting that another coalition leader has the first mandate path.
- Strong anti-Radev coalition statements by pivotal parties.
- Election results that leave Progressive Bulgaria unable to anchor a government.

## What would increase confidence

- Official Bulgarian election or government documentation linking Radev clearly to the government-formation path.
- Independent high-quality reporting showing dominant coalition odds in his favor.
- Post-election mandate / swearing-in timelines pointing specifically to him.

## Net update logic

The evidence converted “possible but maybe misread market” into “Radev is a plausible favorite,” but it did not justify staying anywhere near 90%. What mattered most was the distinction between eligibility/mechanism evidence and actual coalition-outcome evidence.

## Suggested downstream use

Use as an Orchestrator synthesis input and as a prompt for any resolver or legalistic persona to double-check official Bulgarian source-of-truth pathways.