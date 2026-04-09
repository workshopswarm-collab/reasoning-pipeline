---
type: agent_finding
case_key: case-20260407-b34d8893
dispatch_id: dispatch-case-20260407-b34d8893-20260407T004114Z
research_run_id: af88a607-24c2-47ed-b220-0de4e60959b0
analysis_date: 2026-04-07
persona: base-rate
domain: crypto
subdomain: institutions
entity: strategy
topic: will-microstrategy-announce-a-bitcoin-purchase-march-31-april-6
question: "Will Microstrategy announce a Bitcoin purchase March 31-April 6?"
driver:
date_created: 2026-04-07
agent: base-rate
stance: no
certainty: medium-high
importance: medium
novelty: low
time_horizon: "resolves 2026-04-07"
related_entities: ["strategy", "bitcoin"]
related_drivers: []
proposed_entities: ["michael-saylor"]
proposed_drivers: ["company-bitcoin-purchase-announcement-timing"]
upstream_inputs: []
downstream_uses: []
tags: ["polymarket", "strategy", "bitcoin", "official-source-check", "low-difficulty"]
---

# Claim

My base-rate view is **No**: Strategy is more likely than not to **not** announce an additional Bitcoin purchase during March 31-April 6, 2026. I estimate **about 80% No / 20% Yes**.

Evidence-floor compliance: low-difficulty case; I verified the explicitly referenced official company website surface and did an additional verification pass because the market was priced at an extreme. That satisfies the case evidence floor.

## Market-implied baseline

Current market price is **0.9485**, implying about **94.85% Yes**.

## Own probability estimate

**20% Yes / 80% No.**

## Agreement or disagreement with market

I **disagree** with the market.

The market is pricing near-certainty that Strategy will announce another purchase in this exact one-week window. My outside-view anchor is lower because:
- this is a narrow, date-bounded announcement market, not a broad "will eventually buy more BTC" market;
- Strategy purchase announcements are frequent enough to matter, but not so clockwork that any given specific week should be treated as ~95% certain absent direct contemporaneous evidence;
- the official company purchase-history surface I checked still pointed to the prior March 23 update covering holdings as of 3/22/2026, with no later official purchase announcement visible for the target window.

A disciplined base-rate view should require stronger direct evidence than "they often buy" before moving into the mid-90s for a one-week timing question.

## Implication for the question

Absent a qualifying official announcement from Strategy or Michael Saylor dated within March 31-April 6 ET, this should resolve **No**. The market looks overconfident in recurring cadence and underweights the possibility of a skipped week or delayed announcement.

## Key sources used

- **Primary / direct / authoritative settlement source:** Strategy official bitcoin purchases page: https://www.strategy.com/purchases
- **Primary / direct contextual official source:** Strategy official history page: https://www.strategy.com/history
- **Case-level provenance note:** `qualitative-db/40-research/cases/case-20260407-b34d8893/researcher-source-notes/2026-04-07-base-rate-strategy-purchases-official.md`
- **Canonical entity context:** `qualitative-db/20-entities/companies/strategy.md`

Governing source of truth: per market rules, **official information from MicroStrategy/Strategy or Michael Saylor**. The contract also specifically references `https://www.strategy.com/purchases` for holdings tracking.

## Supporting evidence

- The official Strategy purchase page is the most relevant company-controlled source and, during this run, the latest located purchase entry was the March 23, 2026 update covering holdings **as of 3/22/2026**.
- I did **not** find a later official purchase announcement on the checked official Strategy web surfaces covering the market window March 31-April 6.
- For a narrow one-week market, lack of direct official confirmation late in the window is materially bearish relative to a 94.85% Yes market.
- Base-rate framing: even for an entity with a strong accumulation pattern, exact-week announcement timing is noisy enough that 95% requires very fresh case-specific evidence, not just history.

## Counterpoints / strongest disconfirming evidence

Strongest disconfirming consideration: Strategy has an established pattern of recurring Bitcoin purchase announcements, and the market may be inferring a weekly cadence from recent behavior. If there is a very recent Michael Saylor or Strategy post not surfaced cleanly by my retrieval, that could quickly move the answer to Yes.

## Resolution or source-of-truth interpretation

Resolution mechanics are straightforward but timing-sensitive:
- The market resolves **Yes** if Strategy/MicroStrategy announces that it acquired additional Bitcoin **between 12:00 AM ET March 31 and 11:59 PM ET April 6**.
- It resolves from **official information from MicroStrategy or Michael Saylor**.
- The announcement timing matters more than the execution timing; purchases made earlier but announced in-window would still count.

Case-specific checks:
- **Direct company announcement:** checked. I verified the official Strategy purchase-history website surface for a qualifying company announcement.
- **Official website verification:** checked. I verified `strategy.com/purchases` directly and also checked `strategy.com/history` as a second official surface.

## Key assumptions

- If a qualifying official announcement had already been made by the end of the market window, it would likely appear on one of the checked official Strategy surfaces or on another obvious official surface discoverable via those pages.
- Recent cadence alone is not enough to justify a >90% estimate for this exact weekly window.

## Why this is decision-relevant

This case is mostly about not overpaying for recurrence. The decision-relevant issue is whether the market is confusing a strong general tendency to keep buying BTC with near-certainty of a qualifying announcement in this exact weekly slice.

## What would falsify this interpretation / change your mind

What would most change my mind:
- a qualifying official Strategy press release, purchase-page update, SEC-linked filing, or Michael Saylor post dated within March 31-April 6 ET;
- a clean official holdings update showing additional BTC acquired and announced within the market window.

Without that, I remain below market.

## Source-quality assessment

- **Primary source used:** Strategy official bitcoin purchases page.
- **Most important secondary/contextual source:** Strategy official history page (also official, but more contextual as a backup verification surface).
- **Evidence independence:** **low to medium**; both checked sources are company-controlled surfaces, which is acceptable here because the market explicitly resolves from company/Saylor official information.
- **Source-of-truth ambiguity:** **low**; the market clearly defines official Strategy/Michael Saylor information as the governing source.

## Verification impact

- **Additional verification pass performed:** yes.
- Because market-implied probability was >85%, I checked an additional official Strategy surface beyond the main purchases page.
- **Material change from extra verification:** no major change; it modestly increased confidence in the bearish view by failing to reveal a later official in-window announcement.

## Reusable lesson signals

- Possible durable lesson: extreme pricing in narrow timing markets should still be tested against direct source-of-truth timing, not just recurring narrative cadence.
- Possible missing or underbuilt driver: weekly corporate announcement cadence for repeat issuers may deserve a reusable driver only if it recurs across many cases.
- Possible source-quality lesson: official app-driven pages can be enough for low-difficulty cases, but preserving a source note helps later auditability when extraction is messy.
- Reusability confidence: **low to medium**.

## Orchestrator review suggestions

- review later for durable lesson: **no**
- review later for driver candidate: **no**
- review later for canon or linkage issue: **yes**
- one-sentence reason: Michael Saylor appears structurally important to settlement for these markets but I did not confirm a clean canonical slug during this run, so I left him in `proposed_entities` rather than forcing linkage.

## Recommended follow-up

No follow-up suggested unless an official Strategy/Saylor announcement surfaces that post-dates this check but remains inside the resolution window.