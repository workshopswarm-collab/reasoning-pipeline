---
type: agent_finding
domain: energy
subdomain: gasoline_prices
entity: AAA Fuel Prices
topic: Will gas hit (High) $4.00 by March 31?
question: Will the AAA national average regular gas price reach at least $4.000 on any day by March 31, 2026?
driver: pump_price_spike
date_created: 2026-04-05
agent: base-rate
stance: leaning_yes_but_not_certain
certainty: medium
importance: medium
novelty: medium
time_horizon: through_2026-03-31
related_entities: [AAA Fuel Prices, EIA, FRED]
related_drivers: [pump_price_spike, gasoline_price_history]
upstream_inputs: [qualitative-db/40-research/source-notes/by-market/case-20260405-b842cb71-base-rate-aaa-settlement-and-near-deadline-bracket.md, qualitative-db/40-research/source-notes/by-market/case-20260405-b842cb71-base-rate-fred-history-context.md]
downstream_uses: []
tags: [polymarket, aaa, gasoline, threshold-market, base-rate]
---

# Claim
My base-rate view is **Yes, but only moderately**: I estimate about a **70%** chance that AAA's national average regular price hit **at least $4.000** on some day by March 31, 2026.

The main reason is that the governing AAA source itself brackets the move very tightly: AAA reported **$3.981 on March 26** and **$4.081 on April 2**, while saying on April 2 that the average had exceeded $4 "**this week**." That makes a pre-March-31 crossing more likely than not, but not certain, because I did not recover the exact AAA homepage value for March 31 and the contract uses a hard truncation threshold.

## Market-implied baseline
The market price of **0.775** implies about a **77.5%** probability of Yes.

## Own probability estimate
**70% Yes**.

## Agreement or disagreement with market
I **roughly agree but am slightly below the market**.

Why I am not lower:
- AAA is the governing source and its own reports show the national average moving from **$3.981 on March 26** to **$4.081 on April 2**.
- The threshold gap on March 26 was only **1.9 cents**.
- AAA explicitly said on March 26 that the national average "could reach $4/gallon in the coming days," and on April 2 said it had exceeded $4 "this week."

Why I am not higher:
- This is still a **timing-sensitive threshold market** with a hard cutoff on **March 31**.
- The contract's "first two digits" rule means **$3.999 would still be No**; no rounding grace exists.
- A strong contextual check, the FRED/EIA weekly U.S. regular gas series, printed **3.990 on 2026-03-30**, which is extremely close but still below $4 and therefore is meaningful disconfirming context.

## Implication for the question
My outside-view read is that the market is directionally right to lean Yes, because the direct AAA evidence strongly suggests the crossing happened around the deadline window. But the base rate of national U.S. gasoline spending much time above $4 is low, and the exact settlement date matters enough that this should not be treated as near-certain.

## Key sources used
**Authoritative / settlement source**
- AAA Fuel Prices homepage: https://gasprices.aaa.com/
  - Governing surface named by the contract: the cell under **"Regular"** and row **"Current Avg."**
  - Homepage fetched on 2026-04-05 showed **Current Avg. Regular = $4.110**.

**Direct AAA near-deadline evidence**
- AAA, March 26, 2026: "National Gas Average Jumps One Dollar in One Month"
  - https://gasprices.aaa.com/national-gas-average-jumps-one-dollar-in-one-month/
  - Direct value: **$3.981**
  - Direct text: average "could reach $4/gallon in the coming days"
- AAA, April 2, 2026: "For the First Time in Four Years, National Average Exceeds $4/Gallon"
  - https://gasprices.aaa.com/for-the-first-time-in-four-years-national-average-exceeds-4-gallon/
  - Direct value: **$4.081**
  - Direct text: average exceeded $4 "this week"

**Contextual / base-rate verification source**
- FRED GASREGW CSV (weekly U.S. regular gas price series, sourced from EIA): https://fred.stlouisfed.org/graph/fredgraph.csv?id=GASREGW
  - Contextual, not the settlement source
  - Shows **2026-03-30 = 3.990** and that only **2008** and **2022** ever hit $4+ in the long-run weekly series since 1990.

## Supporting evidence
- The strongest direct evidence is the **AAA bracket itself**: $3.981 on March 26 and $4.081 on April 2.
- Moving 10.0 cents over that week means the market only needed to find **1.9 cents** between March 26 and March 31.
- AAA's own language on March 26 already pointed to a likely near-term $4 test.
- April 2's "exceeded $4 this week" wording is more naturally consistent with a crossing inside the March 27-April 2 window than with a much later move.

## Counterpoints / strongest disconfirming evidence
The strongest disconfirming evidence is the **timing ambiguity plus the FRED/EIA weekly contextual print of 3.990 on March 30**.

