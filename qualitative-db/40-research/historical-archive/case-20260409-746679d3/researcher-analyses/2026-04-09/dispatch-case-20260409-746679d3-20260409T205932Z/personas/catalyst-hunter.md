---
type: agent_finding
case_key: case-20260409-746679d3
dispatch_id: dispatch-case-20260409-746679d3-20260409T205932Z
research_run_id: 4e9f9b53-3707-46ac-8a6f-415fdbd92afb
analysis_date: 2026-04-09
persona: catalyst-hunter
domain: crypto
subdomain: short-horizon-price-resolution
entity: ethereum
topic: ethereum-above-2100-on-april-10
question: "Will the price of Ethereum be above $2,100 on April 10?"
driver: reliability
date_created: 2026-04-09
agent: catalyst-hunter
stance: yes-lean
certainty: medium-high
importance: high
novelty: low
time_horizon: "<24h"
related_entities: ["ethereum"]
related_drivers: ["reliability", "operational-risk"]
proposed_entities: ["binance-global"]
proposed_drivers: []
upstream_inputs: []
downstream_uses: []
tags: ["ethereum", "binance", "polymarket", "catalyst-hunter", "short-horizon"]
---

# Claim

ETH is more likely than not to resolve **Yes** on this contract because the governing print is a single Binance ETH/USDT 1-minute candle at **12:00 ET on Apr 10**, and ETH is already trading materially above the $2,100 threshold with less than a day remaining. The most relevant near-term catalysts are not scheduled macro releases so much as **overnight crypto risk sentiment, any exchange-specific disruption, and any sharp broad risk-off move before the noon ET print**. My directional view is Yes, but with meaningful fragility because a one-minute close can still be clipped by a fast selloff even when the broader daily level looks safe.

**Evidence-floor compliance:** met via (1) governing source-of-truth review from Polymarket rules naming Binance, (2) direct Binance documentation on 1-minute klines and timezone behavior, and (3) an additional live Binance public API verification pass checking server time exposure and live 1-minute ETHUSDT candle structure.

## Market-implied baseline

The market-implied probability from the assignment's `current_price` is **0.94 = 94% Yes**.

## Own probability estimate

My own probability estimate is **91% Yes**.

## Agreement or disagreement with market

I **roughly agree** with the market's strong Yes lean, but I am slightly less confident than the market.

Why slightly lower than market:
- the setup is favorable because ETH is already above 2100 and only needs to remain above the threshold into one specific minute tomorrow
- however, this is still a **single-minute close** contract, so microstructure and short-lived volatility matter more than in a daily-close framing
- the market may be underweighting the possibility of a sharp but brief downside move, especially if broader crypto trades risk-off overnight or into U.S. hours tomorrow

## Implication for the question

This should still be interpreted as a high-probability Yes case, but not as a lock. The decisive issue is not whether ETH is fundamentally healthy; it is whether any catalyst before **Apr 10 12:00 ET** can force Binance ETH/USDT below **2100** at the final close of the noon ET one-minute candle.

The most likely repricing path before resolution is:
1. ETH stays comfortably above 2100 overnight and the market drifts toward near-certainty Yes; or
2. a fast downside move compresses spot closer to the threshold, at which point this market could reprice sharply because the contract is threshold-and-timestamp specific.

## Key sources used

**Primary / authoritative settlement mechanics**
- Polymarket event rules page for `ethereum-above-on-april-10`, which states the market resolves on the Binance ETH/USDT 1-minute candle for **12:00 ET** using the final **Close** price.
- Binance Spot API docs for `GET /api/v3/klines`, which state that klines are uniquely identified by **open time**, support a `timeZone` parameter, and still interpret `startTime` / `endTime` in UTC.

**Direct verification source**
- Live Binance public API endpoints checked during this run:
  - `/api/v3/time` for server-time alignment
  - `/api/v3/klines?symbol=ETHUSDT&interval=1m&limit=5` for current 1-minute candle structure and timing behavior

**Case artifact with extracted mechanics**
- `qualitative-db/40-research/cases/case-20260409-746679d3/researcher-source-notes/2026-04-09-catalyst-hunter-binance-rules-and-api.md`

**Assumption / interpretation artifact**
- `qualitative-db/40-research/cases/case-20260409-746679d3/researcher-analyses/2026-04-09/dispatch-case-20260409-746679d3-20260409T205932Z/assumptions/catalyst-hunter.md`

Direct vs contextual distinction:
- **Direct evidence:** Polymarket rules and Binance docs/API mechanics
- **Contextual evidence:** current live ETH level materially above threshold and the short remaining time window

## Supporting evidence

- Live Binance ETHUSDT 1-minute candles during this run were around **2211-2213**, putting spot roughly **5%+ above 2100**.
- Only a limited time window remains before the deciding noon ET minute on Apr 10.
- Contract mechanics are fairly clean once interpreted correctly: a single named venue, a single pair, a single minute candle, and an explicit close-price threshold.
- Binance docs align well with the plain-language reading that the relevant candle is the one **opened at 12:00 ET**, whose final close is observed at the end of that minute.

