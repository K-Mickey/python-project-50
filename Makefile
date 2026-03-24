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

check: test lint