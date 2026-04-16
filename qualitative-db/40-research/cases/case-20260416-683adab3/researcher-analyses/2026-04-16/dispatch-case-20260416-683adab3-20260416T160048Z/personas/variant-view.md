---
type: agent_finding
case_key: case-20260416-683adab3
dispatch_id: dispatch-case-20260416-683adab3-20260416T160048Z
research_run_id: 0bf27ace-80d7-41c2-83a1-e68654d514bc
analysis_date: 2026-04-16
persona: variant-view
domain: culture
subdomain: film-box-office-and-ranking-surfaces
entity: the-numbers
topic: lee-cronins-the-mummy-opening-weekend-box-office
question: "Will \"Lee Cronin's The Mummy\" opening weekend domestic box office be between $10m and $15m on The Numbers' final 3-day weekend figure?"
driver:
date_created: 2026-04-16
agent: variant-view
stance: disagree-with-market-confidence
certainty: medium
importance: medium
novelty: medium
time_horizon: opening-weekend
related_entities: ["box-office-mojo", "the-numbers"]
related_drivers: []
proposed_entities: ["warner-bros", "lee-cronins-the-mummy"]
proposed_drivers: ["box-office-range-fragility", "pre-release-tracking-uncertainty"]
upstream_inputs: []
downstream_uses: []
tags: ["agent-finding", "variant-view", "box-office", "settlement-sensitive"]
---

# Claim

The strongest credible variant view is not that the movie is obviously headed outside $10m-$15m, but that the market is **too confident** that this narrow middle bucket will hit. My best estimate for **Yes** is **58%**, below the market-implied **70%**. The variant thesis is that traders may be over-compressing uncertainty around a familiar "modest wide horror opening" narrative even though this contract loses on both modest downside and modest upside misses.

## Market-implied baseline

Current price is **0.70**, so the market-implied probability is **70%** for the $10m-$15m bracket.

## Own probability estimate

**58%** for Yes.

## Agreement or disagreement with market

I **disagree modestly** with the market.

I agree with the market's strongest argument: a wide Warner Bros. horror release tied to recognizable Mummy branding plausibly opens in the low-to-mid teens.

Where I disagree is on confidence. This is a **narrow-range** contract, not a generic "will it open okay?" question. The checked sources confirm the title, release date, distributor, genre, and settlement mechanics, but they do **not** provide strong direct tracking evidence that should compress the opening-weekend distribution tightly enough to justify 70% for one specific bracket. A pre-release low-teens consensus may be directionally reasonable while still being overpriced in range-market form.

## Implication for the question

Interpret the contract as more fragile than the headline narrative suggests. The $10m-$15m band may still be the single most likely bucket, but not by enough margin to deserve a 70% probability absent stronger late-cycle tracking, preview, or Friday evidence.

## Key sources used

Primary / authoritative:
- **Polymarket market text** for settlement mechanics: final **The Numbers** 3-day opening weekend figure for **April 17-19, 2026**, not studio estimates.
- **The Numbers title page** for Lee Cronin's The Mummy (2026): confirms a live title page exists and shows **April 17th, 2026 (Wide) by Warner Bros.**, horror/supernatural horror classification, and production-company context.

Secondary / contextual:
- **Box Office Mojo release page**: confirms the title, distributor **Warner Bros.**, release date **Apr 17, 2026**, MPAA **R**, runtime, and genre.
- **Box Office Mojo April 17, 2026 calendar page**: confirms the film is listed as a **wide** release.

Direct vs contextual evidence:
- Direct for settlement mechanics: Polymarket rule text.
- Direct for release identity/date/distributor/genre metadata: The Numbers and Box Office Mojo release pages.
- Contextual rather than direct for the actual gross outcome: all currently checked sources, because no final opening-weekend figure exists yet.

Evidence-floor compliance:
- Met with **at least two meaningful sources**: one authoritative settlement source set (**Polymarket + The Numbers as governing surface**) plus one independent contextual cross-check (**Box Office Mojo**).
- Extra verification performed on release-date / wide-release / title-identity mechanics.

## Supporting evidence

- The Numbers already has a live title page for the film and shows **April 17th, 2026 (Wide) by Warner Bros.**, which makes a mainstream opening-weekend result in the relevant commercial range plausible.
- The movie is clearly positioned as **Horror / Supernatural Horror** with recognizable Mummy branding and major horror production partners (New Line, Blumhouse, Atomic Monster), supporting the market's intuition that a low-teens opening is believable.
- The contract counts the **3-day weekend** and notes this typically includes **Thursday previews**, which can help front-loaded horror titles reach a middle bracket quickly.

