.PHONY: all install watch verify list progress hint run reset lint fmt test clean
all: watch

install:
	uv sync

watch: install
	uv run pythonlings watch

verify: install
	uv run pythonlings verify

list: install
	uv run pythonlings list

progress: install
	uv run pythonlings progress

hint: install
	uv run pythonlings hint

run: install
	@test -n "$(name)" || (echo "Usage: make run name=<exercise>"; exit 1)
	uv run pythonlings run $(name)

reset: install
	@test -n "$(name)" || (echo "Usage: make reset name=<exercise>"; exit 1)
	uv run pythonlings reset $(name)

lint: install
	uv run ruff check src tests

fmt: install
	uv run ruff format src tests

test: install
	uv run pytest tests

clean:
	rm -f .pythonlings_progress.json
	find . -type d -name __pycache__ | xargs rm -rf
	find . -type d -name .ruff_cache | xargs rm -rf
