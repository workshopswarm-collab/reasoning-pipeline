---
type: agent_finding
case_key: case-20260330-6c201738
dispatch_id: dispatch-case-20260330-6c201738-20260405T212516Z
research_run_id: dbdd6dfe-eebd-498f-a9e1-1f69619d2e74
analysis_date: 2026-04-05
persona: market-implied
topic: case-20260330-6c201738 | market-implied
question: Will the U.S. tariff rate on China be between 5% and 15% on March 31, 2026?
date_created: 2026-04-05
agent: Orchestrator
stance: disagree
certainty: medium-high
importance: high
novelty: medium
time_horizon: through 2026-03-31
related_entities: []
related_drivers: []
upstream_inputs: []
downstream_uses: []
tags: [market-implied, tariff, china, resolution-risk, source-hierarchy, timing]
---

# Claim

The market appears to be pricing a simple 10% China-wide tariff story, but the stronger official reading is that two general China-wide duties were in effect by the March 31, 2026 checkpoint: a 10% reciprocal tariff plus a separate 10% synthetic-opioid-related China duty. On that reading, the relevant general tariff rate is 20%, so the 5%-15% bracket should resolve **No**.

## Market-implied baseline

The current price is 0.959, implying about **95.9% Yes** that the tariff rate will be between 5% and 15% on March 31, 2026.

## Own probability estimate

**18% Yes / 82% No.**

## Agreement or disagreement with market

I **disagree** with the market.

The best case for the market is that traders are correctly recognizing the May 2025 de-escalation from the extreme April China reciprocal tariff headlines to a 10% in-effect reciprocal tariff, and that they are treating this 10% as the relevant “general tariff rate.” That is a reasonable starting prior and likely explains why the price is so high.

But after taking the market seriously and tracing the official action chain, I think the market is likely underweighting one material point: the separate China-wide synthetic-opioid duty was reduced from 20% to 10% effective November 10, 2025, not removed. If the contract’s additive “general tariff rate” logic is applied as written, then 10% reciprocal + 10% opioid-related China duty = **20%**, which is outside the 5%-15% band.

## Implication for the question

If this interpretation is right, the market price is too high on Yes and is embedding an overly simple single-tariff view. The contract looks more naturally like a **No** market unless there is later policy change or a resolver-specific interpretation that only one of the two general China-wide duties counts.

## Key sources used

1. **Primary / authoritative / direct:** White House executive order, “Modifying Reciprocal Tariff Rates to Reflect Discussions with the People’s Republic of China” (May 12, 2025). Effective May 14, 2025, PRC goods became subject to an additional 10% ad valorem reciprocal tariff while 24 percentage points were suspended and higher retaliatory-modified rates were removed.
2. **Primary / authoritative / direct:** White House executive order, “Further Modifying Reciprocal Tariff Rates to Reflect Ongoing Discussions with the People’s Republic of China” (Aug. 11, 2025). Continued that suspension until Nov. 10, 2025.
3. **Primary / authoritative / direct:** White House executive order, “Modifying Reciprocal Tariff Rates Consistent with the Economic and Trade Arrangement Between the United States and the People’s Republic of China” (Nov. 4, 2025). Continued suspension of heightened reciprocal tariffs until Nov. 10, 2026, leaving the 10% reciprocal tariff in place.
4. **Primary / authoritative / direct:** White House executive order, “Further Amendment to Duties Addressing the Synthetic Opioid Supply Chain in the People’s Republic of China” (Mar. 3, 2025). Raised the PRC duty from 10% to 20%.
5. **Primary / authoritative / direct:** White House executive order, “Modifying Duties Addressing the Synthetic Opioid Supply Chain in the People’s Republic of China” (Nov. 4, 2025). Reduced that PRC duty from 20% to 10% effective Nov. 10, 2025.
6. **Primary / official contextual index:** USTR “Presidential Tariff Actions” page, which lists the China tariff action chain and supports chronology/source hierarchy.
7. **Contract / direct contextual source:** Polymarket market description, especially the additive example, the “in effect” requirement, and the exclusion of item-specific exceptions or increases.

Supporting provenance artifacts:
- Source note: `qualitative-db/40-research/cases/case-20260330-6c201738/source-notes/2026-04-05-market-implied-white-house-china-tariff-actions.md`
- Assumption note: `qualitative-db/40-research/cases/case-20260330-6c201738/analyses/2026-04-05/dispatch-case-20260330-6c201738-20260405T212516Z/assumptions/market-implied.md`
- Evidence map: `qualitative-db/40-research/cases/case-20260330-6c201738/analyses/2026-04-05/dispatch-case-20260330-6c201738-20260405T212516Z/evidence/market-implied.md`

## Supporting evidence

- The May 12, 2025 White House order explicitly set the PRC reciprocal tariff at **10% effective May 14, 2025** while suspending 24 percentage points and removing higher retaliatory-modified rates.
- The Aug. 11 and Nov. 4, 2025 White House orders explicitly extended that reciprocal-tariff suspension, with the Nov. 4 order extending it to **Nov. 10, 2026**. So the reciprocal 10% was still in effect on March 31, 2026.
- The Mar. 3, 2025 opioid-related China duty was raised to **20%**, and the Nov. 4, 2025 order explicitly reduced it to **10% effective Nov. 10, 2025**. So a separate China-wide 10% duty was also in effect on March 31, 2026.
- The market contract says the “general tariff rate” includes general tariffs layered on top of one another and excludes only item-specific exceptions or increases. That wording favors **aggregation** of multiple general China-wide duties.

