---
type: agent_finding
case_key: case-20260407-b34d8893
dispatch_id: dispatch-case-20260407-b34d8893-20260407T004114Z
research_run_id: d761046a-6013-46f9-8f13-f0356f28481c
analysis_date: 2026-04-07
persona: risk-manager
domain: crypto
subdomain: institutions
entity: strategy
topic: "strategy bitcoin purchase announcement"
question: "Will Microstrategy announce a Bitcoin purchase March 31-April 6?"
date_created: 2026-04-07
agent: orchestrator
stance: yes
certainty: high
importance: high
novelty: low
time_horizon: immediate
related_entities: ["strategy", "bitcoin"]
related_drivers: []
proposed_entities: []
proposed_drivers: ["official-company-announcement-cadence"]
upstream_inputs: []
downstream_uses: []
tags: ["risk-manager", "official-source", "low-difficulty", "website-verification"]
driver:
---

# Claim

This should resolve **Yes**. The official Strategy purchases page shows an April 6, 2026 purchase announcement entry and links the supporting 8-K, which is exactly the kind of official company information the market says it will use.

## Market-implied baseline

Current price is **0.9485**, implying about **94.85%** yes.

Embedded confidence looks very high: the market is pricing this as close to settled already, not just likely.

## Own probability estimate

**99% yes**.

## Agreement or disagreement with market

I **roughly agree**, but I am slightly more bullish than market because the official source-of-truth surface now appears to directly contain the qualifying announcement. The remaining gap is mostly operational/timestamp risk, not substantive uncertainty about whether Strategy announced an additional Bitcoin purchase.

## Implication for the question

From a risk-manager lens, the main thesis is no longer “Strategy probably follows its usual Monday pattern.” It is “the official company surface already appears to satisfy the resolution condition.” That shifts residual risk from business behavior to edge-case mechanics.

## Key sources used

- **Primary / direct / authoritative:** Strategy official purchases page, which includes a dated April 6, 2026 purchase row and linked `form-8-k_04-06-2026.pdf`: `https://www.strategy.com/purchases`
- **Primary / direct / authoritative corroboration:** linked official Strategy-hosted PDF asset for the April 6, 2026 8-K, surfaced from the purchases page metadata.
- **Secondary / contextual:** Polymarket event page and market description stating that official information from MicroStrategy or Michael Saylor is the resolution source.
- Case source note: `qualitative-db/40-research/cases/case-20260407-b34d8893/researcher-source-notes/2026-04-07-risk-manager-strategy-purchases-page-and-8k.md`

## Supporting evidence

Strongest evidence is the official Strategy purchases-page structured data for the row labeled **April 2026**, which records:
- `date_of_purchase: 2026-04-06`
- `count: 4871`
- `purchase_price: 67718`
- `btc_holdings: 766970`
- linked PDF: `form-8-k_04-06-2026.pdf`
- company-authored text: “@Strategy has acquired 4,871 BTC for ~$329.9 million at ~$67,718 per bitcoin. As of 4/5/2026, we hold 766,970 $BTC...”

That is direct company evidence of an additional Bitcoin purchase announcement within the title window.

## Counterpoints / strongest disconfirming evidence

The strongest disconfirming consideration is **mechanical rather than factual**: a narrow timestamp/resolution-interpretation issue could still matter if the market operator decided the relevant announcement was posted outside the designated window, or if it required a narrower source subtype than the official purchases page plus linked 8-K. I found no evidence of such a problem, but that is the main remaining tail risk.

## Resolution or source-of-truth interpretation

The governing source of truth is explicitly **official information from MicroStrategy or Michael Saylor**.

This case is low-complexity because:
- the source of truth is explicitly defined
- the event is date-bounded
- the market says announcements made within the window count regardless of when purchases were made
- Strategy provides a dedicated official purchases page that tracks these announcements and links the corresponding filing

### Additional case-specific check: direct company announcement

Passed. The official Strategy purchases page directly states the acquisition and amount, and links the supporting 8-K.

### Additional case-specific check: official website verification

Passed. I verified the official website itself, not just secondary reporting. A shallow readability fetch was insufficient, so I inspected the live page payload and confirmed the April 6, 2026 purchase row in the page’s structured data.

### Evidence-floor compliance

**Evidence floor met clearly.** This is a low-difficulty official-source case, and I verified at least one authoritative source-of-truth surface directly. I also performed an additional verification pass because the market was already above 85%, and that extra pass materially improved auditability by exposing the structured-data row and linked 8-K.

### Canonical-mapping check

- Clean canonical entity matches found: `strategy`, `bitcoin`.
- No clean canonical driver match was obvious from `qualitative-db/30-drivers/` for the specific mechanism “official company announcement cadence / disclosure cadence,” so I did **not** force a weak canonical driver fit.
- Proposed driver recorded instead: `official-company-announcement-cadence`.

## Key assumptions

- The official Strategy purchases page plus linked 8-K qualifies as official company information for settlement.
- The April 6 entry reflects a qualifying announcement inside the market window.
- No later correction/retraction changes the official record.

## Why this is decision-relevant

At 94.85%, the market is already near certainty. The risk-manager question is whether that confidence is unjustified due to hidden resolution fragility. My answer is mostly no: the remaining uncertainty is small and procedural, not directional.

## What would falsify this interpretation / change your mind

What would most quickly change my mind:
- evidence that the April 6 page/8-K publication timestamp falls outside the market window
- an official correction removing or revising the April 6 purchase entry
- a market clarification that the verified Strategy source does not count, despite the rules naming official company information broadly

## Source-quality assessment

- **Primary source used:** Strategy official purchases page with linked April 6, 2026 8-K
- **Most important secondary/contextual source used:** Polymarket event/rules page
- **Evidence independence:** low-to-medium, because the key confirming surfaces are both issuer-controlled; acceptable here because issuer-controlled information is the explicit source of truth
- **Source-of-truth ambiguity:** low

## Verification impact

- **Additional verification pass performed:** yes
- **Did it materially change the estimate or mechanism view?** It did not change the direction, but it materially increased confidence and auditability.
- **How it changed the view:** The case moved from “very likely based on expected cadence” to “effectively confirmed by official structured page data and linked filing.”

## Reusable lesson signals

- Possible durable lesson: official dynamic pages may hide decisive evidence in structured payloads that readability extraction misses.
- Possible missing or underbuilt driver: official-company-announcement-cadence / disclosure cadence for recurring issuer events.
- Possible source-quality lesson: for low-difficulty official-source markets, one authoritative source can be enough, but dynamic-site extraction should sometimes be verified at the HTML/JSON layer.
- Confidence that any lesson here is reusable: **medium**.

## Orchestrator review suggestions

- review later for durable lesson: **yes**
- review later for driver candidate: **yes**
- review later for canon or linkage issue: **no**
- one-sentence reason: repeated issuer-announcement markets may benefit from a reusable “official disclosure cadence” driver or workflow note, but this single case does not justify canon edits yet.

## Recommended follow-up

No urgent follow-up suggested beyond optional timestamp confirmation from the linked 8-K if a reviewer wants belt-and-suspenders validation.