## Counterpoints / strongest disconfirming evidence

The strongest disconfirming consideration against my below-market view is simple: the checked release metadata is exactly what one would expect from a movie that often does land in the low-to-mid teens. A wide R-rated horror title with recognizable branding, Warner Bros. distribution, and major horror producers could very well settle neatly inside $10m-$15m.

## Resolution or source-of-truth interpretation

Governing source of truth: **The Numbers** movie page, specifically the **final 3-day opening weekend (April 17-19, 2026)** value on the Box Office tab.

Material conditions that all must hold for a Yes resolution:
1. The relevant figure must be the **3-day opening weekend** value for **April 17-19, 2026**.
2. The figure used must be the **final** figure, not a studio estimate.
3. The resolution source is **The Numbers**, with **Box Office Mojo** used if there is ambiguity about finality.
4. The final value must be **between $10m and $15m**, with an exact boundary falling to the **higher** bracket per market rules.
5. The contract resolves regardless of whether the underlying site frames domestic as US-only or US+Canada.

Date/timing check:
- Opening weekend window explicitly stated in the market: **April 17-19, 2026**.
- Market closes/resolves around **April 20, 2026** subject to final data workflow.
- If final data is still unavailable by **April 26, 2026 11:59 PM ET**, another credible source may be chosen.

Settlement-mechanics check result:
- This is not a simple point-in-time estimate market.
- It requires final weekend data from a named box-office source and can stay open if finality is ambiguous.

## Key assumptions

- Pre-release uncertainty remains wider than the market price implies.
- No hidden late-cycle tracking evidence exists that would tightly pin the outcome to low teens.
- Range-market fragility matters more here than generic directional plausibility.

## Why this is decision-relevant

If the market is overpricing a narrow middle bucket, then the edge is about **confidence calibration**, not necessarily about calling a dramatic flop or breakout. That matters for portfolio construction because range markets can look safer than they are when participants anchor to a modal estimate and underweight both tails.

## What would falsify this interpretation / change your mind

What could still change my mind:
- credible late tracking or presales evidence clustering tightly in the low teens
- Friday grosses or preview numbers that mechanically imply a 3-day finish around roughly $11m-$14m
- multiple independent trade reports converging on a narrow range with little disagreement

The most important falsifier would be strong direct performance evidence emerging before close that compresses the likely final 3-day gross into the bracket much more tightly than the current evidence does.

## Source-quality assessment

- Primary source used: **The Numbers** as the governing settlement source, plus the Polymarket rule text for exact contract interpretation.
- Most important secondary/contextual source used: **Box Office Mojo** release/calendar pages.
- Evidence independence: **medium**. Box-office surfaces may rely on overlapping industry-reporting ecosystems, but Box Office Mojo is still a useful independent cross-check on release identity/date and finality logic.
- Source-of-truth ambiguity: **medium-low**. The contract explicitly names The Numbers and explains the fallback behavior if finality is ambiguous.

## Verification impact

- Additional verification pass performed: **yes**.
- What was checked: release date, wide-release status, distributor/genre context, and settlement mechanics.
- Did it materially change the view: **no material directional change**. It increased confidence in the contract interpretation and in low-teens plausibility, but it did not justify the market's 70% confidence in a narrow bucket.

## Reusable lesson signals

- Possible durable lesson: narrow range contracts can be materially more fragile than the modal narrative suggests, especially pre-release.
- Possible missing or underbuilt driver: **box-office range fragility / pre-release tracking uncertainty** may deserve a cleaner driver concept later.
- Possible source-quality lesson: release metadata can be easy to verify while actual opening-range precision remains weak.
- Confidence that any lesson here is reusable: **medium**.

## Orchestrator review suggestions

- review later for durable lesson: **yes**
- review later for driver candidate: **yes**
- review later for canon or linkage issue: **yes**
- one-sentence reason: the case highlights a potentially reusable driver around narrow-range market overconfidence, and several causally relevant entities/drivers did not have clean canonical slugs available during this run.

## Recommended follow-up

Watch for Friday actuals, preview reporting, and any trade-tracking update before market close. If direct performance evidence emerges and strongly narrows the range, this variant under-confidence should be revised quickly.
