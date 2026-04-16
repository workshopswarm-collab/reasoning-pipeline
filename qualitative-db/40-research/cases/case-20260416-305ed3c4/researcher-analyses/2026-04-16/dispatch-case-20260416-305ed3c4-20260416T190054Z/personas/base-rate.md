---
type: agent_finding
case_key: case-20260416-305ed3c4
dispatch_id: dispatch-case-20260416-305ed3c4-20260416T190054Z
research_run_id: 70993f7c-d48e-4ede-83aa-fc22b3160c95
analysis_date: 2026-04-16
persona: base-rate
domain: crypto
subdomain: market-structure
entity: ethereum
topic: "ETH above 2200 on April 17"
question: "Will the Binance ETH/USDT 1-minute candle for 12:00 ET on 2026-04-17 close above 2200?"
driver: reliability
date_created: 2026-04-16
agent: Orchestrator
stance: yes
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
tags: ["agent-finding", "crypto", "ethereum", "binance", "threshold-market", "base-rate"]
---

# Claim

ETH is likely to finish above 2200 on this contract, and the market’s high-Yes pricing is broadly justified. My estimate is **96% Yes**. The outside-view reason is simple: with less than a day remaining and Binance ETH/USDT trading around **2343-2344** during this run, the contract only fails if ETH falls roughly **6%+** into a very specific noon ET one-minute close window, or if there is an exchange-specific resolution anomaly.

**Evidence-floor compliance:** Met medium-case floor with (1) an authoritative contract/rules source from Polymarket, (2) an authoritative/direct Binance market-data documentation source plus live Binance endpoint verification, and (3) an explicit additional verification pass for timing and current-price context because the market-implied probability is extreme.

## Market-implied baseline

The assignment’s `current_price` is **0.975**, implying about **97.5% Yes**.

## Own probability estimate

**96% Yes.**

## Agreement or disagreement with market

I **roughly agree** with the market, but I am slightly less bullish than 97.5% because crypto can still move violently over sub-24-hour windows and this resolves on a narrow, specific one-minute candle rather than a broad daily average. The market is pricing near-certainty; I think that is directionally right, but not quite enough room is being left for a sharp overnight selloff or exchange-specific resolution/pathology risk.

## Implication for the question

The base-rate takeaway is that this is not a generic “will ETH be strong tomorrow?” question. It is a short-horizon threshold question with a sizeable existing cushion above the strike. Once ETH is already trading roughly 140+ dollars above the threshold less than a day before settlement, the default outside view shifts toward Yes unless there is evidence of an imminent volatility shock.

## Key sources used

- **Primary / authoritative contract source:** Polymarket rules page for this exact market, confirming the market resolves from the **Binance ETH/USDT 1-minute candle for 12:00 ET on April 17** and uses the final **Close** price.
- **Primary / authoritative contextual mechanics source:** Binance Spot API market-data docs for `/api/v3/klines`, confirming 1-minute kline structure and close-price field.
- **Direct contextual evidence:** Live Binance API endpoints checked during this run:
  - ETHUSDT spot ticker around **2343.56-2344.22**.
  - Recent 1-minute klines around the current time.
  - A timing sanity check querying the **2026-04-16 12:00 ET / 16:00 UTC** one-minute ETHUSDT candle, which returned a close of **2340.51**.
- **Provenance note:** `qualitative-db/40-research/cases/case-20260416-305ed3c4/researcher-source-notes/2026-04-16-base-rate-binance-polymarket-resolution-check.md`
- **Assumption note:** `qualitative-db/40-research/cases/case-20260416-305ed3c4/researcher-analyses/2026-04-16/dispatch-case-20260416-305ed3c4-20260416T190054Z/assumptions/base-rate.md`

## Supporting evidence

- Current Binance ETHUSDT during the run was about **2344**, safely above **2200**.
- Binance 24-hour stats during the run showed a **low of 2285.10**, which was still above the strike.
- The required downside from current spot to lose the contract is roughly **$144**, or a bit more than **6%**, in less than a day and specifically into the noon ET minute.
- Even though a longer-horizon base rate is less helpful here, the immediate structural setup favors Yes because the market is asking about a near-term level already well below prevailing spot.

## Counterpoints / strongest disconfirming evidence

