---
type: agent_finding
case_key: case-20260416-969f7c01
dispatch_id: dispatch-case-20260416-969f7c01-20260416T013210Z
research_run_id: 810c1ece-82f1-479d-9fb3-d4c2b39fb0eb
analysis_date: 2026-04-16
persona: base-rate
domain: crypto
subdomain: spot-price-threshold-markets
entity: ethereum
topic: ethereum-above-2200-on-april-17
question: "Will the Binance ETH/USDT 12:00 ET one-minute candle on 2026-04-17 close above 2200?"
driver: operational-risk
date_created: 2026-04-16
agent: orchestrator
stance: yes-lean
certainty: medium
importance: high
novelty: low
time_horizon: "<48h"
related_entities: ["binance", "ethereum"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: []
tags: ["base-rate", "crypto", "eth", "binance", "threshold-market"]
---

# Claim

Base-rate view: **Yes is more likely than not and still the right side, but I would price it below the market's ~94.5% confidence.** With ETH/USDT currently in the mid-2300s and the strike at 2200 less than a day before resolution, the outside-view prior favors a close above 2200 at noon ET on Apr 17. But crypto is volatile enough, and this contract is narrow enough, that a single-minute noon candle should not be treated as nearly locked.

## Market-implied baseline

The assigned current price is **0.945**, implying about **94.5%** for Yes.

## Own probability estimate

**88% Yes.**

## Agreement or disagreement with market

**Mild disagreement.** I agree with the direction: Yes is the base-rate-favored outcome because current ETH/USDT spot is well above the strike and the remaining time window is short. I disagree with the extremity. A 94.5% market price leaves only 5.5% for a move that requires neither a structural regime change nor a bizarre settlement rule—just a sub-2200 Binance ETH/USDT one-minute close exactly at noon ET on Apr 17. For a major crypto asset, a ~6-7% cushion over less than a day is strong but not close to certainty.

## Implication for the question

The market should still be interpreted as **likely Yes**, but the outside view says the strike is not so far out of reach that No becomes negligible. If the purpose is directional decision support rather than trade execution, the main takeaway is: favor Yes, but keep real respect for single-minute and overnight volatility risk.

## Key sources used

Evidence floor compliance: **met with 3 meaningful sources / source surfaces plus an additional verification pass.**

1. **Primary governing source (authoritative for contract mechanics):** Polymarket market page and rules for this exact contract. Direct and authoritative on what must happen for Yes/No.
2. **Key contextual price source:** CoinMarketCap ETH/USDT converter/history page showing live ETH/USDT around 2354 and prior daily ETH/USDT levels for Apr 10-16. Contextual, not settlement-authoritative.
3. **Independent live-context cross-check:** Binance ETH/USDT search result snippet showing spot around 2318 during research. Useful as a venue-consistent cross-check even though the fetch tool could not cleanly extract Binance page content.
4. **Supporting vault context:** Canonical Ethereum and operational-risk/reliability notes to frame outside-view and venue-mechanics risk, not to settle the market.

Case provenance artifacts:
- `qualitative-db/40-research/cases/case-20260416-969f7c01/researcher-source-notes/2026-04-16-base-rate-market-and-price-context.md`
- `qualitative-db/40-research/cases/case-20260416-969f7c01/researcher-analyses/2026-04-16/dispatch-case-20260416-969f7c01-20260416T013210Z/assumptions/base-rate.md`
- `qualitative-db/40-research/cases/case-20260416-969f7c01/researcher-analyses/2026-04-16/dispatch-case-20260416-969f7c01-20260416T013210Z/evidence/base-rate.md`

## Supporting evidence

- **Current spot cushion:** Contextual sources place ETH/USDT in the low/mid-2300s during the research window, roughly 5-7% above 2200.
- **Short time to resolution:** Less than a day remains until the relevant candle, which usually helps the currently in-the-money side if no catalyst intervenes.
- **Recent range context:** Recent daily context over the prior week is mostly above 2200, implying the strike is below current center-of-mass pricing rather than above it.
- **Simple threshold structure:** Yes only needs the final close of one specified minute to print above 2200; with spot materially above the strike at research time, the base case remains favorable.

## Counterpoints / strongest disconfirming evidence

**Strongest disconfirming consideration:** the market resolves on a **single Binance one-minute close at 12:00 ET**, not on a daily average or broad-market reference. That means a temporary downside move into the exact minute is enough for No.

Additional disconfirmers:
- Contextual recent history includes at least one nearby daily close below 2200 (about 2192 on Apr 12), so a sub-2200 print is plainly within recent realized range.
- Crypto can move several percent quickly on macro or risk-off headlines.
- Clean live extraction from Binance was not available via fetch, so there is modest residual operational/verification uncertainty.

## Resolution or source-of-truth interpretation

**Governing source of truth:** Binance ETH/USDT, specifically the **1-minute candle for 12:00 in ET timezone** on **Apr 17, 2026**, using the **final Close** price shown on Binance. The market resolves Yes only if that close is **strictly higher than 2200**.

Material conditions that all must hold for Yes:
1. The relevant instrument is **Binance ETH/USDT**, not ETH/USD and not another exchange.
2. The relevant observation is the **1-minute candle corresponding to 12:00 ET (noon)** on Apr 17, 2026.
3. The relevant field is the candle's **final Close**.
4. The close must be **greater than 2200**, not equal to it.
5. Price precision follows Binance display precision.

Explicit timing check:
- Assignment metadata gives `resolves_at: 2026-04-17T12:00:00-04:00`, which is **12:00 PM EDT / ET** on Apr 17, 2026.
- I explicitly verified that the contract language is date-sensitive and timezone-sensitive; this is a noon-ET single-minute event, not an end-of-day close.

Explicit canonical-mapping check:
- Clean canonical slug confirmed: `ethereum`.
- Clean canonical driver slugs confirmed: `operational-risk`, `reliability`.
- **Binance** appears causally relevant as the settlement venue, but I was only given `binance-us.md`, not a clear canonical `binance` entity note. I therefore kept `binance` in `proposed_entities` rather than forcing a weak canonical fit.

## Key assumptions

- Binance ETH/USDT trading and charting remain normal through the resolution minute.
- ETH does not experience a sharp enough downside move before noon ET on Apr 17 to erase the current cushion.
- No hidden rule clarification changes which exact minute or data surface counts.

## Why this is decision-relevant

This case is a good example of a market where the headline probability can look almost settled even though the mechanism is still a volatile intraday threshold on a major crypto pair. For synthesis, that means the right output is not “almost certain Yes,” but “clear Yes lean with nontrivial tail risk.”

## What would falsify this interpretation / change your mind

- A fresh check on Apr 17 morning showing ETH/USDT has already fallen into the low 2200s or below.
- Evidence of Binance-specific chart, symbol, or operational problems near the resolution window.
- A clearer venue-level source showing the effective noon ET reference candle is closer to 2200 than current contextual sources imply.
- Any new macro/crypto shock that plausibly produces a >6% downside move before noon ET.

## Source-quality assessment

- **Primary source used:** Polymarket rules page for this exact market; high relevance and authoritative for contract mechanics.
- **Most important secondary/contextual source:** CoinMarketCap ETH/USDT live converter/history page; useful for independent price context but not authoritative for settlement.
- **Evidence independence:** **Medium.** The rules source and contextual price sources are distinct, but all ultimately reflect the same underlying market.
- **Source-of-truth ambiguity:** **Low-to-medium.** The settlement source is clearly named, but there is still some implementation ambiguity around exact Binance candle visibility and ET-to-candle mapping because direct Binance extraction was limited.

## Verification impact

**Additional verification pass performed:** yes.
- I did an explicit second pass on the Binance/Polymarket mechanics and independent price-context checks after the initial contract/template read.
- It **did not materially change** the directional view.
- It **did modestly reduce confidence in the market extreme**, because the extra pass reinforced that this is a single-minute Binance-close market rather than a broader average and that direct Binance extraction was not perfectly clean.

## Reusable lesson signals

- **Possible durable lesson:** short-horizon crypto threshold markets with extreme probabilities can still merit haircutting when settlement depends on one minute of venue-specific data.
- **Possible missing or underbuilt driver:** maybe a more specific driver around `resolution-microstructure` or `venue-specific-settlement-risk`, but confidence is low from one case.
- **Possible source-quality lesson:** when direct exchange extraction is brittle, preserve both the contract rules source and at least one independent contextual price source.
- **Reusable confidence:** low-to-medium.

## Orchestrator review suggestions

- review later for durable lesson: **no**
- review later for driver candidate: **no**
- review later for canon or linkage issue: **yes**
- one-sentence reason: the case highlights that a canonical `binance` entity may be useful distinct from `binance-us`, but this single case alone is not enough to justify broader canon changes.

## Recommended follow-up

No broad follow-up suggested now. Only re-check if ETH/USDT moves materially toward 2200 before the Apr 17 noon ET window or if Binance-specific operational issues emerge.
