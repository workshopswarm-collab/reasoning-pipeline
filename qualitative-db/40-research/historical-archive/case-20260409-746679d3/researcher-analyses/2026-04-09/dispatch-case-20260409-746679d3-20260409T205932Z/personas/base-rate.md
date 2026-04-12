---
type: agent_finding
case_key: case-20260409-746679d3
dispatch_id: dispatch-case-20260409-746679d3-20260409T205932Z
research_run_id: 0df82309-bacf-4ad5-81c2-4aabba0201f4
analysis_date: 2026-04-09
persona: base-rate
domain: crypto
subdomain: spot-price-thresholds
entity: ethereum
topic: will-the-price-of-ethereum-be-above-2-100-on-april-10
question: "Will the price of Ethereum be above $2,100 on April 10?"
driver: reliability
date_created: 2026-04-09
agent: Orchestrator
stance: yes
certainty: medium-high
importance: medium
novelty: low
time_horizon: "<24h"
related_entities: ["binance", "ethereum"]
related_drivers: ["reliability", "operational-risk"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: []
tags: ["base-rate", "crypto", "eth", "binance", "threshold-market", "polymarket"]
---

# Claim

My base-rate view is that **Yes is more likely than not and still the right side, but the market looks somewhat too confident**. ETH/USDT on Binance was already around 2213 at the time checked, giving roughly a $113 cushion over the 2100 threshold for a settlement less than a day away, and short-horizon persistence from that regime is usually strong.

**Evidence-floor compliance:** met. I verified one authoritative/direct source-of-truth surface (Binance spot API for ETHUSDT klines, ticker, exchangeInfo, and server time) plus the contract-context source (Polymarket rules page). I also performed an explicit extra verification pass on timezone conversion and candle-close mechanics because the market was already priced above 85%.

## Market-implied baseline

The assigned current price is 0.94, implying about **94% Yes**.

## Own probability estimate

**88% Yes.**

## Agreement or disagreement with market

I **roughly agree directionally** with the market that Yes is the more likely outcome, but I **disagree modestly on magnitude**. A 94% market price is plausible, yet my outside-view estimate is a bit lower because this still resolves on one specific 1-minute close at one exact time, and single-minute crypto thresholds can fail on ordinary volatility without requiring a regime break.

## Implication for the question

The base-rate implication is: being above 2100 now and resolving within about a day makes Yes the clear baseline, but this is not quite as close to locked as a 94% quote suggests. The relevant question is less "can ETH trade above 2100 at all" and more "how often does a next-day noon minute close stay above a threshold that is already more than 5% below spot?" Outside-view evidence says often, but not almost always.

## Key sources used

- **Primary direct / authoritative source-of-truth surface:** Binance public spot API for `ETHUSDT`, including `ticker/price`, `exchangeInfo`, `time`, and `klines` endpoints. This is the closest machine-readable version of the designated settlement source.
- **Primary contract / resolution source:** Polymarket market rules page for `ethereum-above-on-april-10`, which explicitly says the market resolves from the Binance ETH/USDT 1-minute candle at 12:00 ET and its final close.
- **Case source note:** `qualitative-db/40-research/cases/case-20260409-746679d3/researcher-source-notes/2026-04-09-base-rate-binance-api-and-market-rules.md`
- **In-run contextual base-rate check:** Binance daily ETHUSDT klines over the last 120 days, used to estimate how often the next day stayed above 2100 when the prior close was already above 2100.

Direct vs contextual distinction:
- **Direct:** Binance API fields and Polymarket contract wording.
- **Contextual:** historical conditional frequency from recent Binance daily closes.

## Supporting evidence

- Current Binance ETHUSDT spot at check time was about **2213.08**, already comfortably above 2100.
- Over the last **120 daily Binance candles** fetched in-run, the unconditional frequency of the next day closing above 2100 was about **61.3%**.
- More relevantly for the outside view, when the prior daily close was already above 2100, the next day also closed above 2100 in about **91.8% (67/73)** of observed cases in that recent sample.
- The settlement horizon is short: less than one day from the observation point, which usually favors persistence over large regime shifts absent a clear catalyst.

## Counterpoints / strongest disconfirming evidence

The strongest disconfirming consideration is that this market resolves on **one exact 1-minute Binance close**, not on a daily close or average. Crypto can easily print a brief downside move of 5% or so within a day, and ETH only needs to be below 2100 for that specific settlement minute to resolve No. So even if the broader price regime is healthy, a narrow time-slice contract deserves some discount versus the 91.8% daily-persistence anchor.

## Resolution or source-of-truth interpretation

- **Governing source of truth:** Binance ETH/USDT 1-minute candle close, as designated by Polymarket rules.
- **Case-specific check: verify UTC offset vs Binance server.** Binance `exchangeInfo` reports timezone `UTC`, and Binance `time` provides server time in UTC milliseconds. April 10 is in **EDT (UTC-4)**, so **12:00 ET = 16:00 UTC**. I queried the exact corresponding 1-minute kline window for 2026-04-10 16:00 UTC and received no data yet, which is consistent with the event still being in the future and supports the conversion.
- **Case-specific check: candle close definition.** Binance `klines` responses include open time, close time, and the final close price as the fifth field. For a 1-minute candle beginning at 16:00:00 UTC, the close time is 16:00:59.999 UTC and the settlement-relevant value is the final close for that bar.
- Source-of-truth ambiguity is therefore low-to-medium: low on price source, modest on UI-vs-API phrasing, but the operational reading is still straightforward.

## Key assumptions

- ETH remains in roughly the current price regime through the settlement minute.
- The Binance API and Binance web chart are economically aligned for the same ETH/USDT 1-minute close.
- No unusual exchange or data-display issue disrupts the designated candle close.

## Why this is decision-relevant

At 94%, the market already assumes the cushion over 2100 is very likely to hold. My view says that is directionally right, but the outside view still assigns meaningful failure risk because narrow-timestamp threshold markets are more fragile than they first look. For synthesis, this persona contributes mainly a **small anti-overconfidence discount**, not a directional reversal.

## What would falsify this interpretation / change your mind

- If ETH trades down into the low 2100s or below before the noon ET window, my probability would fall quickly.
- If a verified source showed the relevant candle/timezone interpretation differs from 12:00 ET = 16:00 UTC, I would reassess the contract read.
- If broader crypto markets weaken sharply overnight or early morning ET, the single-minute downside risk would rise materially.

## Source-quality assessment

- **Primary source used:** Binance public spot API for ETHUSDT, which is effectively authoritative because the contract settles to Binance data.
- **Most important secondary/contextual source used:** Polymarket rules page, plus contextual frequency taken from recent Binance daily klines.
- **Evidence independence:** **Low-to-medium.** The direct and contextual evidence both ultimately depend on Binance data, though they answer different questions (settlement mechanics vs persistence frequency).
- **Source-of-truth ambiguity:** **Low-to-medium.** Low regarding which exchange and pair matter; medium only in the minor sense that the contract references the Binance chart UI while I used the API for explicit timestamp inspection.

## Verification impact

Yes, I performed an additional verification pass. Specifically I checked Binance server-time / UTC conventions, queried ETHUSDT kline mechanics directly, and tested the exact converted target minute in UTC. This **did not materially change the directional view**, but it **did reduce contract-interpretation risk** and made me more comfortable keeping the estimate high rather than cutting it further.

## Reusable lesson signals

- Possible durable lesson: narrow crypto threshold markets priced at extremes should still get a timestamp-and-candle audit, because single-minute resolution risk is easy to underweight.
- Possible missing or underbuilt driver: none clear from this run.
- Possible source-quality lesson: when Polymarket points to Binance chart candles, Binance API can be a cleaner audit surface for timezone and close-field interpretation.
- Confidence that any lesson here is reusable: **medium**.

## Orchestrator review suggestions

- review later for durable lesson: **yes**
- review later for driver candidate: **no**
- review later for canon or linkage issue: **yes**
- one-sentence reason: Binance appears causally central for these recurring crypto settlement markets, but the available canonical entity note in scope was `binance-us`, not a clean generic Binance slug, so linkage may need review rather than forcing a weak fit.

## Recommended follow-up

No major follow-up suggested for this persona beyond any final synthesis check on intraday volatility sensitivity closer to settlement.