---
type: evidence_map
case_key: case-20260413-639ecb3f
dispatch_id: dispatch-case-20260413-639ecb3f-20260413T225424Z
research_run_id: 1254c21e-a2cb-4b07-86a9-f78680bcbc40
analysis_date: 2026-04-13
persona: base-rate
domain: crypto
subdomain: ethereum
entity: ethereum
topic: eth-2400-weekly-touch-base-rate
question: "Will Ethereum reach $2,400 April 13-19?"
driver:
date_created: 2026-04-13
agent: orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["ethereum"]
related_drivers: []
proposed_entities: []
proposed_drivers: ["short-horizon-price-thresholds"]
upstream_inputs: ["2026-04-13-base-rate-polymarket-and-price-context.md"]
downstream_uses: ["qualitative-db/40-research/cases/case-20260413-639ecb3f/researcher-analyses/2026-04-13/dispatch-case-20260413-639ecb3f-20260413T225424Z/personas/base-rate.md"]
tags: ["evidence-map", "ethereum", "base-rate", "weekly-threshold"]
---

# Summary

Outside-view net: Ethereum reaching 2,400 during April 13-19 looks slightly more likely than not and broadly consistent with the market, because the required move is small relative to ordinary ETH volatility and recent realized range.

## Question being evaluated

Will Ethereum reach $2,400 at any point during April 13-19?

## Current lean

Lean yes, with probability in the high 70s but not at a level that strongly disagrees with market.

## Prior / starting view

Starting outside view: for a high-volatility asset like ETH, a weekly touch threshold only ~2% above spot should usually be quite live, especially if recent realized range already includes that level.

## Evidence supporting the claim

- Polymarket prices the 2,400 threshold around 76%, which is an information-rich crowd prior. Indirect but useful. Medium weight.
- CoinGecko current price puts ETH around 2,348, so the hurdle is only roughly 2.2% away. Direct contextual evidence. High weight.
- CryptoCompare recent history shows ETH recently traded above 2,400 and has daily volatility large enough that a one-touch weekly hit is plausible. Direct contextual evidence. High weight.
- Because the contract asks whether ETH will hit the level during the week, not necessarily close above it, the base rate should be higher than a close-above framing at the same level. Contract-interpretive / structural evidence. Medium weight.

## Evidence against the claim

- ETH was still below 2,400 at assignment time, so the contract still needs an additional upward move and is not already nearly settled. Direct. Medium weight.
- My empirical check is rough and based on limited recent history, so it could overstate the true touch rate. Methodological caution. Medium weight.
- If macro or crypto sentiment turns abruptly negative, a short-dated threshold contract can miss even when the level looks close. Structural downside risk. Medium weight.

## Ambiguous or mixed evidence

- The market page fetch shows laddered outcomes and FAQs but not perfectly clean rule text for the exact governing price source in the extracted snippet.
- The market may already incorporate more exchange-specific or flow-specific information than the outside-view exercise captures.

## Conflict between inputs

There is no hard factual conflict. The main issue is calibration: how much should the market-implied 76% be trusted versus the rough empirical outside view from current distance-to-threshold and recent volatility.

## Key assumptions

- The contract is effectively about whether ETH touches 2,400 during the week.
- Recent ETH behavior is informative enough for a low-difficulty outside-view estimate.
- No major negative regime break occurs before the weekly window ends.

## Key uncertainties

- Exact governing source-of-truth / price feed for final settlement.
- Whether current market structure or macro news makes this week less typical than the recent sample.
- Whether recent volatility is temporarily elevated or depressed relative to a better long-run reference class.

## Disconfirming signals to watch

- Clear rule text showing a more restrictive settlement method than assumed.
- ETH falling materially away from the threshold early in the week.
- Broader crypto weakness breaking the recent realized range pattern.

## What would increase confidence

- Cleaner rule text confirming exact settlement mechanics and source-of-truth.
- Another independent price-history source confirming similar recent touch behavior.
- Continued ETH strength keeping spot within ~1-2% of the threshold.

## Net update logic

The outside view started positive because the hurdle is small. Recent price history reinforced that rather than undermining it. The main reason I do not go materially above market is that the evidence is adequate but not strong enough to prove the true touch rate is much higher than the current 76% price.

## Suggested downstream use

Use as synthesis input that the base-rate persona is mildly bullish on the event occurring, but only slightly above market and with moderate confidence because rule precision and empirical calibration are good enough, not perfect.