## Counterpoints / strongest disconfirming evidence

The strongest disconfirming consideration is interpretive: the market may be efficiently pricing that only the reciprocal 10% counts as the relevant “general tariff rate,” while the opioid-linked duty is viewed as a distinct emergency measure that resolvers may not aggregate into the headline tariff bracket. If the resolver uses that narrower interpretation, Yes could still be correct despite the additive reading I favor.

## Resolution or source-of-truth interpretation

**Governing source of truth:** per contract, official Trump administration information is primary; consensus of credible information is secondary/fallback.

What counts:
- tariffs that are **in effect** at March 31, 2026 12:00 PM ET
- general China-wide tariffs, including stacked general tariffs if multiple such duties are simultaneously in effect

What does not count:
- paused tariffs
- announced-but-not-yet-effective tariffs
- item-specific exceptions or item-specific increases
- effective tariff calculations that depend on product mix

Case-specific checks:
- **Verify in-effect timing:** satisfied. The key White House orders include explicit effective dates; both the reciprocal 10% and the reduced opioid-related 10% appear in effect before the checkpoint and remain effective through it absent later action.
- **Exclude paused announcements:** satisfied. I am not counting the suspended higher reciprocal China rates; I am counting only the reduced in-effect rates after the suspension orders.
- **Confirm source hierarchy:** satisfied. I relied primarily on White House executive orders and secondarily on the official USTR index page plus the market contract text.
- **Validate rate calculation logic:** satisfied. My logic is additive because the contract’s own example treats the general tariff rate as the sum of general tariffs layered on one another, while excluding only item-specific deviations.

## Key assumptions

The central assumption is that both in-effect China-wide duties count toward the contract’s “general tariff rate.” I think that is the best textual reading, but it remains the main interpretation risk.

## Why this is decision-relevant

This is exactly the kind of market where a high price can still hide a rule-interpretation problem. The market may be directionally anchored to a true fact (China reciprocal tariff de-escalated to 10%) but still be wrong on settlement because another general China-wide 10% duty remained in force.

## What would falsify this interpretation / change your mind

- A later White House/USTR action before March 31, 2026 removing one of the two 10% components.
- An explicit Polymarket clarification saying only one of these China-wide duties counts.
- A stronger official or near-official tariff summary showing that, for this contract’s purposes, the operative general China rate should be treated as 10% rather than 20%.

## Source-quality assessment

- **Primary source used:** White House executive orders on the reciprocal-tariff chain and the synthetic-opioid China-duty chain.
- **Key secondary/contextual source used:** USTR Presidential Tariff Actions page plus the market contract wording itself.
- **Evidence independence:** **medium**. The key official sources are independent enough in form (multiple executive actions plus USTR index), but they all originate from the same administration.
- **Source-of-truth ambiguity:** **medium**. Documentary ambiguity is low; interpretive ambiguity is moderate because the contract says “general tariff rate” rather than specifying an exact legal aggregation formula.

## Verification impact

Yes, I performed an additional verification pass because the market-implied probability was above 85% and the case is high-difficulty/high-resolution-risk.

That extra pass materially strengthened the **No** view. Initial market-respecting prior: maybe 10% is the operative number. After checking the Nov. 2025 official chain, I concluded that a second 10% China-wide duty remained in effect and likely should be counted.

## Reusable lesson signals

- Possible durable lesson: in tariff-bracket markets, “general tariff rate” may require aggregating multiple general duties across legal authorities, not just tracking the most cited headline tariff.
- Possible missing or underbuilt driver: none clearly identified yet.
- Possible source-quality lesson: for tariff markets, executive-order effective dates matter more than headline announcement coverage.
- Confidence reusability: **medium**.

## Orchestrator review suggestions

- review later for durable lesson: **yes**
- review later for driver candidate: **no**
- review later for canon or linkage issue: **no**
- one-sentence reason: this case exposed a reusable pitfall where market participants may anchor on the headline tariff while missing additive contract logic across separate general duties.

## Recommended follow-up

Monitor for any White House/USTR action that changes either the reciprocal 10% or the opioid-related 10% before March 31, 2026, and watch for any resolver clarification on whether both general China-wide duties should be summed.

## Compliance with case checklist / evidence floor

- Market-implied probability stated: **yes** (95.9% Yes)
- Own probability estimate stated: **yes** (18% Yes / 82% No)
- Strongest disconfirming evidence explicitly named: **yes** (narrower resolver interpretation that only one 10% duty counts)
- What could change my mind: **yes**
- Governing source of truth explicitly identified: **yes**
- Source-quality assessment included: **yes**
- Verification impact included: **yes**
- Reusable lesson signals included: **yes**
- Orchestrator review suggestions included: **yes**
- What counts / does not count / contract effect explained: **yes**
- Additional case-specific checks addressed explicitly: **yes**
- Additional verification pass performed and reflected: **yes**
- Evidence floor met with at least three meaningful sources: **yes** (multiple official White House orders + official USTR index + contract text)
- Provenance preserved in auditable artifacts: **yes**