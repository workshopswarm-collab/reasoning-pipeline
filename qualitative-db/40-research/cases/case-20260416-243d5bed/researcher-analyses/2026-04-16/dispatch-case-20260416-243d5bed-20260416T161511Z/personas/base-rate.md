---
type: agent_finding
case_key: case-20260416-243d5bed
dispatch_id: dispatch-case-20260416-243d5bed-20260416T161511Z
research_run_id: 5d168321-d89e-4b52-89c8-1535c009d575
analysis_date: 2026-04-16
persona: base-rate
domain: crypto
subdomain: exchange-market-structure
entity: ethereum
topic: "ETH > 2300 on April 17 at Binance noon ET close"
question: "Will the Binance ETH/USDT 1-minute candle for 12:00 ET on April 17 close above 2300?"
driver: reliability
date_created: 2026-04-16
agent: orchestrator
stance: mildly-yes
certainty: medium
importance: medium
novelty: low
time_horizon: "1 day"
related_entities: ["binance", "ethereum"]
related_drivers: ["reliability", "operational-risk"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: []
tags: ["agent-finding", "base-rate", "crypto", "binance", "eth"]
---

# Claim

I assign **64%** probability that this market resolves **Yes**: Binance ETH/USDT's 12:00 ET one-minute candle on April 17 closes above **2300**. The outside-view case is favorable because ETH is already modestly above the threshold and recent price context puts 2300 near the current trading zone rather than far above it. But this is still a single-minute timestamp market with only a small cushion, so the probability should remain well below certainty.

**Evidence-floor compliance:** medium-difficulty case; I used (1) the direct contract/rules source and Binance kline mechanics as the authoritative/direct evidence floor, plus (2) a separate contextual ETH price-range source for outside-view calibration. I also performed an additional verification pass on live/recent Binance spot data because the market was priced above 70% and the contract is date/time specific.

## Market-implied baseline

The assigned current price is **0.745**, implying a market probability of **74.5%**.

## Own probability estimate

My estimate is **64%**.

## Agreement or disagreement with market

I **disagree modestly** with the market. The market is pricing a stronger hold-above-threshold expectation than I think the outside view warrants.

Why:
- ETH is currently above 2300 on Binance, which clearly supports Yes.
- But the contract is not "ETH trades above 2300 sometime" or even "ETH ends the day above 2300"; it is one exact **1-minute close at 12:00 ET**.
- The current cushion is only on the order of a few dozen dollars, which is small enough for ordinary crypto intraday movement to erase.
- Recent broader ETH context suggests 2300 is achievable and currently in range, but not so entrenched that a one-minute failure should be priced near three-in-four.

## Implication for the question

This should be treated as a **lean Yes, not a strong Yes**. The base-rate interpretation is that a near-threshold short-horizon crypto timestamp market usually behaves like a noisy hold test. Being above the threshold the day before matters, but not enough to eliminate meaningful one-minute downside path risk.

## Key sources used

1. **Primary / direct contract source:** Polymarket rules page for this exact market, which specifies Binance ETH/USDT, the 12:00 ET one-minute candle, and a strict "final Close price higher than 2300" condition. Captured in source note: `qualitative-db/40-research/cases/case-20260416-243d5bed/researcher-source-notes/2026-04-16-base-rate-binance-klines-and-contract.md`
2. **Primary / direct mechanics source:** Binance spot API market-data docs for `/api/v3/klines`, confirming 1-minute klines and the returned close-price field. Also captured in the same source note above.
3. **Direct current-context verification:** recent Binance ETHUSDT 1-minute kline pull on 2026-04-16 around 12:16 ET showing latest closes around 2337-2345.
4. **Secondary / contextual source:** CoinGecko 90-day ETH/USD market-chart history for outside-view range framing. Captured in source note: `qualitative-db/40-research/cases/case-20260416-243d5bed/researcher-source-notes/2026-04-16-base-rate-eth-price-context.md`

**Governing source of truth:** Binance ETH/USDT 1-minute candle data for the **12:00 ET** candle on April 17, as referenced by the Polymarket rules.

## Supporting evidence

- Direct spot context is favorable: recent Binance ETHUSDT closes were around **2337-2345**, above the 2300 threshold.
- Recent ETH context shows 2300 is an active trading-zone level rather than an extreme upside print.
- Over the last several daily observations in contextual data, ETH has repeatedly been near or above 2300, which supports a base-rate hold-above interpretation over the next day.
- There is no gathered evidence of an identified scheduled binary catalyst that obviously overwhelms the short-horizon prior.

## Counterpoints / strongest disconfirming evidence

The **strongest disconfirming consideration** is the contract structure itself: this market needs **all** of the following to hold simultaneously for Yes:
1. the relevant candle must be the Binance **ETH/USDT** candle,
2. it must be the **12:00 ET** one-minute candle on **April 17**,
3. the settlement value is the **final close** of that candle,
4. that close must be **strictly greater than 2300**.

Because the price cushion is modest, an otherwise normal crypto move could easily put the final one-minute close at 229x even if ETH spends much of the surrounding period above 2300. That narrow timestamp dependence is the main reason I stay materially below the market.

## Resolution or source-of-truth interpretation

- The market description is fairly explicit and I interpret source-of-truth ambiguity as **low to medium**, not high.
- The relevant date/time check is **April 17, 2026 at 12:00 ET (America/New_York)**, which corresponds to **16:00 UTC** on that date because April is in daylight saving time.
- The all-material conditions for Yes are: Binance spot ETH/USDT, one-minute candle, the 12:00 ET candle on April 17, final close field, and strict comparison **> 2300**.
- Other exchanges, other pairs, broader ETH/USD aggregates, intraminute highs, or prices before/after the target minute do **not** govern resolution.

## Key assumptions

- ETH remains in roughly its current trading regime through the target window rather than breaking sharply lower before noon ET.
- Binance ETH/USDT remains a reliable and representative settlement venue around the target minute.
- No major late-breaking macro or crypto-specific shock appears before resolution.

A separate assumption note was written at: `qualitative-db/40-research/cases/case-20260416-243d5bed/researcher-analyses/2026-04-16/dispatch-case-20260416-243d5bed-20260416T161511Z/assumptions/base-rate.md`

## Why this is decision-relevant

The main practical question is whether current spot-above-threshold should be treated as almost enough by itself. My answer is no. The outside view says current level matters a lot, but the single-minute resolution mechanic preserves meaningful fragility. That distinction matters if later synthesis is deciding whether the market is fairly priced versus overconfidently extrapolating current spot.

## What would falsify this interpretation / change your mind

I would move toward the market or above it if:
- ETH builds a larger cushion and is trading materially above 2300 closer to the target window,
- additional Binance-specific evidence shows especially low intraday downside volatility into noon ET,
- or there is credible information that a supportive catalyst is likely before resolution.

I would move lower if:
- ETH loses 2300 decisively before the event window,
- volatility increases sharply,
- or Binance-specific market/operational issues emerge near settlement.

## Source-quality assessment

- **Primary source used:** Polymarket rules for this exact market plus Binance spot API documentation for kline mechanics.
- **Key secondary/contextual source used:** CoinGecko ETH/USD 90-day market-chart data.
- **Evidence independence:** **medium**. Contract wording and Binance docs are separate, while current price context and CoinGecko range context are partially correlated through the same underlying ETH market.
- **Source-of-truth ambiguity:** **low to medium**. The contract is explicit, but there is still a small implementation-level ambiguity because Polymarket references the Binance UI/chart surface while my verification also used Binance API docs and recent API output.

## Verification impact

- **Extra verification performed:** yes.
- I performed an extra Binance spot-data check because the market-implied probability was above 70% and the contract is narrow, date-sensitive, and time-specific.
- **Material impact on view:** modest, not major. It reinforced that Yes should still be favored because current Binance spot is above 2300, but it did not persuade me to match the market's 74.5% because the one-minute timing fragility remained unchanged.

## Reusable lesson signals

- Possible durable lesson: timestamp-specific crypto threshold markets should be discounted relative to looser "above at any point" intuitions when the cushion is small.
- Possible missing or underbuilt driver: none confidently identified from this run.
- Possible source-quality lesson: for Binance-settled markets, preserving both the contract wording and the exchange kline field definition is useful for auditability.
- Confidence that any lesson here is reusable: **medium**.

## Orchestrator review suggestions

- review later for durable lesson: **no**
- review later for driver candidate: **no**
- review later for canon or linkage issue: **yes**
- one-sentence reason: this run used Binance as a causally important settlement venue, but I did not see a clean canonical Binance entity slug in the provided case context, so I kept it in `proposed_entities` rather than forcing a weak fit.

## Recommended follow-up

Closer to resolution, the most decision-useful follow-up would be a short refreshed check of Binance ETH/USDT level and volatility within the final few hours before **April 17 12:00 ET**.