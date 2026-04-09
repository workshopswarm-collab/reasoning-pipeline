---
type: evidence_map
case_key: case-20260409-21554cf3
dispatch_id: dispatch-case-20260409-21554cf3-20260409T073402Z
research_run_id: bdb694fc-fb8e-4ff6-af28-2bb34b139a8f
analysis_date: 2026-04-09
persona: risk-manager
domain: crypto
subdomain: exchange-market-structure
entity: ethereum
topic: will-the-price-of-ethereum-be-above-2-100-on-april-9
question: "Will the price of Ethereum be above $2,100 on April 9?"
driver: operational-risk
date_created: 2026-04-09T03:36:30-04:00
agent: risk-manager
status: draft
confidence: medium-high
conflict_status: low
action_relevance: high
related_entities: ["ethereum"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: ["binance exchange global"]
proposed_drivers: []
upstream_inputs: []
downstream_uses: []
tags: ["eth", "binance", "exact-candle", "noon-et"]
---

# Summary

This is a narrow settlement-mechanics case. Direct evidence favors Yes because Binance ETH/USDT is currently well above $2,100, but the remaining risk is concentrated in one future minute close and therefore should not be treated as certainty.

## Question being evaluated

Whether the Binance ETH/USDT 1-minute candle for 12:00 ET on 2026-04-09 will have a final close above 2,100.

## Current lean

Lean Yes, high but not absolute confidence.

## Prior / starting view

Starting view was that the market price around 95.15% likely reflected a large current spot cushion, but that the exact-candle wording could make the market somewhat more fragile than headline ETH strength suggests.

## Evidence supporting the claim

- Binance direct price evidence: recent 1-minute closes around 2181-2184 and spot ticker around 2183.31 several hours before resolution.
  - Source: 2026-04-09-risk-manager-binance-resolution-source.md
  - Why it matters: this is direct evidence from the governing venue and pair.
  - Direct or indirect: direct.
  - Weight: high.

- Polymarket rules explicitly name Binance ETH/USDT 1m at 12:00 ET.
  - Source: 2026-04-09-risk-manager-polymarket-rules-context.md
  - Why it matters: removes ambiguity about venue and comparison operator.
  - Direct or indirect: direct for contract interpretation, contextual for outcome.
  - Weight: high.

- Threshold cushion is roughly $80+ at verification time.
  - Source: Binance direct checks.
  - Why it matters causally: normal minute noise is unlikely by itself to erase that full buffer.
  - Direct or indirect: direct/contextual hybrid.
  - Weight: medium-high.

## Evidence against the claim

- Settlement depends on one exact future one-minute close, not on the current price level.
  - Source: Polymarket rules plus Binance timing logic.
  - Why it matters causally: path risk can still dominate a seemingly easy threshold market.
  - Direct or indirect: direct.
  - Weight: high.

- Binance-specific dislocation risk remains even if broad ETH markets stay firm elsewhere.
  - Source: contract source-of-truth structure.
  - Why it matters causally: only Binance ETH/USDT counts.
  - Direct or indirect: contextual.
  - Weight: medium.

- Single-source authority means evidence independence is inherently limited.
  - Source: rules architecture.
  - Why it matters causally: additional verification can check mechanics, but not diversify settlement authority.
  - Direct or indirect: contextual.
  - Weight: medium.

## Ambiguous or mixed evidence

- The web-fetched Polymarket page showed roughly 97% for the 2,100 threshold while the assignment snapshot gave 95.15%; this is not a thesis conflict, just a reminder that market price moved and should not be treated as fixed.

## Conflict between inputs

There is no material factual conflict. The only mild tension is between the market's very high confidence and the risk-manager view that exact-minute settlement leaves a little more tail risk than a casual reading suggests.

## Key assumptions

- Noon ET maps to 16:00 UTC on this date.
- Binance API timestamps and Binance UI candle labels refer to the same underlying 1-minute market data.
- ETH will not suffer a sharp exchange-specific or market-wide drop into the governing minute.

## Key uncertainties

- Intraday volatility between now and noon ET.
- Potential exchange-specific noise or wick behavior at the exact minute.
- Whether the final market move compresses the cushion materially before settlement.

## Disconfirming signals to watch

- ETH/USDT on Binance falling toward or below 2120 ahead of noon ET.
- Large volatility spikes in the hour before the resolution minute.
- Any evidence of mismatch between ET labeling and the expected 16:00 UTC candle.

## What would increase confidence

- A later-morning recheck still showing ETH comfortably above 2100.
- Continued low-volatility trading on Binance ETH/USDT as noon ET approaches.

## Net update logic

The direct Binance check was enough to establish the main directional view: Yes is favored because the authoritative venue is already well above the threshold. The extra verification mainly reinforced that the true risk is timing fragility rather than source confusion. I downweighted generic ETH-bullish context because this contract is decided by one exact Binance minute.

## Suggested downstream use

- forecast update
- orchestrator synthesis input
- retrospective evaluation of narrow exact-candle markets