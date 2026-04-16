---
type: agent_finding
case_key: case-20260414-9f18b170
dispatch_id: dispatch-case-20260414-9f18b170-20260414T142057Z
research_run_id: 26aa0112-d56c-4350-8c4d-e932b86dc3a4
analysis_date: 2026-04-14
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: will-bitcoin-reach-76-000-april-13-19
question: "Will Bitcoin reach $76,000 April 13-19?"
driver:
date_created: 2026-04-14
agent: Orchestrator
stance: "mildly bullish vs market"
certainty: medium
importance: medium
novelty: low
time_horizon: "2026-04-13 to 2026-04-19 ET"
related_entities: ["bitcoin"]
related_drivers: []
proposed_entities: []
proposed_drivers: ["short-horizon-crypto-threshold-touch-probability"]
upstream_inputs: []
downstream_uses: []
tags: ["bitcoin", "btc", "polymarket", "base-rate", "threshold-market"]
---

# Claim

Bitcoin reaching $76,000 at least once between Apr 13 and Apr 19 ET looks likely but not automatic. My base-rate view is that once BTC is already trading in the mid-$75k area with several days left and the contract only requires a one-minute Binance wick, the outside-view probability is a bit above the market's 89%, but not close to certainty.

## Market-implied baseline

The assignment gives current_price = 0.89, implying an 89% market probability.

## Own probability estimate

92%.

Compliance with evidence floor: met. I used two meaningful sources plus an explicit extra verification pass: (1) the Polymarket rules / Binance-resolution source note, (2) CoinGecko contextual BTC market data, and (3) a separate Kraken ticker cross-check as additional verification.

## Agreement or disagreement with market

I roughly agree with the market, but lean slightly more bullish. The market is already recognizing that this is a touch-the-threshold contract, not a weekly close-above contract. My modest disagreement comes from the structural setup: BTC was already around $75.6k-$75.7k on Apr 14, so the remaining distance to $76k was only about 0.4-0.5%, and the recent realized intraday range was much larger than that. In similar near-threshold crypto setups, a one-minute wick over the line within several remaining trading days is common enough that 89% looks a bit low rather than too high.

## Implication for the question

The key question is no longer whether BTC can stage a major breakout. It is whether BTC can trade roughly another few hundred dollars higher at any point before the week ends. Framed that way, the base rate favors Yes unless momentum breaks sharply.

## Key sources used

- Primary / authoritative rules source: Polymarket market page and embedded rules indicating resolution depends on the Binance BTC/USDT 1-minute candle high during Apr 13 12:00 AM ET through Apr 19 11:59 PM ET. See source note: `qualitative-db/40-research/cases/case-20260414-9f18b170/researcher-source-notes/2026-04-14-base-rate-binance-btc-usdt-high-and-polymarket-rules.md`
- Primary contextual exchange check: direct Binance BTC/USDT 24-hour ticker API showing high around $75,715 and last around $75,683 at the time checked. Captured in the same source note above.
- Secondary / contextual independent cross-check: CoinGecko BTC market data and 7-day OHLC showing BTC around $75,648 and a recent rise from low-$71k to high-$74k/$75k zone. See source note: `qualitative-db/40-research/cases/case-20260414-9f18b170/researcher-source-notes/2026-04-14-base-rate-coingecko-seven-day-ohlc.md`
- Extra verification pass: direct Kraken XBT/USD ticker cross-check showing spot around $75,750, used only as an additional sanity check on price level.

## Supporting evidence

- Governing source of truth is favorable to a high probability: the contract only needs one Binance BTC/USDT 1-minute candle high at or above $76,000 during the week.
- BTC was already trading in the mid-$75k area by Apr 14, leaving only a small remaining gap.
- CoinGecko OHLC data showed BTC had already moved several thousand dollars over the prior day; the remaining gap to $76k was small versus recent realized range.
- A threshold-touch market is mechanically easier to satisfy than a sustained-trade or weekly-close condition.

## Counterpoints / strongest disconfirming evidence

