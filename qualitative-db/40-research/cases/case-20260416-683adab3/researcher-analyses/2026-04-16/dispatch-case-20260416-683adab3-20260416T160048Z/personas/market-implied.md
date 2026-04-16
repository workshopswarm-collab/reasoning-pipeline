---
type: agent_finding
case_key: case-20260416-683adab3
dispatch_id: dispatch-case-20260416-683adab3-20260416T160048Z
research_run_id: 7df07f2b-9dd6-42b5-aebc-688a89026d91
analysis_date: 2026-04-16
persona: market-implied
domain: culture
subdomain: film-box-office-and-ranking-surfaces
entity: the-numbers
topic: will-lee-cronin-s-the-mummy-opening-weekend-box-office-be-between-10m-and-15m
question: "Will \"Lee Cronin's The Mummy\" Opening Weekend Box Office be between 10m and 15m?"
driver:
date_created: 2026-04-16
agent: Orchestrator
stance: "modestly market-aligned, slightly under market confidence"
certainty: medium
importance: high
novelty: medium
time_horizon: "opening weekend"
related_entities: ["box-office-mojo", "the-numbers"]
related_drivers: []
proposed_entities: ["warner-bros", "lee-cronins-the-mummy"]
proposed_drivers: ["theater-count-scale", "horror-opening-demand"]
upstream_inputs: []
downstream_uses: []
tags: ["agent-finding", "market-implied", "box-office", "settlement-mechanics"]
---

# Claim

The market’s yes price is directionally defensible, but a bit too confident. I think the most reasonable current read is that **Lee Cronin’s The Mummy is somewhat more likely than not to land in the 10m–15m opening-weekend bracket, but not at the 70% level**.

## Market-implied baseline

Current price is **0.70**, implying roughly **70%** probability that the finalized The Numbers 3-day opening weekend figure lands between **$10m and $15m**.

## Own probability estimate

**62%**.

## Agreement or disagreement with market

**Roughly agree on direction, mildly disagree on confidence.**

The strongest case for the market being efficient is straightforward: the contract’s governing source is The Numbers, and the best directly inspected public evidence from The Numbers supports a meaningful wide opening. The title page confirms an **April 17, 2026 domestic wide release by Warner Bros.**, and The Numbers’ April 9 theater-count context says the film is **projected to launch in 3,200 theaters**. On that footprint, a 10m–15m opening only requires a plausible middle-of-the-road per-theater average for an R-rated horror film.

Where I stop short of the market is evidence concentration. I did not retrieve a clean public pre-release gross forecast number, and usable independent corroboration was weak in this run. For a bracket market already priced at 70%, I would prefer stronger direct tracking evidence that the title is centered specifically in the 10m–15m range rather than merely opening wide enough to make that range plausible.

## Implication for the question

My read is **yes-leaning but not high-conviction**. The market does not look stale or obviously wrong; it looks like it is probably pricing a sensible wide-release prior. But it may be slightly **overextended** because the available public evidence I could directly verify supports plausibility more than tight bracket concentration.

## Key sources used

1. **Primary / authoritative settlement source:** The Numbers title page for the film (`https://www.the-numbers.com/movie/Lee-Cronins-The-Mummy-(2026)`) and the contract language specifying that final Weekend Box Office Performance figures on The Numbers for the **3-day weekend April 17–19** govern resolution.
2. **Key contextual source:** The Numbers homepage/news and release-schedule surfaces inspected on April 16, especially the April 9 item stating the film is projected to launch in **3,200 theaters** and the release-schedule listing the title as a **Wide** release on **April 17**.
3. **Secondary cross-check attempt:** Box Office Mojo title/weekend pages were reached but not extractable into a useful content read during this run, so they did not materially change the estimate.
4. **Internal provenance artifacts:**
   - `qualitative-db/40-research/cases/case-20260416-683adab3/researcher-source-notes/2026-04-16-market-implied-the-numbers-release-and-context.md`
   - `qualitative-db/40-research/cases/case-20260416-683adab3/researcher-analyses/2026-04-16/dispatch-case-20260416-683adab3-20260416T160048Z/assumptions/market-implied.md`
   - `qualitative-db/40-research/cases/case-20260416-683adab3/researcher-analyses/2026-04-16/dispatch-case-20260416-683adab3-20260416T160048Z/evidence/market-implied.md`

**Evidence-floor compliance:** met with at least **two meaningful sources/surfaces**: (1) The Numbers title page plus contract settlement language for direct mechanics, and (2) The Numbers release-schedule/news context for launch-scale evidence. Independence is limited because both are within the The Numbers ecosystem, which lowers confidence but does not invalidate the read.

## Supporting evidence

