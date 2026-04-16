---
type: agent_finding
case_key: case-20260414-9c18e804
dispatch_id: dispatch-case-20260414-9c18e804-20260414T135145Z
research_run_id: 30bb7de4-3878-4aee-8cbe-953f9f737bbd
analysis_date: 2026-04-14
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: "weekly bitcoin threshold-touch market"
question: "Will Bitcoin reach $76,000 April 13-19?"
date_created: 2026-04-14
agent: base-rate
stance: yes-lean
certainty: medium
importance: medium
novelty: low
time_horizon: days
related_entities: ["bitcoin"]
related_drivers: []
proposed_entities: []
proposed_drivers: ["intraperiod-threshold-touch-dynamics"]
upstream_inputs: []
downstream_uses: []
tags: ["btc", "polymarket", "base-rate", "weekly-hit-price"]
driver:
---

# Claim

BTC is more likely than not to touch $76,000 on Binance during Apr 13-19, but the market looks somewhat too optimistic. My base-rate estimate is **76%**, versus the market-implied **82.5%**.

**Evidence-floor compliance:** met. I used (1) the Polymarket event page / embedded JSON as the primary source for live pricing and governing rules, and (2) independent exchange price data from Binance and Coinbase for recent BTC path/context. I also performed an additional verification pass because the market was above the 85%/below 15% trigger neighborhood in spirit and my estimate differs from market by more than a few points.

## Market-implied baseline

The assigned market current_price was 0.75, but the live Polymarket event JSON checked during this run showed the specific `$76k` market at **0.825 Yes / 0.175 No**, with best bid/ask roughly **0.81 / 0.84**. I treat **82.5%** as the live market-implied probability for comparison.

## Own probability estimate

**76% Yes**.

## Agreement or disagreement with market

**Roughly agree on direction, but mildly disagree on level.**

The market is directionally sensible because this is a **touch-style** contract, not a weekly close contract. BTC was already trading within about 1% of the threshold in checked exchange data, and there were still nearly six days left in the window. That combination usually makes a threshold-touch event fairly likely.

I mark the market somewhat rich because 82.5% implies something close to “expected unless something unusual intervenes.” From an outside-view perspective, being near a round-number threshold is favorable, but not enough to make failure rare. Short-dated crypto thresholds still miss often enough through stall, rejection, or risk-off reversal that I do not want to go all the way to the low/mid-80s without stronger direct intraday evidence.

## Implication for the question

The best base-rate read is **Yes is favored, but not close to certain**. This should be interpreted as a moderately strong but not overwhelming positive setup: current distance-to-threshold and remaining time do most of the work, while the residual No case is basically “momentum stalls before the wick arrives.”

## Key sources used

- **Primary / authoritative for rules and pricing:** Polymarket event page and embedded JSON for `what-price-will-bitcoin-hit-april-13-19`, including the specific `will-bitcoin-reach-76k-april-13-19` market and its rule text. See source note: `qualitative-db/40-research/cases/case-20260414-9c18e804/researcher-source-notes/2026-04-14-base-rate-polymarket-rules-and-pricing.md`
- **Contextual but strong market-data source:** Binance BTCUSDT daily klines API for recent highs.
- **Independent contextual cross-check:** Coinbase BTC-USD daily candles API for recent highs. See source note: `qualitative-db/40-research/cases/case-20260414-9c18e804/researcher-source-notes/2026-04-14-base-rate-binance-coinbase-price-context.md`
- **Assumption note:** `qualitative-db/40-research/cases/case-20260414-9c18e804/researcher-analyses/2026-04-14/dispatch-case-20260414-9c18e804-20260414T135145Z/assumptions/base-rate.md`

Direct vs contextual split:
- **Direct for settlement mechanics:** Polymarket rules naming Binance BTC/USDT 1-minute highs.
- **Contextual for probability:** recent Binance/Coinbase daily highs showing BTC already near 76k.

## Supporting evidence

- The contract resolves on **any Binance BTC/USDT 1-minute high >= 76,000** during the window, which is materially easier than requiring a daily or weekly close above 76k.
- Checked recent exchange data put BTC already around **75.4k-75.5k** on recent highs, i.e. only about **1%** below the threshold.
- There are still almost six days left in the contract window from the time checked, which is a lot of time for BTC to print a brief wick through a nearby round number.
- Neighboring ladder prices are internally coherent: 74k has already resolved Yes, 78k trades around mid-40s, 80k around high-teens, 82k around mid-single digits. That makes 76k as favorite outcome structurally plausible.