That matters because:
- the market resolves on **or before March 31**, not "around then"
- the rule is **truncate, not round**
- a late-March price just under $4 is completely plausible
- if the actual AAA daily crossing first occurred on April 1 or April 2, the contract would still resolve **No**

## Resolution or source-of-truth interpretation
The governing source of truth is explicitly **AAA Fuel Prices**, specifically the homepage table cell under **Regular / Current Avg.**

Two case-specific mechanics matter:
1. **AAA gas price table check**: this is the exact settlement surface named by the contract, so it outranks EIA, FRED, news writeups, or any other gas-price source.
2. **First two digits rule check**: the contract says values are resolved on the first two digits after the decimal (example given: **$3.157 -> $3.15 bracket**). So the practical threshold here is **AAA Current Avg. Regular >= $4.000**. Values like **$3.999** do **not** count as hitting $4.00.

Because I did not recover a March 31 AAA snapshot, my probability remains probabilistic rather than definitive.

## Key assumptions
- AAA's April 2 phrase "this week" is informative about the threshold being crossed close to the end of March, not long after it.
- The AAA daily national average likely moved fairly continuously rather than jumping from below $3.98 to above $4.08 only after March 31.
- The contract is interpreted literally on truncation, with no hidden rounding convention.

## Why this is decision-relevant
This is a classic threshold-and-source market where the key question is not the broad gasoline story but **whether the authoritative source cleared the hard line in time**. The market's edge, if any, lives in the difference between "almost certainly soon" and "in time under the exact AAA rule."

## What would falsify this interpretation / change your mind
The main thing that would change my mind is an archived AAA homepage or other first-party AAA daily record showing:
- **March 31 Current Avg. Regular < $4.000** and
- the first **AAA** reading at or above $4.000 occurred only on **April 1 or later**.

Conversely, an archived March 31 or March 30 AAA page with **Current Avg. Regular >= $4.000** would move me to near-certainty Yes.

## Source-quality assessment
- **Primary source used:** AAA Fuel Prices homepage plus AAA's own March 26 and April 2 posts.
- **Most important secondary/contextual source used:** FRED GASREGW weekly series (contextual outside-view / disconfirming cross-check).
- **Evidence independence:** **medium**. The contextual check is meaningfully separate in format and methodology, but still within the same broad gas-price information ecosystem.
- **Source-of-truth ambiguity:** **low**. The contract clearly names AAA and the exact table cell, though exact archived daily retrieval for March 31 was not recovered.

## Verification impact
- **Additional verification pass performed:** yes.
- **Did it materially change the estimate or mechanism view?** yes, modestly.
- The extra contextual check (FRED/EIA weekly 3.990 on 2026-03-30) kept me from moving to an 80%+ Yes despite the bullish AAA bracket. It reinforced that the main uncertainty is exact timing around the deadline, not whether prices were generally surging.

## Reusable lesson signals
- **Possible durable lesson:** threshold markets tied to a named official table should be treated as source-archive retrieval problems, not generic narrative commodity calls.
- **Possible missing or underbuilt driver:** none clearly beyond the usual oil-shock / seasonal gasoline-demand driver.
- **Possible source-quality lesson:** when the settlement source is a live-updating homepage table, archived snapshots or first-party dated posts near the cutoff can matter more than richer but non-settlement datasets.
- **Confidence that any lesson here is reusable:** medium.

## Orchestrator review suggestions
- **Review later for durable lesson:** no.
- **Review later for driver candidate:** no.
- **Review later for canon or linkage issue:** no.
- **Reason:** this looks like a normal threshold-settlement case; no clear canon gap emerged beyond ordinary emphasis on archived source-of-truth retrieval.

## Recommended follow-up
If a higher-confidence pre-resolution read is needed, the best next step would be to recover a **March 30-31 archived AAA homepage snapshot or first-party AAA daily capture**. Short of that, I would treat **Yes as more likely than No, but not decisively so**.

## Evidence floor compliance
- **Assigned evidence floor:** one authoritative source may be sufficient.
- **How I met it:** I used the authoritative settlement source (**AAA homepage / AAA posts**) and added one contextual verification source (**FRED/EIA weekly series**) because the case is timing-sensitive and my estimate is not identical to the market.
- **Extra verification required by prompt:** not required, but I performed it anyway.
- **Provenance preserved in:**
  - `qualitative-db/40-research/source-notes/by-market/case-20260405-b842cb71-base-rate-aaa-settlement-and-near-deadline-bracket.md`
  - `qualitative-db/40-research/source-notes/by-market/case-20260405-b842cb71-base-rate-fred-history-context.md`
