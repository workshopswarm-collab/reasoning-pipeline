---
type: agent_finding
case_key: case-20260416-a8277fc8
dispatch_id: dispatch-case-20260416-a8277fc8-20260416T001420Z
research_run_id: bb273820-bcdd-4521-8c8d-c966f1df5f00
analysis_date: 2026-04-16
persona: catalyst-hunter
domain: crypto
subdomain: daily-threshold-close
entity: sol
topic: "SOL above $80 on Apr 19 noon ET"
question: "Will the Binance SOL/USDT 1-minute candle at 12:00 ET on 2026-04-19 close above 80?"
driver: reliability
date_created: 2026-04-16
agent: catalyst-hunter
stance: yes-lean
certainty: medium-high
importance: high
novelty: medium
time_horizon: "through 2026-04-19 12:00 ET"
related_entities: ["sol", "solana"]
related_drivers: ["reliability", "operational-risk"]
proposed_entities: []
proposed_drivers: ["threshold proximity"]
upstream_inputs: ["qualitative-db/40-research/cases/case-20260416-a8277fc8/researcher-source-notes/2026-04-16-catalyst-hunter-binance-polymarket-resolution-surface.md", "qualitative-db/40-research/cases/case-20260416-a8277fc8/researcher-analyses/2026-04-16/dispatch-case-20260416-a8277fc8-20260416T001420Z/assumptions/catalyst-hunter.md", "qualitative-db/40-research/cases/case-20260416-a8277fc8/researcher-analyses/2026-04-16/dispatch-case-20260416-a8277fc8-20260416T001420Z/evidence/catalyst-hunter.md"]
downstream_uses: []
tags: ["sol", "binance", "polymarket", "threshold", "close-above"]
---

# Claim

I lean **Yes**: SOL is already trading materially above $80, so the highest-probability path is that Binance SOL/USDT still closes above $80 in the 12:00 ET one-minute candle on Sunday Apr 19. This is not a touch market, though, so the relevant risk is a badly timed dip at the exact resolving minute.

## Market-implied baseline

Current market-implied probability from `current_price: 0.885` is **88.5% Yes**.

## Own probability estimate

My estimate is **84% Yes**.

## Agreement or disagreement with market

I **roughly agree but am modestly less bullish** than the market.

Why: direct Binance verification showed SOL/USDT around **84.67**, which is about **$4.67 / 5.8%** above the threshold and clearly supportive of Yes. But this contract resolves on one exact **Binance 1-minute close at 12:00 ET on Apr 19**, not on current spot, not on another venue, and not on an intraday high. That timestamp-specific mechanic keeps me below the market rather than at or above it.

## Implication for the question

The market probably should still be read as a high-probability Yes, but not as near-certainty. The most important question is not whether Solana has bullish narrative momentum; it is whether the current above-$80 cushion survives through a single Sunday noon ET close on Binance.

## Key sources used

- **Primary / authoritative contract-mechanics source:** Polymarket rules page for this market, which states the governing source is Binance SOL/USDT 1-minute candle close at 12:00 ET on Apr 19. See source note: `qualitative-db/40-research/cases/case-20260416-a8277fc8/researcher-source-notes/2026-04-16-catalyst-hunter-binance-polymarket-resolution-surface.md`
- **Primary direct verification source for current state:** Binance public API spot and recent 1-minute klines for SOLUSDT, showing price around 84.67-84.74 during the verification pass.
- **Secondary / contextual source:** CoinGecko Solana market data, showing roughly 84.73 spot-equivalent context with positive short-horizon performance but weaker 30-day performance.

Direct vs contextual distinction:
- Direct for mechanics: Polymarket rules.
- Direct contextual for current price state: Binance API.
- Contextual secondary: CoinGecko.

## Supporting evidence

- **Governing source directly verified.** The contract resolves from the **Binance SOL/USDT 12:00 ET one-minute close** on Apr 19, and that mechanism is clear enough to evaluate precisely.
- **Current price cushion is meaningful.** Direct Binance verification showed SOL/USDT around **84.67**, comfortably above the $80 threshold.
- **No additional upside is required.** Unlike a higher strike touch market, this contract can resolve Yes simply if current regime broadly persists.
- **Timing/catalyst view:** the most material catalyst is essentially **time decay without breakdown**. Each hour that passes with SOL holding above low-80s increases the chance that Sunday noon ET also prints above $80.

## Counterpoints / strongest disconfirming evidence

The strongest disconfirming consideration is that this is a **single-minute close-above** market. A weekend altcoin downdraft, or even a transient Binance-specific dip near the relevant minute, could still produce a No despite SOL trading above $80 today. Put differently: **not yet verified for the governing timestamp is not the same as not likely**, but it is still a real resolution risk.

## Resolution or source-of-truth interpretation

### Governing source of truth

The governing source of truth is **Binance**, specifically the **SOL/USDT** market with **1m Candles** selected, using the **final Close price** for the **12:00 ET** candle on **2026-04-19**.

