import json, subprocess, sys
def test_benchmark_offline_passes():
    from src.benchmark import run_all
    s = run_all("off")
    assert s["all_pass"], json.dumps(s, indent=2)[:3000]

def test_registry_covers_100():
    from src.hacks_registry import REGISTRY
    assert len(REGISTRY) == 100
    nos = sorted(h.n for h in REGISTRY)
    assert nos == list(range(1, 101))

def test_live_fetchers_never_raise():
    from src import fetch_live as fl
    for fn in [fl.fetch_usgs_earthquakes, fl.fetch_open_meteo_forecast,
               fl.fetch_frankfurter_fx, fl.fetch_coingecko_btc, fl.fetch_nasa_donki]:
        out = fn()
        assert isinstance(out, dict) and "live" in out
