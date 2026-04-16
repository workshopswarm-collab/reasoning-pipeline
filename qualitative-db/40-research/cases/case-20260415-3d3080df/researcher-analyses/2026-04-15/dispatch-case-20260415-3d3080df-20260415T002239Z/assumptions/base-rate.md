---
type: assumption_note
case_key: case-20260415-3d3080df
dispatch_id: dispatch-case-20260415-3d3080df-20260415T002239Z
research_run_id: ac95181d-697f-4ec0-844c-dd432b46037f
analysis_date: 2026-04-15
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: bitcoin-above-70k-on-april-20
question: "Will the price of Bitcoin be above $70,000 on April 20?"
driver: operational-risk
date_created: 2026-04-14
agent: orchestrator
status: active
certainty: medium
importance: high
time_horizon: "through 2026-04-20 12:00 ET"
related_entities: ["bitcoin"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260415-3d3080df/researcher-analyses/2026-04-15/dispatch-case-20260415-3d3080df-20260415T002239Z/personas/base-rate.md"]
tags: ["assumption", "settlement", "crypto"]
---

# Assumption

The main base-rate view assumes no exchange-specific disruption or extraordinary market shock pushes Binance BTC/USDT down more than roughly 6% by noon ET on April 20.

## Why this assumption matters

The current price is materially above the strike, so the Yes thesis mostly relies on ordinary continuation and the absence of a large adverse move over a short horizon.

## What this assumption supports

- A probability estimate above the market-neutral baseline.
- Treating current spot-versus-strike distance as the dominant outside-view input.
- Downweighting vivid but currently unsupported crash narratives.

## Evidence or logic behind the assumption

- Binance spot is around 74.5k during this run, already above the target.
- Recent daily closes show BTC has spent most recent sessions above 70k.
- Over a five-day window, requiring a drop from mid-74k to below 70k by one exact minute is plausible but not the modal path absent new negative catalysts.

## What would falsify it

- A sharp BTC selloff that breaks the recent 70k support region before April 20.
- A Binance-specific outage, price dislocation, or unusual settlement ambiguity near the resolution minute.
- New macro or crypto-specific news that quickly reprices BTC risk downward.

## Early warning signs

- BTC losing 72k and then 70k on Binance with momentum.
- Large realized intraday volatility expansion and repeated rejection from the mid-74k to 76k area.
- Operational issues or unusual spreads on Binance near the event window.

## What changes if this assumption fails

If BTC decisively loses the current buffer above 70k or exchange-specific reliability becomes questionable, the base-rate Yes view should compress sharply and may flip to roughly even or No-leaning depending on timing.

## Notes that depend on this assumption

- Main persona finding for base-rate
- Source notes on Binance market data and Polymarket rules