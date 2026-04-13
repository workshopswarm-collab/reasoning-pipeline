---
type: agent_finding
case_key: case-20260413-9c835dfe
dispatch_id: dispatch-case-20260413-9c835dfe-20260413T162509Z
research_run_id: 9121e3c6-f005-4128-93cc-a16e903fc68b
analysis_date: 2026-04-13
persona: variant-view
domain: crypto
subdomain: institutions
entity: strategy
topic: "MicroStrategy/Strategy >1000 BTC announcement April 7-13 2026"
question: "Will MicroStrategy / Strategy announce a purchase of more than 1000 BTC between April 7 and April 13, 2026?"
driver: reliability
date_created: 2026-04-13
agent: variant-view
stance: yes
certainty: high
importance: medium
novelty: low
time_horizon: immediate
related_entities: ["strategy", "bitcoin"]
related_drivers: ["reliability", "capital-markets"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: []
tags: ["polymarket", "strategy", "bitcoin", "official-disclosure", "extra-verification"]
---

# Claim

Strategy already appears to have satisfied this market. The strongest credible variant view is not a bearish thesis on the event itself, but a contract-mechanics caution: the only serious way the market misses is if the apparent April 13 official disclosure somehow does not count as a valid announcement under the named source-of-truth standard. On the evidence checked, that failure mode looks remote.

## Market-implied baseline

The assignment snapshot gives `current_price: 0.96`, so the market-implied probability is about 96% Yes.

## Own probability estimate

99%

## Agreement or disagreement with market

I roughly agree with the market, but I am slightly more confident than 96% because an official Strategy disclosure surface now shows a 2026-04-13 announcement for 13,927 BTC acquired, far above the >1,000 BTC threshold. The main remaining risk is not factual magnitude but settlement mechanics: whether the official page / linked filing / official social text cleanly qualifies as the governing announcement source within the window.

## Implication for the question

This should be interpreted as an effective Yes unless a narrow source-of-truth or timestamp problem emerges. The market's broad direction looks right; the only live edge case is administrative rather than substantive.

## Key sources used

Evidence-floor compliance: met with two meaningful official/near-authoritative sources plus an explicit extra verification pass.

Primary / direct / governing-source evidence:
- Strategy official purchases page: `https://www.strategy.com/purchases`
- Case source note: `qualitative-db/40-research/cases/case-20260413-9c835dfe/researcher-source-notes/2026-04-13-variant-view-strategy-purchases-page.md`

Additional direct verification:
- Same-day linked SEC filing artifact URL from the Strategy purchases page: `https://assets.contentstack.io/v3/assets/bltf8d808d9b8cebd37/blt3d42b5dfaeefd97a/69dc6fdaa22d2281611ded4f/form-8-k_04-13-2026.pdf`
- Embedded plain-text official social/disclosure text on the purchases page entry: `@Strategy has acquired 13,927 BTC for ~$1.00 billion... As of 4/12/2026, we hodl 780,897 BTC...`

Context / contract source:
- Polymarket market description in assignment prompt: resolves on announcements made in the stated window; resolution source is official information from MicroStrategy or Michael Saylor.

## Supporting evidence

- Strategy's official purchases page contains a latest entry dated `2026-04-13` with `count = 13,927 BTC`, clearly above the market threshold.
- That entry links a same-day filing artifact titled `form-8-k_04-13-2026.pdf`, which is consistent with formal public disclosure.
- The same entry includes official plain-text disclosure language stating that `@Strategy has acquired 13,927 BTC...` and gives updated holdings as of 4/12/2026.
- Because the market resolves on announcement timing rather than execution timing, an official April 13 disclosure is the key governing fact.

## Counterpoints / strongest disconfirming evidence

The strongest disconfirming consideration is a narrow contract/source issue: if the linked page entry were posted or materially updated after the market window, or if the market required a different authoritative surface than the company page / linked filing / official company statement, resolution could become messier than the headline suggests. I did not find affirmative evidence of such a problem, but that is the only materially plausible failure mode.

## Resolution or source-of-truth interpretation

The governing source of truth is explicit: official information from MicroStrategy/Strategy or Michael Saylor.

The contract also explicitly says the market resolves based on announcements made within the designated time frame regardless of when the actual purchases were made. So the decisive question is not when Strategy executed the BTC acquisition, but whether an official announcement occurred between 12:00 AM ET April 7 and 11:59 PM ET April 13.

On the evidence reviewed, the official Strategy purchases page and its linked same-day filing/public statement satisfy that standard. This is the main reason I am above the market.

## Canonical-mapping check

Checked assigned canonical surfaces and nearby relevant canon.

Clean canonical mappings used:
- entity: `strategy`
- related_entities: `bitcoin`, `btc`
- related_drivers: `reliability`, `capital-markets`

No important missing canonical slug surfaced that needs `proposed_entities` or `proposed_drivers` for this run.

## Key assumptions

- The official Strategy purchases page is a valid company disclosure surface for this contract.
- The April 13 entry reflects a public announcement made within the market window, not a later retroactive backfill.
- The linked filing/public text is sufficient extra verification of the page entry's legitimacy.

See assumption note: `qualitative-db/40-research/cases/case-20260413-9c835dfe/researcher-analyses/2026-04-13/dispatch-case-20260413-9c835dfe-20260413T162509Z/assumptions/variant-view.md`

## Why this is decision-relevant

At 96%, this market is already pricing near-certain Yes. The useful contribution here is not to fight the direction, but to isolate the residual risk correctly: it is almost entirely a source/timestamp/contract-mechanics risk, not a debate about whether the purchase size exceeded 1,000 BTC.

## What would falsify this interpretation / change your mind

- Evidence that the official Strategy disclosure was not actually public until after 11:59 PM ET on April 13.
- A market clarification saying the company webpage entry does not count and only a different named surface counts.
- Evidence that the April 13 entry was erroneous or later retracted.

Absent one of those, I would stay at a near-certain Yes.

## Source-quality assessment

- Primary source used: Strategy official purchases page, which is directly tied to the entity named in the contract and includes the exact >1,000 BTC disclosure.
- Most important secondary/contextual source: the same-day linked SEC filing artifact / embedded official statement associated with that page entry.
- Evidence independence: medium. The sources are not highly independent because the filing link and social text are bundled through the same company disclosure stack, but they do provide useful cross-confirmation of the same announcement.
- Source-of-truth ambiguity: low. The contract explicitly names official information from MicroStrategy or Michael Saylor, and the checked evidence sits inside that lane.

## Verification impact

- Additional verification pass performed: yes.
- What was checked: the official purchases page entry was inspected beyond the rendered webpage, including its embedded structured data, same-day linked filing URL, and accompanying official plain-text disclosure.
- Did it materially change the view: only modestly. It moved me from "market probably right" to "almost certainly Yes unless there is a timestamp/settlement edge case."

## Reusable lesson signals

- Durable lesson candidate: for Strategy BTC-announcement markets, the official purchases page can be a decisive first-stop source because it exposes both summarized transaction data and filing linkage.
- Missing/underbuilt driver: none.
- Source-quality lesson: extreme-probability event markets can still merit one extra verification pass focused on timestamp and source-of-truth mechanics rather than on searching for more generic commentary.
- Confidence that any lesson here is reusable: medium.

## Orchestrator review suggestions

- Review later for durable lesson: no
- Review later for driver candidate: no
- Review later for canon or linkage issue: no
- One-sentence reason: this case looks straightforward and does not expose a new canonical gap beyond a routine reminder to check official disclosure timing on narrow event contracts.

## Recommended follow-up

No major follow-up suggested beyond, if needed for settlement ops, confirming the public timestamp of the April 13 Strategy disclosure / filing in the official record.