The strongest disconfirming consideration is that **crypto can move 6% or more in under 24 hours**, especially during risk-off episodes, and this market resolves on a **single minute close**, not on a broader average. So a fast selloff, liquidation cascade, or macro shock could still take ETH below 2200 at exactly the wrong moment. That is the main reason I am below the market’s 97.5% and not at 99%+.

## Resolution or source-of-truth interpretation

The governing source of truth is **Polymarket’s contract rule text**, which says the market resolves Yes if the **Binance ETH/USDT 1-minute candle for 12:00 ET on April 17, 2026** has a final **Close** price **higher than 2200**.

Material conditions that all must hold for a Yes resolution:
1. The relevant instrument is **Binance ETH/USDT**, not another exchange or pair.
2. The relevant bar is the **1-minute candle for 12:00 ET** on **2026-04-17**.
3. The relevant field is the candle’s **final Close** price.
4. The Close must be **strictly above 2200**; equality would not satisfy “higher than 2200.”
5. ET timing matters explicitly; on this date ET is **EDT (UTC-4)**, so noon ET corresponds to **16:00 UTC**.

Canonical-mapping check:
- Clean canonical entity slug found: **ethereum**.
- Clean canonical driver slugs found: **reliability**, **operational-risk**.
- No clean canonical slug was verified for the exchange entity actually governing settlement, so I did **not** force one into canonical fields and instead recorded **`binance-global`** in `proposed_entities`.

## Key assumptions

- ETH avoids a sudden >6% downside move into the noon ET resolution minute.
- Binance’s displayed/charted settlement surface remains operational and consistent with the underlying market data.
- No major exchange-specific anomaly distorts the final candle.

## Why this is decision-relevant

The contract is priced at an extreme probability. For synthesis, the key question is not whether Yes is favored, but whether the remaining No tail is being under- or over-priced. My view is that the tail risk is real but still small enough that **Yes remains the correct directional answer**.

## What would falsify this interpretation / change your mind

What could still change my mind:
- ETH trades down toward or below **2200** before the final morning.
- A major macro or crypto-specific shock sharply increases realized volatility overnight.
- Evidence emerges that the operative Binance charted settlement surface can diverge from the API/context checks in a way relevant to this market.
- A fresh verification closer to resolution shows the cushion has narrowed materially.

## Source-quality assessment

- **Primary source used:** Polymarket’s own rules page for this exact market.
- **Most important secondary/contextual source used:** Binance Spot API market-data documentation, plus direct live Binance API checks.
- **Evidence independence:** **Medium**. The contract source and the market-data source are distinct surfaces, but both ultimately depend on Binance as the underlying exchange reference.
- **Source-of-truth ambiguity:** **Low to medium**. The contract wording is straightforward, but the formal settlement surface is the Binance chart/web display rather than the API, so API checks are contextual verification rather than the final legal source.

## Verification impact

- **Additional verification pass performed:** Yes.
- I performed a second-pass check on Binance docs, current ETHUSDT ticker/klines, 24h range, and an explicit ET-to-UTC timing sanity check for the noon candle mechanics.
- **Material impact on view:** It did not change the directional view, but it increased confidence that the time-window interpretation and current price buffer are both correctly understood.

## Reusable lesson signals

- Possible durable lesson: narrow crypto threshold markets close to resolution should be treated mainly as **buffer-versus-volatility** questions, not as broad directional thesis questions.
- Possible missing or underbuilt driver: perhaps an exchange-specific **settlement-surface / reference-price mechanics** driver could be useful in future crypto cases.
- Possible source-quality lesson: when Polymarket references an exchange UI as the resolution source, API verification is useful but should be labeled as contextual rather than strictly dispositive.
- Confidence that any lesson here is reusable: **medium**.

## Orchestrator review suggestions

- Review later for durable lesson: **no**
- Review later for driver candidate: **yes**
- Review later for canon or linkage issue: **yes**
- Reason: crypto threshold markets repeatedly depend on exchange-specific settlement mechanics, and the governing Binance exchange entity/linkage was not cleanly represented by a verified canonical slug in this run.

## Recommended follow-up

If this case is rerun close to resolution, do one final direct verification of the Binance ETHUSDT level and the exact 12:00 ET candle output shortly after 16:00 UTC on 2026-04-17. For the current run, further research is unlikely to move the estimate by 5 percentage points absent a live price shock.