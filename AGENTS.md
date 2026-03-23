# Repository Guidelines

## Project Structure & Module Organization
This project uses a `src` layout.
- `src/rpgleveler/`: package code.
- `src/rpgleveler/data/`: static rules tables (XP, saves, spell slots, etc.).
- `src/rpgleveler/engine/`: leveling and progression logic.
- `src/rpgleveler/shared/`: shared models and literals.
- `tests/unit/` and `tests/integration/`: automated test suites.
- `docs/`: MkDocs site content; API pages are under `docs/api/`.

Keep new modules in the matching domain folder (`data`, `engine`, or `shared`)
and mirror test paths under `tests/`.

## Build, Test, and Development Commands
Install for development:
```bash
pip install -e .[dev]
```
Run standard checks (matches CI):
```bash
ruff check .
mypy src
pytest
python -m build
```
Pytest defaults exclude integration tests (`-m "not integration"` in
`pytest.ini`). Run integration explicitly with:
```bash
pytest -m integration
```
Serve docs locally:
```bash
mkdocs serve
```

## Coding Style & Naming Conventions
- Python 3.14+; 4-space indentation.
- Ruff enforces lint/import order; max line length is 100.
- Use double quotes (Ruff formatter setting).
- Prefer explicit type hints; mypy runs with strict options
  (`disallow_any_generics`, `warn_return_any`).
- Naming: modules/functions/variables `snake_case`, classes `PascalCase`,
  constants `UPPER_SNAKE_CASE`.

## Testing Guidelines
- Framework: `pytest` with `pytest-cov`.
- Test files: `test_*.py`; test functions: `test_*`.
- Use markers consistently: `@pytest.mark.unit` or `@pytest.mark.integration`.
- Add unit tests for logic changes in `engine/` and table validation tests for
  `data/` updates.

## Commit & Pull Request Guidelines
Commit history favors short, lowercase summaries (for example: `engine prep`,
`unit testing updates`). Keep subjects concise and action-oriented.

For pull requests:
- describe behavior changes and affected modules,
- link related issues,
- include test evidence (commands run / coverage impact),
- update docs when API or CLI behavior changes.

PRs should pass the CI workflow (`ruff`, `mypy`, `pytest`, `build`) before merge.
