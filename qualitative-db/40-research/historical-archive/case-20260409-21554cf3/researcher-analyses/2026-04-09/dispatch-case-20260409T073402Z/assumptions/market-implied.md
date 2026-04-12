---
type: assumption_note
case_key: case-20260409-21554cf3
dispatch_id: dispatch-case-20260409-21554cf3-20260409T073402Z
research_run_id: 40cb1ed4-bd75-4c99-8e87-bef5746a0e06
analysis_date: 2026-04-09
persona: market-implied
domain: crypto
subdomain: ethereum
entity: ethereum
topic: case-20260409-21554cf3 | market-implied
question: Will the price of Ethereum be above $2,100 on April 9?
driver: reliability
date_created: 2026-04-09T03:36:00-04:00
agent: orchestrator
status: active
certainty: medium
importance: high
time_horizon: intraday
related_entities: [ethereum]
related_drivers: [reliability]
proposed_entities: [binance]
proposed_drivers: []
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260409-21554cf3/researcher-analyses/2026-04-09/dispatch-case-20260409-21554cf3-20260409T073402Z/personas/market-implied.md]
tags: [intraday, threshold-market, settlement-minute]
---

# Assumption

The market's very high Yes pricing is reasonable if ETH/USDT is unlikely to fall more than about 3.8% from the observed Binance spot level before the exact 12:00 ET settlement minute.

## Why this assumption matters

The market is not asking whether ETH is generally strong; it asks whether the exact Binance 1-minute close at noon ET stays above 2100. The current premium above the strike is the main reason the market can rationally price a very high Yes probability.

## What this assumption supports

- A market-respecting view near but slightly below the 95.15% implied probability.
- The conclusion that current pricing is broadly efficient rather than obviously stale.
- The idea that the main live risk is intraday volatility into the settlement minute, not ambiguity about the source of truth.

## Evidence or logic behind the assumption

- Direct Binance API spot check showed ETHUSDT around 2183.68 at approximately 03:34 ET.
- Recent 1-minute candles around observation time were consistently above 2180.
- With only hours remaining, a drop through 2100 requires a meaningful intraday move rather than ordinary noise.
- Polymarket rules tightly define the contract, reducing interpretive uncertainty.

## What would falsify it

- ETHUSDT falling below 2100 on Binance before or at the 12:00 ET candle close.
- Evidence of elevated event risk or sharp market-wide selling likely to produce a >3.8% drawdown before settlement.
- A discovered mismatch between the expected settlement-minute mapping and Binance's actual displayed candle convention.

## Early warning signs

- ETH quickly losing the 2160-2170 area during the morning.
- A broad crypto risk-off move led by BTC or macro headlines.
- Large Binance-specific dislocation or data-display issues near settlement.

## What changes if this assumption fails

If ETH trades materially lower into noon ET, the current market price would look overconfident rather than efficient, and the correct probability would need to be marked down sharply.

## Notes that depend on this assumption

- qualitative-db/40-research/cases/case-20260409-21554cf3/researcher-analyses/2026-04-09/dispatch-case-20260409-21554cf3-20260409T073402Z/personas/market-implied.md
- qualitative-db/40-research/cases/case-20260409-21554cf3/researcher-source-notes/2026-04-09-market-implied-binance-polymarket-resolution-and-spot-check.md