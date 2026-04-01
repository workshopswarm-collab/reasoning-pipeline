---
type: agent_finding
case_key: case-20260401-a419b7be
case_id: 62126d7c-37e0-4bde-a8c4-e498142566a2
market_id: 470d6a37-dc64-4012-a9f3-63260115f10d
title: Will Crude Oil (CL) settle at $90+ in March?
researcher: base-rate
status: complete
date: 2026-04-01
market_price: 0.868
market_implied_probability: 0.868
my_probability: 0.72
verdict_vs_market: disagree
confidence: medium
related_drivers: [energy, macro, conflicts]
upstream_inputs:
  - roles/orchestrator/pipeline-launch-procedure/planner/prompts/researcher_base_contract.md
  - roles/orchestrator/pipeline-launch-procedure/planner/prompts/researcher_base-rate.md
  - qualitative-db/00-system/roles-protocols/researcher-operating-protocol.md
  - qualitative-db/10-domains/geopolitics/energy/00-overview.md
  - qualitative-db/20-entities/organizations/opec.md
  - qualitative-db/20-entities/companies/cme-group.md
  - qualitative-db/30-drivers/energy.md
  - qualitative-db/30-drivers/macro.md
  - qualitative-db/30-drivers/conflicts.md
  - https://www.eia.gov/outlooks/steo/
  - https://www.cmegroup.com/markets/energy/crude-oil/light-sweet-crude.contractSpecs.html
  - https://fred.stlouisfed.org/series/DCOILWTICO
tags: [research, oil, crude, wti, base-rate]
---

# Base-rate finding

## Question
Will the active-month CME crude oil (CL) settlement be **$90 or higher** on the final trading day of March 2026?

## Market-implied view
Current market price is **0.868**, implying roughly **86.8%**.

## My view
My outside-view estimate is **72%**.

That is a **disagreement** with the market. I still think YES is more likely than NO, but not nearly as close to a lock as the market price implies.

## Why the base rate pulls lower than the market

### 1) $90+ WTI is not the normal regime
From a long-run outside view, WTI settling at or above $90 is a relatively elevated price regime, not the default state. Historically, crude spends a lot of time below that threshold, and periods above it are often tied to either:
- major supply disruption,
- acute geopolitical escalation,
- cartel restraint with credible compliance,
- or a macro/inventory backdrop that stays unusually tight.

The key base-rate point is that **high oil prices can persist, but they are usually conditional**, not automatic.

### 2) Even when oil spikes, holding the level into a specific resolution date is harder than narrative suggests
This market is not asking whether crude can trade above $90 intraday or for a few sessions. It asks whether the **official CME active-month settlement on the final trading day of March** is $90+.

That creates several structural frictions:
- spot-like headline moves do not always equal settlement,
- late-month mean reversion can matter,
- active-month roll mechanics reduce the value of loosely saying “oil is above $90,”
- and conflict-premium markets are especially vulnerable to retracement if outage fears ease.

Base-rate lesson: **path-dependent commodity spikes are common; clean settlement above a round threshold on a specific date is less automatic than a bullish narrative makes it sound.**

### 3) EIA’s current outlook supports high near-term prices, but also explicitly embeds temporary conflict assumptions
The March 10 EIA STEO says Brent had risen sharply, notes disrupted Hormuz shipments and shut-in Middle East production, and forecasts Brent above $95 for the next two months before falling below $80 in Q3 2026 and around $70 by year-end.

That supports the bullish side of this market. But from an outside-view perspective, the important part is **why**: the forecast is explicitly tied to modeled assumptions about conflict duration and outage persistence. That is not a normal steady-state equilibrium; it is a contingency-heavy scenario.

Because the EIA forecast itself says the price path is highly dependent on conflict/outage assumptions, the outside view should discount “currently high” a bit when translating it into an 87% probability for a specific end-of-March settlement threshold.

## Why I am still above 50%

### 1) The present regime is already near/above the threshold area
The market is not pricing an abstract possibility from a cold start. It is pricing a market that has already been pushed into a high-price regime by Middle East disruption and transit stress.

If the current disruption remains broadly in place through March, settlement at $90+ is very plausible.

### 2) EIA’s near-term price outlook is directionally supportive
EIA’s latest STEO says Brent should remain above $95 over the next two months. WTI is not Brent, but in a stressed global oil market that forecast is directionally consistent with WTI staying near levels where a $90+ settlement is realistic.

### 3) OPEC+/supply management plus geopolitical risk can keep the market tight longer than base rates alone would suggest
Outside view starts cautious, but it should not ignore live structural support. If supply risks remain active and the market continues to price constrained flows rather than quick normalization, the high-price regime can persist into the resolution date.

## Why I do not go all the way to the market
The market at **86.8%** looks too confident for a commodity threshold market with:
- a specific settlement-date requirement,
- dependence on geopolitical persistence,
- plausible de-escalation or partial flow normalization,
- and the usual commodity tendency toward volatile overshoot and retracement.

In other words, I think the market is probably **underweighting the chance that oil remains elevated but ends up settling just below the line**, or that the acute conflict premium fades enough before the relevant final settlement.

## Strongest evidence that would move me upward
I would move materially closer to the market if I saw evidence that:
- Hormuz disruption/outages were likely to persist through the end of March rather than just the near term,
- physical balances and inventories were tightening further rather than stabilizing,
- OPEC+ restraint remained credible and additive rather than mostly rhetorical,
- and front-month/active-month structure remained firmly supportive of a late-month $90+ settlement.

## Strongest evidence that would move me downward
I would move lower if I saw evidence that:
- shipping/transit conditions were normalizing,
- shut-in production was returning faster than expected,
- the move was mostly fear premium rather than sustained physical tightness,
- or the active-month contract most relevant for settlement was trading with enough discount/mean reversion risk to threaten a sub-$90 settlement.

## Bottom line
**Base-rate estimate: 72% YES.**

I agree with the broad bullish direction, because the market is already in an unusually tight, conflict-sensitive regime and EIA’s near-term outlook is supportive. But I **disagree with the market’s 86.8% confidence**. The outside view says $90+ crude is an elevated, conditional state, and converting a live spike into a specific late-March CME settlement above a round-number threshold is not as close to certain as the market implies.

## Source quality / provenance notes
- **EIA STEO**: strongest primary/public macro-energy source used here; especially relevant because it gives a current official outlook and explicitly describes the conflict/outage assumptions behind the high-price scenario.
- **CME contract specs**: used to ground the market in the actual active-month futures context rather than generic spot oil commentary.
- **FRED/EIA WTI history page**: used as a historical anchor confirming that WTI history exists as a long-run series suitable for outside-view framing, even though this note does not rely on a precise bespoke historical frequency calculation.

## Uncertainty
Main uncertainty is that the current market regime is conflict-driven and can therefore persist longer than a simple historical average would suggest. The main risk to this note is underestimating how sticky the current supply disruption is through the exact resolution window.