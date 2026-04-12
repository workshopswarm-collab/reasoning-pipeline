---
type: assumption_note
case_key: case-20260409-746679d3
dispatch_id: dispatch-case-20260409-746679d3-20260409T205932Z
research_run_id: 068d43a3-3de5-4288-bf28-4fcce89ebdfb
analysis_date: 2026-04-09
persona: variant-view
domain: crypto
subdomain: spot-market-structure
entity: ethereum
topic: ethereum-above-2100-on-april-10
question: "Will the price of Ethereum be above $2,100 on April 10?"
driver: reliability
date_created: 2026-04-09
agent: Orchestrator
status: active
certainty: medium
importance: high
time_horizon: intraday
related_entities: ["ethereum"]
related_drivers: ["reliability", "operational-risk"]
proposed_entities: ["binance-global"]
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260409-746679d3/researcher-analyses/2026-04-09/dispatch-case-20260409-746679d3-20260409T205932Z/personas/variant-view.md"]
tags: ["settlement", "timezone", "candle-interpretation"]
---

# Assumption

The resolving candle for this market should be interpreted as the Binance ETH/USDT 1-minute candle opened at 12:00:00 ET on April 10, 2026, which maps to 16:00:00 UTC under EDT.

## Why this assumption matters

If that mapping is wrong, the market could resolve off the wrong minute or off a differently labeled candle on the Binance UI, which is the main realistic path by which an otherwise obvious Yes trade could still contain hidden rule risk.

## What this assumption supports

- A high-probability Yes view.
- A conclusion that the market is directionally correct but slightly vulnerable to overconfidence on implementation details.
- Use of Binance API timing semantics as a strong proxy for the web chart settlement surface.

## Evidence or logic behind the assumption

- The market rules explicitly point to Binance ETH/USDT 1-minute candles as the resolution source.
- April 10, 2026 is in EDT, so noon ET converts to 16:00 UTC.
- Binance docs state klines are uniquely identified by open time.
- Binance live API output confirms 1-minute candles carry an open time and a close time ending at `:59.999` of the same minute.

## What would falsify it

- Direct evidence from the Binance web interface showing that the candle labeled `12:00` ET corresponds to a different open-time bucket than 16:00:00 UTC.
- A Polymarket clarification specifying settlement by end-of-minute labeling rather than Binance's open-time identification.
- Any official adjudication precedent for these daily crypto close markets that uses a different minute mapping.

## Early warning signs

- Conflicting trader commentary about which minute counts.
- UI screenshots that show a different local-time candle label convention.
- Polymarket mods issuing a clarification near settlement.

## What changes if this assumption fails

The confidence on Yes should fall modestly because contract-interpretation risk would rise; the core price-direction view may still favor Yes, but the settlement-risk discount would need to widen.

## Notes that depend on this assumption

- Main variant-view finding for this dispatch.
- Source note on Binance resolution mechanics and kline semantics.