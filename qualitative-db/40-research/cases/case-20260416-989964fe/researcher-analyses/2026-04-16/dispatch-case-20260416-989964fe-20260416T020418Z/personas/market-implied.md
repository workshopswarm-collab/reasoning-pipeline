---
type: agent_finding
case_key: case-20260416-989964fe
dispatch_id: dispatch-case-20260416-989964fe-20260416T020418Z
research_run_id: bc1386c8-af21-4134-ab96-549437c00cbc
analysis_date: 2026-04-16
persona: market-implied
domain: crypto
subdomain: ethereum
entity: ethereum
topic: will-the-binance-eth-usdt-12-00-et-one-minute-candle-close-on-2026-04-17-be-above-2200
question: "Will the Binance ETH/USDT 12:00 ET one-minute candle close on 2026-04-17 be above 2200?"
driver: reliability
date_created: 2026-04-15
agent: market-implied
stance: "mildly below market"
certainty: medium-high
importance: high
novelty: low
time_horizon: "<24h"
related_entities: ["ethereum"]
related_drivers: ["reliability", "operational-risk"]
proposed_entities: ["binance global exchange venue / exact canonical slug uncertain"]
proposed_drivers: []
upstream_inputs: []
downstream_uses: []
tags: ["crypto", "ethereum", "polymarket", "binance", "market-implied"]
---

# Claim

The 95.5 percent Yes price looks broadly justified by the evidence, because Binance ETH/USDT is currently around 2355 and the contract only asks whether the specific 12:00 ET one-minute candle close on April 17 finishes above 2200. I roughly agree with the market's direction but shade slightly lower at 92 percent because a one-minute exchange-specific settlement on a volatile crypto asset still leaves nontrivial tail risk.

## Market-implied baseline

Current market-implied probability is 95.5 percent Yes from the assigned `current_price: 0.955`.

## Own probability estimate

92 percent Yes.

## Agreement or disagreement with market

Roughly agree, but modestly below market.

The strongest case for market efficiency is straightforward: the governing venue for settlement, Binance ETH/USDT, is already trading about 155 dollars above the 2200 threshold, and an independent CoinGecko cross-check places ETH at essentially the same broad market level. That means the market is not demanding a further rally; it is pricing only the chance of a meaningful drop before a very near settlement window.

The assumption embedded in the current price is that ETH is unlikely to fall roughly 6.6 to 7 percent or more before the exact noon ET minute close. That seems reasonable. Where I differ slightly is that the contract settles on one exact minute close from one exchange, so ordinary short-horizon crypto downside and venue-specific microstructure risk deserve a bit more residual No probability than a 95.5 percent Yes price leaves.

## Implication for the question

This should be interpreted as a high-probability Yes market that looks mostly efficient rather than obviously stale or overextended. The main mechanism is simple threshold distance plus short remaining time, not hidden informational asymmetry. If anything is underweighted, it is tail risk around one exact settlement minute rather than the broad ETH level.

## Key sources used

Evidence floor compliance: met with two meaningful sources plus an explicit extra verification pass.

Primary / authoritative resolution sources:
- Polymarket rules page for `ethereum-above-on-april-17`, which explicitly states the market resolves from the Binance ETH/USDT 12:00 ET one-minute candle close and excludes other exchanges or pairs.
- Binance API spot and recent 1-minute klines for ETHUSDT, used as the governing source of truth for current price context.
- Source note: `qualitative-db/40-research/cases/case-20260416-989964fe/researcher-source-notes/2026-04-16-market-implied-binance-polymarket-resolution-and-spot.md`

Key secondary / contextual source:
- CoinGecko Ethereum USD spot and 1-day market chart as an independent broad-market cross-check.
- Source note: `qualitative-db/40-research/cases/case-20260416-989964fe/researcher-source-notes/2026-04-16-market-implied-coingecko-crosscheck.md`

Direct vs contextual evidence:
- Direct for contract interpretation: Polymarket rules.
- Direct for current settlement-venue price context: Binance spot and Binance 1m klines.
- Contextual for cross-market sanity check: CoinGecko.

Governing source of truth:
- The Binance ETH/USDT 1-minute candle labeled 12:00 ET on 2026-04-17. That is the only source that will actually resolve the contract.

## Supporting evidence

- Binance spot fetched at 2355.61, putting ETH roughly 7.1 percent above 2200 at research time.
- Recent Binance 1-minute closes clustered around 2353.88 to 2355.60, so the market is not sitting near the threshold.
- CoinGecko cross-check showed ETH at 2354.45, almost identical to Binance, reducing concern that Binance is displaying an isolated premium.
- The contract wording is narrow and mechanically clear: all that must hold for Yes is that the Binance ETH/USDT one-minute candle for 12:00 ET on April 17 has a final Close greater than 2200. The relevant conditions are:
  1. the venue must be Binance,
  2. the pair must be ETH/USDT,
  3. the timeframe must be 1 minute,
  4. the relevant candle must be the one labeled 12:00 ET on April 17,
  5. the final Close must be higher than 2200.

