PYTHON = .venv/bin/python
PIP = .venv/bin/pip
PYTEST = .venv/bin/pytest
RUFF = .venv/bin/ruff
FLET = .venv/bin/flet

.PHONY: all test lint build-web hooks run-server run-server-web install clean

all: test

lint:
	$(RUFF) check src/ tests/

test: lint
	$(PYTEST) --cov=src \
		--cov-report=term-missing --cov-report=html \
		--cov-fail-under=80 --cov-config=.coveragerc

hooks:
	$(PIP) install pre-commit
	.venv/bin/pre-commit install

build-web:
	$(FLET) build web src/ --module-name main

run-server:
	$(PYTHON) -m flet run src/main.py

run-server-web:
	$(PYTHON) -m flet run src/main.py --web

install:
	$(PIP) install -r requirements.txt
	$(PIP) install pytest pytest-cov

clean:
	rm -rf .pytest_cache .coverage htmlcov build
