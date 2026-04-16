---
type: agent_finding
case_key: case-20260413-64e915de
dispatch_id: dispatch-case-20260413-64e915de-20260413T234340Z
research_run_id: c68f2c43-8bb5-470e-a302-be302f47d634
analysis_date: 2026-04-13
persona: base-rate
domain: crypto
subdomain: protocols
entity: ethereum
topic: will-ethereum-reach-2400-april-13-19
question: "Will Ethereum reach $2,400 April 13-19?"
date_created: 2026-04-13
agent: orchestrator
stance: yes-lean
certainty: medium
importance: medium
novelty: low
time_horizon: "2026-04-13 to 2026-04-19"
related_entities: ["ethereum"]
related_drivers: []
proposed_entities: []
proposed_drivers: ["short-horizon-crypto-threshold-touch"]
upstream_inputs: []
downstream_uses: []
tags: ["agent-finding", "base-rate", "crypto", "ethereum", "polymarket"]
driver:
---

# Claim

My base-rate view is that Ethereum is likely to reach $2,400 at some point during April 13-19, but the market is priced too close to certainty. This looks like a high-probability threshold-touch setup, not a lock.

**Evidence-floor compliance:** met with two meaningful sources plus an extra verification pass: (1) the Polymarket market page as the primary contract/market surface and (2) CoinGecko hourly ETH/USD data as an independent external price verification source.

## Market-implied baseline

Current market-implied probability from `current_price` is **90.5%** for the "$2,400" outcome. A direct fetch of the Polymarket page also showed the "$2,400" bucket around **92%** at check time, which is close enough to treat the market as pricing this event at roughly **90-92%**.

## Own probability estimate

**84%**.

## Agreement or disagreement with market

**Roughly agree on direction, but modestly disagree on magnitude.**

Base-rate logic supports a high probability because:
- this is a **threshold-touch** style question over roughly a week, not a requirement to close above $2,400;
- ETH was already trading in the **mid-$2,300s**, so the remaining gap was only about **1%** on the extra verification pass;
- in crypto, a 1% move over a week is usually within ordinary noise unless there is a fresh negative shock.

I still shade below the market because extreme probabilities deserve extra skepticism, and the independent price verification I checked still showed ETH below $2,400 at the time of review.

## Implication for the question

The outside view says this should be favored, but not treated as resolved. The market is probably directionally right that the path of least resistance is a wick or brief touch through $2,400 during the window, yet the remaining uncertainty is larger than a 90%+ price suggests.

## Key sources used

- **Primary / governing market surface:** Polymarket event page for the live bucket pricing and the contract/rules surface. Source note: `qualitative-db/40-research/cases/case-20260413-64e915de/researcher-source-notes/2026-04-13-base-rate-polymarket-market-page.md`
- **Secondary / contextual but independent verification:** CoinGecko ETH/USD 7-day hourly market chart API, used to verify whether ETH had already reached the threshold and how close it was. Source note: `qualitative-db/40-research/cases/case-20260413-64e915de/researcher-source-notes/2026-04-13-base-rate-coingecko-eth-price.md`
- **Canonical mapping check:** `qualitative-db/20-entities/protocols/ethereum.md` confirms `ethereum` as the clean entity slug. I did **not** force any canonical driver slug; `short-horizon-crypto-threshold-touch` is recorded only as a **proposed_driver**.

Direct vs contextual:
- Direct for market baseline / contract surface: Polymarket.
- Contextual external price verification: CoinGecko.

Governing source of truth:
- **The Polymarket market rules / official data source for this event are the governing source of truth**, even though the fetch extract did not expose the full rules text cleanly.

## Supporting evidence

- The market itself prices the event near certainty, implying participants view this as a routine short-horizon touch.
- Independent external verification showed ETH around **$2,374.36** at the latest sampled point, meaning only a small additional move was needed.
- For a volatile asset like ETH, a roughly 1% threshold breach during a week is usually common enough that the outside view remains favorable absent a new regime break.

