---
type: agent_finding
case_key: case-20260413-07f0191d
dispatch_id: dispatch-case-20260413-07f0191d-20260413T201947Z
research_run_id: 68c87da3-0cf0-4813-8848-9ec81e8daa2b
analysis_date: 2026-04-13
persona: catalyst-hunter
domain: politics
subdomain: bulgarian-parliamentary-election
entity:
topic: "GERB-SDS exact second-place risk"
question: "Will GERB-UDF (GERB-SDS) finish second in the 2026 Bulgarian parliamentary election?"
driver: elections
date_created: 2026-04-13
agent: Orchestrator
stance: lean-no-vs-market
certainty: medium-low
importance: high
novelty: medium
time_horizon: "through election day and result reporting"
related_entities: []
related_drivers: ["elections", "polling"]
proposed_entities: ["GERB-SDS", "Revival", "PP-DB", "DPS", "Central Election Commission of Bulgaria"]
proposed_drivers: []
upstream_inputs: []
downstream_uses: []
tags: ["bulgaria", "election", "exact-rank", "catalyst-hunter", "verification-pass"]
---

# Claim

GERB–SDS looks like a plausible **top-two** finisher, but the available evidence in this run does **not** justify treating “GERB–SDS finishes exactly second” as a ~96% event. My directional view is **below market**: GERB–SDS finishing second is still more likely than not, but not close to locked.

Evidence-floor compliance: this run used (1) the market contract and resolution wording supplied in assignment context, (2) a contextual election-overview source note, (3) an independent contextual polling-aggregation source note, and (4) an additional verification pass on election-date text and canonical-mapping / driver checks. Source access was partially constrained, so confidence is reduced and that limitation is made explicit rather than hidden.

## Market-implied baseline

The market price is **0.96**, implying roughly **96%** probability that GERB–SDS finishes second.

## Own probability estimate

My estimate is **62%**.

## Agreement or disagreement with market

I **disagree** with the market.

Why: the contract is about **exact rank**, not broad competitiveness. Accessible evidence supports GERB–SDS as a major Bulgarian electoral force and plausible top-two finisher, but I did not find commensurately strong evidence that it is already near-certain to finish **second specifically** rather than first. A party/coalition that may still be live for first place should not usually trade like an almost-settled second-place outcome without much stronger late polling or authoritative reporting than I could verify here.

## Implication for the question

The most important implication is that this market should be analyzed as an **ordering problem among top blocs**, not as a “will GERB–SDS do well?” question. If GERB–SDS remains competitive for first, then the main risk to a YES position is precisely that it wins more seats than the market’s assumed leader and therefore resolves NO.

## Key sources used

Primary governing source of truth:
- Market contract text in assignment context: resolution is by seat count in the next Bulgarian National Assembly election, with ambiguity resolved by the **Central Election Commission of Bulgaria (CIK)**.

Key contextual sources:
- Source note: `qualitative-db/40-research/cases/case-20260413-07f0191d/researcher-source-notes/2026-04-13-catalyst-hunter-wikipedia-election-overview.md`
  - secondary / contextual
  - used for election date, caretaker-election timeline, and current parliamentary baseline
- Source note: `qualitative-db/40-research/cases/case-20260413-07f0191d/researcher-source-notes/2026-04-13-catalyst-hunter-politico-poll-of-polls.md`
  - secondary / contextual / compromised-access
  - used only as a weak independent check that GERB-linked coalition remains among the leading parties, not as decisive rank evidence
- Driver files: `qualitative-db/30-drivers/elections.md` and `qualitative-db/30-drivers/polling.md`
  - internal contextual guidance on election and polling failure modes

Direct vs contextual distinction:
- Direct evidence for settlement logic came from the market wording supplied in assignment context.
- External sources in this run were mostly contextual rather than direct settlement evidence.

## Supporting evidence

- The contract’s governing logic is clear: rank parties/coalitions by **seats won**, not vibes or coalition desirability. That makes first-vs-second ordering the core issue.
- Accessible election overview material still places GERB–SDS as the current largest parliamentary bloc, which is consistent with it remaining live for first place rather than being cleanly slotted into second.
- The limited independent polling context I could access did not show persuasive evidence that GERB–SDS had already been durably displaced into second.
- In fragmented parliamentary systems, exact second-place markets are more fragile than broad “top two” intuitions suggest.

## Counterpoints / strongest disconfirming evidence

The strongest disconfirming consideration is simple: GERB–SDS **could** be the most natural runner-up if another bloc has genuinely become the clear favorite for first in late polling or in election-night reporting that I could not fully access during this run. If high-quality late Bulgarian polling already shows GERB–SDS consistently second, then my 62% estimate is too low.

I did **not** find a stronger credible disconfirming source than that during this run; the main disconfirming risk is omitted late-cycle evidence, not a directly contradictory high-quality source I was able to verify.

