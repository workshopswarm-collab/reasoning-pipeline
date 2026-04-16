---
type: agent_finding
case_key: case-20260414-fdd1ff67
dispatch_id: dispatch-case-20260414-fdd1ff67-20260414T200433Z
research_run_id: ca8bc1f5-e9c1-4900-a07d-ad70e7fb19df
analysis_date: 2026-04-14
persona: variant-view
domain: sports
subdomain: football
entity:
topic: "Al Qadisiyah Saudi Club vs. Al Shabab Saudi Club draw market"
question: "Will Al Qadisiyah Saudi Club vs. Al Shabab Saudi Club end in a draw?"
driver:
date_created: 2026-04-14
agent: Orchestrator
stance: disagree
certainty: medium-low
importance: medium
novelty: medium
time_horizon: event-date
related_entities: []
related_drivers: []
proposed_entities: ["al-qadsiah-fc", "al-shabab-club-riyadh"]
proposed_drivers: ["football-match-outcome-pricing", "market-contract-surface-integrity"]
upstream_inputs: []
downstream_uses: []
tags: ["variant-view", "saudi-pro-league", "football", "draw-market", "source-of-truth-ambiguity"]
---

# Claim

The strongest credible variant view is that the apparent draw consensus is overconfident and may be partly contaminated by contract-surface ambiguity. Conditional on the assignment title being the intended proposition, I estimate the match draw probability materially below the market.

## Market-implied baseline

The assignment gives `current_price: 0.76`, so the market-implied baseline is **76%**.

## Own probability estimate

My own estimate for the **draw** outcome is **36%**.

**Evidence-floor compliance:** met the low-difficulty evidence floor with two meaningful sources: (1) direct Polymarket contract/resolution text and (2) independent contextual league/team verification via Wikipedia. I also performed an additional verification pass because my estimate differs from the market by more than 10 percentage points, but that extra pass did not produce a clean fixture-odds source.

## Agreement or disagreement with market

I **disagree** with the market.

The market's strongest argument, if the assignment is taken at face value, is that some hidden team-news or matchup context may have driven a very high draw price. But the more compelling variant interpretation is that **76% is implausibly high for a standard first-division football draw market**, and the fetched Polymarket surface creates a more important concern: the visible contract text appears to describe a **Qadisiyah win** market rather than a draw market.

So my disagreement is not just "the crowd is bad at football." It is that the crowd/price may be anchored to a stale or mislabeled contract surface, or the assignment-to-market mapping may be off. In that setting, a conservative variant view should resist inheriting the raw 0.76 at face value.

## Implication for the question

If the assignment title is correct and the market really is about a draw, I would treat YES-on-draw as overpriced at 0.76. If the Polymarket page text is the true governing contract, then the case itself needs relabeling before the price can be interpreted correctly.

## Key sources used

- **Primary / authoritative for resolution mechanics:** `researcher-source-notes/2026-04-14-variant-view-polymarket-resolution-source.md`
  - direct evidence on what counts for settlement
  - direct evidence of source-of-truth wording
  - direct evidence of the contract-surface mismatch
- **Secondary / contextual:** `researcher-source-notes/2026-04-14-variant-view-league-context.md`
  - contextual verification that Al Qadsiah and Al Shabab are real current Saudi Pro League clubs relevant to the fixture framing
- **Supporting provenance artifacts:**
  - assumption note: `researcher-analyses/2026-04-14/dispatch-case-20260414-fdd1ff67-20260414T200433Z/assumptions/variant-view.md`
  - evidence map: `researcher-analyses/2026-04-14/dispatch-case-20260414-fdd1ff67-20260414T200433Z/evidence/variant-view.md`

## Supporting evidence

- The Polymarket fetch states that the market resolves YES if **Al Qadisiyah wins**, otherwise NO. That is the most important piece of evidence in the run because it does not match the assignment title.
- The same source clearly states the governing source of truth: **official statistics of the event as recognized by the governing body or event organizers**, with credible-reporting fallback only if official final stats are unavailable within 2 hours.
- The contract is clearly a normal football-outcome market limited to **90 minutes plus stoppage time**, which makes an extreme 76% draw price look suspicious absent extraordinary external evidence.
- League/team contextual verification supports that the entities themselves are real and current, reducing the chance that the mismatch comes from researching the wrong sport or wrong clubs.