## Counterpoints / strongest disconfirming evidence

The strongest disconfirming consideration is not rule ambiguity; it is that crypto can move several percent inside a day, and this contract only needs one unfavorable exact-minute close on one venue to resolve No. A sharp overnight or morning selloff, or a Binance-specific print anomaly near settlement, could still beat an otherwise strong spot cushion.

## Resolution or source-of-truth interpretation

I explicitly verified the timing and contract mechanics. The assignment and Polymarket rules both point to the Binance ETH/USDT 1-minute candle for 12:00 ET on April 17, 2026. The market resolves at 12:00 PM America/New_York on 2026-04-17. This is a date-sensitive, narrow-resolution contract, so the material interpretation is:

- not any ETH/USD reference price,
- not another exchange,
- not another Binance pair,
- not intraday highs or lows,
- not whether ETH trades above 2200 at some other point,
- only whether the final Close of that exact Binance 1-minute candle is above 2200.

Source-of-truth ambiguity looks low after review, though venue-specific settlement risk remains because only Binance counts.

## Key assumptions

- ETH does not suffer a large enough downside move before noon ET to drag the exact Binance settlement minute below 2200.
- Binance remains a functioning and representative venue at settlement.
- The current cross-venue ETH level is informative for tomorrow's noon ET settlement probability.

Canonical-mapping check:
- `ethereum`, `reliability`, and `operational-risk` appear to have clean canonical slugs and were used.
- The causally important settlement venue is Binance global exchange, but the provided entity file was `binance-us.md`, which is not a clean fit for this contract. I therefore did not force a weak canonical mapping and recorded `binance global exchange venue / exact canonical slug uncertain` in `proposed_entities`.

## Why this is decision-relevant

The market is already at an extreme Yes probability, so the key question is whether that extremity is warranted or complacent. My read is that the crowd is mostly pricing the setup correctly: this is a near-dated threshold market with a sizeable cushion. That means the market deserves respect as an information-rich prior. The only meaningful caution is that a 95+ percent label on a one-minute crypto settlement should not be mistaken for certainty.

## What would falsify this interpretation / change your mind

I would move meaningfully lower if, before settlement, Binance ETH/USDT falls into the low 2200s, if broad crypto sells off sharply, or if there is evidence of Binance-specific operational or microstructure disruption near noon ET. A fresh pre-settlement check still showing Binance comfortably above 2200 would increase confidence and likely narrow the gap between my 92 percent and the market's 95.5 percent.

## Source-quality assessment

- Primary source used: Polymarket rules for settlement mechanics plus Binance ETHUSDT price and 1-minute kline data for the governing venue context.
- Most important secondary/contextual source: CoinGecko ETH/USD spot and recent market chart.
- Evidence independence: medium. Binance and Polymarket are mechanically linked by design; CoinGecko adds an independent contextual check but not an independent settlement source.
- Source-of-truth ambiguity: low. The contract wording is explicit, though one-exchange one-minute settlement creates venue-specific operational sensitivity.

## Verification impact

Yes, an additional verification pass was performed because the market-implied probability was above 85 percent and the contract is date- and rule-sensitive.

The extra pass materially improved confidence in the interpretation of the contract and confirmed there was no meaningful cross-source disagreement on the broad ETH price level. It did not materially change the directional view; it mainly kept me from overstating certainty.

## Reusable lesson signals

- Possible durable lesson: for near-dated crypto threshold markets, market extremes can be efficient when the governing exchange is already materially through the strike, but exact-minute settlement means residual tail risk should not be rounded to zero.
- Possible missing or underbuilt driver: maybe a more specific driver around single-venue settlement microstructure / exchange-specific resolution risk, though confidence is low from one case.
- Possible source-quality lesson: when Polymarket settles on one venue and one minute, use the venue itself plus at least one independent broad-market cross-check.
- Confidence that any lesson here is reusable: medium-low.

## Orchestrator review suggestions

- review later for durable lesson: no
- review later for driver candidate: no
- review later for canon or linkage issue: yes
- one-sentence reason: the settlement-relevant entity is Binance global rather than Binance US, so the current canonical entity coverage may be missing a cleaner slug for cases keyed to Binance global market data.

## Recommended follow-up

No major follow-up suggested for this lane beyond a normal pre-settlement refresh if the controller wants last-hour confirmation.