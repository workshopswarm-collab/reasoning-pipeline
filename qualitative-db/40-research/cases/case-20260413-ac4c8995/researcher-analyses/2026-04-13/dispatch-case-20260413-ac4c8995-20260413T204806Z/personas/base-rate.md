---
type: agent_finding
case_key: case-20260413-ac4c8995
dispatch_id: dispatch-case-20260413-ac4c8995-20260413T204806Z
research_run_id: 38ca8319-d97a-4030-a20a-1f490786b6c7
analysis_date: 2026-04-13
persona: base-rate
domain: politics
subdomain: elections
entity:
topic: "Will United Left (BSP) win at least one seat in the 2026 Bulgarian parliamentary election?"
question: "Will United Left (BSP) win at least one seat in the 2026 Bulgarian parliamentary election?"
driver: elections
date_created: 2026-04-13
agent: Orchestrator
stance: yes-lean
certainty: medium
importance: medium
novelty: low
time_horizon: "through election day and official/result-consensus reporting"
related_entities: []
related_drivers: ["elections"]
proposed_entities: ["BSP – United Left coalition"]
proposed_drivers: []
upstream_inputs: []
downstream_uses: []
tags: ["agent-finding", "base-rate", "bulgaria", "elections", "threshold"]
---

# Claim

Base-rate view: **Yes, BSP–United Left is more likely than not to win at least one seat**, but I am a bit below the market because this is still a threshold election and the key failure mode is a nonlinear drop below 4%.

**Evidence-floor compliance:** met using at least two meaningful sources: (1) the market's own resolution text for the governing source-of-truth logic and timing, and (2) accessible public contextual election material showing the election date, 4% threshold, BSP–United Left prior result above threshold, current parliamentary presence, and continued ballot presence. Supporting provenance is preserved in two source notes plus an assumption note and evidence map.

**Canonical-mapping check:** I used canonical driver `elections`. I did **not** force a canonical entity slug because I did not verify a clean vault entity slug for the market-relevant formation; I recorded `BSP – United Left coalition` in `proposed_entities` instead.

## Market-implied baseline

Current price is **0.735**, implying about **73.5%** probability of Yes.

## Own probability estimate

My estimate is **68%**.

## Agreement or disagreement with market

I **roughly agree but am modestly below the market**.

Why:
- The outside-view anchor is favorable. BSP–United Left is not a new entrant; it is an already seated parliamentary coalition that recently cleared the threshold by a meaningful margin.
- Bulgarian parliamentary entry is structurally governed by the 4% threshold, so recent performance around 6.8-7.3% makes Yes the default unless there is evidence of sharp deterioration.
- I stay below the market because threshold systems are discontinuous. If support slides just a few points, seat probability can collapse quickly, and I was unable in this run to recover strong late polling or directly access CIK due to technical blocking.

## Implication for the question

The default interpretation should be that **Yes is likelier than No**, but not so safe that threshold risk can be ignored. A seat-winning incumbent coalition with recent mid-single-digit support should usually re-enter parliament; the main risk is not ordinary underperformance but slipping under the legal threshold.

## Key sources used

- **Primary resolution source:** Polymarket market description and rule text, including explicit fallback to the Central Election Commission of Bulgaria (CIK) if reporting is ambiguous.
- **Key contextual source:** accessible public election-context material for the 2026 Bulgarian parliamentary election, used for election date, threshold mechanics, prior BSP–United Left result, current seats, and ballot presence.
- **Key contextual source:** accessible public BSP party context page, used for organizational durability and legacy-party base-rate context.
- Source notes:
  - `qualitative-db/40-research/cases/case-20260413-ac4c8995/researcher-source-notes/2026-04-13-base-rate-election-mechanics-and-resolution.md`
  - `qualitative-db/40-research/cases/case-20260413-ac4c8995/researcher-source-notes/2026-04-13-base-rate-bsp-context-and-prior-result.md`

Direct vs contextual:
- Direct for contract mechanics: the market rule text.
- Contextual for the probability estimate: public election and party context pages.

## Supporting evidence

- BSP–United Left reportedly won roughly **6.85-7.32%** in the prior cycle, comfortably above the **4%** seat threshold.
- The coalition currently holds **19 seats**, so this is a retention question for an already parliamentary entrant, not a first-breakthrough question.
- Accessible public election context lists BSP–United Left among contesting formations for the **19 April 2026** election.
- BSP is a longstanding national party with durable organization, making total disappearance less likely than for a weak or ad hoc list.