## Counterpoints / strongest disconfirming evidence

The strongest disconfirming consideration is that **this is a one-minute threshold market, not a daily-close market**. Even if ETH spends most of the next day above 2100, a fast risk-off move, exchange-specific dislocation, or brief volatility spike around the deciding minute could still produce a No resolution. That fragility is the main reason I am below the market's 94% rather than at or above it.

## Resolution or source-of-truth interpretation

**Governing source of truth:** Binance ETH/USDT, specifically the 1-minute candle shown for **12:00 ET** on Apr 10, using the final **Close** price.

### Case-specific check: verify UTC offset vs Binance server

I performed this explicitly.
- Apr 10, 2026 in New York is under **Eastern Daylight Time (UTC-4)**, so **12:00 ET = 16:00 UTC**.
- Binance exposes `serverTime` in UTC-mapped epoch milliseconds via `/api/v3/time`, which I checked successfully.
- This means the operationally relevant timestamp to monitor is the candle beginning at **2026-04-10 16:00:00 UTC** if using API time.

### Case-specific check: candle close definition

I performed this explicitly.
- Binance docs state klines are uniquely identified by **open time**.
- Binance API responses show each 1-minute candle includes both open time and close time, with close time ending at `...9999`, consistent with the final close price being the last price of that one-minute interval.
- On the plain reading, the decisive candle is the one **opened at 12:00:00 ET**, and the contract uses that candle's final close price, not the previous minute's close.

Source-of-truth ambiguity is therefore **low-to-medium**, not zero: the retail web UI naming convention could still create some edge-case confusion, but the docs and rules align well enough for a practical forecast.

## Key assumptions

- ETH will not suffer a roughly 5%+ downside move into the noon ET deciding minute.
- No exchange-specific Binance operational issue or anomalous print will distort the relevant ETH/USDT close.
- Polymarket will interpret the named candle consistently with Binance's open-time-based kline definition.

## Why this is decision-relevant

The market is priced at an extreme level, so even small contract-interpretation or timing mistakes matter. For a decision-maker, the useful distinction is:
- **terminal direction** still strongly favors Yes
- **repricing risk** is concentrated in short-horizon volatility and contract microstructure, not in long-form fundamental debate

The catalyst that would most likely move this market before resolution is a **sharp, broad crypto downside move** that compresses ETH toward 2100. Salient but lower-information narrative chatter matters less than actual price-level proximity to the threshold.

## What would falsify this interpretation / change your mind

The main things that would change my view materially:
- ETH trading decisively down toward **2100-2120** before U.S. morning on Apr 10
- an official clarification showing the relevant candle is interpreted differently from the open-time reading above
- evidence of Binance chart/API irregularity or a venue-specific operational problem near resolution time
- a major overnight macro or crypto shock that materially increases the probability of a brief but deep downside wick

## Source-quality assessment

- **Primary source used:** Polymarket rules naming Binance ETH/USDT 12:00 ET 1-minute close, plus Binance spot API docs for kline mechanics
- **Most important secondary/contextual source:** live Binance public API checks of server time and current ETHUSDT 1-minute candles
- **Evidence independence:** low-to-medium, because the mechanics verification necessarily relies heavily on Binance surfaces; acceptable here because Binance is the contract's named source of truth
- **Source-of-truth ambiguity:** low-to-medium; the rules are fairly explicit, but there is still mild interpretive risk around candle labeling conventions unless/until the exact deciding minute is observed live

## Verification impact

Yes, an **additional verification pass** was performed.
- I checked live Binance server time and live ETHUSDT 1-minute kline output after reading the rules/docs.
- This **did not materially change** my directional view, but it **did improve confidence** in the timezone mapping and candle-close interpretation.
- The verification mainly reduced contract-mechanics ambiguity rather than changing the price outlook.

## Reusable lesson signals

- **Possible durable lesson:** for Binance minute-candle Polymarket contracts, timezone mapping and candle-open vs candle-close naming should be audited explicitly before treating the market as trivial
- **Possible missing or underbuilt driver:** none clearly required from this run; existing `reliability` and `operational-risk` tags are sufficient
- **Possible source-quality lesson:** when the contract names a single exchange UI, pairing the public rules page with Binance API docs and a live API spot-check is a strong lightweight verification pattern
- **Confidence that any lesson here is reusable:** medium

## Orchestrator review suggestions

- review later for durable lesson: **yes**
- review later for driver candidate: **no**
- review later for canon or linkage issue: **yes**
- one-sentence reason: Binance contract-resolution work would benefit from a reusable house note on timezone conversion and kline open-time interpretation, and `binance-global` appears causally relevant but lacks a clearly confirmed canonical slug in this run.

## Recommended follow-up

- If this case remains live closer to resolution, monitor Binance ETH/USDT spot relative to **2100** during the final few hours and especially into **15:55-16:01 UTC / 11:55-12:01 ET**.
- If spot falls near the threshold, do a final mechanics check directly against the Binance chart/UI named in the rules.
- Otherwise, no major additional research looks likely to move the estimate by 5 percentage points before resolution.
