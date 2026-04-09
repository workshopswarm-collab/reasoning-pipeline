---
type: assumption_note
case_key: case-20260406-574ca6af
dispatch_id: dispatch-case-20260406-574ca6af-20260406T013239Z
research_run_id: 98f19f60-9ceb-4985-a375-2f6fdff8e994
analysis_date: 2026-04-06
persona: catalyst-hunter
domain: crypto
subdomain: ethereum
entity: Ethereum
topic: resolution mechanics dominate over narrative catalysts near expiry
question: Will Ethereum reach $2,200 March 30-April 5?
driver: exchange-specific settlement mechanics
date_created: 2026-04-06T01:38:00Z
agent: catalyst-hunter
status: active
certainty: high
importance: high
time_horizon: immediate
related_entities: [Ethereum, Binance, Polymarket]
related_drivers: [resolution mechanics, expiry timing]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260406-574ca6af/researcher-analyses/2026-04-06/dispatch-case-20260406-574ca6af-20260406T013239Z/personas/catalyst-hunter.md]
tags: [assumption, expiry-window, binance-only]
---

# Assumption

The decisive assumption is that Polymarket will resolve strictly from finalized Binance ETH/USDT 1-minute candle highs in the ET date window, with no substitution from DEX, index, or other CEX prints.

## Why this assumption matters

If true, the market is almost entirely a mechanical question once the Binance 1-minute history is checked. If false, then cross-venue spikes or alternate settlement logic could reopen the case.

## What this assumption supports

- A low residual probability for Yes near expiry.
- The view that remaining catalysts are mostly non-material unless they produce an actual Binance ETH/USDT print through 2200 before the deadline.
- The conclusion that the market’s current 0.74 price materially overstates Yes odds if the threshold has already not been touched and little time remains.

## Evidence or logic behind the assumption

- The Polymarket market page explicitly names Binance ETH/USDT 1-minute Highs as the resolution source.
- The same page explicitly excludes other exchanges, trading pairs, and spot markets.
- Binance provides finalized 1-minute kline history directly, allowing the rule to be checked without interpretive interpolation.

## What would falsify it

- A formal Polymarket clarification or override saying another venue, pair, aggregation method, or chart source controls.
- Evidence that Binance UI/chart values materially differ from API historical kline highs for the relevant finalized candles.
- Discovery of a market-maker attribution rule or settlement hierarchy not visible on the market page that supersedes the stated rule.

## Early warning signs

- Public Polymarket moderator clarification changing the designated source.
- Disagreement between Binance charted 1-minute highs and API-returned highs around the alleged threshold.
- A late sharp cross-venue move that approaches 2200 while Binance remains just under it, increasing interpretation pressure.

## What changes if this assumption fails

The estimated probability would need to move up, potentially sharply, because alternate venues or broader spot/index measures could count even if Binance did not print 2200.

## Notes that depend on this assumption

- Main catalyst-hunter finding for this dispatch.
- Source note on Polymarket/Binance resolution and observed highs.
- Evidence map for this dispatch.
