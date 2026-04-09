---
type: evidence_map
case_key: case-20260409-21554cf3
dispatch_id: dispatch-case-20260409-21554cf3-20260409T073402Z
research_run_id: 40cb1ed4-bd75-4c99-8e87-bef5746a0e06
analysis_date: 2026-04-09
persona: market-implied
domain: crypto
subdomain: ethereum
entity: ethereum
topic: will-the-price-of-ethereum-be-above-2-100-on-april-9
question: "Will the price of Ethereum be above $2,100 on April 9?"
driver: reliability
date_created: 2026-04-09T03:37:00-04:00
agent: orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["binance", "ethereum"]
related_drivers: ["reliability"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260409-21554cf3/researcher-analyses/2026-04-09/dispatch-case-20260409-21554cf3-20260409T073402Z/personas/market-implied.md"]
tags: ["market-implied", "intraday", "verification", "timezone"]
---

# Summary

Evidence nets to a strong but not absolute Yes lean. The market's ~95% pricing is mostly justified by ETH trading comfortably above the strike with only hours remaining, but it is a little hard to justify full near-certainty before the exact settlement minute is observed.

## Question being evaluated

Whether Binance ETH/USDT will have a final close above 2100 on the 1-minute candle corresponding to 12:00 ET on 2026-04-09.

## Current lean

Lean Yes with high confidence, but slightly less confident than the market.

## Prior / starting view

Start from the market prior: 95.15% Yes implied by the current Polymarket price.

## Evidence supporting the claim

- **Direct Binance spot level above strike**
  - Source: source note on Binance API and Polymarket rules.
  - Why it matters causally: the contract is a simple threshold on Binance ETH/USDT.
  - Direct or indirect: direct contextual evidence.
  - Weight: very high.

- **Observed cushion versus threshold**
  - Source: Binance ticker around 2183.68 versus 2100 strike.
  - Why it matters causally: market can absorb some downside and still resolve Yes.
  - Direct or indirect: direct contextual evidence.
  - Weight: high.

- **Rules are narrow and explicit**
  - Source: Polymarket rules page.
  - Why it matters causally: reduces ambiguity about exchange, pair, timeframe, and measured field.
  - Direct or indirect: direct resolution evidence.
  - Weight: high.

## Evidence against the claim

- **Settlement depends on one exact minute close**
  - Source: Polymarket rules page.
  - Why it matters causally: even a broadly bullish day can still fail if a brief selloff hits the exact minute.
  - Direct or indirect: direct resolution-structure evidence.
  - Weight: medium.

- **Research occurred several hours before settlement**
  - Source: session time plus settlement time.
  - Why it matters causally: crypto can move materially over a few hours.
  - Direct or indirect: direct timing consideration.
  - Weight: medium.

## Ambiguous or mixed evidence

- Binance API is a direct exchange surface, but the rules cite the Binance trading page UI specifically. That is not a major ambiguity, but it is still worth noting because the exact settlement artifact is the web candle display rather than the public API endpoint.

## Conflict between inputs

No substantive source conflict found. The only issue is interpretive weighting: whether the current price cushion is enough to justify 95%+ confidence rather than something slightly lower.

## Key assumptions

- The API-observed Binance price is a fair proxy for what the web candle surface would show absent display anomalies.
- Intraday volatility before noon ET is unlikely to produce a sufficiently large selloff.

## Key uncertainties

- The exact 12:00 ET / 16:00 UTC candle close had not yet occurred.
- No independent volatility or order-flow measure was gathered beyond price-level checks.

## Disconfirming signals to watch

- ETH losing the cushion and trading near or below 2120 before noon ET.
- Exchange-specific anomalies on Binance near settlement.
- Sudden macro or crypto-specific shock causing a sharp intraday dump.

## What would increase confidence

- A fresh Binance spot/candle check closer to 12:00 ET still showing ETH clearly above 2100.
- Confirmation from Binance UI or another direct Binance-rendered surface that the exact minute mapping is interpreted the same way.

## Net update logic

The market prior already looked strong. Direct Binance checks and explicit rule review confirm that the market is probably pricing the right mechanism: ETH is already comfortably above 2100, and the contract is a narrow source-defined threshold. The only meaningful reason not to fully match the market is residual intraday volatility risk before the exact settlement minute.

## Suggested downstream use

Use as an Orchestrator synthesis input showing that the market-implied view appears broadly efficient, with only modest overconfidence risk from exact-minute settlement mechanics.