## Counterpoints / strongest disconfirming evidence

The strongest disconfirming consideration is that my independent verification source still showed ETH **below $2,400** as of review time, despite the market pricing the touch above 90%. That means the event had not yet obviously occurred, and there is still real path dependence over the remaining days.

A second disconfirming consideration is **source-of-truth ambiguity**: I could not cleanly extract the exact settlement source/rules text from the rendered Polymarket page, so there is some residual uncertainty around exactly what reference counts as "hit."

## Resolution or source-of-truth interpretation

This market appears to be about **what price Ethereum will hit during April 13-19**, which strongly suggests an intraperiod threshold-touch interpretation rather than a closing-price requirement. That interpretation is the main reason the base rate is high.

Still, the **official Polymarket rules and designated data source govern resolution**, not CoinGecko or any other contextual chart. Because the market is date-specific and the implied probability is extreme, that contract surface matters explicitly here.

## Key assumptions

- The contract resolves on a standard threshold-hit basis rather than a stricter close/settlement condition.
- ETH remains in an ordinary short-horizon volatility regime through the rest of the window.
- No major negative shock pushes price materially away from $2,400 before a touch occurs.

See supporting assumption note: `qualitative-db/40-research/cases/case-20260413-64e915de/researcher-analyses/2026-04-13/dispatch-case-20260413-64e915de-20260413T234340Z/assumptions/base-rate.md`

## Why this is decision-relevant

This is the kind of setup where the market can be broadly right while still too compressed near certainty. For sizing or synthesis, the useful takeaway is not "fight the market," but "do not round 90%+ to 100% when the event has not yet printed on an external verification pass."

## What would falsify this interpretation / change your mind

I would move meaningfully lower if:
- the full rules show the contract requires something stricter than an ordinary touch;
- higher-frequency or settlement-source data show repeated failure near $2,400 with weakening conditions;
- ETH sells off materially away from the level early in the window.

I would move higher if:
- the governing source confirms ETH already traded at or above $2,400; or
- a clean rules check confirms a broad and permissive threshold-touch definition with no narrow exclusions.

## Source-quality assessment

- **Primary source used:** Polymarket event page / contract surface.
- **Most important secondary/contextual source used:** CoinGecko ETH/USD hourly market-chart API.
- **Evidence independence:** **medium** — the two sources serve different functions and are meaningfully distinct, but both concern the same live market state.
- **Source-of-truth ambiguity:** **medium** — the governing source is clearly the Polymarket rules, but the detailed rules text was not cleanly exposed in the fetched page extract.

## Verification impact

**Additional verification pass performed:** yes.

I explicitly checked an independent external price source after seeing the extreme market probability. It **did not materially change the directional view**, but it **did** keep me below the market because the sampled external series still showed ETH under $2,400 at review time.

## Reusable lesson signals

- **Possible durable lesson:** Short-horizon crypto threshold-touch markets can deserve high priors when the asset is already within ~1% of the target, but extreme market pricing still warrants an explicit independent price check.
- **Possible missing or underbuilt driver:** `short-horizon-crypto-threshold-touch` may be a reusable driver family if similar markets recur.
- **Possible source-quality lesson:** For rendered market pages, rules extraction can be lossy; explicit rule capture may matter even in low-difficulty cases with extreme probabilities.
- **Confidence reusable:** medium.

## Orchestrator review suggestions

- **Review later for durable lesson:** no
- **Review later for driver candidate:** yes
- **Review later for canon or linkage issue:** no
- **Reason:** repeated threshold-touch crypto markets may justify a reusable driver or heuristic note, but this single case alone is not enough for canon change.

## Recommended follow-up

If synthesis needs tighter confidence bounds, do one more targeted rules/source-of-truth pull from the exact Polymarket resolution source and, if available, a higher-frequency price source closer to the threshold event.