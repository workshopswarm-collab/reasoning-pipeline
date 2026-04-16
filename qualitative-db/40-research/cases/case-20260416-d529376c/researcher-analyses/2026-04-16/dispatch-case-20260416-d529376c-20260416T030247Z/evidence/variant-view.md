---
type: evidence_map
case_key: case-20260416-d529376c
dispatch_id: dispatch-case-20260416-d529376c-20260416T030247Z
research_run_id: b27be0ee-555f-4651-86bc-3ac3cfee5667
analysis_date: 2026-04-16
persona: variant-view
domain: crypto
subdomain: token-price
entity: sol
topic: solana-above-80-on-april-19
question: "Will the Binance SOL/USDT 12:00 ET 1-minute candle close above 80 on April 19, 2026?"
driver: reliability
date_created: 2026-04-16
agent: Orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["sol", "solana"]
related_drivers: ["reliability", "operational-risk"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["variant-view-finding"]
tags: ["evidence-netting", "contract-interpretation", "crypto"]
---

# Summary

The case is directionally Yes because current Binance spot is above the threshold, but the variant view is that the market is pricing the cushion too confidently for a volatile asset over a multi-day horizon and a one-minute-close settlement rule.

## Question being evaluated

Will the Binance SOL/USDT 1-minute candle at 12:00 ET on April 19, 2026 close above 80?

## Current lean

Lean Yes, but less strongly than the market.

## Prior / starting view

Starting view was that a 91.5% market price for Yes likely implied SOL was already comfortably above 80 and the question would probably be more about timing mechanics than direction.

## Evidence supporting the claim

- **Binance direct price source:** SOLUSDT spot around 85.28-85.30 and recent 1-minute closes above 85. Weight: high. Direct.
- **Binance 24h ticker:** positive 24h change (~+2.3%), intraday high 85.83, low 82.65. Weight: medium-high. Direct/contextual.
- **CoinGecko verification:** external contextual price around 85.19 and +2.22% 24h move broadly matched Binance. Weight: medium. Indirect/contextual.
- **Distance to strike:** current level is meaningfully above 80, so No requires a multi-dollar drop by the exact settlement minute. Weight: medium. Derived.

## Evidence against the claim

- **Short-horizon crypto volatility:** a ~6% cushion over ~3.5 days is not invulnerable for SOL. Weight: high. Contextual/structural.
- **One-minute close resolution:** the contract depends on one exact noon ET minute, so transient weakness at the wrong time is sufficient for No. Weight: high. Direct from rules.
- **Extreme market confidence:** 91.5% leaves little room for ordinary downside path risk; variant view is mainly about overconfidence, not opposite direction. Weight: medium-high. Market-structure inference.

## Ambiguous or mixed evidence

- Positive recent momentum helps the Yes case, but momentum itself can reverse quickly in crypto.
- Using Binance as settlement source reduces source ambiguity, but it does not eliminate market-path uncertainty before settlement.

## Conflict between inputs

No major factual conflict across checked sources. The disagreement is weighting-based: how much safety does a current mid-80s price level provide against an 80 threshold several days away?

## Key assumptions

- The current price cushion is helpful but not so large that the market should price Yes above 90%.
- No hidden contract mechanic changes the plain reading of the noon ET 1-minute close rule.

## Key uncertainties

- Broader crypto market direction through April 19.
- Whether SOL extends upward and creates a larger buffer, or retraces into the low 80s/high 70s.
- Intraday position exactly around noon ET on settlement date.

## Disconfirming signals to watch

- SOL sustaining high-80s or better into April 18-19.
- Evidence of unusually compressed realized volatility.
- Strong cross-market risk-on continuation that materially widens the cushion.

## What would increase confidence

- More detailed realized-volatility context for recent SOL trading.
- Evidence that noon-ET prints have not been unusually weak relative to surrounding intraday levels.
- Continued price action that either preserves or erodes the current cushion.

## Net update logic

Direct exchange data makes Yes the correct directional lean. The non-consensus part is that current price level alone does not justify treating Yes as almost locked. The most important underweighted mechanism is path volatility plus the exact one-minute-close rule.

## Suggested downstream use

- forecast update
- orchestrator synthesis input
- decision-maker review