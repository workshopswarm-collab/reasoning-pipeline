---
type: assumption_note
case_key: case-20260414-fdd1ff67
dispatch_id: dispatch-case-20260414-fdd1ff67-20260414T200433Z
research_run_id: ca8bc1f5-e9c1-4900-a07d-ad70e7fb19df
analysis_date: 2026-04-14
persona: variant-view
domain: sports
subdomain: football
entity:
topic: "contract-surface interpretation for draw-vs-win ambiguity"
question: "Will Al Qadisiyah Saudi Club vs. Al Shabab Saudi Club end in a draw?"
driver:
date_created: 2026-04-14
agent: Orchestrator
status: active
certainty: low-medium
importance: high
time_horizon: event-date
related_entities: []
related_drivers: []
proposed_entities: ["al-qadsiah-fc", "al-shabab-club-riyadh"]
proposed_drivers: ["football-match-outcome-pricing"]
upstream_inputs: []
downstream_uses: []
tags: ["assumption", "contract-interpretation", "market-ambiguity"]
---

# Assumption

The assignment title correctly represents the intended market question (draw) even though the fetched Polymarket contract text appears to describe a Qadisiyah-win market.

## Why this assumption matters

The main probability estimate depends on what proposition is actually being priced. A draw market and a home-win market can have very different probabilities, so contract-surface ambiguity is first-order rather than cosmetic.

## What this assumption supports

- Treating current_price 0.76 as the market-implied probability for the draw proposition supplied in the assignment.
- Framing the variant view as skepticism toward an apparently very high draw probability rather than skepticism toward a home-win probability.

## Evidence or logic behind the assumption

- The runtime assignment repeatedly labels the case as a draw market.
- The exact output paths and persona assignment are all tied to that draw phrasing.
- The fetched market page may be mislabeled, cross-routed, or returning a neighboring sports contract text rather than the intended outcome text.

## What would falsify it

- A clean Polymarket contract fetch or independent market record showing that this slug truly resolves YES on a Qadisiyah win rather than a draw.
- Controller clarification that the assignment title is wrong.

## Early warning signs

- Other market surfaces for the same slug repeat the Qadisiyah-win wording.
- A verified odds or exchange page implies a draw probability nowhere near 76%, suggesting the title-price combination is malformed.

## What changes if this assumption fails

The main finding would need major revision because the disagreement is partly built on the implausibility of a 76% draw probability in a normal football match. If the true proposition is instead a Qadisiyah win, the current memo should not be used for decision support without relabeling and re-estimation.

## Notes that depend on this assumption

- Main finding at the assigned persona path.
- Reasoning sidecar for this run.