## Counterpoints / strongest disconfirming evidence

The strongest disconfirming consideration is that the **assignment metadata consistently says the market is about a draw**, which could mean the assignment layer is right and the fetched Polymarket page is the misleading surface. Also, I did **not** secure a clean independent sportsbook/exchange odds page for the exact fixture during this run, so my 36% estimate partly relies on base-rate skepticism toward a 76% draw number rather than fixture-specific price triangulation.

## Resolution or source-of-truth interpretation

The governing source of truth at settlement should be the **official match statistics recognized by the governing body or event organizers** for the specific match outcome after 90 minutes plus stoppage time.

However, there is a separate and more immediate ambiguity: the fetched contract text appears inconsistent with the assignment title. So I distinguish:

- **Settlement source of truth:** official match statistics / governing-body-recognized event stats.
- **Question-definition ambiguity:** whether the intended proposition is actually "draw" or instead "Qadisiyah win." That ambiguity remains unresolved in this run.

## Key assumptions

- The assignment title reflects the intended proposition despite the fetched contract-text mismatch.
- A normal football draw base rate is informative enough that 76% should be treated as extraordinary and requiring strong corroboration.
- Failure to find clean independent odds/context in a low-difficulty case is itself mildly negative for trusting the extreme market price.

## Why this is decision-relevant

This is decision-relevant because the variant edge is not a subtle tactical read; it is that the market may be **structurally misread**. If the proposition mapping is wrong, downstream synthesis should not use the 0.76 number as clean evidence of consensus confidence on draw.

## What would falsify this interpretation / change your mind

What would most change my mind:

- a second clean Polymarket/API retrieval confirming that the intended contract for this slug is genuinely **draw YES** rather than **Qadisiyah win YES**;
- a reputable independent sportsbook or exchange showing the exact fixture's draw price consistent with roughly 70%+ draw probability;
- controller clarification that the assignment title is wrong and the actual market is home win, not draw.

## Source-quality assessment

- **Primary source used:** Polymarket market page text fetched from the assigned slug.
- **Most important secondary/contextual source:** Wikipedia league/team pages confirming the clubs and competition context.
- **Evidence independence:** **medium-low**. I have one direct authoritative market source plus one contextual source, but I lacked a clean independent odds source.
- **Source-of-truth ambiguity:** **high** for question definition, **low-medium** for settlement mechanics once the intended contract is known.

## Verification impact

- **Additional verification pass performed:** yes.
- **Did it materially change the estimate or mechanism view?** No; it mostly reinforced that the main issue is contract-surface ambiguity and limited independent odds retrieval.
- **How it affected the view:** it reduced confidence somewhat, but did not move me toward accepting 0.76 as a trustworthy draw estimate.

## Reusable lesson signals

- **Possible durable lesson:** for sports-outcome markets, contract-surface integrity checks can matter more than handicapping when the displayed probability is extreme.
- **Possible missing or underbuilt driver:** `market-contract-surface-integrity` may deserve future review if this kind of mismatch recurs.
- **Possible source-quality lesson:** extreme sports prices should be independently triangulated before being trusted, especially when the visible contract text and assignment title diverge.
- **Confidence that any lesson here is reusable:** medium.

## Orchestrator review suggestions

- **review later for durable lesson:** yes
- **review later for driver candidate:** yes
- **review later for canon or linkage issue:** yes
- **one-sentence reason:** this run surfaced a potentially important recurring failure mode where assignment metadata, market title, and fetched contract text may diverge.

## Recommended follow-up

- Verify the exact Polymarket contract definition for slug `spl-qad-sha-2026-04-23` via a second market surface or API.
- If the true proposition is indeed draw, obtain one clean independent odds screen before taking the market price seriously.
- If the true proposition is Qadisiyah win, relabel the case and discard this draw estimate.