### Date / deadline / timezone check

- Resolution-relevant timestamp: **Sunday, 2026-04-19 at 12:00 ET**
- Equivalent UTC time: **2026-04-19 16:00 UTC**

### Material conditions that all must hold for Yes

All of the following must hold:
1. The relevant market is Binance **SOL/USDT**.
2. The relevant candle is the **1-minute candle for 12:00 ET** on **Apr 19, 2026**.
3. The relevant value is the candle’s **final Close**, not high/low/open.
4. That final close must be **strictly higher than $80**.

### Explicit mechanism-status labeling

- **Verified now:** contract mechanics; governing source; current Binance spot context above $80.
- **Not yet verified:** the actual Apr 19 12:00 ET closing print.
- **Not yet occurred:** the governing resolution minute itself has not happened yet.

### Governing-source proof status

Because the event is not near-complete yet, there is no final governing-source proof to capture for settlement. What is captured here is proof of the governing mechanism plus proof that current Binance trading is above threshold.

## Key assumptions

- The current roughly 5.8% cushion above $80 is large enough that ordinary weekend volatility is more likely to leave SOL above $80 than below it at the exact resolving minute.
- Binance-specific pricing will not deviate in a meaningful way from broader spot conditions at Sunday noon ET.
- No material risk-off catalyst arrives that specifically pressures SOL before resolution.

## Why this is decision-relevant

This is a short-dated crypto threshold market with an extreme market baseline. The decision edge, if any, is not about long-run Solana fundamentals. It is about correctly weighting:
- present cushion above threshold,
- exact timestamp settlement mechanics,
- and whether any upcoming catalyst is likely to move the price enough before Sunday.

My read is that the market is broadly right on direction, but probably compresses timestamp risk a bit too much.

## What would falsify this interpretation / change your mind

I would turn materially more bearish if:
- SOL loses the low-80s and starts trading near or below **81** well before Sunday;
- broader crypto turns sharply risk-off into the weekend;
- Binance SOL/USDT weakens versus other spot references;
- or a closer-to-resolution verification pass shows the price cushion has eroded to near-flat.

I would become more bullish if a later verification pass still shows SOL trading comfortably above $80, especially late Saturday or early Sunday.

## Source-quality assessment

- **Primary source used:** Polymarket rules page for contract mechanics and governing source.
- **Key secondary/contextual source:** Binance public API for current SOLUSDT price / 1-minute klines; CoinGecko as extra contextual confirmation.
- **Evidence independence:** **medium**. The mechanics source and the current-price verification source are not fully independent, but they serve distinct functions.
- **Source-of-truth ambiguity:** **low-to-medium**. The governing venue and pair are explicit, but the rules reference Binance’s interface candle display rather than naming an API endpoint.

## Verification impact

- **Additional verification performed:** yes.
- I performed an extra direct Binance verification pass because the market-implied probability was above 85% and the contract is date/timestamp-specific.
- **Materially changed view?** modestly yes.
- It moved me from a generic high-Yes lean to a more defensible **84% Yes** with clearer mechanism framing. The extra pass increased confidence that Yes is the right direction, but it also reinforced that this is a close-above timestamp market, which kept me below the 88.5% market baseline.

## Reusable lesson signals

- Possible durable lesson: in short-dated crypto close-above markets, current cushion matters, but it should not be treated like a touch/high market.
- Possible missing or underbuilt driver: **threshold proximity** may deserve future review if it recurs often across daily crypto threshold cases.
- Possible source-quality lesson: explicit separation of **verified mechanism**, **current-context verification**, and **final governing print not yet observed** is useful.
- Confidence reusable: **medium**.

## Orchestrator review suggestions

- review later for durable lesson: **no**
- review later for driver candidate: **yes**
- review later for canon or linkage issue: **no**
- reason: `threshold proximity` looks structurally useful for these daily threshold markets, but one case is not enough for canon promotion.

## Compliance with evidence floor and mechanism checks

- Evidence floor met: **yes** for a medium-difficulty, date-sensitive market.
- Authoritative / direct source verified: **yes** — Polymarket rules for governing mechanism, plus direct Binance public API check for current pair state.
- Additional verification pass performed: **yes**.
- Primary governing source identified explicitly: **yes**.
- Governing-source proof captured where available: **partial / appropriate to event timing** — mechanism and current above-threshold state captured; final settlement print cannot yet be captured because it has not occurred.
- Canonical mapping check performed: **yes**. Used canonical slugs `sol`, `solana`, `reliability`, and `operational-risk`. Did not force a canonical driver for `threshold proximity`; recorded it in `proposed_drivers` instead.

## Recommended follow-up

One closer-to-resolution verification pass late Apr 18 or early Apr 19 would have the highest information value. If SOL is still comfortably above $80 then, the market likely deserves to stay high-Yes; if the cushion has narrowed materially, timestamp risk becomes the main live issue.