## Counterpoints / strongest disconfirming evidence

The strongest disconfirming consideration is simple: **BTC had not yet clearly touched 76k in the current window when checked, despite already trading near it.** Near-threshold setups often fail through repeated rejection, and 82.5% leaves limited room for a stall or reversal scenario. If momentum fades and BTC backs off into the low-70ks, the miss path becomes very live.

## Resolution or source-of-truth interpretation

This section matters a lot here.

- The governing source of truth is **Binance BTC/USDT 1-minute candle `High` prices**.
- The contract is **touch-based**: it resolves Yes if **any** 1-minute candle high during Apr 13-19 ET reaches or exceeds 76,000.
- It is **not** based on the weekly closing price, daily close, Coinbase, CoinMarketCap, or cross-exchange spot composites.
- The rules explicitly exclude other exchanges, other trading pairs, and other spot markets.

So the relevant question is not “Will BTC end the week above 76k?” but “Will Binance print even a momentary 76k wick sometime during the window?” That interpretation is the main reason the probability is high.

## Key assumptions

- The recent BTC volatility regime remains roughly intact over the remaining days.
- Binance BTC/USDT behavior will remain representative enough that a broad BTC move near 76k would likely print on the governing source.
- No abrupt regime break lower dominates the rest of the week.

## Why this is decision-relevant

If a synthesizer treats this as a close-above threshold market, it will understate Yes odds. If it treats “already near threshold” as almost equivalent to “will definitely touch,” it will overstate Yes odds. The right outside-view framing is in between: touch contracts are easier than they look, but still miss often enough that 80%+ deserves some skepticism.

## What would falsify this interpretation / change your mind

I would move lower if:
- intraday data showed repeated rejection below 75.5k with momentum fading,
- BTC sold off materially away from the threshold into the low-70ks,
- realized volatility compressed sharply, reducing touch probability.

I would move higher if:
- Binance 1-minute data showed repeated tests of 75.8k-75.9k,
- BTC regained strong upside momentum and the threshold became effectively one ordinary intraday swing away,
- additional direct Binance intraday evidence showed the market was understating wick frequency around nearby round numbers.

## Source-quality assessment

- **Primary source used:** Polymarket event page / embedded JSON with explicit rule text for the exact contract.
- **Most important secondary/contextual source used:** Binance BTCUSDT daily klines, cross-checked against Coinbase BTC-USD daily candles.
- **Evidence independence:** **medium**. The contextual price sources are partly independent (Binance + Coinbase), but both reflect the same underlying BTC market regime.
- **Source-of-truth ambiguity:** **low after verification**. The page’s generic FAQ copy was noisy, but the embedded market JSON and rules text were explicit that settlement uses Binance BTC/USDT 1-minute highs.

## Verification impact

- **Additional verification pass performed:** yes.
- **Did it materially change the estimate or mechanism view?** It clarified the mechanism more than the level.
- The extra pass confirmed the exact source of truth and the live 82.5% pricing, which strengthened confidence that this should be analyzed as a threshold-touch problem. It did not move me all the way to the market because the outside-view miss path still looks nontrivial.

## Reusable lesson signals

- Possible durable lesson: **short-dated crypto “reach X” contracts can be materially easier than naive readers expect because they are wick/touch contracts, not close contracts.**
- Possible missing or underbuilt driver: **intraperiod-threshold-touch-dynamics** for markets where remaining time, current distance, and volatility interact.
- Possible source-quality lesson: Polymarket page FAQ copy can be generic/noisy; embedded market JSON plus explicit rules text are safer for precise contract interpretation.
- Confidence that any lesson here is reusable: **medium**.

## Orchestrator review suggestions

- review later for durable lesson: **yes**
- review later for driver candidate: **yes**
- review later for canon or linkage issue: **no**
- one-sentence reason: Threshold-touch versus close-based interpretation is recurring and decision-relevant in crypto price markets, and may deserve a reusable driver or lesson note.

## Canonical-mapping check

- Canonical entities checked: `btc`, `bitcoin` exist and are used.
- Canonical drivers checked: no clean existing driver slug was provided for this mechanism.
- Important unmapped driver recorded in `proposed_drivers`: **intraperiod-threshold-touch-dynamics**.
- No weak canonical driver fit was forced.

## Recommended follow-up

No major additional research needed for this persona lane unless a later synthesis wants direct Binance 1-minute wick-frequency evidence or updated intraday price action closer to resolution.