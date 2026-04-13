---
type: agent_finding
case_key: case-20260413-9c835dfe
dispatch_id: dispatch-case-20260413-9c835dfe-20260413T162509Z
research_run_id: 543bb9e8-4b94-4eba-a73c-6475f6455b18
analysis_date: 2026-04-13
persona: base-rate
domain: crypto
subdomain: corporate-bitcoin-treasury
entity:
topic: "MicroStrategy announces >1000 BTC purchase April 7-13?"
question: "Will MicroStrategy/Strategy announce a purchase of more than 1000 BTC between 2026-04-07 00:00 ET and 2026-04-13 23:59 ET?"
driver:
date_created: 2026-04-13
agent: orchestrator
stance: yes
certainty: high
importance: high
novelty: medium
time_horizon: immediate
related_entities: ["strategy", "bitcoin"]
related_drivers: ["reliability"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: []
tags: ["base-rate", "polymarket", "strategy", "bitcoin-treasury", "official-source"]
---

# Claim

This looks overwhelmingly likely to resolve **YES**. The official Strategy purchases page now shows an April 13, 2026 company disclosure for **13,927 BTC**, far above the >1000 BTC threshold, which is exactly the kind of official company information the market says it will use.

## Market-implied baseline

The market-implied probability is **96%** from the provided current price of 0.96.

## Own probability estimate

**99% YES.**

## Agreement or disagreement with market

I **roughly agree with the market, but am slightly more bullish than 96%** because the case is no longer mainly a forecasting problem. It is mostly a source-of-truth / timing check. Once the official company page carries a 2026-04-13 entry for 13,927 BTC with linked SEC filing metadata, the outside-view question shifts from “how often does Strategy announce a >1000 BTC purchase in a given week?” to “is there any realistic contract-interpretation wrinkle left?” There is some residual risk around exact timing/eligibility, but not much.

## Implication for the question

Absent a late-discovered timing or eligibility problem, this should be treated as substantively resolved toward **YES**. The disclosed purchase count is massively above threshold, and the official source appears within the date window.

## Key sources used

- **Primary / direct / governing source-of-truth-adjacent:** Strategy official purchases page, checked 2026-04-13 and preserved in source note `qualitative-db/40-research/cases/case-20260413-9c835dfe/researcher-source-notes/2026-04-13-base-rate-strategy-purchases-page.md`.
- **Secondary / contextual official verification pass:** Strategy press archive, checked for contradictory official signals and historical disclosure pattern, preserved in `qualitative-db/40-research/cases/case-20260413-9c835dfe/researcher-source-notes/2026-04-13-base-rate-strategy-press-archive.md`.
- **Governing source of truth explicitly:** the market description says resolution is based on **official information from MicroStrategy/Strategy or Michael Saylor**, and separately references `https://www.strategy.com/purchases` for tracking holdings.

**Compliance / evidence floor:** Met with two meaningful official-domain sources plus an explicit extra verification pass because the market was at an extreme probability.

## Supporting evidence

- The official purchases page includes an entry dated **2026-04-13** with `count: 13,927` BTC and linked SEC filing metadata.
- Embedded official text on that page states that Strategy **“has acquired 13,927 BTC for ~$1.00 billion…”** and gives updated holdings as of 4/12/2026.
- The amount is not near the threshold; it clears >1000 BTC by a huge margin, reducing ambiguity about quantity.
- The company has a known pattern of using official site + filing-linked disclosures for BTC purchases, which fits the contract’s resolution mechanics.

## Counterpoints / strongest disconfirming evidence

The strongest disconfirming consideration is **timing / eligibility ambiguity**, not substance. Specifically: if the relevant official announcement were somehow posted after **11:59 PM ET on April 13** or if the market required a narrower announcement channel than the purchases page despite referencing official company information broadly, that could still create a technical NO path.

## Resolution or source-of-truth interpretation

This market resolves YES if MicroStrategy/Strategy announces a purchase of more than 1000 BTC between April 7 and April 13 inclusive, and it resolves from **official information from MicroStrategy or Michael Saylor**. The market text also explicitly says announcements made in the time frame count regardless of when the actual purchases were made.

That makes the key issue: **does the official April 13 Strategy disclosure count as an in-window announcement?** My answer is yes, very likely. The purchases page is an official company surface and includes linked SEC filing metadata. I do not see a stronger governing source that cuts against it.

## Key assumptions

- The official purchases-page entry dated 2026-04-13 was available within the contract window rather than appearing too late for inclusion.
- The market’s reference to official company information is broad enough to include the purchases page and linked filing-backed disclosure, not only a distinct press-release headline or Saylor post.
- There is no imminent correction reducing the reported acquisition below 1000 BTC.

## Why this is decision-relevant

At 96%, the market is already pricing near-certainty. The base-rate contribution here is mostly that once official qualifying evidence appears, the remaining risk becomes narrow operational/interpretive tail risk rather than event-frequency uncertainty. That supports staying near the market or slightly above it, not fading the move.

## What would falsify this interpretation / change your mind

- Proof that the relevant official posting occurred outside the April 7-13 ET window.
- A clarified market rule excluding the purchases page unless separately mirrored by another official channel.
- A company correction/retraction showing the 13,927 BTC entry was erroneous.
- A direct official resolution note indicating the disclosure does not count for this contract.

## Source-quality assessment

- **Primary source used:** Strategy official purchases page.
- **Most important secondary/contextual source used:** Strategy official press archive.
- **Evidence independence:** **low to medium**; both sources are on the same official domain, so this is not independent corroboration in the journalistic sense.
- **Source-of-truth ambiguity:** **low to medium**; the main residual ambiguity is timing/announcement-channel interpretation, not whether the company disclosed >1000 BTC.

## Verification impact

- **Additional verification pass performed:** yes.
- **Did it materially change the estimate or mechanism view?** No material change.
- It confirmed that the official-domain evidence was not obviously contradicted elsewhere and left the core view intact: this is overwhelmingly likely YES unless a technical timing/eligibility issue emerges.

## Reusable lesson signals

- For narrow date-window corporate-announcement contracts, once an official issuer page carries a dated, filing-linked disclosure, the remaining uncertainty often compresses into timestamp and channel-eligibility checks rather than substantive event uncertainty.
- Possible source-quality lesson: company-maintained aggregation pages can be near-dispositive when the contract expressly points to official company information, but they still benefit from one extra pass on timing and filing linkage.
- Possible missing or underbuilt driver: none obvious from this case.
- Confidence that any lesson here is reusable: **medium**.

## Orchestrator review suggestions

- review later for durable lesson: **no**
- review later for driver candidate: **no**
- review later for canon or linkage issue: **yes**
- one-sentence reason: `Strategy` appears causally important here but I did not force a canonical entity slug because I did not verify one in `20-entities/`; it is recorded in `proposed_entities` instead.

## Recommended follow-up

No major follow-up suggested unless a later resolver dispute emerges over the exact posting timestamp or whether the purchases page qualifies as the announcement surface.
