---
type: agent_finding
case_key: case-20260407-b34d8893
dispatch_id: dispatch-case-20260407-b34d8893-20260407T004114Z
research_run_id: 436ed12f-ab89-44dd-bef0-a07429be0fd3
analysis_date: 2026-04-07
persona: market-implied
domain: crypto
subdomain: corporate-bitcoin-treasury
entity:
topic: will-microstrategy-announce-a-bitcoin-purchase-march-31-april-6
question: "Will Microstrategy announce a Bitcoin purchase March 31-April 6?"
driver:
date_created: 2026-04-07
agent: market-implied
stance: yes
certainty: high
importance: medium
novelty: low
time_horizon: immediate
related_entities: []
related_drivers: ["sentiment"]
proposed_entities: ["strategy"]
proposed_drivers: []
upstream_inputs: []
downstream_uses: []
tags: ["market-implied", "official-source", "direct-company-announcement", "website-verification"]
---

# Claim

The market's high Yes price was justified and still slightly conservative by the time of review: Strategy had already posted an official April 6 Bitcoin purchase announcement on its official purchases page, with a linked Form 8-K, which appears to satisfy the market's source-of-truth and timing requirements.

## Market-implied baseline

Current market-implied probability from assignment context: **94.85%**.

The strongest case for market efficiency is straightforward here: traders were likely pricing the routine Strategy weekly-Bitcoin-announcement pattern plus the expectation that official confirmation would land on the usual Monday cadence. In this case, the market was not merely anticipating an announcement; the official company surface appears to have already validated that expectation.

## Own probability estimate

**99% Yes**.

## Agreement or disagreement with market

**Roughly agree, with a slight lean that the market was still underpricing Yes once the official company page was checked.**

Why:
- The governing source of truth is unusually clean: official information from MicroStrategy/Strategy or Michael Saylor.
- Strategy's official `purchases` page contains an April 2026 acquisition entry and links a `form-8-k_04-06-2026.pdf` filing.
- The entry states Strategy acquired **4,871 BTC** and that as of **4/5/2026** it held **766,970 BTC**.
- That is a direct company announcement inside the title window March 31-April 6.

The market looks efficient rather than overextended. If anything, a sub-95% price lagged the strength of the direct source once the official page was verified.

## Implication for the question

This should be interpreted as a **Yes** barring a technical timing/retraction issue. The market was effectively pricing the right answer.

## Key sources used

- **Primary / direct / governing source-of-truth surface:** Strategy official purchases page: `https://www.strategy.com/purchases`.
  - See source note: `qualitative-db/40-research/cases/case-20260407-b34d8893/researcher-source-notes/2026-04-07-market-implied-strategy-purchases-and-8k.md`
- **Primary / direct verification artifact:** linked official Form 8-K PDF referenced on the purchases page (`form-8-k_04-06-2026.pdf`).
- **Secondary / contextual source:** Polymarket market page and assignment-provided contract details for current price and rule framing.

Evidence-floor compliance: **met via one authoritative official company source plus one contextual verification pass**. That is sufficient for this low-difficulty, low-resolution-risk, source-bounded market.

## Supporting evidence

- Official company webpage shows an **April 2026** purchase entry.
- Entry includes **date_of_purchase: 2026-04-06** and linked **Form 8-K**.
- Entry text states Strategy acquired **4,871 BTC for ~$329.9 million at ~$67,718 per bitcoin**.
- Market rules say Yes if the company **announces** it acquired additional Bitcoin during the window, regardless of when the purchases were actually made.
- Market rules specify official information from MicroStrategy/Strategy or Michael Saylor; this source fits that exactly.

## Counterpoints / strongest disconfirming evidence

The strongest disconfirming consideration is **technical timing ambiguity**: if the official post were somehow published after the eligible ET cutoff or later deemed outside-window despite the April 6 company entry, the near-certain Yes view would be too high.

I did not find substantive evidence against Yes; only this residual mechanical caveat remained.

## Resolution or source-of-truth interpretation

**Governing source of truth:** official information from MicroStrategy/Strategy or Michael Saylor.

Case-specific checks:
- **Direct company announcement:** satisfied. The Strategy purchases page is an official company announcement surface and explicitly reports the additional BTC acquisition.
- **Official website verification:** satisfied. I directly verified the official `https://www.strategy.com/purchases` page and confirmed the April 2026 acquisition entry plus linked 8-K artifact.

Important contract nuance:
- The market resolves on **announcement timing**, not necessarily trade-execution timing.
- The rules say announcements made within the window count **regardless of when the actual purchases were made**.
- That makes the official announcement surface more important than reconstructing exact execution dates from other sources.

## Key assumptions

- The Strategy purchases page counts as official company information for resolution purposes.
- The relevant April 6 posting occurred within the market's eligible time window.
- No official correction/retraction will invalidate the entry.

## Why this is decision-relevant

This is a clean example of a market probably being right for the obvious reason: it was anchored to a narrow, authoritative source-of-truth process. There is little edge in fading a source-bounded market once the official surface prints the event.

## What would falsify this interpretation / change your mind

- Evidence that the official posting timestamp fell outside the allowed ET window.
- A retraction/correction from Strategy.
- A clarifying resolution interpretation that excludes the purchases page / linked filing combination.

## Source-quality assessment

- **Primary source used:** Strategy official purchases page, with linked Form 8-K.
- **Most important secondary/contextual source used:** Polymarket event page / assignment-provided rule summary.
- **Evidence independence:** medium. The decisive evidence is mostly one official source chain, but that is acceptable because this is a source-bounded official-announcement market.
- **Source-of-truth ambiguity:** low. Rules explicitly point to official information from the company or Michael Saylor, and the market description itself references the purchases page.

## Verification impact

- **Additional verification pass performed:** yes.
- **Did it materially change the view?** yes, slightly.
- Before direct verification, a market-respecting view would have been high-Yes because of cadence and market prior; after direct official website verification, the estimate moved to near-certain Yes.

## Reusable lesson signals

- Possible durable lesson: in narrow official-announcement markets, once the explicitly authorized company surface is checked, extra search often has sharply diminishing value.
- Possible missing or underbuilt driver: none confidently identified from this simple case.
- Possible source-quality lesson: when the market description names a specific official webpage, check that page early before doing broader search.
- Confidence reusable: **medium**.

## Orchestrator review suggestions

- review later for durable lesson: **no**
- review later for driver candidate: **no**
- review later for canon or linkage issue: **no**
- one-sentence reason: this case is simple and mostly confirms an existing best practice about checking named official resolution surfaces first.

## Recommended follow-up

No substantive follow-up suggested unless a resolver later disputes timestamp eligibility; if that occurs, inspect the linked 8-K filing timestamp directly.

## Canonical-mapping check

- Explicit check performed: **yes**.
- Clean canonical entity slug for Strategy/MicroStrategy in `qualitative-db/20-entities/`: **not confirmed during this run**, so I used `proposed_entities: [strategy]` rather than forcing a weak canonical fit.
- Clean canonical driver slug for the main causal lens: **`sentiment`** was confirmed as an existing driver, but this case did not require a heavy driver structure.

## Provenance / trust note

This run is trustworthy because it relied on the named official website in the market description, preserved a source note for that official surface, explicitly audited the source-of-truth logic, and recorded the small remaining technical caveat instead of pretending absolute certainty.
