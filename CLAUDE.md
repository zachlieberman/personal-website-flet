# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository. 

If any suggestions are made by the user about how they want things done, update CLAUDE.md with instructions.

Create and run tests and lint before saving any changes to ensure everything works.

## Commands

```bash
# Run desktop app
make run-server
# or: .venv/bin/python -m flet run src/main.py

# Run web app
make run-server-web

# Lint (ruff) — also runs automatically before tests
make lint

# Run all tests (runs lint first)
make test
# or: .venv/bin/pytest

# Run a single test file
.venv/bin/pytest tests/test_home_page.py

# Run a single test by name
.venv/bin/pytest tests/test_app.py::test_home_page_renders

# Install dependencies
make install
```

## Architecture

The app is a multi-page Flet (Python UI framework) personal portfolio site. `src/main.py` is the entry point — it calls `build()`, which creates tabs and a footer and wires up routing. `build()` is also called on `page.on_resized` so the UI redraws with responsive dimensions.

**Import convention:** All `src/` files use bare imports (`from components.footer import ...`, `from utils.routing import ...`). This works because `flet run` adds `src/` to `sys.path`. `conftest.py` at the project root does the same for pytest.

**Routing:** `src/utils/routing.py` maps routes (`/home`, `/about`, etc.) to tab indices. `update_route` converts tab changes → route changes; `route_change` converts route changes → tab updates. Each guards against the other to prevent infinite loops.

**Responsive sizing:** `src/utils/responsive.py` exposes `get_dims(page)`, which reads `page.window.width` and returns a dict of scaled dimension values. Every page and `get_tabs` calls this at render time. Non-numeric widths (e.g. MagicMock in tests) fall back to 800px.

**Pages:** Each page in `src/pages/` exports a single `get_view(page) -> Container`. Pages are instantiated fresh on each `build()` call (including resizes), so they always reflect current window dimensions.

**Tests:** All tests mock `ft.Page` with `MagicMock`. The shared fixture pattern (`page` fixture returning a `MagicMock`) is defined per-file. `test_app.py` is the main comprehensive test file covering all pages, footer, and routing together.
