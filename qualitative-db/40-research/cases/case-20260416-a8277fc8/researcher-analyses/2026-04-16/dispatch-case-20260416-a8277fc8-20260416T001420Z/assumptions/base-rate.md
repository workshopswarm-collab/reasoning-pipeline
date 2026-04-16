---
type: assumption_note
case_key: case-20260416-a8277fc8
dispatch_id: dispatch-case-20260416-a8277fc8-20260416T001420Z
research_run_id: e8526594-b409-4185-951b-611d87cde68a
analysis_date: 2026-04-16
persona: base-rate
domain: crypto
subdomain: threshold-close-markets
entity: sol
topic: "Short-dated close-above threshold persistence for SOL"
action: research
question: "Will the Binance SOL/USDT 12:00 ET 1-minute candle close on April 19, 2026 be above 80?"
driver: reliability
date_created: 2026-04-15
agent: orchestrator
status: active
certainty: medium
importance: high
time_horizon: short
related_entities: ["sol", "solana"]
related_drivers: ["reliability", "operational-risk"]
proposed_entities: []
proposed_drivers: ["threshold-close mechanics"]
upstream_inputs: ["qualitative-db/40-research/cases/case-20260416-a8277fc8/researcher-source-notes/2026-04-16-base-rate-binance-sol-price-and-contract-context.md"]
downstream_uses: ["qualitative-db/40-research/cases/case-20260416-a8277fc8/researcher-analyses/2026-04-16/dispatch-case-20260416-a8277fc8-20260416T001420Z/personas/base-rate.md"]
tags: ["assumption-note", "crypto", "sol", "short-dated"]
---

# Assumption

SOL will not suffer a roughly 5.6%-6.0% drawdown from the current mid-84s area by the specific April 19 12:00 ET 1-minute Binance close.

## Why this assumption matters

The forecast is mainly a persistence question rather than a discovery question. If the current cushion above 80 broadly persists, Yes is favored; if short-term crypto volatility erases that cushion by the deadline, No wins.

## What this assumption supports

- A Yes-leaning probability above the current market-implied baseline.
- The interpretation that current spot level is the dominant outside-view input.
- The view that no special bullish catalyst is needed for Yes to resolve.

## Evidence or logic behind the assumption

- Current Binance spot and 1-minute closes are above 84.6-84.8.
- Independent spot checks from CoinGecko and Coinbase closely match Binance.
- With only a few days remaining, the event reduces to whether ordinary crypto volatility is likely to push SOL below 80 exactly at the relevant minute.
- Base-rate logic says a modestly above-threshold asset in a short window is more likely than not to remain above, but not close to certain because crypto can move several percent quickly.

## What would falsify it

- A broad crypto selloff or SOL-specific weakness that moves Binance SOL/USDT back below 80 before the deadline.
- Material Binance-specific dislocation causing its print to diverge downward from other venues.
- Evidence that the relevant noon ET minute historically behaves with unusual volatility relative to surrounding minutes.

## Early warning signs

- SOL losing the 82-83 area before April 19.
- Sharp BTC/ETH-led risk-off move across majors.
- Binance SOL/USDT trading persistently weaker than Coinbase or broader consolidated spot.

## What changes if this assumption fails

The probability should fall sharply toward No, because this contract depends on a single exact minute close and offers no credit for trading above 80 earlier if the settlement minute closes below.

## Notes that depend on this assumption

- qualitative-db/40-research/cases/case-20260416-a8277fc8/researcher-analyses/2026-04-16/dispatch-case-20260416-a8277fc8-20260416T001420Z/personas/base-rate.md