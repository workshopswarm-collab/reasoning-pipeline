---
type: agent_finding
case_key: case-20260414-4ed80a0a
dispatch_id: dispatch-case-20260414-4ed80a0a-20260414T174040Z
research_run_id: 23445208-5ef6-4cd8-978c-62c7f846d319
analysis_date: 2026-04-14
persona: base-rate
domain: crypto
subdomain: protocols
entity: ethereum
topic: eth-price-threshold
question: "Will Ethereum reach $2,400 April 13-19?"
date_created: 2026-04-14
agent: orchestrator
stance: yes
certainty: high
importance: medium
novelty: low
time_horizon: days
related_entities: ["ethereum"]
related_drivers: []
proposed_entities: []
proposed_drivers: ["binance-venue-specific-price-threshold-resolution"]
upstream_inputs: []
downstream_uses: []
tags: ["base-rate", "polymarket", "binance", "threshold", "crypto"]
driver:
---

# Claim

This should be treated as a Yes / already-met threshold case. The decisive fact is not a narrative about Ethereum momentum but the contract-specific source of truth: Polymarket says this resolves Yes if any Binance ETH/USDT 1-minute candle High during Apr 13-19 ET reaches at least $2,400, and both Polymarket market metadata and direct Binance data support that condition having been met.

## Market-implied baseline

The assigned current_price was 0.916, implying a 91.6% market probability at assignment time. On verification, Polymarket machine-readable market state showed the contract already closed/resolved with Yes effectively at 1.00.

## Own probability estimate

99.5% Yes.

## Agreement or disagreement with market

I roughly agree with the market's strong Yes lean and, after the additional verification pass, would be even more confident than the 91.6% assignment snapshot. The outside-view/base-rate starting point already leaned Yes because a one-week ETH threshold at $2,400 is only modestly above a contemporaneous ETH price in the low-$2300s. But the real reason to move from high probability to near-certainty is not base-rate alone; it is that the named settlement venue itself reported a high above the threshold and Polymarket's own market metadata showed the contract resolved Yes.

## Implication for the question

For this contract, the practical question is no longer "is ETH generally strong this week?" but "did Binance ETH/USDT print a qualifying 1-minute high in the specified window?" The evidence says yes, so the market should be interpreted as correctly resolved or effectively certain to resolve Yes absent some unlikely rules/data mismatch.

## Key sources used

Evidence-floor compliance: met with two meaningful sources plus an explicit extra verification pass.

Primary / authoritative settlement source:
- `qualitative-db/40-research/cases/case-20260414-4ed80a0a/researcher-source-notes/2026-04-14-base-rate-polymarket-rules-and-state.md`
  - Polymarket CLOB / market metadata for condition `0x9a91f5fa90b334c224cb4e638248acc8907b44fa8ed56361b24573cd20491763`
  - direct for contract wording and current market state
  - governing source of truth named in the rule text: Binance ETH/USDT 1-minute candle High values during Apr 13-19 ET

Key secondary/contextual verification source:
- `qualitative-db/40-research/cases/case-20260414-4ed80a0a/researcher-source-notes/2026-04-14-base-rate-binance-24h-ticker.md`
  - Binance public API `ticker/24hr?symbol=ETHUSDT`
  - direct same-venue exchange data, though not the exact 1-minute candle table
  - showed `highPrice` = 2415.50, above the 2400 threshold

Additional context:
- canonical entity note: `qualitative-db/20-entities/protocols/ethereum.md`

## Supporting evidence

- Polymarket's machine-readable description explicitly states the contract resolves Yes if any Binance ETH/USDT 1-minute candle High in the Apr 13-19 ET window is >= $2,400.
- The same Polymarket market object showed the market already closed/resolved with Yes at effectively 1 and No at 0.
- Binance's public 24-hour ETHUSDT ticker reported `highPrice` 2415.50, which exceeds the threshold by 15.50.
- Outside-view/base-rate support: for a weekly crypto threshold only modestly above current spot, a high hit rate is structurally common enough that a strong Yes prior is reasonable even before direct verification.

## Counterpoints / strongest disconfirming evidence

The strongest disconfirming consideration is audit precision, not direction: my extra verification used Binance's 24-hour summary ticker rather than the exact 1-minute candle history surface named in the rules. A strict postmortem auditor would still prefer the precise qualifying minute and timestamp. If there were some data-window mismatch, that would be the most plausible path to error.

## Resolution or source-of-truth interpretation

The governing source of truth is explicit: Binance ETH/USDT, specifically the 1-minute candle "High" values on Binance, for the period from 12:00 AM ET on Apr 13 through 11:59 PM ET on Apr 19. Other exchanges, other pairs, and generic spot references do not count.

Canonical-mapping check:
- Clean canonical entity slug found: `ethereum`.
- No clean existing canonical driver slug was provided for this case.
- The materially important mechanism here is venue-specific threshold resolution on Binance; I am recording that in `proposed_drivers` as `binance-venue-specific-price-threshold-resolution` rather than forcing a weak canonical fit.

## Key assumptions

- Polymarket's API-visible rule text accurately matches the actual resolving contract.
- Binance's reported 24-hour high above 2400 corresponds to at least one qualifying minute candle inside the stated Apr 13-19 ET window.
- No settlement correction/reversal is forthcoming.

## Why this is decision-relevant

This case is a good example of why rule-sensitive crypto threshold markets should be resolved from venue-specific mechanics, not from broad market narrative. If a trader were still discounting the Yes side materially below certainty after the named venue printed a high above threshold, that would usually be a rules-processing error rather than a superior market view.

## What would falsify this interpretation / change your mind

I would materially change my view only if one of the following appeared:
- a Binance 1-minute candle audit showed no qualifying >=2400 High inside the contract window
- Polymarket corrected the rule/source text or reversed settlement status
- evidence emerged that the 24-hour Binance high fell outside the qualifying ET window despite the current interpretation

## Source-quality assessment

- Primary source used: Polymarket CLOB / market metadata for the exact contract; high quality for contract wording and current state.
- Most important secondary/contextual source: Binance ETHUSDT 24-hour ticker API; high quality direct exchange data from the named venue.
- Evidence independence: medium. The sources are not fully independent because the contract itself names Binance, but they are operationally distinct enough for a useful verification pass.
- Source-of-truth ambiguity: low after checking machine-readable rules. It looked ambiguous from the rendered webpage, but the API description made the governing rule explicit.

## Verification impact

Yes, an additional verification pass was performed because the market was at an extreme probability and the rendered webpage was noisy. That extra pass materially improved confidence in the source-of-truth interpretation, but it did not change the directional view; it moved the case from "strong Yes" to "near-certain / already satisfied."

## Reusable lesson signals

- Possible durable lesson: in crypto hit-price markets, venue-specific rule text often matters more than broad price summaries.
- Possible missing or underbuilt driver: venue-specific threshold-resolution mechanics for exchange-defined hit-price contracts.
- Possible source-quality lesson: rendered market pages can be noisy or misleading; machine-readable market metadata is often the better rules surface.
- Confidence reusable: medium.

## Orchestrator review suggestions

- review later for durable lesson: yes
- review later for driver candidate: yes
- review later for canon or linkage issue: no
- reason: this run suggests a reusable driver/lesson around exchange-specific threshold resolution, but not a clear canonical entity/linkage defect.

## Recommended follow-up

No immediate follow-up suggested for this low-difficulty case beyond optional archival capture of the exact qualifying Binance 1-minute candle timestamp if later retrospective auditability is desired.