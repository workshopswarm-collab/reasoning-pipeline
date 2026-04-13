---
type: evidence_map
case_key: case-20260413-de71fc13
dispatch_id: dispatch-case-20260413-de71fc13-20260413T130158Z
research_run_id: 5a0b9f39-ac2e-4e97-a91c-4959e6000f5e
analysis_date: 2026-04-13
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: will-the-binance-btc-usdt-1-minute-candle-for-12-00-et-on-2026-04-13-close-above-68000
question: "Will the Binance BTC/USDT 1-minute candle for 12:00 ET on 2026-04-13 close above 68000?"
driver: reliability
date_created: 2026-04-13
agent: Orchestrator
status: draft
confidence: medium-high
conflict_status: low
action_relevance: high
related_entities: ["bitcoin"]
related_drivers: ["reliability", "operational-risk"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: []
tags: ["evidence-map", "market-implied", "intraday", "contract-interpretation"]
---

# Summary

The evidence nets to a strong Yes lean because the governing exchange/pair is already trading materially above the threshold with less than three hours left, and the main remaining risk is simply an adverse intraday move rather than an unresolved factual mystery.

## Question being evaluated

Will the Binance BTC/USDT 1-minute candle for 12:00 ET on April 13, 2026 have a final close above 68,000?

## Current lean

Strong Yes lean; market is directionally right and only mildly overconfident if one leaves room for residual intraday downside risk.

## Prior / starting view

Start from the market's 0.929 implied probability and ask whether anything in the rules or live Binance tape suggests that price is stale, misread, or overextended.

## Evidence supporting the claim

- `2026-04-13-market-implied-binance-btcusdt-klines.md` — direct / primary — high weight  
  Binance spot and recent 1-minute candles around 09:00 ET were near 71.1k, more than 3k above the strike. This means the contract is comfortably in the money with limited time remaining.

- `2026-04-13-market-implied-polymarket-rules-page.md` — direct for contract mechanics — high weight  
  The rules confirm the relevant source, pair, timeframe, and timezone. This removes ambiguity about what needs to happen for Yes.

- Extreme ladder structure on the same Polymarket page — contextual — medium weight  
  The adjacent threshold prices (70k at ~94%, 72k at ~15%) are broadly consistent with a spot near 71k and suggest the market is internally coherent rather than obviously broken.

## Evidence against the claim

- Residual intraday volatility — indirect — medium weight  
  The contract is not settled yet. A 4%+ selloff between roughly 09:00 ET and noon ET would still flip the result to No.

- Exact settlement surface mismatch — indirect / operational — low-to-medium weight  
  I verified Binance through API endpoints rather than the exact web-chart surface named in the rule text. That should usually align, but it is still a modest process caveat.

## Ambiguous or mixed evidence

- The assignment current_price is 0.929 while the fetched Polymarket page displayed the 68k line around 99.7%. That looks like either a stale assignment snapshot or a page-state timing mismatch, but both still imply an extreme Yes prior. This did not change the directional view.

## Conflict between inputs

There is no serious factual conflict. The only mismatch is timing/state drift between two market-price snapshots, which is normal for a live market page and not central to the resolution mechanism.

## Key assumptions

- Noon ET corresponds to the Binance minute beginning at 16:00 UTC / labeled 12:00 ET.
- Binance API price series is representative of the same venue data family used by the settlement chart.
- No major late-morning BTC shock occurs before settlement.

## Key uncertainties

- Magnitude of late-morning BTC volatility.
- Small operational ambiguity around exact chart/API alignment.

## Disconfirming signals to watch

- BTC/USDT falling rapidly toward 68k late in the morning.
- Binance-specific outage or pricing anomaly.
- Clarification showing a different timestamp interpretation for the noon ET candle.

## What would increase confidence

- A second late-morning verification pass closer to noon ET on Binance.
- Direct confirmation from the Binance chart UI surface if available.

## Net update logic

The evidence did not materially move me away from the market prior. Instead, it mostly validated the market's logic: same-venue pricing is comfortably above the strike, the contract mechanics are straightforward once timezone and pair are checked, and the remaining downside scenario is real but not large enough to justify a major markdown from an extreme Yes prior.

## Suggested downstream use

- Orchestrator synthesis input.
- Forecast update with explicit note that remaining risk is mostly path volatility, not evidence uncertainty.
- Retrospective evaluation of how far-from-strike intraday crypto threshold markets should still be discounted for residual volatility.