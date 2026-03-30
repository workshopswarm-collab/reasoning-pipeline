import sys
import requests
import json
from datetime import datetime, timedelta, timezone

# --- Configuration & API ---
GAMMA_API_BASE = "https://gamma-api.polymarket.com"
OUTPUT_FILE = "filtered_markets.json"

# --- Filtering Criteria ---
MIN_VOLUME = 20000.0
MAX_VOLUME = 15000000.0
MIN_LIQUIDITY = 5000.0
MIN_YES_PROBABILITY = 0.70
MAX_YES_PROBABILITY = 0.96  

def fetch_and_filter_all_markets():
    filtered_markets = []
    total_markets_scanned = 0
    
    # --- NEW TIME CONSTRAINTS ---
    # Set time constraints (Between 1 day and 10 days from now)
    now_utc = datetime.now(timezone.utc)
    one_day_from_now = now_utc + timedelta(days=1)
    ten_days_from_now = now_utc + timedelta(days=10)
    # ----------------------------
    
    limit = 100
    offset = 0
    
    print("[INFO] Initiating global sweep of Polymarket events...")

    while True:
        params = {
            "active": "true",
            "closed": "false",
            "limit": limit,
            "offset": offset
        }

        try:
            response = requests.get(f"{GAMMA_API_BASE}/events", params=params, timeout=90)
            response.raise_for_status()
            events = response.json() 
            
            if not events:
                break
            
            for event in events:
                # 1. End Date Filter
                event_end_date_str = event.get("endDate")
                if not event_end_date_str:
                    continue  
                
                try:
                    clean_date_str = event_end_date_str.replace("Z", "+00:00")
                    event_end_date = datetime.fromisoformat(clean_date_str)
                    
                    # --- NEW LOGIC: Must be > 24 hours away AND < 10 days away ---
                    if not (one_day_from_now <= event_end_date <= ten_days_from_now):
                        continue
                    # -----------------------------------------------------------
                        
                except ValueError:
                    continue  

                markets = event.get("markets", [])
                event_slug = event.get("slug", "")
                
                for market in markets:
                    total_markets_scanned += 1
                    
                    # 2. Volume Filter
                    volume = float(market.get("volume", 0.0))
                    if not (MIN_VOLUME <= volume <= MAX_VOLUME):
                        continue

                    # 3. Liquidity Filter
                    liquidity = float(market.get("liquidity", 0.0))
                    if liquidity < MIN_LIQUIDITY:
                        continue
                    
                    # 4. Odds Filter
                    outcome_prices_raw = market.get("outcomePrices", "[]")
                    outcomes_raw = market.get("outcomes", "[]")
                    
                    try:
                        prices = json.loads(outcome_prices_raw) if isinstance(outcome_prices_raw, str) else outcome_prices_raw
                        outcomes = json.loads(outcomes_raw) if isinstance(outcomes_raw, str) else outcomes_raw
                    except json.JSONDecodeError:
                        continue
                    
                    try:
                        yes_index = [str(out).lower() for out in outcomes].index("yes")
                        yes_price = float(prices[yes_index])
                    except (ValueError, IndexError, AttributeError):
                        continue

                    # Final Check: Bounded between target probabilities
                    if MIN_YES_PROBABILITY <= yes_price <= MAX_YES_PROBABILITY:
                        market_slug = market.get("slug", "")
                        url = f"https://polymarket.com/event/{event_slug}" if event_slug else f"https://polymarket.com/market/{market_slug}"
                        
                        # --- NESTED POSTGRES SCHEMA PAYLOAD ---
                        filtered_markets.append({
                            "platform": "polymarket",
                            "external_market_id": market.get("conditionId", market.get("id", "N/A")),
                            "slug": market_slug,
                            "title": market.get("question", "No question"),
                            "description": event.get("description", ""),
                            "category": "polymarket-discovery",
                            "status": "open",
                            "outcome_type": "binary",
                            "closes_at": event_end_date.strftime("%Y-%m-%dT%H:%M:%SZ"),
                            "resolves_at": event_end_date.strftime("%Y-%m-%dT%H:%M:%SZ"),
                            "metadata": {
                                "source": "intake-filter.py",
                                "contract_type": "binary",
                                "event_title": event.get("title", "No title"),
                                "url": url
                            },
                            "snapshot": {
                                "observed_at": now_utc.strftime("%Y-%m-%dT%H:%M:%SZ"),
                                "last_price": yes_price,
                                "yes_price": yes_price,
                                "no_price": round(1.0 - yes_price, 4),
                                "volume": volume,
                                "open_interest": liquidity,
                                "raw_payload": {
                                    "event_slug": event_slug
                                }
                            }
                        })
                        
        except requests.exceptions.RequestException as e:
            print(f"[ERROR] Failed to fetch events at offset {offset}: {e}")
            break

        print(f"       -> Scanned offset {offset}... Found {len(filtered_markets)} passing markets so far.")
        offset += limit

    total_passed = len(filtered_markets)
    print("-" * 50)
    print(f"[DEBUG] FILTERING FUNNEL RESULTS:")
    print(f"  -> Total nested markets scanned: {total_markets_scanned}")
    print(f"  -> Markets passed to JSON:       {total_passed}")
    print("-" * 50)

    if not filtered_markets:
        print("[CRITICAL ERROR] No markets matched the current criteria. Halting pipeline.")
        sys.exit(1)

    output_json = json.dumps(filtered_markets, indent=4)
    
    try:
        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            f.write(output_json)
        print(f"[SUCCESS] Saved output to {OUTPUT_FILE}")
    except IOError as e:
        print(f"[ERROR] Could not write to file: {e}")

    return output_json

if __name__ == "__main__":
    fetch_and_filter_all_markets()