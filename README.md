# Personal Website (Flet)

A multi-page personal portfolio site built with [Flet](https://flet.dev/) (Python UI framework). Runs as a desktop app or in the browser.

## Setup

```bash
python -m venv .venv
make install
```

`make install` installs all dependencies from `requirements.txt` plus `pytest` and `pytest-cov`.

## Running the App

```bash
# Desktop
make run-server

# Web (browser)
make run-server-web
```

## Development

```bash
# Lint (ruff)
make lint

# Run all tests (lint runs first, 80% coverage required)
make test

# Install pre-commit hooks
make hooks
```

Run a single test file or test:

```bash
.venv/bin/pytest tests/test_home_page.py
.venv/bin/pytest tests/test_app.py::test_home_page_renders
```

## Project Structure

```
src/
  main.py          # Entry point — builds tabs, footer, wires routing
  pages/           # One file per page, each exports get_view(page)
  components/      # Reusable UI components (e.g. footer)
  utils/
    routing.py     # Route ↔ tab index mapping
    responsive.py  # get_dims(page) — returns scaled dimensions by window width
  assets/          # Static assets
tests/             # pytest test suite (mirrors src/ structure)
```

## Architecture Notes

- **Entry point:** `src/main.py` calls `build()`, which instantiates tabs and footer. `build()` is also called on `page.on_resized` so the UI redraws responsively.
- **Imports:** All `src/` files use bare imports (`from components.footer import ...`). `flet run` adds `src/` to `sys.path`; `conftest.py` does the same for pytest.
- **Routing:** `update_route` (tab → route) and `route_change` (route → tab) guard against each other to prevent infinite loops.
- **Responsive sizing:** `get_dims(page)` reads `page.window.width` and returns scaled dimension values. Falls back to 800px for non-numeric widths (e.g. in tests).
- **Pages:** Each page is instantiated fresh on every `build()` call, so dimensions are always current.
