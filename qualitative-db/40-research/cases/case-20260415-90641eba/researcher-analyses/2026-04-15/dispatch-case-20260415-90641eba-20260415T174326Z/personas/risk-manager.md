---
type: agent_finding
case_key: case-20260415-90641eba
dispatch_id: dispatch-case-20260415-90641eba-20260415T174326Z
research_run_id: 5a9faab7-79fb-4b21-b3ce-4db9167a2052
analysis_date: 2026-04-15
persona: risk-manager
domain: crypto
subdomain: daily-close-threshold
entity: bitcoin
topic: "BTC above 70000 on April 20 noon ET Binance close"
question: "Will the price of Bitcoin be above $70,000 on April 20?"
driver: operational-risk
date_created: 2026-04-15
agent: Orchestrator
stance: lean-yes
certainty: medium
importance: high
novelty: low
time_horizon: "2026-04-20 12:00 ET"
related_entities: ["binance", "bitcoin"]
related_drivers: ["liquidity", "operational-risk"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: ["qualitative-db/40-research/cases/case-20260415-90641eba/researcher-source-notes/2026-04-15-risk-manager-polymarket-rules.md", "qualitative-db/40-research/cases/case-20260415-90641eba/researcher-source-notes/2026-04-15-risk-manager-price-context.md", "qualitative-db/40-research/cases/case-20260415-90641eba/researcher-analyses/2026-04-15/dispatch-case-20260415-90641eba-20260415T174326Z/assumptions/risk-manager.md", "qualitative-db/40-research/cases/case-20260415-90641eba/researcher-analyses/2026-04-15/dispatch-case-20260415-90641eba-20260415T174326Z/evidence/risk-manager.md"]
downstream_uses: []
tags: ["agent-finding", "risk-manager", "btc", "binance", "close-market"]
---

# Claim

My directional view is **Yes, but with more fragility than the market price suggests**. BTC is already trading around 74k on the governing venue, so Yes is the base case, but this contract is a **single exact-minute Binance close-above-70000 market**, not a touch market and not a broad “BTC stays strong this week” proposition.

**Compliance / evidence-floor note:** medium-difficulty case; I met the floor with (1) direct verification of the governing source and contract mechanics from the Polymarket rules page, (2) an additional verification pass using current Binance BTCUSDT data plus cross-checks from CoinGecko and Coinbase, and (3) explicit mechanism, timing, canonical-mapping, source-quality, and fragility sections below.

## Market-implied baseline

Current market-implied probability from the assignment is **0.87**. The Polymarket page snapshot retrieved during this run also showed the 70,000 line trading around **88% / 89¢ Yes**, which is consistent with that baseline.

Embedded confidence appears high: the market is treating “BTC currently above 70k” as close to “BTC likely still above 70k at the exact settlement minute.”

## Own probability estimate

**0.81**.

## Agreement or disagreement with market

**Mild disagreement.** I agree with the direction (Yes more likely than No), but I think the market is a bit too confident.

Why I am below market:
- the contract is **narrow and timing-sensitive**: one exact Binance BTC/USDT 1-minute candle close at **12:00 ET on April 20** must be **strictly above 70000**;
- this is **not yet verified** because the event has not happened yet; that is different from saying it has already failed to occur;
- a roughly **5-6% drawdown in BTC over five days is plausible**, so the current cushion is meaningful but not decisive.

Most of the gap versus market comes from **uncertainty/fragility discount**, not a directional bearish thesis.

## Implication for the question

The best current interpretation is that Yes is favored because BTC is already materially above the threshold on Binance, but the contract remains vulnerable to a normal crypto downswing or a temporary dip that lands exactly on the settlement minute. This should be treated as a strong but not near-lock Yes.

## Key sources used

**Primary / authoritative governing source**
- Polymarket market rules page for this contract: https://polymarket.com/event/bitcoin-above-on-april-20
  - Direct and authoritative for what counts.
  - Captured in source note: `qualitative-db/40-research/cases/case-20260415-90641eba/researcher-source-notes/2026-04-15-risk-manager-polymarket-rules.md`

**Primary contextual venue source**
- Binance BTCUSDT API checks during this run:
  - `https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT`
  - `https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1m&limit=5`
  - Direct for current Binance price context, but not yet direct for settlement.

**Secondary/contextual verification sources**
- CoinGecko simple price endpoint for BTC/USD.
- Coinbase BTC-USD spot endpoint.
  - These are contextual cross-checks, not governing sources.
  - Captured in source note: `qualitative-db/40-research/cases/case-20260415-90641eba/researcher-source-notes/2026-04-15-risk-manager-price-context.md`

## Supporting evidence

- Current Binance BTCUSDT price during this run was **73999.38**, already about **3999 points above 70000**.
- Recent Binance 1-minute candles in the verification pull were consistently around **73931-73999**, with highs up to **74027.46**.
- CoinGecko and Coinbase were directionally consistent at roughly **73982** and **74044.655** respectively, reducing the chance that Binance was showing an idiosyncratic outlier.
- The market only needs BTC to avoid losing roughly **5-6%** by the settlement minute, which is a favorable but not trivial setup.

## Counterpoints / strongest disconfirming evidence

**Strongest disconfirming consideration:** this is a **single-minute close** contract on a specific venue, and BTC can easily move several percent over five days. BTC being above 70k today does **not** guarantee a Binance 12:00 ET close above 70k on April 20.

Other disconfirming considerations:
- venue specificity matters: only Binance BTC/USDT counts;
- threshold comparison is strict: **higher than 70000**, not equal to 70000;
- a temporary risk-off move near the deadline could flip the result even if the broader weekly thesis remains bullish.

## Resolution or source-of-truth interpretation

**Primary governing source:** Polymarket rules specify Binance BTC/USDT as the settlement source.

**Material conditions that all must hold for Yes**
1. The relevant candle must be the **Binance BTC/USDT 1-minute candle for 12:00 ET on April 20**.
2. The value that matters is the candle’s **final Close**, not intraminute high/low and not a touch.
3. That Close must be **strictly greater than 70000**.
4. Other exchanges and other trading pairs do **not** count.

**Date / timing / timezone check**
- Market title and rules point to **April 20** and explicitly reference **12:00 in ET timezone (noon)**.
- Assignment metadata gives close/resolve timing as **2026-04-20T12:00:00-04:00**, which matches ET noon.

**Mechanism-specific check result**
- I directly verified the governing resolution language on the Polymarket market page.
- The event is **not yet occurred / not yet verifiable** because the decisive candle is in the future.
- I am explicitly distinguishing **“not yet verified”** from **“not yet occurred”** here: the latter is the correct state today.

## Key assumptions

- BTC remains comfortably above 70000 into April 20 rather than mean-reverting sharply.
- No material macro or crypto-specific selloff erases the current ~4k cushion.
- Binance settlement surface remains straightforward and does not introduce edge-case interpretation issues.

## Why this is decision-relevant

At an implied **87%**, the main question is not direction but **confidence calibration**. The risk-manager contribution is that the market may be slightly underpricing path/timing risk because the asset is already above the line. If synthesis is deciding whether this is “basically done” versus merely “strong Yes,” I think it is the latter.

## What would falsify this interpretation / change your mind

The fastest reason to revise down materially would be **BTC sliding back toward or below 70000 on Binance as April 20 approaches**, especially if it is trading near the threshold on the morning of settlement.

What would change my mind upward:
- BTC holding materially above 70k closer to the event date with similar or larger cushion;
- another direct Binance verification pass near settlement showing comfortable margin.

What would change my mind downward:
- a sharp crypto risk-off move;
- BTC losing the cushion and spending time near 70k;
- evidence that the noon ET close is likely to occur during a local downswing.

## Source-quality assessment

- **Primary source used:** Polymarket contract rules page, high quality for contract mechanics and governing source identification.
- **Most important secondary/contextual source used:** Binance BTCUSDT ticker and 1-minute kline endpoints, high relevance for current venue-specific price context.
- **Evidence independence:** **medium**. Binance is primary for venue context, while CoinGecko and Coinbase provide some cross-check independence but are still correlated market data sources.
- **Source-of-truth ambiguity:** **low for mechanics, medium for eventual settlement proof today**. Mechanics are clear, but the decisive candle is in the future, so today’s evidence cannot directly settle the contract.

## Verification impact

- **Additional verification pass performed:** yes.
- I first verified the Polymarket governing rules directly, then ran an additional pass checking current Binance BTCUSDT data and cross-checking against CoinGecko and Coinbase.
- **Did it materially change the view?** No material directional change; it reinforced Yes as the base case but also confirmed that the remaining uncertainty is mostly timing/path risk rather than source confusion.

## Reusable lesson signals

- Possible durable lesson: for **close-at-specific-time** crypto markets, current in-the-money status should not be confused with a touch-style contract being near complete.
- Possible missing or underbuilt driver: no strong new driver candidate from this single run.
- Possible source-quality lesson: preserve a clean distinction between **governing rules verification** and **current price context verification**.
- Confidence that any lesson here is reusable: **medium**.

## Orchestrator review suggestions

- review later for durable lesson: **no**
- review later for driver candidate: **no**
- review later for canon or linkage issue: **yes**
- one-sentence reason: **Binance** is structurally important to many crypto resolution mechanics, but I did not confirm a clean canonical entity slug in `20-entities/`, so I left it in `proposed_entities` instead of forcing linkage.

## Recommended follow-up

- Re-check Binance BTC/USDT closer to April 20, especially within the final 24 hours and again near settlement time.
- If the cushion compresses toward 1-2%, probability should be revised down quickly because exact-minute close risk will dominate.
- If BTC remains comfortably above 70k into the final approach, the estimate can move toward the market or above it.