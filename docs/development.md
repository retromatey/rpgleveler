# Development

This page describes the development workflow for the **rpgleveler** project.

The project uses a modern Python development toolchain including:

- pytest for testing
- ruff for linting and formatting
- mypy for static type checking
- coverage for test coverage
- MkDocs for documentation
- GitHub Actions for continuous integration

---

## Development Installation

Clone the repository and install the development dependencies.

```bash
git clone https://github.com/retromatey/rpgleveler.git
cd rpgleveler
pip install -e .[dev]
```

This installs the project in **editable mode**, allowing local code changes
to immediately affect the installed package.

---

## Project Layout

The repository uses the **src layout**.

```
rpgleveler
├── src
│   └── rpgleveler
│       ├── data
│       │   ├── attack_bonus.py
│       │   ├── saving_throws.py
│       │   ├── spell_slots.py
│       │   ├── thief_skills.py
│       │   ├── turn_undead.py
│       │   └── xp_tables.py
│       ├── engine
│       │   ├── advancement.py
│       │   ├── hit_points.py
│       │   ├── leveler.py
│       │   └── progression.py
│       └── shared
│           ├── character.py
│           ├── level_up_result.py
│           └── literals.py
├── tests
├── docs
├── mkdocs.yml
└── pyproject.toml
```

Key directories:

| Directory        | Purpose              |
|------------------|----------------------|
| `src/rpgleveler` | Library source code  |
| `tests`          | Unit tests           |
| `docs`           | MkDocs documentation |
| `dist`           | Build artifacts      |

---

## Running Tests

Tests are written using **pytest**.

```bash
pytest
```

To run tests with coverage:

```bash
pytest --cov=rpgleveler --cov-report=term-missing
```

---

## Linting

The project uses **ruff** for linting.

```bash
ruff check .
```

Ruff can automatically fix many issues:

```bash
ruff check . --fix
```

---

## Type Checking

Static type checking is performed with **mypy**.

```bash
mypy src
```

Type hints are used throughout the project to improve reliability and
developer tooling support.

---

## Building the Package

The project uses the standard Python build backend.

To build the package locally:

```bash
python -m build
```

This produces wheel and source distribution files inside the `dist/` directory.

---

## Documentation

Documentation is built using **MkDocs** with the Material theme.

Start a local documentation server:

```bash
mkdocs serve
```

The site will be available at:

```
http://127.0.0.1:8000
```

The server automatically reloads when documentation files change.

---

## Documentation Features

The documentation site includes:

- API documentation generated automatically from docstrings
- CLI examples and usage guides
- syntax-highlighted code blocks
- cross-links between API symbols

API documentation is generated using **mkdocstrings**.

---

## Continuous Integration

GitHub Actions automatically runs the following checks:

- unit tests
- linting
- type checking
- coverage reporting

CI runs on every push and pull request.

---

## Releases

Releases are created by tagging a version in Git.

Example:

```bash
git tag v0.1.0
git push origin v0.1.0
```

The GitHub Actions release workflow will:

1. Build the project
2. Upload the wheel file to the GitHub release page
3. Attach release artifacts