- The market’s governing source of truth is explicit and inspectable: **The Numbers**.
- The title page confirms the movie exists at the exact The Numbers title surface the market expects to use.
- The title page lists **Domestic Releases: April 17th, 2026 (Wide) by Warner Bros.**
- The release-schedule page also lists **Lee Cronin’s The Mummy** as a **Wide** release on **April 17**.
- The Numbers’ April 9 theater-count context says the movie is projected to open in **3,200 theaters**.
- A 10m–15m opening on 3,200 theaters implies roughly **$3.1k–$4.7k per theater**, which is plausible for a decently distributed horror opener and is a credible embedded assumption behind the current price.

## Counterpoints / strongest disconfirming evidence

The strongest disconfirming consideration is **not a contradictory source but missing specificity**: I did not obtain a clean direct public tracking estimate centered on 10m–15m, and bracket contracts are fragile because a movie can miss by being either **too weak (<10m)** or **too strong (>15m)**. That means a 70% yes price requires more concentration around the middle band than the verified evidence alone proves.

## Resolution or source-of-truth interpretation

This section matters a lot here.

- The market resolves from the **The Numbers** movie page’s **Weekend Box Office Performance** figures once the values for the **3-day opening weekend (April 17–April 19)** are **final**, not studio estimates.
- The market text says this 3-day figure **typically includes Thursday previews**.
- If there is ambiguity about whether The Numbers figures are final, the market remains open until **both The Numbers and Box Office Mojo** confirm finalized figures.
- If the reported value falls exactly on a bracket boundary, the market resolves to the **higher range bracket**.

So the material conditions for a **yes** resolution are:
1. The relevant movie page on The Numbers must post a **final** 3-day opening-weekend figure for **April 17–19, 2026**.
2. That final figure must be **at least $10,000,000 and less than $15,000,000**, except that an exact boundary would resolve to the **higher** bracket per market rules.
3. The settlement should use The Numbers’ Weekend Box Office Performance figure regardless of whether “domestic” in practice reflects USA-only or USA+Canada framing.

## Key assumptions

- The projected **3,200-theater** footprint is close to the realized opening footprint.
- The movie’s demand profile is closer to a normal mid-tier horror opener than either a breakout or a collapse.
- The market may already be incorporating private or harder-to-retrieve trade chatter that supports a mid-band opening.
- No late-breaking release-date, theater-count, or reporting anomaly materially changes the settlement window.

## Why this is decision-relevant

For synthesis, this persona’s main job is to test whether the market deserves deference. My answer is **mostly yes on direction, no on full confidence**. The price appears to embed a coherent release-scale story, so a strongly contrarian under call would need better evidence than I found. But the current public proof set still looks a bit thin for a 70% bracket price.

## What would falsify this interpretation / change your mind

I would move meaningfully if any of the following appeared:

- a direct trade forecast clearly clustering the opening **below 10m** or **above 15m**;
- a confirmed opening theater count materially below the projected **3,200**;
- preview/opening-day data pointing to a full weekend outside the band;
- a settlement mechanics clarification showing a different reporting window than the assumed finalized **April 17–19** 3-day figure.

## Source-quality assessment

- **Primary source used:** The Numbers title page and market contract language tying settlement to The Numbers Weekend Box Office Performance.
- **Most important secondary/contextual source used:** The Numbers release-schedule/homepage news context indicating a projected **3,200-theater** launch.
- **Evidence independence:** **low-to-medium**. The two strongest usable sources come from the same provider ecosystem.
- **Source-of-truth ambiguity:** **low-to-medium**. The governing source is explicit, but “final” status may require cross-confirmation with Box Office Mojo if ambiguity remains.

## Verification impact

- **Additional verification pass performed:** yes.
- I did an explicit mechanics/date/window audit and a separate pass on The Numbers release-schedule/news surfaces, plus a Box Office Mojo cross-check attempt.
- **Material change to view:** modest. The extra pass increased confidence that the market’s logic is sensible because the 3,200-theater context makes the bracket more believable, but it did **not** justify moving all the way up to the market’s 70% confidence.

## Reusable lesson signals

- Possible durable lesson: for bracketed opening-weekend box-office markets, **settlement mechanics and launch footprint can matter more than generic title narrative**.
- Possible missing or underbuilt driver: **theater-count-scale** / launch-width as a reusable driver for box-office bracket cases.
- Possible source-quality lesson: when the named settlement source also supplies the best contextual data, confidence should still be discounted for **source-independence weakness**.
- Confidence that any lesson here is reusable: **medium**.

## Orchestrator review suggestions

- review later for durable lesson: **yes**
- review later for driver candidate: **yes**
- review later for canon or linkage issue: **yes**
- one-sentence reason: recurring box-office cases would benefit from a cleaner canonical driver for **launch width / theater-count scale**, and likely canonical entities for **Warner Bros.** and **Box Office Mojo** if they are not already present.

## Recommended follow-up

If more time or better source access is available before lock, the highest-value next check is **direct pre-release tracking or preview data** from a usable independent trade source. Short of that, this should be carried forward as **market-respecting but slightly under market confidence**: market-implied **70%**, own estimate **62%**, strongest disconfirming consideration = lack of direct bracket-centered tracking evidence.