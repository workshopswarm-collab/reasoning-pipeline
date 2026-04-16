---
type: agent_finding
case_key: case-20260415-7b143efd
dispatch_id: dispatch-case-20260415-7b143efd-20260415T132144Z
research_run_id: 20911a87-71cd-48c0-8cdc-124dfa4e259b
analysis_date: 2026-04-15
persona: risk-manager
domain: crypto
subdomain: exchange-resolution
entity: bitcoin
topic: will-the-price-of-bitcoin-be-above-70-000-on-april-20
question: "Will the price of Bitcoin be above $70,000 on April 20?"
driver: operational-risk
date_created: 2026-04-15
agent: Orchestrator
stance: yes-lean
certainty: medium
importance: high
novelty: medium
time_horizon: "2026-04-20 noon ET"
related_entities: ["bitcoin"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: ["timing-risk"]
upstream_inputs: []
downstream_uses: []
tags: ["bitcoin", "binance", "resolution-risk", "timing-risk", "polymarket"]
---

# Claim

The market should still lean **Yes**, but the current 0.88 price looks somewhat too confident for a contract that resolves on one exact Binance 1-minute close at **12:00 ET / 12:00 EDT on April 20, 2026**. My estimate is **0.83** that Binance BTC/USDT closes above 70,000 on that exact minute.

**Compliance / evidence-floor note:** This run exceeded the medium-case floor by using (1) the governing Polymarket rule surface, (2) Binance's official kline documentation, (3) direct Binance live ticker/1m kline data, and (4) an extra contextual verification pass via CoinGecko spot. I also completed the required explicit timing/mechanics audit, canonical-mapping check, source-quality assessment, and additional verification pass because the market-implied probability is extreme (>85%).

## Market-implied baseline

Current market-implied probability is **0.88** from the assignment's `current_price: 0.88`.

That price embeds not just a directional BTC-above-70k view, but fairly high confidence that the current cushion survives until the exact settlement minute.

## Own probability estimate

**0.83**.

## Agreement or disagreement with market

I **roughly agree directionally** with the market (Yes is more likely than No), but I **disagree modestly on confidence**. The market is pricing near-high-confidence success; I think that understates contract fragility.

Main reason for the discount:
- BTC/USDT is currently around **74.27k-74.31k on Binance**, which supports Yes.
- But the contract is not "BTC above 70k that day"; it is the **final close of one specific Binance 1-minute candle at noon ET**.
- That exact-minute structure adds more path and timing risk than a casual directional reading suggests.

## Implication for the question

If the question is strictly whether this contract should resolve Yes, the answer is still probably yes because current Binance prices sit materially above the threshold. But this is better understood as a **high-probability timing trade** than as a near-certain directional BTC call.

## Key sources used

**Authoritative / governing source of truth**
- Polymarket rules page for this market: `https://polymarket.com/event/bitcoin-above-on-april-20`  
  - Direct contract source  
  - Governs settlement conditions: Binance BTC/USDT, 1-minute candle, 12:00 ET, final close, strict `>` 70,000.

**Primary operational verification source**
- Binance official spot API docs for market-data endpoints: `https://developers.binance.com/docs/binance-spot-api-docs/rest-api/market-data-endpoints`  
  - Direct source on how Binance defines and returns kline close prices.

**Primary direct market-state sources**
- Binance ticker endpoint: `https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT`
- Binance 1m klines endpoint: `https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1m&limit=5`

**Secondary / contextual verification source**
- CoinGecko BTC/USD simple price endpoint: `https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd`

**Case source notes**
- `qualitative-db/40-research/cases/case-20260415-7b143efd/researcher-source-notes/2026-04-15-risk-manager-polymarket-rules-binance-resolution.md`
- `qualitative-db/40-research/cases/case-20260415-7b143efd/researcher-source-notes/2026-04-15-risk-manager-binance-klines-and-spot-context.md`

## Supporting evidence

Strongest support for Yes:

1. **Direct Binance prices are already comfortably above the threshold.**  
   On 2026-04-15, direct Binance reads showed BTCUSDT at **74,273.07**, with recent 1-minute closes around **74,275 to 74,301**. That is roughly a **4.27k buffer** above 70,000.

2. **The settlement source and current evidence are aligned.**  
   This is not a case where current support comes from another venue or an index. The same exchange family named in the contract is currently above the threshold.

3. **Extra verification pass did not reveal exchange-vs-broader-market divergence.**  
   CoinGecko spot was also near **74,307**, which suggests Binance is not obviously trading at an outlier premium relative to a broader spot reference right now.

## Counterpoints / strongest disconfirming evidence

The strongest disconfirming consideration is **single-minute timing risk**.

BTC can trade above 70k before and after noon ET on April 20 and still resolve **No** if the exact Binance 1-minute candle closing at 12:00 ET finishes below 70,000.

This matters because:
- a roughly **5.7-6.0%** downside move over five days is not absurd for BTC,
- crypto can gap or wick sharply on short horizons,
- exact-minute settlement creates more fragility than a daily-close or broader-window contract.

## Resolution or source-of-truth interpretation

This section is material.

### Governing source of truth

The governing source of truth is **Binance BTC/USDT**, specifically the **1-minute candle close** for **12:00 ET** on **April 20, 2026**, as stated on the Polymarket market page.

### Material conditions that all must hold for Yes

For Yes to resolve, all of the following must be true:
1. The relevant market is **Binance BTC/USDT**, not another exchange and not another pair.
2. The relevant time is the **12:00 ET / EDT noon minute on April 20, 2026**.
3. The relevant datapoint is the candle's **final Close** price, not high, last trade elsewhere, TWAP, VWAP, or daily close.
4. That final close price must be **strictly greater than 70,000**; exactly 70,000 is not enough.

### Explicit date / deadline / timezone verification

- Assignment close and resolve times are both `2026-04-20T12:00:00-04:00`, which is **EDT** and consistent with the contract's noon ET wording on that date.
- April 20, 2026 falls during U.S. daylight saving time, so noon ET corresponds to **UTC-4**, not UTC-5.
- Binance documentation confirms that 1-minute kline intervals exist and that timezone interpretation can be specified for intervals. The contract still points to Binance's own BTC/USDT candle surface as the settlement reference.

### Residual source-of-truth ambiguity

There is still a **small operational ambiguity** because Polymarket's wording references the Binance trading UI with 1m candles selected, while Binance docs naturally describe API endpoints. I do not think this is large enough to change the directional view, but it is a real audit note.

## Key assumptions

- Current Binance BTCUSDT cushion above 70k is large enough to survive ordinary 5-day volatility.
- No major BTC-specific negative catalyst hits before April 20 noon ET.
- Binance does not experience a venue-specific anomaly that causes its BTCUSDT candle to diverge meaningfully from broader spot around settlement.
- Traders are right that current price level matters more than a narrow timing trap, but they may be slightly underpricing that trap.

## Why this is decision-relevant

This matters because the market is already in extreme-probability territory. At **0.88**, small overlooked contract risks become valuable. The key decision question is not whether BTC is generally strong, but whether the confidence level embedded in the market is too high for a single-minute exchange-settled threshold contract.

## What would falsify this interpretation / change your mind

Most likely evidence that would change my view:
- **Toward the market / more bullish:** BTCUSDT holds comfortably above **72k+** into April 19-20 with low realized volatility and no Binance-specific dislocations.
- **Away from the market / more bearish:** BTCUSDT retraces sharply toward **71k or lower**, volatility spikes, or Binance shows any operational or market-structure irregularity near settlement.
- **Fastest invalidator of current view:** evidence that the assumed implementation of the settlement minute is wrong, or that Binance's relevant candle handling differs from my interpretation.

## Source-quality assessment

- **Primary source used:** Polymarket rules page for the exact contract, plus Binance official kline documentation and direct Binance market-data endpoints.
- **Most important secondary/contextual source:** CoinGecko spot price as an independent contextual check on whether Binance price level is broadly aligned with wider spot.
- **Evidence independence:** **medium**. The decisive evidence is intentionally Binance-centric because the contract settles on Binance; independence is improved slightly by CoinGecko but not transformed.
- **Source-of-truth ambiguity:** **low-to-medium**. The source family is clear (Binance BTC/USDT 1m close), but a minor UI-vs-API implementation ambiguity remains.

## Verification impact

- **Additional verification pass performed:** yes.
- Because the market-implied probability is above 85%, I performed an explicit extra pass using Binance docs, direct Binance ticker/klines, and CoinGecko contextual spot.
- **Did it materially change the view?** No major directional change. It **reinforced Yes** while keeping the main caution on timing mechanics. It modestly increased confidence that the current level is genuinely above the threshold across sources, but did not remove the settlement-minute fragility discount.

## Reusable lesson signals

- **Possible durable lesson:** narrow crypto threshold contracts can look easier than they are when market participants mentally substitute "trades above level" for "exact exchange-specific minute close above level." 
- **Possible missing or underbuilt driver:** `timing-risk` may deserve review as a distinct reusable driver or subdriver for exact-window settlement markets.
- **Possible source-quality lesson:** when settlement is exchange-native, independence should be added via contextual verification rather than replacing the governing venue with broader but non-governing market data.
- **Confidence that lesson is reusable:** medium.

## Orchestrator review suggestions

- **Review later for durable lesson:** yes
- **Review later for driver candidate:** yes
- **Review later for canon or linkage issue:** no
- **Reason:** this case cleanly illustrates a recurring pattern where exact-window settlement mechanics deserve explicit `timing-risk` treatment, but I do not see a current canonical linkage break requiring repair.

## Recommended follow-up

- Recheck Binance BTCUSDT level and realized volatility closer to April 19-20 if this market is still being actively priced.
- If price compresses toward the threshold, escalate the weight on exact-minute mechanics and Binance-specific execution risk.
- If price remains well above 72k into settlement eve, the remaining disagreement versus market likely shrinks.