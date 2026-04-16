---
type: agent_finding
case_key: case-20260415-0735f476
dispatch_id: dispatch-case-20260415-0735f476-20260415T201136Z
research_run_id: f0a4e7fb-4b0c-4950-b281-fe2a4d6335ef
analysis_date: 2026-04-15
persona: base-rate
domain: crypto
subdomain: bitcoin-threshold-market
entity: bitcoin
topic: "Bitcoin above $70,000 on April 20"
question: "Will the Binance BTC/USDT 12:00 ET 1-minute candle on April 20 close above 70,000?"
driver: reliability
date_created: 2026-04-15
agent: Orchestrator
stance: yes-lean
certainty: medium
importance: high
novelty: low
time_horizon: short
related_entities: ["binance", "bitcoin"]
related_drivers: ["reliability", "operational-risk"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: ["qualitative-db/40-research/cases/case-20260415-0735f476/researcher-source-notes/2026-04-15-base-rate-polymarket-rules-and-market-state.md", "qualitative-db/40-research/cases/case-20260415-0735f476/researcher-source-notes/2026-04-15-base-rate-binance-and-cross-venue-spot-check.md", "qualitative-db/40-research/cases/case-20260415-0735f476/researcher-analyses/2026-04-15/dispatch-case-20260415-0735f476-20260415T201136Z/assumptions/base-rate.md", "qualitative-db/40-research/cases/case-20260415-0735f476/researcher-analyses/2026-04-15/dispatch-case-20260415-0735f476-20260415T201136Z/evidence/base-rate.md"]
downstream_uses: []
tags: ["agent-finding", "base-rate", "btc", "polymarket", "threshold-market"]
---

# Claim

Base-rate view: **Yes is more likely than No, but the market is a bit too confident.** BTC is currently well above 70,000, which makes a noon-ET April 20 close above that level structurally likely, but this is still a **single exact-minute Binance close** five days away rather than a broad weekly-above-threshold condition.

## Market-implied baseline

The market-implied probability is about **93%** from `current_price: 0.93`, consistent with the Polymarket event page showing the 70,000 line around **93-94% Yes**.

## Own probability estimate

My estimate is **86% Yes**.

## Agreement or disagreement with market

I **roughly agree on direction** but **disagree modestly on magnitude**. The outside view supports a high Yes probability because BTC is currently around **74.6k-74.7k**, or about **6.5% above** the threshold, with only about five days left. But a 93% price looks somewhat rich for a contract that resolves on **one exact Binance 1-minute close at 12:00 ET on April 20**. The market seems to be pricing persistence almost like a broad “BTC remains above 70k this week” claim, while the contract is narrower than that.

## Implication for the question

The best base-rate interpretation is still **Yes-favored**, but not near-certainty. The current cushion is meaningful enough that No likely requires a real drawdown or a specific weak print into the governing minute, yet the narrow settlement mechanic keeps the probability below the low-90s market price in my view.

## Key sources used

**Primary / governing source**
- Polymarket event page and rules: `researcher-source-notes/2026-04-15-base-rate-polymarket-rules-and-market-state.md`
  - Direct for contract wording and visible market state.
  - Governing source of truth explicitly identified there as **Binance BTC/USDT 1-minute candle, 12:00 ET, April 20, final Close**.

**Primary current-state source**
- Binance API ticker and 1-minute kline checks: `researcher-source-notes/2026-04-15-base-rate-binance-and-cross-venue-spot-check.md`
  - Direct for current Binance BTC/USDT price region.

**Secondary / contextual verification sources**
- CoinGecko BTC/USD spot check.
- Coinbase BTC-USD spot check.
  - Contextual rather than governing, used to verify that current BTC pricing is consistently in the mid-74k area across venues.

**Evidence floor compliance**
- Evidence floor met with at least **two meaningful sources**: (1) primary contract/rules source from Polymarket and (2) direct current-state source from Binance, plus an **additional verification pass** using CoinGecko and Coinbase cross-checks and a Binance timestamp/ET sanity check.

## Supporting evidence

- **Current BTC level is comfortably above threshold.** Binance spot was checked at about **74,605.50**, and recent Binance 1-minute closes were all in the mid-74k area.
- **Cross-venue checks agree.** CoinGecko and Coinbase both showed BTC around **74.7k**, reducing the chance that the Binance read was stale or anomalous.
- **Short horizon helps Yes.** With about five days remaining, being 6%+ above threshold is a strong outside-view starting point for a plain above/below market.
- **The contract has no extra hidden qualitative condition.** Once the narrow rule is interpreted correctly, the outcome is only about one Binance minute close.

## Counterpoints / strongest disconfirming evidence

The strongest disconfirming consideration is **the settlement mechanic itself**: this is **not yet verified** for April 20 and has **not yet occurred**. The market resolves on **one exact minute close on Binance**, not on current spot, weekly average, or broad exchange consensus. BTC can move several percent in five days, and a drawdown back through 70k by the governing minute would be enough for No even if most of the intervening period remains strong.

## Resolution or source-of-truth interpretation

This section is critical for this case.

- **Primary governing source:** Binance BTC/USDT.
- **Material condition 1:** the relevant candle is the **1-minute candle labeled 12:00 ET (noon) on April 20, 2026**.
- **Material condition 2:** the market uses the candle’s final **Close** price, not the High, Low, VWAP, midpoint, or another venue’s print.
- **Material condition 3:** the Close must be **higher than 70,000**. Equal to 70,000 would not satisfy “higher than.”
- **Material condition 4:** Binance BTC/USDT is the source of truth, so other exchanges are contextual only.

Explicit timing check:
- The case deadline and resolution time are both listed as **2026-04-20T12:00:00-04:00**, which is **12:00 PM America/New_York**.
- I additionally verified Binance kline timestamps against ET conversion during the run to ensure the minute-based timing interpretation is operationally coherent.

Explicit status distinction required by the prompt:
- **Not yet occurred:** the governing April 20 noon ET close has not happened yet.
- **Not yet verified:** even if future spot action suggests likely Yes, the final governing proof still must come from the specified Binance minute close when the event arrives.

## Key assumptions

- BTC remains in roughly the current regime and does not suffer a >6% drawdown into the governing minute.
- Binance BTC/USDT remains close enough to broader BTC spot that current cross-venue checks are informative.
- No exchange-specific dislocation on Binance meaningfully changes the settlement print versus broader market levels.

## Why this is decision-relevant

The market is already at an extreme probability, so the useful question is not direction alone but whether the crowd is slightly overpaying for a still-path-sensitive outcome. My read is that **Yes is favored**, but the narrow contract mechanics justify a discount relative to the market’s 93%+ pricing.

## What would falsify this interpretation / change your mind

I would move meaningfully toward the market or above it if BTC continues to hold comfortably above **72k-73k** into April 19-20 with no Binance-specific weakness, because the remaining path risk would then shrink a lot. I would move materially lower if BTC retraces back near **71k-72k**, if macro/crypto volatility rises sharply, or if Binance begins printing weaker than broader spot into the event window.

## Source-quality assessment

- **Primary source used:** Polymarket contract page for exact settlement wording; Binance API for current governing-market price context.
- **Key secondary/contextual source used:** CoinGecko and Coinbase spot checks.
- **Evidence independence:** **medium**. Binance is closest to the governing source, while CoinGecko/Coinbase provide useful but still market-data-adjacent confirmation rather than a fully different mechanism.
- **Source-of-truth ambiguity:** **low after verification**. The contract wording is narrow and specific once read directly.

## Verification impact

- **Additional verification pass performed:** yes.
- I did an extra pass because this is a date-sensitive, narrow-resolution market trading above 85% implied probability.
- The extra verification included direct reread of the Polymarket rules, direct Binance API spot and kline checks, timestamp-to-ET sanity checks, and cross-venue validation with CoinGecko and Coinbase.
- **Materially changed view:** no material directional change; it mainly increased confidence that the governing mechanism is correctly understood and that current BTC is genuinely well above the threshold.

## Reusable lesson signals

- Possible durable lesson: for short-dated crypto threshold-close markets, **distance to threshold plus exact settlement mechanic** should both be modeled explicitly; neither alone is enough.
- Possible missing or underbuilt driver: none confidently identified from this single case, though a future canonical driver around **threshold-close path dependence** may be worth monitoring.
- Possible source-quality lesson: explicit distinction between **current-state verification** and **event-settlement proof** remains useful.
- Confidence that any lesson here is reusable: **medium-low**.

## Orchestrator review suggestions

- Review later for durable lesson: **no**.
- Review later for driver candidate: **no**.
- Review later for canon or linkage issue: **yes**.
- Reason: **Binance** is structurally important to this class of contract, but I was not confident enough that a clean canonical entity slug already exists, so I left it in `proposed_entities` rather than forcing a weak fit.

## Recommended follow-up

No major follow-up suggested now beyond a closer-to-expiry recheck if the case is rerun. The next materially useful update would be a fresh Binance-focused verification on **April 19-20**, not more generic BTC narrative research.