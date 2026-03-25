install:
	uv sync

build:
	uv build

package-install:
	uv tool install --force dist/*.whl

lint:
	uv run ruff check gendiff --fix

test:
	uv run pytest

test-coverage:
	uv run pytest --cov=gendiff --cov-report xml

check: test lint

.PHONY: install build package-install lint test test-coverage check