## Counterpoints / strongest disconfirming evidence

The strongest disconfirming consideration is **threshold fragility**. In Bulgaria's system, a party or coalition that slips below **4%** gets **zero seats**, so even a formation that recently polled or performed in the high single digits is not immune if fragmentation, voter drift, or coalition confusion cuts a few points. My other material disconfirming issue is that I did **not** recover robust fresh polling in this run, so I cannot rule out a late-cycle collapse as confidently as I would like.

## Resolution or source-of-truth interpretation

- **Election date/time check:** the market description says the election is scheduled for **19 April 2026**; the contract closes/resolves on **18 April 2026 8:00 PM ET**, i.e. before voting concludes, so this is a pre-resolution forecast on an imminent event.
- **Primary resolution logic:** consensus of credible reporting.
- **Fallback governing source of truth:** official results reported by the **Central Election Commission of Bulgaria (CIK)** if there is ambiguity.
- **What counts:** at least one seat in the next Bulgarian National Assembly as a result of this election.
- **Fallback/Other timing:** if results are not known definitively by **31 October 2026 11:59 PM ET**, the market resolves Other.
- **Naming / contract interpretation:** the market says “United Left (BSP).” Accessible contextual material uses “BSP–United Left.” I treat these as the same practical formation, but because entity naming matters for settlement, this should still be checked against official reporting if ambiguity emerges.

## Key assumptions

- BSP–United Left remains the relevant ballot line for the market label.
- The coalition remains organizationally intact through election day.
- Its support remains above the 4% threshold.

## Why this is decision-relevant

This is mainly a **threshold-retention** market. For such questions, the best base-rate anchor is not campaign narrative but recent threshold clearance plus party durability. That points to Yes, while reminding synthesis not to overstate certainty if fresh evidence on late polling is weak.

## What would falsify this interpretation / change your mind

I would move lower if any of the following appeared:
- one or more credible late polls showing BSP–United Left consistently **below 4%**;
- official or credible reporting of coalition breakup, ballot disqualification, or a naming mismatch that weakens contract mapping;
- fresh evidence that the coalition's prior support base fragmented badly enough to make sub-threshold performance likely.

I would move higher if I saw direct CIK confirmation of the exact ballot identity plus independent late polling showing the coalition safely above threshold.

## Source-quality assessment

- **Primary source used:** the market's own rule text for resolution and source-of-truth logic.
- **Most important secondary/contextual source used:** accessible public 2026 election context showing threshold mechanics, prior result, current seats, and contesting-party status.
- **Evidence independence:** **medium-low**. The sources are not fully independent in the sense of multiple separate late-cycle reporting streams; they are partly cross-referential contextual sources plus the contract itself.
- **Source-of-truth ambiguity:** **medium**. The contract is clear that CIK governs if reporting is ambiguous, but I could not directly access CIK in this environment, and the market/entity naming should be kept in view.

## Verification impact

- **Additional verification pass performed:** yes.
- I made an explicit extra pass on source-of-truth access, election date, threshold mechanics, ballot presence, and party context.
- **Material change to estimate or mechanism view:** no major change. The extra pass reinforced the structural Yes view but also confirmed that official-source access limitations and naming care justify staying a bit below market rather than matching it.

## Reusable lesson signals

- Possible durable lesson: for parliamentary seat-entry markets, recent threshold clearance plus current representation is often the dominant outside-view anchor.
- Possible missing or underbuilt driver: none clearly identified beyond existing `elections` driver.
- Possible source-quality lesson: when official election commission sites are blocked, preserve the contract's explicit fallback logic and clearly separate resolution authority from contextual evidence.
- Confidence that any lesson here is reusable: **medium**.

## Orchestrator review suggestions

- review later for durable lesson: **no**
- review later for driver candidate: **no**
- review later for canon or linkage issue: **yes**
- one-sentence reason: the market-relevant formation name (“United Left (BSP)” / “BSP–United Left”) may merit a clean canonical entity/linkage check later, but not a routine canon rewrite now.

## Recommended follow-up

A narrow follow-up would be worthwhile only if synthesis needs more confidence: verify the exact official CIK ballot naming and pull one or two independent late polls or seat projections to test whether BSP–United Left is safely above 4% or drifting toward threshold risk.