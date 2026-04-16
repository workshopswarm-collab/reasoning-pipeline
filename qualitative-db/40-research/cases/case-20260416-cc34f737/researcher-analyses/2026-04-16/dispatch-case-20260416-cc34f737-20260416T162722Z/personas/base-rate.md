---
type: agent_finding
case_key: case-20260416-cc34f737
dispatch_id: dispatch-case-20260416-cc34f737-20260416T162722Z
research_run_id: c3a170b1-81e5-4e94-8ea5-6ba1b6daa406
analysis_date: 2026-04-16
persona: base-rate
domain: crypto
subdomain: "spot-market microstructure"
entity: ethereum
topic: "ETH noon threshold on Binance"
question: "Will the Binance ETH/USDT 12:00 ET 1-minute candle on 2026-04-17 close above 2300?"
driver: reliability
date_created: 2026-04-16
agent: Orchestrator
stance: yes-lean
certainty: medium
importance: medium
novelty: low
time_horizon: "1 day"
related_entities: ["ethereum", "binance"]
related_drivers: ["reliability", "operational-risk"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: []
tags: ["agent-finding", "crypto", "ethereum", "binance", "base-rate", "date-sensitive"]
---

# Claim

My base-rate view is modestly **Yes**: Ethereum being above $2,300 on the Binance ETH/USDT 12:00 ET one-minute candle on April 17 looks somewhat more likely than not because ETH is already trading above that threshold and recent Binance closes have usually been above it, but the edge is not huge because the contract is settled on a single minute and crypto can move more than 1-2% in less than a day.

## Market-implied baseline

The assignment gives `current_price: 0.72`, so the market-implied probability is about **72%** for Yes.

## Own probability estimate

My estimate is **64% Yes**.

## Agreement or disagreement with market

I **somewhat disagree** with the market. I agree that Yes should be favored, but 72% looks a bit rich for a one-minute, next-day crypto threshold market when the threshold is only around 1.5-1.7% below current Binance pricing. The outside view says short-horizon continuation matters, but single-minute path dependence and ordinary ETH volatility still leave a substantial No path.

## Implication for the question

The base-rate interpretation is that Yes deserves to be the favorite, but not an overwhelming one. This is more a question of whether ETH avoids a modest downside move into a very specific settlement minute than a question of whether ETH is broadly strong.

## Key sources used

Evidence floor compliance: **met with two meaningful sources (one primary rule/source-of-truth source set and one strong contextual source set).**

1. **Primary / authoritative for resolution mechanics:** Polymarket market page and rules for this exact market, which state that resolution is based on the Binance ETH/USDT 12:00 ET 1-minute candle close and specify Binance as the governing source of truth.
2. **Primary / direct exchange context:** Binance Spot API market-data documentation and public ETHUSDT endpoints, captured in source note `qualitative-db/40-research/cases/case-20260416-cc34f737/researcher-source-notes/2026-04-16-base-rate-binance-market-structure-and-recent-range.md`.

Direct vs contextual distinction:
- Direct for settlement mechanics: Polymarket rules and Binance candle definition.
- Direct for current exchange price context: Binance ETHUSDT public endpoints and recent klines.
- Contextual inference: using recent Binance closes/current spot to estimate the probability of the next-day noon threshold outcome.

## Supporting evidence

- Binance spot on 2026-04-16 was about **2335.94**, above the threshold by roughly **35.94 points**.
- Binance 5-minute average price endpoint was about **2334.26**, also above the threshold.
- Recent Binance daily closes from April 10-16 were **2245.05, 2284.99, 2191.65, 2369.46, 2322.44, 2359.95, 2335.94**; **6 of the last 7** were above 2300.
- The threshold is not far from current price, but it is still below the prevailing recent central tendency, so a continuation prior favors Yes.

## Counterpoints / strongest disconfirming evidence

The strongest disconfirming consideration is that the contract resolves on **one specific one-minute candle at noon ET**, not on the daily close or broad daily average. ETH only needs a routine sub-2% downward move by that minute to flip the market to No, which is well within ordinary crypto short-horizon volatility.

## Resolution or source-of-truth interpretation

Governing source of truth: **Binance ETH/USDT 1-minute candle close at 12:00 ET on April 17, as specified by Polymarket.**

Material conditions that all must hold for a **Yes** resolution:
1. The relevant instrument must be **Binance ETH/USDT**, not another exchange or pair.
2. The relevant interval must be the **1-minute candle**.
3. The relevant timestamp must be **12:00 ET (noon) on April 17, 2026**.
4. The relevant field is the candle's final **Close** price.
5. That close price must be **strictly higher than 2300**; equal to 2300 would be No.

Date/timing verification:
- The market closes/resolves at **2026-04-17T12:00:00-04:00**, so timezone handling matters.
- Binance API docs confirm candle mechanics and note timezone handling for klines; Polymarket specifies ET noon. Final operational reference remains the Binance ETH/USDT candle displayed/available for that minute.

Canonical-mapping check:
- Clean canonical entity slugs identified: `ethereum`, `binance`.
- Clean canonical driver slugs identified: `reliability`, `operational-risk`.
- No additional causally important entities or drivers clearly required canonical proposals for this memo.

## Key assumptions

- ETH remains in roughly the same short-run trading regime through noon ET on April 17.
- No exchange-specific anomaly on Binance materially distorts the settlement candle.
- No major overnight macro/crypto shock forces ETH materially below 2300 before settlement.

## Why this is decision-relevant

If this base-rate read is right, the market is directionally sensible but slightly overconfident. The useful takeaway is not “ETH is bullish,” but “Yes is favored, though the remaining No probability is still meaningful because of short-horizon volatility and narrow settlement mechanics.”

## What would falsify this interpretation / change your mind

- ETH trading materially below 2300 during the hours leading into noon ET on April 17.
- A sharp crypto-wide selloff or catalyst-driven risk-off move before settlement.
- Evidence that Binance noon-minute candles are behaving anomalously or that the market's contract interpretation differs from the apparent API/UI reading.

## Source-quality assessment

- Primary source used: **Polymarket rules plus Binance market-data documentation / live Binance endpoints**.
- Most important secondary/contextual source used: **recent Binance ETHUSDT daily closes and live price context from Binance endpoints**.
- Evidence independence: **medium**, because both major sources ultimately rely on Binance for the relevant price truth, though Polymarket independently specifies the contract terms.
- Source-of-truth ambiguity: **low to medium**. The contract is explicit, but there is slight ambiguity because Polymarket references the Binance website chart UI while my verification also used Binance API documentation/endpoints to understand candle mechanics.

## Verification impact

- Additional verification pass performed: **yes**.
- What was checked: contract wording, Binance candle mechanics, timezone relevance, live ETHUSDT price, and recent Binance closes.
- Material change from verification: **no major directional change**. The extra pass reinforced that Yes should be favored, but it also kept me from moving all the way up to the market because the narrow noon-minute mechanic remains genuinely fragile.

## Reusable lesson signals

- Possible durable lesson: narrow crypto threshold markets can look easier than they are because traders anchor to current spot rather than the exact settlement minute.
- Possible missing or underbuilt driver: none clearly identified from this run.
- Possible source-quality lesson: for Binance-settled contracts, it is useful to verify both the contract text and Binance candle mechanics/timezone handling explicitly.
- Confidence that any lesson here is reusable: **medium**.

## Orchestrator review suggestions

- Review later for durable lesson: **no**.
- Review later for driver candidate: **no**.
- Review later for canon or linkage issue: **no**.
- One-sentence reason: this looks like a routine, well-scoped market where the main lesson is procedural rather than a strong candidate for canon promotion.

## Recommended follow-up

If another persona is doing more case-specific or catalyst-sensitive work, the most decision-useful comparison is whether they have a concrete reason to expect a >1.5% downside move into noon ET tomorrow; absent that, the outside view remains mildly pro-Yes but below the market's confidence.