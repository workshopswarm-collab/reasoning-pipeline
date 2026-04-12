---
type: evidence_map
case_key: case-20260406-574ca6af
dispatch_id: dispatch-case-20260406-574ca6af-20260406T013239Z
research_run_id: 4bdf6b0a-f878-4814-bdb6-1482c609fe49
analysis_date: 2026-04-06
persona: variant-view
topic: case-20260406-574ca6af | variant-view
question: Will Ethereum reach $2,200 March 30-April 5?
date_created: 2026-04-06
agent: Orchestrator
status: draft
confidence: high
conflict_status: low
action_relevance: high
related_entities: [ethereum, binance, polymarket, coingecko]
related_drivers: []
upstream_inputs: []
downstream_uses: [orchestrator synthesis, retrospective evaluation]
tags: [evidence-map, settlement-rules, price-threshold]
---

# Summary

The plausible variant thesis was that the market might be overconfident or sloppy about what counts as “ETH reached $2,200,” especially if broader market prints, DEX wicks, or non-Binance venues touched the level. After checking the contract mechanics and Binance-specific data, that variant does not survive: the designated venue’s observed 1m highs stayed materially below $2,200.

## Question being evaluated

Will Ethereum reach $2,200 March 30-April 5, under this market’s actual settlement rules?

## Current lean

Strong lean No; estimated probability of Yes only about 1% ex ante for any unresolved data-surface discrepancy, not because price action looked close enough on the designated source.

## Prior / starting view

Starting expectation was that a variant angle might exist via source-of-truth ambiguity or venue mismatch, since the case was flagged for CEX vs DEX and settlement hierarchy ambiguity.

## Evidence supporting the claim

- Polymarket rule text explicitly names Binance ETH/USDT 1m candle High as the settlement source and excludes other exchanges/pairs/prices. Direct, very high weight.
- Paginated Binance ETHUSDT 1m kline pull over the relevant window showed max High 2167.85, below threshold by 32.15. Direct, very high weight.
- CoinGecko contextual cross-check also stayed below $2,200, reducing odds that a broad-market breakout occurred but Binance uniquely missed it. Indirect/contextual, medium weight.

## Evidence against the claim

- The exact rule names the Binance chart UI, while the verification used Binance API klines as proxy rather than an archived screenshot of the UI chart. This is a methodology caveat, not strong directional evidence for Yes.
- The web-fetched rule text includes awkward wording about other exchanges/pairs/spot markets, which could confuse less careful readers about hierarchy. Low directional weight after direct reading.

## Ambiguous or mixed evidence

- Broader ETH sentiment or intraperiod strength could have made a Yes feel plausible in real time, but this becomes weak once the designated threshold source is checked directly.

## Conflict between inputs

There is little factual conflict. The main tension is interpretive: whether one should treat broad ETH price reports as relevant. The rules resolve that conflict in favor of Binance ETH/USDT 1m highs only.

## Key assumptions

- Binance kline API is a faithful proxy for the referenced Binance 1m chart.
- No hidden special attribution rule overrides the candle-high test.

## Key uncertainties

- Whether any reviewer would insist on direct archival proof from the exact Binance chart surface rather than API data.

## Disconfirming signals to watch

- Any Binance-native chart evidence showing a 1m High >= $2,200 in the window.
- Any overlooked Polymarket clarification altering the source hierarchy or threshold logic.

## What would increase confidence

- A direct screenshot or export from the Binance UI chart confirming the same maximum high.
- A Polymarket rules/FAQ page confirming no special market-maker attribution rule exists for this event type.

## Net update logic

The flagged ambiguity initially made a contrarian “market may be using the wrong notion of ETH price” thesis worth testing. But once the contract was narrowed to Binance ETH/USDT 1m highs and those highs were checked directly, the neglected-mechanism thesis collapsed. The market may have been directionally correct, though arguably still too high if interpreted strictly before settlement.

## Suggested downstream use

Use as orchestrator synthesis input and as retrospective evidence that rule-sensitive crypto threshold markets should be audited first for venue/interval/source hierarchy before broader price narrative work.
