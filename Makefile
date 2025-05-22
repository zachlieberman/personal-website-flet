PYTHON = .venv/bin/python
PIP = .venv/bin/pip
PYTEST = .venv/bin/pytest
COVERAGE = .venv/bin/coverage

.PHONY: all test coverage run-server run-server-web install clean

all: test

test:
	$(PYTEST) --cov=src --cov=components --cov=pages --cov=utils --cov-report=term --cov-fail-under=80 --cov-config=.coveragerc

coverage:
	$(COVERAGE) run --source=src,components,pages,utils -m pytest tests/ --cov-config=.coveragerc
	$(COVERAGE) report --fail-under=80
	$(COVERAGE) html

run-server:
	$(PYTHON) -m flet run src/main.py

run-server-web:
	$(PYTHON) -m flet run src/main.py --web

install:
	$(PIP) install -r requirements.txt
	$(PIP) install coverage

clean:
	rm -rf .pytest_cache .coverage htmlcov
