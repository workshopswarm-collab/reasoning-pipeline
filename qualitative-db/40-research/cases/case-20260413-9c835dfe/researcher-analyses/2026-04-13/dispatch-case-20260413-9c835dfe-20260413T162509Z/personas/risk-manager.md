---
type: agent_finding
case_key: case-20260413-9c835dfe
dispatch_id: dispatch-case-20260413-9c835dfe-20260413T162509Z
research_run_id: d9988cce-3672-4953-b04c-0077f20b7784
analysis_date: 2026-04-13
persona: risk-manager
domain: crypto
subdomain: corporate-treasury
entity: bitcoin
topic: will-microstrategy-strategy-announce-a-purchase-of-more-than-1000-btc-between-april-7-and-april-13-2026-et
question: "Will MicroStrategy/Strategy announce a purchase of more than 1000 BTC between April 7 and April 13, 2026 ET?"
driver: operational-risk
date_created: 2026-04-13
agent: orchestrator
stance: lean-yes
certainty: medium
importance: high
novelty: low
time_horizon: immediate
related_entities: ["bitcoin"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: ["strategy-company"]
proposed_drivers: []
upstream_inputs: []
downstream_uses: []
tags: ["risk-manager", "polymarket", "strategy", "bitcoin", "timing-risk", "resolution-risk"]
---

# Claim

I lean **Yes**, but with more residual risk than a 96%-100% market price suggests. My working view is that this is probably a routine Strategy/MicroStrategy BTC-announcement case, yet the real tail risk is contract mechanics: the market resolves on an **official announcement** of **more than 1000 BTC** inside the **April 7-13 ET** window, not merely on presumed buying activity or an off-window disclosure.

## Market-implied baseline

The assignment snapshot gives a current price of **0.96**, implying roughly **96%**. The public page extraction during this run rounded the market to effectively **100% Yes**, but I treat the assignment snapshot as the cleaner baseline.

Embedded confidence in that price looks extremely high: the market is acting as though the qualifying announcement is either already known or close enough to certain that timing/wording risk is negligible.

## Own probability estimate

**89% Yes.**

## Agreement or disagreement with market

I **roughly agree directionally** with the market, but I am modestly below it. The gap is mostly about **uncertainty quality**, not a major directional disagreement.

Why I am below market:
- I could verify the official source surfaces and the resolution mechanics.
- I could **not** directly verify, in this run environment, the exact official announcement text or purchases-table content showing the qualifying >1000 BTC event within the stated window.
- In a narrow announcement market, that remaining verification gap matters more than usual.

## Implication for the question

This should still be treated as a **high-probability Yes** case, but not as risk-free. The main way this fails is not a broad change in Strategy's BTC posture; it is a narrower failure mode where no qualifying official announcement is visible in-window, or the wording/source timing does not cleanly satisfy the contract.

## Key sources used

**Evidence-floor / compliance note:** met the stated floor with **two meaningful sources** plus an explicit extra verification pass.

Primary / authoritative-resolution sources:
- Official Strategy BTC purchases page: `https://www.strategy.com/purchases`  
  Source note: `qualitative-db/40-research/cases/case-20260413-9c835dfe/researcher-source-notes/2026-04-13-risk-manager-strategy-purchases-page.md`
- Governing source-of-truth from the contract: official information from **MicroStrategy/Strategy or Michael Saylor**.

Secondary / contextual / contract-mechanics source:
- Polymarket market/rules page: `https://polymarket.com/event/microstrategy-announces-1000-btc-purchase-april-7-13`  
  Source note: `qualitative-db/40-research/cases/case-20260413-9c835dfe/researcher-source-notes/2026-04-13-risk-manager-polymarket-rules-page.md`

Additional verification pass performed:
- Verified live accessibility and corporate-domain mapping of `strategy.com/purchases`.
- Verified `microstrategy.com` redirects into the current Strategy domain, reducing attribution ambiguity around the company rename.

Direct vs contextual evidence:
- **Direct on source-of-truth / settlement mechanics:** Strategy purchases page existence; Polymarket rules text.
- **Indirect on the underlying event in this run:** the available fetches did not expose the full dynamic page body or a visible Saylor post confirming the specific >1000 BTC announcement.

## Supporting evidence

- The market's governing source is narrow and explicit: official information from Strategy/MicroStrategy or Michael Saylor.
- Strategy maintains an official BTC purchases page on its active company domain, and the legacy MicroStrategy domain redirects to Strategy, which reduces source confusion.
- These weekly Strategy BTC-announcement markets often exist against a background of recurring corporate purchase disclosures, so a high Yes prior is not unreasonable.

## Counterpoints / strongest disconfirming evidence

The **strongest disconfirming consideration** is simple: in this run I was **unable to directly verify the exact qualifying official announcement text or dynamic purchases-page content** for the April 7-13 window.

That matters because the contract is narrow:
- it requires an **announcement**, not just a purchase having happened,
- it requires **more than 1000 BTC**,
- and it requires the announcement to land **within the exact April 7-13 ET window**.

If that official in-window post is absent, late, or ambiguously worded, the market can still resolve No despite very high trader confidence.

## Resolution or source-of-truth interpretation

The governing source of truth is explicitly **official information from MicroStrategy/Strategy or Michael Saylor**.

Key contract interpretation points:
- This is an **announcement market**, not a purchase-execution market.
- The market resolves on announcements made **between 12:00 AM ET on April 7 and 11:59 PM ET on April 13**.
- The market description notes the Strategy purchases page as a reference tracking surface.
- Therefore, third-party reporting alone should not be treated as sufficient unless it clearly points back to an official Strategy/Saylor announcement.

## Key assumptions

- The market's extreme confidence is anchored to a real, qualifying official announcement rather than just a routine expectation.
- Any relevant company disclosure will be attributable cleanly to accepted source channels.
- The qualifying amount is indeed **>1000 BTC**, not merely near that threshold or inferred from holdings changes.

## Why this is decision-relevant

When a market is already at 96%+, what matters is not generic support for the thesis but the **small set of ways it can still fail**. Here, those failure modes are mostly operational and wording-based:
- no in-window official post,
- ambiguous announcement language,
- source attribution issues,
- threshold mismatch.

That is exactly where a risk-manager discount belongs.

## What would falsify this interpretation / change your mind

I would revise **down materially toward No** if any of the following happened:
- by end of April 13 ET there is **no traceable official Strategy or Michael Saylor announcement** of a >1000 BTC purchase,
- the only available official disclosure falls **outside** the window,
- the official disclosure references holdings or strategy context but **not** a qualifying >1000 BTC purchase announcement,
- a direct official source shows the amount was **1000 BTC or less**.

I would revise **up toward market certainty** if I saw either:
- the full Strategy purchases page/body content showing the specific dated purchase/announcement, or
- a visible Strategy/Michael Saylor post explicitly announcing a >1000 BTC purchase within the window.

## Source-quality assessment

- **Primary source used:** official Strategy BTC purchases page on `strategy.com`.
- **Key secondary/contextual source used:** Polymarket market/rules page for exact contract mechanics.
- **Evidence independence:** **low to medium**. The best evidence class is company-controlled, and this run's contextual source mainly clarified rules rather than independently proving the event.
- **Source-of-truth ambiguity:** **low** on who counts as authoritative, **medium** on direct event verification in this run because the dynamic official content was not fully visible through available extraction.

## Verification impact

- **Additional verification pass performed:** yes.
- I explicitly checked the official purchases page, the current Strategy domain, and the MicroStrategy→Strategy redirect/corporate mapping.
- **Did it materially change the view?** Not directionally. It increased confidence that the source-of-truth path is clean, but it did **not** eliminate the residual timing/announcement-verification risk because the exact qualifying content was still not directly visible here.

## Reusable lesson signals

- Possible durable lesson: extreme-confidence markets tied to recurring corporate disclosures can still deserve a small discount when the contract is announcement-window specific.
- Possible missing or underbuilt driver: none clear from this run.
- Possible source-quality lesson: dynamic official pages can confirm legitimacy while still failing to expose enough content for full event verification; separate source-legitimacy from event-proof.
- Confidence that any lesson here is reusable: **medium**.

## Orchestrator review suggestions

- Review later for durable lesson: **yes**
- Review later for driver candidate: **no**
- Review later for canon or linkage issue: **yes**
- Reason: there may be value in a reusable note or linkage around **announcement-window resolution risk** for recurring corporate treasury markets, and `strategy-company` may need a clean canonical entity slug instead of forcing weak linkage.

## Recommended follow-up

- If a final pre-resolution check is possible, directly inspect the official Strategy purchases page body or an official Michael Saylor/Strategy post for the exact qualifying announcement text.
- If not, treat this as a high-probability Yes with residual tail risk concentrated in contract wording and timing rather than underlying business behavior.