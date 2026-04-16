---
type: agent_finding
case_key: case-20260413-ac4c8995
dispatch_id: dispatch-case-20260413-ac4c8995-20260413T204806Z
research_run_id: 2adddce6-efd6-4113-bab5-ae0f3105b850
analysis_date: 2026-04-13
persona: catalyst-hunter
domain: politics
subdomain: elections
entity:
topic: "Will United Left (BSP) win at least one seat in the 2026 Bulgarian parliamentary election?"
question: "Will United Left (BSP) win at least one seat in the 2026 Bulgarian parliamentary election?"
driver: elections
date_created: 2026-04-13
agent: orchestrator
stance: yes
certainty: medium
importance: high
novelty: medium
time_horizon: days
related_entities: []
related_drivers: ["elections"]
proposed_entities: ["BSP – United Left", "Bulgarian Socialist Party", "Central Election Commission of Bulgaria"]
proposed_drivers: []
upstream_inputs: []
downstream_uses: []
tags: ["bulgaria", "parliamentary-election", "bsp", "catalyst-hunter", "threshold", "evidence-floor-met"]
---

# Claim

BSP–United Left is likely to win at least one seat in the 19 April 2026 Bulgarian parliamentary election. My directional view is **Yes, about 80%**. The key catalyst logic is simple: this is fundamentally a threshold-survival question, and the coalition appears to be an established parliamentary actor still contesting the election rather than a fringe entrant flirting with zero viability.

## Market-implied baseline

The current market price is **0.735**, implying about **73.5%**.

## Own probability estimate

**80%**.

## Agreement or disagreement with market

I **roughly agree, with a modest bullish lean** versus market pricing.

Why: the market already prices BSP–United Left as more likely than not to clear the line, which is sensible. I lean somewhat higher because the available contextual evidence points to an established coalition that recently cleared the threshold comfortably and is again listed as contesting. For this contract, the most important near-term question is not whether BSP becomes large or pivotal, but whether it avoids a late collapse below the 4% parliamentary threshold.

## Implication for the question

This looks more like a **threshold monitoring** market than a broad government-formation market. If BSP–United Left remains an active ballot-qualified coalition and does not suffer a final-week polling or organizational collapse, at least one seat is the default path. The main repricing risk before resolution is a late signal that it is actually near or below threshold.

## Key sources used

**Evidence floor compliance:** met with at least two meaningful sources.

1. **Primary / governing source-of-truth surface:** Polymarket market description and contract language, which explicitly says the market resolves by consensus of credible reporting and falls back to the **Central Election Commission of Bulgaria (CIK)** if ambiguous. This is the governing resolution source for the contract.
2. **Key contextual source:** `researcher-source-notes/2026-04-13-catalyst-hunter-election-basics-and-resolution.md` based on the raw Wikipedia page for the 2026 Bulgarian parliamentary election, used for election date and threshold context.
3. **Key contextual source:** `researcher-source-notes/2026-04-13-catalyst-hunter-bsp-position-and-contestation.md` based on the raw Wikipedia pages for BSP–United Left and the 2026 election page, used for recent parliamentary baseline and evidence that the coalition is contesting.
4. **Assumption artifact:** `.../assumptions/catalyst-hunter.md`, which makes explicit that the thesis depends on BSP–United Left remaining above threshold into election day.

Direct vs contextual distinction:
- **Direct for resolution mechanics:** Polymarket contract language naming credible reporting and CIK fallback.
- **Contextual, not authoritative for the 2026 result:** Wikipedia raw pages used to establish election timing, threshold mechanics, coalition existence, and prior baseline.

## Supporting evidence

- The market resolves on whether BSP–United Left wins **at least one seat**, not on whether it wins a large bloc.
- The election is on **19 April 2026**, so the relevant catalyst window is very short and mostly about threshold risk.
- The electoral system context indicates a **4% threshold** for parties/coalitions; once above that line, an established coalition is likely to translate votes into seats.
- BSP–United Left is shown as an **existing parliamentary coalition** with a recent baseline around **7.32% and 19 seats** in the prior parliamentary result summary used here.
- BSP–United Left is listed as **contesting** the 2026 election, so this is not a speculative or dormant label.

## Counterpoints / strongest disconfirming evidence

The strongest disconfirming consideration is **source quality around current late-campaign strength**. I did not obtain a clean primary or high-grade independent polling read for 13 April 2026 from this environment. If BSP–United Left has actually slid close to or below the 4% threshold in late polling, then this contract becomes much riskier than the historical/parliamentary baseline suggests.

