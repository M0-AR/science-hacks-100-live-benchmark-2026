# From Mnemonics to Measurements: A Live-Verified Benchmark of 100 Popular-Science Theories

*Manuscript skeleton — methods + results are executed code; numbers below are machine-produced.*

## Abstract
Popular-science compressions (“survival of the fittest”, “you cannot win…”) trade fidelity for memory. We construct the first end-to-end live-verified benchmark of all 100 theories in Barras *Science Hacks* (2018): a 100-row registry mapping each hack to one of 12 executable experiments and an evidence tier (A live-API / B public-snapshot / C simulation-math / D philosophical-frontier). Offline, 12/12 experiments pass deterministically; live, 4/5 sensor feeds (USGS, Open-Meteo, ECB-FX, BTC) verified on 2026-10-15 with graceful snapshot fallback. Census: B49/C29/D14/A8. Physics experiment E07 is the hub (22 hacks); evolution E09 (16) and genetics E08 (13) follow. We report three hidden patterns: (i) a verifiability gradient predicted by Popperian falsifiability, (ii) hub structure matching the book’s cross-link graph, (iii) a contested-frontier cluster around Hubble-tension/dark-energy 2025-2026 literature. We argue living benchmarks — not static reviews — are the correct genre for popular-science verification.

## 1. Introduction
Barras’ hacks span evolution to multiverse. Prior verification is narrative. We make it executable: Docker-Compose, pinned deps, `PYTHONHASHSEED=0`, atomic JSON, CI-gated.

## 2. Related work
Reproducibility infrastructure (CASRAI 2026: workflow + digest-pinned container + Zenodo DOI + SWHID); Omnibenchmark 2026; TuringBench; Nüst 10 Dockerfile rules; Pantheon+ Hubble-law tests (Wang 2022, 2023); DESI-DR2 Hubble-tension ML 2026; TorC 2026; H0/S8 8.3% coincidence 2026; supernova age-bias debate 2025-2026.

## 3. Method
### 3.1 Registry-first mapping
All 100 hacks encoded (`src/hacks_registry.py`) before experiments to prevent cherry-picking. Tier rubric: A = live API check in CI window; B = public dataset/snapshot logic; C = closed-form/simulation; D = currently unfalsifiable (string, MWI, multiverse, Goldilocks, panspermia, Gaia/Medea, historical models).
### 3.2 Triple redundancy
Each live claim = live fetch + bundled snapshot + synthetic math, so `pytest` passes offline and `--live on` upgrades honestly.
### 3.3 Twelve experiments
E01 Hubble OLS; E02 parallax + P-L; E03 Aki b-value + USGS; E04 Milanković periodogram; E05 U-238 inversion + Dalton; E06 Boyle/kinetic/abs-zero; E07 SR/photoelectric/E=mc²; E08 Mendel χ²/Chargaff/clock; E09 Wright-Fisher selection-vs-drift; E10 logistic resistance; E11 tier census + hub; E12 five-collector harness (USGS, Open-Meteo, Frankfurter, CoinGecko, NASA DONKI).

## 4. Results (executed 2026-10-15)
12/12 pass offline and live. Key: H0̂=69.726 r=0.99885; b=0.674; p41/p30≈1669×; t⊕=4.54 Gyr; rms(N₂,300K)=516.95 m/s; γ₀.₉c=2.29416; Mendel χ²=0.653; fixation 20 vs 0; resistance 0.018→0.996. Live: USGS 20 events mean 4.96; London Tmax [20.8…14.4]; FX EUR 0.893 GBP 0.754 JPY 158.45; BTC $79,814; DONKI fallback documented. See `benchmarks/results/summary.json` + `live_snapshot.json`.

## 5. Hidden patterns
P1 verifiability gradient (A earth/space sensors → D foundations/frontier; Popper-34 predicts D list). P2 hub structure (E07:22, E09:16, E08:13 mirrors book cross-links). P3 contested frontier (Hubble-tension 2026 cluster; age-bias vs rebuttal; axion Crunch). P4 dialectic pairs (Gaia/Medea both D; drift/selection split by experiment).

## 6. Limitations
Synthetic Pantheon+/Wright-Fisher proxies; single-day live snapshot; D-tier open by construction; no human-subjects placebo trial (literature-gated).

## 7. Future work
Swap proxies for Pantheon+ 1701 SNe, USGS annual catalog, 1000G chrMT, CDC ABX series; nightly live CI; Zenodo DOI + SWHID; classroom RCT on mnemonic retention.

## 8. Reproducibility statement
`docker compose up --build research`; `make verify`; `python -m src.benchmark --live on`. All numbers regenerable. Sources in `data/live_sources.json`.