## Resolution or source-of-truth interpretation

What counts:
- The market resolves on the party or coalition winning the **second-greatest number of seats** in the 2026 Bulgarian parliamentary election.
- If tied on seats, ties are broken by **valid votes**, then alphabetical order of listed party abbreviations if still tied.
- If ambiguity remains, resolution falls back to **official Bulgarian government reporting, specifically CIK**.

What does not count:
- Narrative strength, coalition potential after the election, or pre-election expectations do not matter unless they translate into the official ranking by seats.
- A broad claim like “GERB–SDS will perform strongly” is not enough; the contract is about **exactly second**, not merely top-two or first.

Date / timing / reporting-window check:
- Assignment context says the election is scheduled for **19 April 2026**.
- Additional verification on the accessible election-overview source also matched **19 April 2026**.
- The market closes/resolves on **2026-04-18 20:00 ET**, which is before local election-day counting concludes, so repricing risk before final settlement is highly sensitive to the final pre-election information set and then to election-night consensus reporting.

Primary resolution source and fallback logic:
- Primary practical source before official finality: consensus of credible reporting.
- Fallback / ultimate governing source: **CIK official results**.

## Key assumptions

- GERB–SDS remains live for first place rather than being already locked into second.
- No hidden contract nuance changes normal seat-ranking interpretation.
- Late credible reporting will broadly align with eventual official CIK seat ranking.

## Why this is decision-relevant

Because the market is priced at an extreme **96%**, even modest uncertainty about first-vs-second ordering matters a lot. The key catalyst is not generic campaign noise; it is the next piece of information that sharply resolves whether GERB–SDS is the **leader** or the **runner-up**.

Most important catalysts from here:
- late, methodologically credible polling convergence showing another bloc clearly ahead of GERB–SDS
- election-night exit polls or near-final tabulations that establish the first-place bloc
- credible Bulgarian media consensus before full official finalization

Most likely repricing path before resolution:
- If late polling/reporting shows GERB–SDS still in first-place contention, this market should soften from extreme YES.
- If late polling/reporting shows a rival clearly first and GERB–SDS clearly next, the market’s current pricing becomes more defensible.

Highest-information catalyst:
- **Election-night consensus reporting anchored to seat estimates**, because this is an exact-rank seat market and not a generic popularity market.

## What would falsify this interpretation / change your mind

I would move materially higher toward the market if I saw:
- at least two independent, late, methodologically credible polls showing another bloc clearly first and GERB–SDS clearly second
- or a strong election-night consensus from credible reporting that puts GERB–SDS unambiguously second by seat projection
- or direct CIK/official reporting that effectively settles the ordering

## Source-quality assessment

- Primary source used: the market contract / assignment resolution wording, with explicit CIK fallback.
- Most important secondary/contextual source used: the election-overview source note based on the 2026 Bulgarian parliamentary election page.
- Evidence independence: **medium-low**. I have one useful contextual election source and one weaker independent contextual polling aggregator, but broader independent confirmation was constrained by source-access failures.
- Source-of-truth ambiguity: **low for final settlement**, because CIK is explicit; **medium for pre-settlement market interpretation**, because consensus reporting may move prices before official finality.

## Verification impact

Additional verification pass performed: **yes**.

What I checked in the additional pass:
- explicit date confirmation for **19 April 2026**
- explicit review of contract wording and what counts / does not count
- canonical-mapping check in local entity/driver files
- additional source attempts for CIK and broader news / polling access

Did it materially change the view?
- **No major directional change**, but it increased confidence that the main issue is exact-rank overprecision rather than a missed contract nuance. It also lowered confidence somewhat because source-access constraints prevented a stronger independent polling read.

## Reusable lesson signals

- Possible durable lesson: exact-rank election markets can look deceptively easy when the party is obviously strong, but “strong” and “exactly second” are very different claims.
- Possible missing or underbuilt driver: none clearly beyond existing `elections` and `polling` drivers.
- Possible source-quality lesson: for high-probability political rank markets, compromised access to current local polling should be treated as a confidence reducer, not papered over with narrative certainty.
- Confidence that any lesson here is reusable: **medium**.

## Orchestrator review suggestions

- review later for durable lesson: **yes**
- review later for driver candidate: **no**
- review later for canon or linkage issue: **yes**
- one-sentence reason: Bulgarian party / institution entities that matter here do not appear to have clean canonical entity pages in the current vault, so this case had to use `proposed_entities` instead of strong linkage.

## Recommended follow-up

- Before synthesis, add one stronger late-cycle polling or election-reporting source if accessible.
- On election night, prioritize seat-based consensus reporting and then CIK updates rather than broad headline framing.
- Treat any claim that GERB–SDS is “obviously second” as requiring direct rank evidence, not just general competitiveness.