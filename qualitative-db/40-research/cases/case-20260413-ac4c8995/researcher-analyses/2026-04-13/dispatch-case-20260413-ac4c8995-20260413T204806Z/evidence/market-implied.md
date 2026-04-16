---
type: evidence_map
case_key: case-20260413-ac4c8995
dispatch_id: dispatch-case-20260413-ac4c8995-20260413T204806Z
research_run_id: 13fefed7-29bb-470b-b639-6f6f6e26ee5b
analysis_date: 2026-04-13
persona: market-implied
domain: politics
subdomain: elections
entity:
topic: will-united-left-bsp-win-at-least-one-seat-in-the-2026-bulgarian-parliamentary-election
question: "Will United Left (BSP) win at least one seat in the 2026 Bulgarian parliamentary election?"
driver: elections
date_created: 2026-04-13
agent: market-implied
status: draft
confidence: medium
conflict_status: "low visible source conflict"
action_relevance: high
related_entities: []
related_drivers: ["elections"]
proposed_entities: ["BSP – United Left", "Central Election Commission of Bulgaria"]
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260413-ac4c8995/researcher-analyses/2026-04-13/dispatch-case-20260413-ac4c8995-20260413T204806Z/personas/market-implied.md"]
tags: ["auditability", "market-vs-own-view"]
---

# Summary

The market’s 73.5% price looks directionally justified by public context, but probably a bit rich given the limited direct campaign evidence gathered in this run and the inability to access the official CIK pages directly because of anti-bot gating.

## Question being evaluated

Will United Left (BSP) win at least one seat in the 2026 Bulgarian parliamentary election?

## Current lean

Lean yes, with probability somewhat below but close to market.

## Prior / starting view

Start from the market prior of 73.5%, then ask whether public evidence supports BSP–United Left as a still-viable threshold-clearing coalition.

## Evidence supporting the claim

- BSP–United Left is described as an existing parliamentary coalition with **19 current seats**.
  - Source: source note on BSP–United Left context.
  - Why it matters: existing representation strongly raises the prior for winning at least one seat again.
  - Direct/indirect: indirect but highly relevant contextual evidence.
  - Weight: high.

- The 2026 election contextual source describes a **4% threshold** and shows BSP–United Left above that level in the prior election.
  - Source: source note on election date and resolution source.
  - Why it matters: one-seat viability is primarily about surviving the threshold.
  - Direct/indirect: indirect contextual evidence.
  - Weight: high.

- POLITICO confirms a snap election is actually scheduled for April 2026, reducing timing ambiguity.
  - Why it matters: confirms the event is live and date-sensitive as contracted.
  - Direct/indirect: contextual.
  - Weight: medium.

## Evidence against the claim

- No direct polling, registration list, or official CIK election materials were successfully accessed in this run.
  - Why it matters: missing direct verification makes a high-confidence yes thesis less robust.
  - Direct/indirect: direct gap in evidence.
  - Weight: medium.

- Parliamentary systems with thresholds can punish fragmentation abruptly; a previously represented coalition can still fall out if support decays or the coalition structure changes.
  - Why it matters: the contract requires at least one seat, but the real failure mode is a drop below threshold or identity mismatch.
  - Direct/indirect: structural contextual risk.
  - Weight: medium.

## Ambiguous or mixed evidence

- Wikipedia seat and vote-share summaries are useful and internally coherent, but not independent of upstream media and not authoritative.
- The market may be incorporating local-language polling or registration information not visible in this quick English-language pass.

## Conflict between inputs

No major factual conflict found. The tension is mostly between reasonably supportive context and missing direct verification.

## Key assumptions

- BSP–United Left remains the relevant ballot-mapped entity for the contract.
- It remains registered and politically intact enough to compete above the 4% threshold.
- No late shock has materially reduced its support.

## Key uncertainties

- Official registration status in directly accessible CIK materials.
- Fresh Bulgarian polling.
- Whether consensus reporting later tracks the exact contract label cleanly.

## Disconfirming signals to watch

- CIK registration mismatch.
- Credible polling below threshold.
- Coalition split or candidate-list dispute.

## What would increase confidence

- Direct CIK registration page access.
- Recent Bulgarian poll average showing BSP–United Left safely above 4%.
- Multiple independent Bulgarian outlets describing BSP–United Left as a likely entrant.

## Net update logic

The market prior already captured the main public logic: this is not asking whether a tiny outsider enters parliament, but whether an existing left coalition with prior threshold-clearing performance holds on for at least one seat. That supports a yes-lean. I shade below market because direct official and polling verification remained incomplete.

## Suggested downstream use

Use as orchestrator synthesis input and as a reminder that the price likely reflects continuity/threshold survival rather than aggressive bullishness.