---
type: agent_finding
case_key: case-20260413-2d3a41aa
dispatch_id: dispatch-case-20260413-2d3a41aa-20260413T134928Z
research_run_id: b89b38bb-2851-41e8-be03-d6ae510de8c2
analysis_date: 2026-04-13
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: bitcoin-above-70k-on-april-13
question: "Will the Binance BTC/USDT 12:00 ET 1-minute candle on 2026-04-13 close above 70000?"
driver: operational-risk
date_created: 2026-04-13
agent: Orchestrator
stance: yes-leaning
certainty: medium
importance: high
novelty: low
time_horizon: intraday
related_entities: ["bitcoin"]
related_drivers: ["operational-risk"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: []
tags: ["btc", "binance", "polymarket", "base-rate", "intraday"]
---

# Claim

Base-rate view: **Yes is more likely than the 71% market price implies**. As of about 09:50 ET, BTC/USDT on Binance was around 71,600, with the reported 24h low still above 70,000. For a highly liquid asset with only about 2 hours 10 minutes left until the governing 12:00 ET candle, the outside-view default is path persistence rather than an immediate >2% downside break. My estimate is **78% Yes**.

**Evidence-floor compliance:** I met the medium-difficulty evidence floor with (1) the governing contract/rules surface on Polymarket, (2) the authoritative resolution source surface on Binance, and (3) an additional contextual verification pass via Coinbase. Extra verification did not materially change the directional view.

# Market-implied baseline

The assignment gives `current_price: 0.71`, so the market-implied probability is **71%**.

# Own probability estimate

**78% Yes** that the Binance BTC/USDT **12:00 ET 1-minute candle close** on 2026-04-13 finishes **strictly above 70,000**.

# Agreement or disagreement with market

I **moderately disagree** with the market in a Yes direction. The market is already pricing Yes as likely, and I agree with that direction, but I think the outside-view odds are a bit higher because:

- the settlement minute was still only ~130 minutes away at research time
- Binance spot was already about **71,600**, roughly **2.3% above** the threshold
- Binance 24h low was still about **70,505.88**, already above the strike
- absent a new catalyst, a liquid benchmark asset usually remains within its recent short-horizon range over the next couple of hours

The market may be leaving extra room for crypto intraday volatility, but from a base-rate perspective the remaining path to failure requires a fairly meaningful and fairly prompt drop.

# Implication for the question

The contract resolves Yes only if **all** of the following hold:

1. the relevant source is **Binance BTC/USDT**, not another exchange or pair
2. the relevant bar is the **1-minute candle labeled 12:00 ET** on 2026-04-13
3. the relevant field is that candle's final **Close**
4. the Close is **strictly greater than 70,000**

Given current pricing context, the most likely path is that all four conditions are satisfied. The only live unresolved condition is whether BTC remains above 70,000 at the exact governing minute close.

# Key sources used

- **Primary / authoritative settlement source:** Binance BTC/USDT market surface and Binance API ticker data (`/api/v3/ticker/price` and `/api/v3/ticker/24hr`) showing live price around 71,600 and 24h low around 70,505.88.
- **Primary contract surface:** Polymarket market page and rules for “Bitcoin above ___ on April 13?” specifying Binance BTC/USDT, 1-minute candle, 12:00 ET, and final Close as the source of truth.
- **Secondary / contextual verification:** Coinbase BTC spot API showing ~71,433.47 at roughly the same time, directionally confirming Binance was not obviously anomalous.
- Supporting note: `qualitative-db/40-research/cases/case-20260413-2d3a41aa/researcher-source-notes/2026-04-13-base-rate-binance-polymarket-btc70k.md`
- Assumption note: `qualitative-db/40-research/cases/case-20260413-2d3a41aa/researcher-analyses/2026-04-13/dispatch-case-20260413-2d3a41aa-20260413T134928Z/assumptions/base-rate.md`

# Supporting evidence

- **Direct contract evidence:** Polymarket rules explicitly identify Binance BTC/USDT 1m candle close at 12:00 ET as governing.
- **Direct price evidence:** Binance spot ticker was about **71,601.08** around 09:50 ET.
- **Direct contextual range evidence:** Binance 24h stats showed:
  - open **71,000.65**
  - high **71,700.82**
  - low **70,505.88**
  - last **71,590.52**
- **Outside-view structural point:** with only ~130 minutes left and price already >2% above the threshold, the default is that a liquid market remains in range more often than it breaks materially lower without a fresh shock.

# Counterpoints / strongest disconfirming evidence

The strongest disconfirming consideration is simple: **BTC is volatile enough that a >2% intraday drop in two hours is absolutely plausible**, especially in crypto. This contract is decided by one exact minute close, not by the broader day range, so even a temporary selloff into noon ET could flip the outcome to No.

# Resolution or source-of-truth interpretation

Governing source of truth: **Binance BTC/USDT**.

Relevant timing check:
- market closes/resolves at **2026-04-13 12:00 ET** per assignment
- Polymarket rules specify the **12:00 ET** 1-minute candle on that date
- ET on 2026-04-13 is EDT (UTC-4), so the governing timestamp corresponds to **16:00 UTC**

Material interpretation points:
- this is **not** based on Coinbase, index prices, or BTC/USD elsewhere
- this is **not** about whether BTC traded above 70,000 at any point in the day
- this is **not** about the open, high, or low of the candle
- the question is only whether the final Binance BTC/USDT **Close** for that exact 1-minute bar is **strictly above 70,000**

# Key assumptions

- Short-horizon path persistence is a better base-rate than sudden regime change over the next ~2 hours.
- No exchange-specific dislocation on Binance appears before settlement.
- There is no new macro or crypto-specific catalyst large enough to force BTC below 70,000 into the settlement minute.

# Why this is decision-relevant

This is a narrow time-and-source-sensitive contract. The main decision value is not a grand Bitcoin thesis; it is whether the current cushion above the strike is large enough, given the short remaining time, to justify odds above market. My view is that it is.

# What would falsify this interpretation / change your mind

I would move materially lower if any of the following happened before noon ET:

- Binance BTC/USDT lost **71,000** quickly and momentum turned sharply negative
- Binance diverged downward from other major spot venues, raising source-specific settlement risk
- a fresh macro or crypto shock made a sub-70,000 noon close substantially more likely
- additional verified intraday data showed much higher short-horizon downside frequency than this simple outside-view estimate assumes

# Source-quality assessment

- **Primary source used:** Binance BTC/USDT, which is the contract's named source of truth.
- **Most important secondary/contextual source:** Coinbase BTC spot as an operationally separate verification surface.
- **Evidence independence:** **Medium**. Binance and Coinbase are separate venues, but both reflect the same underlying BTC market.
- **Source-of-truth ambiguity:** **Low**. The contract mechanics are explicit about exchange, pair, timeframe, and price field.

# Verification impact

- **Additional verification pass performed:** Yes.
- **What was checked:** I verified the contract mechanics on Polymarket and cross-checked live BTC price context on Coinbase after checking Binance.
- **Did it materially change the view?** No. It increased confidence in the contract interpretation and that Binance was not showing an obvious outlier price, but it did not materially alter the Yes-leaning estimate.

# Reusable lesson signals

- **Possible durable lesson:** For short-horizon crypto threshold markets, current distance from strike plus remaining time often matters more than broad narrative views.
- **Possible missing or underbuilt driver:** None confidently identified from this run.
- **Possible source-quality lesson:** When Polymarket names a single exchange and candle field, use that surface first and add one cross-venue check mainly for operational sanity.
- **Confidence that any lesson here is reusable:** Medium.

# Orchestrator review suggestions

- **Review later for durable lesson:** no
- **Review later for driver candidate:** no
- **Review later for canon or linkage issue:** no
- **Reason:** This looks like a routine narrow-resolution market with clear source-of-truth mechanics rather than a canon gap.

# Recommended follow-up

No major follow-up suggested for the base-rate lane. If another lane finds an imminent catalyst in the next two hours, that would be the main reason to revisit the estimate.