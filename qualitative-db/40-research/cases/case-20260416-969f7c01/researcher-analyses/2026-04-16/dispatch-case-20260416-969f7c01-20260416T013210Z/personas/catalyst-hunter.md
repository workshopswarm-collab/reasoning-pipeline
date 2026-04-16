---
type: agent_finding
case_key: case-20260416-969f7c01
dispatch_id: dispatch-case-20260416-969f7c01-20260416T013210Z
research_run_id: bf3202e7-01fb-467a-9b76-ed89ca9c9287
analysis_date: 2026-04-16
persona: catalyst-hunter
domain: crypto
subdomain: spot-market-resolution
entity: ethereum
topic: april-17-binance-ethusdt-noon-threshold
question: "Will the Binance ETH/USDT 12:00 ET 1-minute candle close above 2200 on April 17, 2026?"
driver: operational-risk
date_created: 2026-04-15
agent: Orchestrator
stance: bullish-yes
certainty: medium
importance: high
novelty: low
time_horizon: "<48h"
related_entities: ["ethereum"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: ["binance-global-spot-market"]
proposed_drivers: ["intraday-volatility-window"]
upstream_inputs: []
downstream_uses: []
tags: ["agent-finding", "catalyst-hunter", "eth", "polymarket", "binance"]
---

# Claim

ETH is more likely than not to resolve **Yes** comfortably, because the governing Binance ETH/USDT spot price is currently well above 2200 and I do not see a clearly identified scheduled catalyst before Friday noon ET that is likely to force a >6% drawdown into the exact resolving minute. My directional view is **Yes**, but slightly less confident than the market because this contract resolves on one narrow 1-minute candle rather than a broader daily average or end-of-day print.

## Market-implied baseline

The assigned current market price is **0.945**, implying about **94.5%** for Yes.

## Own probability estimate

**91% Yes**.

## Agreement or disagreement with market

I **roughly agree** with the market directionally, but I am modestly less bullish on the exact probability. The market is correctly seeing that ETH already has a sizeable cushion over 2200, but 94.5% leaves only a small residual allowance for a sharp downside move into one specific minute. In crypto, that residual risk is not negligible.

## Implication for the question

On current information, the base case is that the noon ET Binance close on April 17 stays above 2200. For this market to resolve No, all of the following material conditions would likely need to hold:

1. ETH/USDT must suffer a meaningful downside move from the current ~2353.84 area.
2. That move must persist or intensify into the exact **12:00 ET** 1-minute candle on **2026-04-17**.
3. The **final close** of that Binance 1-minute candle must be **2200.00 or lower**; only a strict close above 2200 resolves Yes.
4. Binance ETH/USDT, not another exchange or pair, is the governing source.

## Key sources used

1. **Primary / authoritative contract source:** Polymarket event page and rule text for `ethereum-above-on-april-17`, which explicitly says resolution is the Binance ETH/USDT **12:00 ET** 1-minute candle close.
2. **Primary / direct underlying market source:** Binance spot API endpoints for ETH/USDT ticker price, 24h stats, average price, and recent 1-minute klines sampled during this run.
3. **Secondary / contextual source:** CME crypto market pages / trading-hours material confirming an active around-the-clock ETH risk market and giving context for potential macro-sensitive repricing windows, though not a case-settling source.
4. **Provenance artifact:** `qualitative-db/40-research/cases/case-20260416-969f7c01/researcher-source-notes/2026-04-16-catalyst-hunter-binance-polymarket-resolution.md`
5. **Supporting audit artifacts:** assumption note and evidence map written for this dispatch.

Evidence floor compliance: **met**. I used at least three meaningful sources/surfaces: (1) Polymarket contract text, (2) Binance direct market data, and (3) an additional contextual verification pass via CME/trading-hours context plus extra Binance endpoint checks. Provenance is preserved in a source note, assumption note, evidence map, and enumerated source list here.

## Supporting evidence

- **Live cushion over threshold:** Binance ETH/USDT last price sampled at **2353.84**, roughly **6.9% above 2200**.
- **24h downside buffer:** Binance 24h low sampled at **2308.50**, still above 2200.
- **Recent minute-level stability above line:** sampled recent 1-minute closes remained around **2353.11–2353.85** during the check.
- **No identified hard scheduled catalyst** in the assignment window that obviously deserves to move the probability sharply lower before Friday noon ET.
- **Contract interpretation is fairly clean:** unlike some rule-sensitive markets, the source-of-truth and threshold condition are explicit.

## Counterpoints / strongest disconfirming evidence

The strongest disconfirming consideration is the **single-minute resolution window itself**. ETH can trade above 2200 most of the time and still resolve No if a fast selloff, wick, or localized Binance-specific dislocation lands exactly in the noon ET candle. That timing convexity is the main reason I stay below the market.

## Resolution or source-of-truth interpretation

The governing source of truth is **Binance ETH/USDT**, specifically the **1-minute candle for 12:00 ET on April 17, 2026**. I explicitly verified the timing conversion: **2026-04-17 12:00:00 America/New_York = 2026-04-17 16:00:00 UTC**.

Important contract mechanics:

- This is **not** about ETH/USD broadly, CME settlement, Coinbase, or any multi-exchange composite.
- This is **not** about whether ETH trades above 2200 at some other time that day.
- This is **not** about the candle high; it is about the **final close** for that exact minute.
- The threshold is **strictly higher than 2200**. A final close exactly at 2200 does **not** satisfy Yes.

## Key assumptions

- No fresh negative macro or crypto-specific catalyst arrives before the resolution window that is large enough to push ETH down more than ~6% and keep it there into noon ET.
- Binance market functioning remains normal enough that the final printed close is representative rather than distorted by an outage or abnormal liquidity event.
- Current spot context is informative for next-day noon risk even though it is not determinative.

## Why this is decision-relevant

The market is already extreme, so the useful question is not “is ETH above 2200 right now?” but “what catalyst could still knock it below 2200 **at the exact resolving minute**?” Right now I do not see a clearly scheduled high-information bearish catalyst, which supports Yes, but the narrow settlement window still matters for sizing confidence.

## What would falsify this interpretation / change your mind

I would cut the probability materially if any of the following occurred before the resolving minute:

- ETH/USDT breaks and holds below roughly the **2300** area with downside momentum.
- A clear risk-off macro shock or crypto-specific negative headline emerges during the remaining window.
- Binance shows abnormal spread, outage, or candle behavior near resolution.
- A more authoritative catalyst calendar check identifies a concrete event before noon ET Friday that is plausibly large enough to drive a >6% move.

## Source-quality assessment

- **Primary source used:** Polymarket contract text plus Binance direct market data.
- **Most important secondary/contextual source:** CME crypto/trading-hours material for context on continuous ETH risk pricing and macro sensitivity.
- **Evidence independence:** **medium**. The core thesis leans heavily on one exchange and the market's own contract structure, though the contextual source adds some independence around timing regime rather than settlement.
- **Source-of-truth ambiguity:** **low**. The contract wording is unusually explicit for this type of market.

## Verification impact

- **Additional verification pass performed:** yes.
- I explicitly re-checked live Binance endpoints (ticker, 24h stats, avg price, recent klines) and verified the ET-to-UTC resolution time conversion because the market is date-sensitive and already priced at an extreme probability.
- **Did it materially change the view?** No material directional change. It increased confidence that the contract is mechanically straightforward and that spot currently has a meaningful cushion, but it did not eliminate the single-minute timing risk.

## Reusable lesson signals

- **Possible durable lesson:** for single-minute crypto threshold markets, distinguish “currently above the line” from “robust to an exact-minute print.”
- **Possible missing or underbuilt driver:** an intraday-resolution / narrow-print timing driver may deserve future review rather than forcing a weak fit into existing drivers.
- **Possible source-quality lesson:** when Polymarket names one exchange and one minute candle, exchange API/timezone verification is higher value than broad news scraping.
- **Confidence that any lesson here is reusable:** **medium**.

## Orchestrator review suggestions

- review later for durable lesson: **yes**
- review later for driver candidate: **yes**
- review later for canon or linkage issue: **yes**
- one-sentence reason: narrow-window exchange-print markets recur and may deserve a cleaner canonical driver/entity treatment than the current fallback to operational-risk/reliability.

## Recommended follow-up

- Watch ETH/USDT during late Asia / Europe / U.S. morning trading on April 17 for any fast move back toward 2300 and below.
- If doing a final rerun close to resolution, prioritize Binance live candle verification over additional generic crypto commentary.
- No follow-up suggested beyond near-resolution monitoring unless a new downside catalyst appears.