The strongest disconfirming consideration is simple: extreme-probability markets still fail when the price stalls just below a round-number resistance level and then reverses. The sampled Binance high was still below $76,000 at the time checked, so the event had not yet happened. If BTC rejects near $75.7k-$75.9k and trades back down, the remaining probability falls fast.

## Resolution or source-of-truth interpretation

The governing source of truth is Polymarket's embedded rule text pointing to Binance BTC/USDT high prices with 1-minute candles. The relevant window is Apr 13 12:00 AM ET through Apr 19 11:59 PM ET. Other exchanges, other pairs, or broader spot averages do not govern resolution. This matters because cross-exchange prints are only contextual; Binance is decisive.

Explicit canonical-mapping check: the important canonical entity match is clean for `btc`. I did not find a clean existing canonical driver slug for the short-horizon phenomenon of near-threshold crypto touch probability under high realized volatility, so I left canonical driver fields empty and recorded `short-horizon-crypto-threshold-touch-probability` in proposed_drivers instead of forcing a weak fit.

## Key assumptions

- BTC remains within striking distance rather than suffering a sharp reversal early in the remaining window.
- Binance remains broadly representative enough of live BTC pricing that a market-wide push higher is likely to appear there too.
- The rule text is interpreted literally: a one-minute high is sufficient, with no additional settlement wrinkle beyond the stated Binance chart source.

## Why this is decision-relevant

At 89%, the market is already pricing this as very likely. The practical decision question is whether the remaining upside is still worth respecting or whether the market is already too optimistic. My answer is that the price is high but still defensible; if anything, the extreme probability is slightly under rather than over my base-rate estimate because the required remaining move is modest and the contract condition is permissive.

## What would falsify this interpretation / change your mind

- Evidence from Binance 1-minute data that repeated attempts near the threshold are failing and BTC is losing momentum.
- A broad crypto risk-off move that quickly pushes BTC materially away from $76k, especially back toward low-$74k or below.
- Better base-rate data showing that near-threshold weekly touch markets fail materially more often than this heuristic implies.
- Any contract-language clarification that makes resolution stricter than the plain reading of the current rule text.

## Source-quality assessment

- Primary source used: Polymarket rules text identifying Binance BTC/USDT 1-minute candle highs as the governing resolution source.
- Most important secondary/contextual source used: CoinGecko BTC market data and 7-day OHLC for an independent level/range cross-check.
- Evidence independence: medium. Binance/Polymarket are tightly linked to the same mechanism; CoinGecko and Kraken provide some independent validation of the broader price level but are not independent of the underlying market reality.
- Source-of-truth ambiguity: low after explicit rule check. The contract appears operationally simple and source-specific.

## Verification impact

Yes, an additional verification pass was performed because the market-implied probability was already extreme (>85%). I cross-checked live price level with Kraken and independently checked CoinGecko contextual data after confirming the Polymarket/Binance rules. This did not materially change my view; it mainly increased confidence that the near-threshold framing was real rather than an artifact of one stale source.

## Reusable lesson signals

- Possible durable lesson: in short-horizon crypto threshold markets, once spot is already within roughly half a percent of the target and only a touch is required, outside-view touch probability may still be slightly higher than already-bullish market pricing.
- Possible missing or underbuilt driver: short-horizon crypto threshold-touch dynamics may deserve a cleaner driver concept if this pattern recurs.
- Possible source-quality lesson: for date-bounded crypto price markets, explicit verification of the named exchange and candle rule matters more than broad crypto news flow.
- Confidence that any lesson here is reusable: low-medium.

## Orchestrator review suggestions

- review later for durable lesson: no
- review later for driver candidate: yes
- review later for canon or linkage issue: no
- one-sentence reason: the analysis surfaced a recurring mechanism candidate around short-horizon threshold-touch probability, but this single low-difficulty case is not enough for a durable lesson by itself.

## Recommended follow-up

Minimal further work needed unless price action sharply reverses. If synthesis wants tighter calibration, the best next step would be to quantify historical touch rates for BTC after entering within 0.5% of a round-number threshold with 4-6 days remaining, but that is unlikely to move this estimate by more than a few points for the current case.