## Resolution or source-of-truth interpretation

The governing source of truth is the market contract itself:
- first, a **consensus of credible reporting** on the election result
- if ambiguous, fallback to the **official results reported by the Bulgarian Central Election Commission (CIK)**

That means this is ultimately an **official-results-backed seat market**, not a polling market.

Date/timing check:
- election date: **19 April 2026**
- market close / resolve timestamp in assignment: **2026-04-18 20:00 ET**, i.e. before election day in Bulgaria, so late campaign information can still move the market materially before close
- `Other` only applies if results are not known definitively by **31 October 2026 11:59 PM ET**

Canonical-mapping check:
- I found canonical driver slug **`elections`** and used it.
- I did **not** find clean canonical entity slugs for BSP–United Left, Bulgarian Socialist Party, or CIK in `qualitative-db/20-entities/`, so I left canonical entity linkage fields empty and recorded them under `proposed_entities` instead of forcing a weak fit.

## Key assumptions

- BSP–United Left remains ballot-qualified and organizationally intact into election day.
- The coalition's real support remains above the effective threshold.
- No contract-interpretation edge case emerges where a naming/coalition-label issue separates BSP from United Left for resolution purposes.

## Why this is decision-relevant

This contract likely reprices on **one or two specific catalysts**, not on diffuse narrative drift:

1. **Highest-information catalyst:** any credible final-week polling or reputable Bulgarian/wire reporting placing BSP–United Left clearly above or below 4%.
2. **Secondary catalyst:** any official reporting or reliable media indication of registration/ballot issues, coalition fracture, or withdrawal.
3. **Terminal catalyst:** election-night credible reporting and then CIK official results.

Most likely repricing path before resolution:
- absent negative surprise, price should stay elevated or grind upward as election day approaches
- a sudden drop would most likely require fresh evidence that BSP–United Left is actually in threshold danger

## What would falsify this interpretation / change your mind

I would materially reduce the estimate if any of the following appeared:
- reputable late polling showing BSP–United Left **below 4%** or clustered right at the threshold
- official or near-official evidence of ballot/registration problems
- credible reports of a coalition split, boycott, or sharp campaign implosion
- reliable reporting suggesting the contract should resolve on a narrower entity definition than the market label implies

## Source-quality assessment

- **Primary source used:** Polymarket contract language for resolution mechanics and source-of-truth logic.
- **Most important secondary/contextual source used:** raw Wikipedia page for the 2026 Bulgarian parliamentary election, supplemented by raw BSP–United Left page.
- **Evidence independence:** **low to medium**. The contextual evidence is not strongly independent because it leans on related encyclopedia summaries rather than multiple independent newsrooms or official election pages.
- **Source-of-truth ambiguity:** **low for final resolution**, because the contract names CIK as fallback; **medium for pre-election interpretation**, because live CIK access was blocked from this environment and current polling verification was limited.

## Verification impact

- **Additional verification pass performed:** yes.
- I performed extra checks on election date, threshold mechanics, coalition contestation, canonical slug availability, and the market's explicit fallback to CIK.
- **Did it materially change the view?** No major directional change. It mainly increased confidence that this is a threshold-and-timing question rather than a deeper interpretive one.

## Reusable lesson signals

- **Possible durable lesson:** for parliamentary entry markets, separate "wins seats" from "is politically relevant"; threshold mechanics dominate.
- **Possible missing or underbuilt driver:** none clearly beyond existing `elections` for this case.
- **Possible source-quality lesson:** blocked official-election sites can leave an avoidable verification gap; preserving explicit contract fallback logic is valuable.
- **Confidence that lesson is reusable:** medium.

## Orchestrator review suggestions

- **Review later for durable lesson:** no.
- **Review later for driver candidate:** no.
- **Review later for canon or linkage issue:** yes.
- **Reason:** BSP–United Left / BSP / Bulgarian CIK appear materially relevant recurring objects for Bulgarian election cases, but I did not find clean canonical entity slugs and therefore recorded them as proposed entities instead of forcing linkage.

## Recommended follow-up

- Highest-value next check before market close: one credible late poll or Bulgarian wire/media summary specifically addressing whether BSP–United Left is safely above the 4% threshold.
- If such a source shows it comfortably above threshold, the market likely deserves a modest upward lean from current 73.5%.
- If such a source shows it near/below threshold, this estimate should be revised down quickly.