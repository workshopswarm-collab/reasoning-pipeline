---
type: agent_finding
case_key: case-20260416-1f25d147
dispatch_id: dispatch-case-20260416-1f25d147-20260416T035120Z
research_run_id: 5afb3e7a-47ad-4114-8b44-4ea2c2320c67
analysis_date: 2026-04-16
persona: base-rate
domain: crypto
subdomain: market-structure
entity: sol
topic: solana-above-80-on-april-19
question: "Will the Binance SOL/USDT 12:00 ET 1-minute candle close above 80 on April 19, 2026?"
driver: operational-risk
date_created: 2026-04-16
agent: orchestrator
stance: yes
certainty: medium-high
importance: medium
novelty: low
time_horizon: multi-day
related_entities: ["sol", "solana"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: []
tags: ["base-rate", "crypto", "polymarket", "binance", "threshold-market"]
---

# Claim

SOL being above 80 at the relevant settlement minute on April 19 is the clear outside-view favorite. My base-rate estimate is **89% Yes**, slightly below the market's **92%** because the contract settles on a single noon-ET Binance 1-minute close rather than on a looser daily or multi-hour condition.

## Market-implied baseline

The assignment gives current_price **0.92**, implying a **92%** market probability for Yes.

## Own probability estimate

**89% Yes**.

## Agreement or disagreement with market

I **roughly agree** with the market directionally but am slightly less confident. The outside view is strongly bullish for this threshold because SOL is already around **85.23-85.24** on Binance and has closed above 80 on **171 of the last 180 daily sessions (96.7%)** in the retrieved sample. The reason to shade below market is structural: this contract requires **all material conditions** to hold simultaneously at a specific instant:

1. the exchange is **Binance**,
2. the pair is **SOL/USDT**,
3. the relevant bar is the **1-minute candle labeled 12:00 ET (noon)** on **April 19, 2026**,
4. the final **Close** of that candle must be **strictly greater than 80**,
5. no other exchange, pair, or broader time window matters.

That single-minute path dependence makes the event a little less robust than the raw persistence stats suggest.

## Implication for the question

From a base-rate lens, this looks like a high-probability Yes market, but not one that should be rounded to certainty. The prior is strong because the threshold is already in-the-money by about **6.5%** and recent persistence above 80 has been overwhelming. The main live risk is short-horizon volatility between now and the exact settlement minute.

## Key sources used

- **Authoritative governing source of truth for contract mechanics:** Polymarket market page and rules for `solana-above-on-april-19`, which explicitly define the market as the Binance SOL/USDT 1-minute candle close at 12:00 ET on April 19.
- **Direct primary price source / settlement surface:** Binance SOL/USDT API endpoints used during this run:
  - ticker price endpoint for current spot context
  - 1-minute klines endpoint for timing-window verification
  - daily klines endpoint for base-rate persistence context
- Case source note: `qualitative-db/40-research/cases/case-20260416-1f25d147/researcher-source-notes/2026-04-16-base-rate-binance-polymarket-rules.md`

Direct vs contextual distinction:
- **Direct evidence:** Polymarket rules and Binance price/klines surfaces.
- **Contextual evidence:** Historical daily-close frequency above 80 as an outside-view proxy for the narrower settlement condition.

Compliance with evidence floor:
- **Met.** This is a medium-difficulty, date-sensitive, multi-condition contract. I used the governing rules page plus multiple direct Binance data surfaces and performed an explicit additional verification pass on the ET timing mapping before finalizing.

## Supporting evidence

- Current Binance SOL/USDT price is about **85.23-85.24**, comfortably above the 80 threshold.
- Over the last **180** daily sessions in retrieved Binance data, SOL closed above 80 on **171/180 = 96.7%**.
- Over the last **14** daily sessions, SOL closed above 80 on **14/14 = 100%**.
- Over the last **30** daily sessions, SOL closed above 80 on **29/30 = 96.7%**.
- Conditional persistence is also strong: when SOL was already above 80, the next 3 daily closes also remained above 80 on **159/171 = 93.0%** of observed cases in the sample.
- ET timing verification found the Binance kline corresponding to **2026-04-15 12:00 ET**, confirming a clean operational mapping from Binance UTC kline times into the market's ET settlement instruction.

## Counterpoints / strongest disconfirming evidence

The strongest disconfirming consideration is that the contract is decided by **one exact minute**, not by the daily close. Crypto can move more than 6% in a few days, and a brief risk-off move or SOL-specific drawdown could put the noon-ET candle close below 80 even if the broader trend still looks healthy. Put differently: the historical daily-close base rate likely **overstates** the true probability for this narrower single-minute condition.

## Resolution or source-of-truth interpretation

The governing source of truth is explicitly **Binance SOL/USDT**, not Coinbase, not a market-wide SOL index, and not any other trading pair. The market resolves Yes only if the **final Close** of the **12:00 ET** Binance **1-minute** candle on **April 19, 2026** is **higher than 80**. Equal to 80 would resolve **No** because the rule says "higher than." I explicitly checked the date/timing logic and verified that Binance 1-minute kline timestamps can be mapped into **America/New_York** for the relevant noon-ET bar.

Canonical mapping check:
- Clean canonical entities used: `sol`, `solana`.
- Clean canonical drivers used: `operational-risk`, `reliability`.
- No additional causally important entity or driver required a proposed slug for this case.

## Key assumptions

The main assumption is that SOL stays in roughly the current trading regime over the next three days and does not experience a sufficiently sharp selloff to break below 80 exactly at settlement. See the linked assumption note for the path-sensitive version of this assumption.

## Why this is decision-relevant

The market is already pricing a very high chance of Yes. My outside-view work says that is broadly warranted, but the remaining edge is small because the market has already incorporated the obvious price-level fact. The only meaningful reason to resist the Yes side is if one thinks short-horizon volatility risk is materially underpriced.

## What would falsify this interpretation / change your mind

- A sharp crypto-wide drawdown or SOL-specific selloff that brings Binance SOL/USDT into the **79-81** area before April 19 noon ET.
- Evidence that Binance-specific pricing is diverging materially from other venues in a way that raises settlement risk.
- A fresh verification pass nearer settlement showing repeated intraday dips below 80 or a much thinner cushion than exists now.

## Source-quality assessment

- **Primary source used:** Binance direct API market data, which is the operative settlement venue.
- **Most important secondary/contextual source used:** Polymarket rules page for contract mechanics; historical Binance daily klines as contextual frequency evidence.
- **Evidence independence:** **Medium.** Rules and price data are not fully independent, but they answer different parts of the case: what counts vs how likely the threshold is.
- **Source-of-truth ambiguity:** **Low.** The contract wording is specific about exchange, pair, timeframe, and price field, though the ET-to-Binance timestamp mapping needed explicit checking.

## Verification impact

Yes, I performed an **additional verification pass** because the market probability is extreme (>85%) and the contract is date/time specific. The extra pass checked the ET noon mapping against Binance 1-minute kline timestamps. It **did not materially change** the directional view, but it increased confidence that the contract mechanics were being interpreted correctly and supported keeping the estimate high.

## Reusable lesson signals

- Possible durable lesson: threshold crypto markets that settle on a single exchange-specific minute should usually be discounted somewhat relative to broader daily-close base rates.
- Possible missing or underbuilt driver: none.
- Possible source-quality lesson: for date-specific crypto threshold markets, direct API timestamp checks are worth doing even when the rules look straightforward.
- Confidence that any lesson here is reusable: **medium**.

## Orchestrator review suggestions

- review later for durable lesson: **no**
- review later for driver candidate: **no**
- review later for canon or linkage issue: **no**
- one-sentence reason: this looks like a routine application of existing crypto threshold-market handling rather than evidence of a missing canonical concept.

## Recommended follow-up

Re-check Binance SOL/USDT price cushion and intraday volatility on April 18-19, with special attention if SOL trades below 82 before settlement.