all: verify

verify:
	python -m pytest tests -q
	python -m src.benchmark --live off --out benchmarks/results/summary.json

live:
	python -m src.fetch_live --out benchmarks/results/live_snapshot.json
	python -m src.benchmark --live on --out benchmarks/results/summary.json

docker:
	docker compose up --build research
