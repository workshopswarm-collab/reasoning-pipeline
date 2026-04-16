---
type: evidence_map
case_key: case-20260416-969f7c01
dispatch_id: dispatch-case-20260416-969f7c01-20260416T013210Z
research_run_id: bf3202e7-01fb-467a-9b76-ed89ca9c9287
analysis_date: 2026-04-16
persona: catalyst-hunter
domain: crypto
subdomain: spot-market-resolution
entity: ethereum
topic: april-17-noon-binance-threshold
question: "Will the Binance ETH/USDT 12:00 ET 1-minute candle close above 2200 on April 17, 2026?"
driver: operational-risk
date_created: 2026-04-15
agent: Orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["ethereum"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: ["binance-global-spot-market"]
proposed_drivers: ["intraday-volatility-window"]
upstream_inputs: []
downstream_uses: []
tags: ["evidence-map", "catalyst-hunter", "eth"]
---

# Summary

The evidence nets to a bullish but not absolute Yes lean: the live Binance cushion over 2200 is meaningful, the contract wording is clear, and the main residual risk is a sharp downside move landing exactly into the noon ET candle.

## Question being evaluated

Will the Binance ETH/USDT 1-minute candle for 12:00 ET on April 17, 2026 have a final close above 2200?

## Current lean

Yes, with high probability but below the market's 94.5% implied level.

## Prior / starting view

Starting view was that a 94.5% market implies either a very large live cushion or an underappreciated contract nuance. The contract turned out straightforward; the main question is timing risk.

## Evidence supporting the claim

- **Binance live spot above threshold by a wide margin** — direct, high weight. Last sampled ETH/USDT trade 2353.84, about 6.9% above 2200.
- **24h low remains above threshold** — direct contextual, medium-high weight. Binance reports 24h low 2308.50, suggesting the threshold has not been recently threatened.
- **Contract wording is operationally clean** — direct, high weight. Polymarket explicitly points to the Binance ETH/USDT 12:00 ET 1m candle close and a strict above-2200 test.

## Evidence against the claim

- **Single-minute resolution risk** — direct contract/timing risk, medium-high weight. Even if ETH trades above 2200 most of the time, a localized drop into the resolving minute is sufficient for No.
- **Crypto can move >6% intraday on catalyst shocks** — indirect contextual, medium weight. The cushion is meaningful but not untouchable in crypto.
- **Binance-specific print dependency** — direct structural risk, low-medium weight. This is not a broad market VWAP or multi-exchange measure; the exact Binance close governs.

## Ambiguous or mixed evidence

- CME crypto product pages confirm active regulated ETH derivatives trading and therefore round-the-clock macro sensitivity, but they do not point to a specific bearish catalyst before resolution.
- CoinDesk market page fetch was low-value due to weak extractability here; it adds little incremental signal.

## Conflict between inputs

No major factual conflict. The tension is weighting-based: how much probability to assign to a >6% downside move into one exact minute versus the current cushion and absence of a clearly identified major scheduled catalyst.

## Key assumptions

- No major negative macro or crypto-specific catalyst lands before 2026-04-17 12:00 EDT.
- Binance market functioning remains normal enough that the final printed close is representative.

## Key uncertainties

- Unscheduled macro headlines.
- Sudden broad-crypto liquidation.
- Exchange-specific instability into the resolving minute.

## Disconfirming signals to watch

- ETH/USDT breaking below 2300 with momentum late on April 16 or early April 17.
- Broad risk-off move across BTC and equities futures during U.S. morning hours.
- Binance spread/candle anomalies near noon ET.

## What would increase confidence

- Holding comfortably above 2300 through the U.S. morning on April 17.
- No abnormal volatility or exchange-specific disruptions near the resolving window.

## Net update logic

The main update versus a generic prior was that the contract is cleaner than many rule-sensitive crypto markets, so most remaining uncertainty is genuine price risk, not interpretive risk. That supports a high Yes probability, but the narrow one-minute settlement window still argues against treating 94.5% as near-certain.

## Suggested downstream use

Use as forecast update and orchestrator synthesis input, with explicit watch on intraday downside catalysts and Binance-specific operational anomalies into the resolution window.
