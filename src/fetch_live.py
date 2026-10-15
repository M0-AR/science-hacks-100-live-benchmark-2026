"""Live-data fetchers with graceful offline fallback.

Each fetcher tries a public live API with a short timeout and returns
{"source":..., "live": bool, "data":...}. Nothing here is allowed to raise:
offline CI must still pass using bundled snapshots.
"""
import json
import urllib.request
import urllib.parse

TIMEOUT = 8

def _get_json(url, params=None):
    q = ("?" + urllib.parse.urlencode(params)) if params else ""
    req = urllib.request.Request(url + q, headers={"User-Agent": "science-hacks-benchmark/1.0"})
    with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
        return json.loads(r.read().decode("utf-8", "replace"))

def fetch_usgs_earthquakes(limit=20):
    """Live: USGS earthquake feed (plate tectonics Hacks 39-41)."""
    try:
        j = _get_json("https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_month.geojson")
        feats = j.get("features", [])[:limit]
        mags = [f["properties"]["mag"] for f in feats if f.get("properties", {}).get("mag") is not None]
        return {"source": "USGS", "live": True, "n": len(feats),
                "mean_mag": sum(mags)/len(mags) if mags else None, "max_mag": max(mags) if mags else None}
    except Exception as e:
        # bundled snapshot: realistic fallback so benchmark is deterministic offline
        return {"source": "USGS-snapshot", "live": False, "n": 20, "mean_mag": 4.9, "max_mag": 6.2, "note": str(e)[:120]}

def fetch_open_meteo_forecast(lat=51.5, lon=-0.12):
    """Live: Open-Meteo forecast (Milankovic/climate Hacks 42-44 harness check)."""
    try:
        j = _get_json("https://api.open-meteo.com/v1/forecast",
                      {"latitude": lat, "longitude": lon, "daily": "temperature_2m_max", "timezone": "UTC"})
        temps = j.get("daily", {}).get("temperature_2m_max", [])[:7]
        return {"source": "open-meteo", "live": True, "tmax_7d": temps}
    except Exception as e:
        return {"source": "open-meteo-snapshot", "live": False, "tmax_7d": [14.1, 15.0, 13.8, 14.5, 15.2, 14.9, 14.0], "note": str(e)[:120]}

def fetch_frankfurter_fx():
    """Live: ECB FX via Frankfurter (live-harness proof for 'real market data' requirement)."""
    try:
        j = _get_json("https://api.frankfurter.app/latest", {"from": "USD", "to": "EUR,GBP,JPY"})
        return {"source": "frankfurter-ecb", "live": True, "rates": j.get("rates", {})}
    except Exception as e:
        return {"source": "frankfurter-snapshot", "live": False, "rates": {"EUR": 0.92, "GBP": 0.79, "JPY": 149.5}, "note": str(e)[:120]}

def fetch_coingecko_btc():
    """Live: CoinGecko BTC price (second live-market proof)."""
    try:
        j = _get_json("https://api.coingecko.com/api/v3/simple/price", {"ids": "bitcoin", "vs_currencies": "usd"})
        return {"source": "coingecko", "live": True, "btc_usd": j["bitcoin"]["usd"]}
    except Exception as e:
        return {"source": "coingecko-snapshot", "live": False, "btc_usd": 67000.0, "note": str(e)[:120]}

def fetch_nasa_donki():
    """Live: NASA DONKI space-weather (space Hacks 89-99 harness check, keyless)."""
    try:
        j = _get_json("https://api.nasa.gov/DONKI/FLR", {"startDate": "2026-01-01", "endDate": "2026-02-01", "api_key": "DEMO_KEY"})
        return {"source": "nasa-donki", "live": True, "n_flares": len(j) if isinstance(j, list) else 0}
    except Exception as e:
        return {"source": "nasa-snapshot", "live": False, "n_flares": 12, "note": str(e)[:120]}

def collect_all(out="benchmarks/results/live_snapshot.json"):
    import os
    snap = {
        "usgs": fetch_usgs_earthquakes(),
        "meteo": fetch_open_meteo_forecast(),
        "fx": fetch_frankfurter_fx(),
        "btc": fetch_coingecko_btc(),
        "nasa": fetch_nasa_donki(),
    }
    os.makedirs(os.path.dirname(out) or ".", exist_ok=True)
    with open(out, "w") as f:
        json.dump(snap, f, indent=2)
    print(json.dumps(snap, indent=2))
    return snap

if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="benchmarks/results/live_snapshot.json")
    a = ap.parse_args()
    collect_all(a.out)
