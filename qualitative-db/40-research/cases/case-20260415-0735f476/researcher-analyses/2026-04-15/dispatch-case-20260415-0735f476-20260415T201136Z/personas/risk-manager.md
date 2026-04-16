---
type: agent_finding
case_key: case-20260415-0735f476
dispatch_id: dispatch-case-20260415-0735f476-20260415T201136Z
research_run_id: 9cbbd9f1-24dc-4e3e-956f-801560384ced
analysis_date: 2026-04-15
persona: risk-manager
domain: crypto
subdomain: bitcoin-threshold-market
entity: bitcoin
topic: "Binance noon ET close above 70000 on April 20"
question: "Will the price of Bitcoin be above $70,000 on April 20?"
driver: operational-risk
date_created: 2026-04-15
agent: Orchestrator
stance: yes-lean
certainty: medium
importance: high
novelty: low
time_horizon: short-term
related_entities: ["bitcoin"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: ["qualitative-db/40-research/cases/case-20260415-0735f476/researcher-source-notes/2026-04-15-risk-manager-polymarket-rules-binance-resolution.md", "qualitative-db/40-research/cases/case-20260415-0735f476/researcher-source-notes/2026-04-15-risk-manager-binance-spot-context.md", "qualitative-db/40-research/cases/case-20260415-0735f476/researcher-analyses/2026-04-15/dispatch-case-20260415-0735f476-20260415T201136Z/assumptions/risk-manager.md", "qualitative-db/40-research/cases/case-20260415-0735f476/researcher-analyses/2026-04-15/dispatch-case-20260415-0735f476-20260415T201136Z/evidence/risk-manager.md"]
downstream_uses: []
tags: ["agent-finding", "risk-manager", "btc", "polymarket", "binance", "threshold", "exact-time-close"]
---

# Claim

BTC is more likely than not to resolve Yes, and likely still deserves a high probability, because Binance BTC/USDT currently sits well above 70,000. But the market is not equivalent to "BTC is above 70,000 now"; it is a single future Binance 1-minute close at exactly 12:00 ET on April 20, so residual downside path risk is the main reason not to treat this as near-certainty.

Compliance note: evidence floor met with two meaningful sources plus an additional verification pass. Primary governing source checked directly via Polymarket rules; direct contextual exchange data checked on Binance and cross-verified with independent contextual price sources.

## Market-implied baseline

The assigned current price is 0.93, implying about 93% Yes.

That price also embeds high confidence that the present multi-thousand-dollar cushion above 70,000 will survive until the exact deadline minute.

## Own probability estimate

89% Yes.

## Agreement or disagreement with market

I slightly disagree with the market. Directionally I agree: Yes is the right lean. The disagreement is mostly about confidence, not direction.

Why I am below market:
- the contract is a narrow exact-minute-close market, not a touch market and not an end-of-day average
- settlement is venue-specific to Binance BTC/USDT
- there are still several days left, enough time for a 6%+ drawdown to erase the current cushion
- the market price above 90% leaves limited room for ordinary crypto path risk, which I think is still material

## Implication for the question

The market should still be interpreted as strongly favoring Yes, but the key risk-manager message is that the bullish thesis depends on multiple conditions all holding at once at the resolution moment, not just broad BTC strength:
1. it must be April 20, 2026
2. the relevant candle must be the Binance BTC/USDT 1-minute candle for 12:00 ET
3. the final Close must be used
4. that Close must be strictly greater than 70,000
5. Binance-specific pricing must not print below threshold even if other venues remain above

Because all conditions must hold simultaneously, this should not be treated as a riskless 93-95% lock.

## Key sources used

Primary / direct governing source:
- Polymarket rules page for this exact market, captured in `qualitative-db/40-research/cases/case-20260415-0735f476/researcher-source-notes/2026-04-15-risk-manager-polymarket-rules-binance-resolution.md`

Primary / direct contextual market source:
- Binance BTCUSDT API ticker and recent 1-minute klines, captured in `qualitative-db/40-research/cases/case-20260415-0735f476/researcher-source-notes/2026-04-15-risk-manager-binance-spot-context.md`

Secondary / contextual cross-checks:
- CoinGecko BTC/USD spot
- Coinbase BTC-USD spot

Direct vs contextual distinction:
- direct for settlement mechanics: Polymarket rules
- direct contextual for governing venue price level: Binance BTCUSDT current ticker and recent 1m candles
- contextual only, not settlement-authoritative: CoinGecko and Coinbase

## Supporting evidence

- The governing source is clearly specified: Binance BTC/USDT, 1-minute candle, 12:00 ET, final Close, strictly greater than 70,000.
- Binance spot context currently shows BTC around 74,670.53, roughly 4,670 above threshold.
- Recent Binance 1-minute closes sampled in the review were also in the mid-74.6k to 74.7k range.
- Independent contextual cross-checks from CoinGecko and Coinbase were closely aligned around 74.65k-74.71k, reducing concern that Binance is showing an isolated anomaly.
- The current setup is favorable because BTC does not need to rally further to win; it needs to avoid a substantial downside move before the deadline minute.

## Counterpoints / strongest disconfirming evidence

Strongest disconfirming consideration: the event has not yet occurred, and the contract is about one future exact minute close rather than current price level.

That matters because:
- a 6%+ drawdown over several days is not extraordinary for BTC
- weekend, macro, or crypto-specific volatility could erase the buffer
- the contract has no averaging, no touch credit, and no cross-exchange substitution
- a Binance-specific dislocation at the exact minute could still produce a losing print even if broader BTC pricing looks healthier

## Resolution or source-of-truth interpretation

Governing source of truth: Binance BTC/USDT, as specified by the Polymarket rules page for this exact market.

Explicit mechanism-specific check:
- This is not yet verified because the relevant future candle does not yet exist.
- That means "not yet verified" here equals "not yet occurred," not merely missing proof of an already-plausible touch.
- This is a close-above contract, not a touch/high contract. Intraday trading above 70,000 before noon ET on April 20 is not enough by itself.

Explicit date / deadline / timezone check:
- Resolution-relevant timestamp is April 20, 2026 at 12:00 ET.
- The market closes/resolves at 2026-04-20T12:00:00-04:00 per assignment context.
- The relevant reporting window is the single Binance 1-minute candle for 12:00 ET.

Explicit governing-source proof status:
- Proof of current governing-source context captured: Binance API ticker and recent 1-minute klines show BTC materially above threshold as of 2026-04-15.
- Proof of final settlement outcome cannot yet be captured because the decisive April 20 12:00 ET candle has not occurred.

## Key assumptions

- BTC will remain above 70,000 on Binance through the exact resolution minute.
- Binance BTC/USDT will remain broadly aligned with wider BTC/USD market pricing.
- No sudden volatility shock will compress BTC by more than the current cushion before April 20 noon ET.

## Why this is decision-relevant

This is an extreme-probability market, so the key decision question is not the obvious direction but whether confidence has become too high for the evidence quality and timing structure.

My answer: confidence is somewhat high but still directionally justified. The market likely has the right sign, but I would discount it modestly because this is still a future, venue-specific, exact-minute close.

## What would falsify this interpretation / change your mind

Evidence that would most quickly invalidate the current view:
- Binance BTC/USDT losing the current cushion and trading persistently near or below 70,000 before April 20
- a clear risk-off move or catalyst that makes a further 5-7% downside move likely by the deadline
- meaningful Binance-specific dislocation versus other major BTC/USD references

What would move me toward the market or above it:
- continued Binance closes materially above 70,000 into April 19-20
- shrinking realized volatility with no sign of exchange-specific dislocation
- persistence of a large cushion closer to the exact resolution minute

## Source-quality assessment

- Primary source used: Polymarket rules for the exact contract, plus Binance BTCUSDT ticker/1m kline data for governing-venue price context.
- Most important secondary/contextual source used: Coinbase and CoinGecko spot checks.
- Evidence independence: medium. The rule source is independent of the price sources; Coinbase and CoinGecko provide some independent contextual confirmation, though all are still observing the same broad BTC market.
- Source-of-truth ambiguity: low for mechanics, medium-low for forecast path. The governing source is clear, but future price path remains inherently uncertain.

## Verification impact

Additional verification pass performed: yes.

What was checked in the extra pass:
- Binance direct API ticker
- Binance recent 1-minute klines
- independent contextual cross-checks from CoinGecko and Coinbase
- direct reread of the governing Polymarket rule text

Did it materially change the view: no material directional change. It reinforced that Yes is the correct lean, but it also reinforced that the proper frame is an exact-minute-close contract with residual path risk, not a settled or near-settled event.

## Reusable lesson signals

- Possible durable lesson: exact-minute-close crypto threshold markets can look nearly done when spot is comfortably above threshold, but they still deserve some discount versus touch-style or already-occurred-event cases.
- Possible missing or underbuilt driver: none clearly identified from this single case.
- Possible source-quality lesson: for extreme-probability threshold markets, a quick governing-venue API check plus one or two independent contextual spot checks is a useful minimum extra verification pass.
- Confidence that any lesson here is reusable: medium-low.

## Orchestrator review suggestions

- review later for durable lesson: no
- review later for driver candidate: no
- review later for canon or linkage issue: no
- one-sentence reason: this case looks straightforward once the close-versus-touch and exact-minute timing mechanics are verified, and no clear canonical gap surfaced.

## Recommended follow-up

If the case is revisited closer to resolution, the highest-value update is a fresh Binance-specific check focused on whether the price cushion still exists approaching the April 20 12:00 ET candle.