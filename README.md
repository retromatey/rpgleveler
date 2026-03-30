[![CI](https://github.com/retromatey/rpgleveler/actions/workflows/ci.yml/badge.svg)](https://github.com/retromatey/rpgleveler/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/retromatey/rpgleveler/branch/main/graph/badge.svg)](https://codecov.io/gh/retromatey/rpgleveler)
[![GitHub release](https://img.shields.io/github/v/release/retromatey/rpgleveler)](https://github.com/retromatey/rpgleveler/releases)
![Python](https://img.shields.io/badge/python-3.14+-blue.svg)
![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)

# rpgleveler

A Python library + CLI for leveling up **Basic Fantasy RPG** characters.

---

## What this project does

`rpgleveler` provides a **fully deterministic, rules-driven leveling engine**
for Basic Fantasy RPG.

It handles:

- XP-based level advancement
- Hit point gains (including CON modifiers and racial caps)
- Attack bonus progression
- Saving throws
- Spell slots
- Thief skills
- Turn undead abilities

All game rules are implemented using **immutable data tables** and **pure
functions**, making the system predictable, testable, and easy to extend.

---

## Key Features

- **Pure functional design** — no mutation of input characters
- **Deterministic randomness** via seeded dice rolls
- **Modular architecture** (engine, data, IO, CLI)
- **Immutable rule tables** for safety and correctness
- **Fully tested** with high coverage
- **CLI + library support**

---

## Quick Start

### CLI

```bash
rpgleveler character.json
```

With deterministic rolls:

```bash
rpgleveler character.json --seed 42
```

Write output to a file:

```bash
rpgleveler character.json --out updated_character.json
```

---

## Installation

### Install from release

Install the `.whl` from the latest release:

```bash
pip install https://github.com/retromatey/rpgleveler/releases/download/v0.1.0/rpgleveler-0.1.0-py3-none-any.whl
```

**NOTE:** Replace `v0.1.0` with the latest version from the 
[GitHub releases page](https://github.com/retromatey/rpgleveler/releases).

---

### Development install

```bash
git clone https://github.com/retromatey/rpgleveler.git
cd rpgleveler
pip install -e .[dev]
```

Run checks:

```bash
ruff check .
mypy src
pytest --cov=rpgleveler --cov-report=term-missing
python -m build
```

---

## Usage (Library)

```python
from diceroller.core import DiceRoller
from rpgleveler import level_up, load_character

rng = DiceRoller(seed=42)

character = load_character("character.json")
new_character, result = level_up(character, rng=rng)

print(new_character.to_dict())
```

---

## Project Structure

```
rpgleveler
└── src
    └── rpgleveler
        ├── cli     # Command-line interface
        ├── core    # Data models (Character, LevelUpResult)
        ├── data    # Immutable rule tables
        ├── engine  # Level-up logic
        └── io      # JSON import/export
```

---

## Design Philosophy

### Pure Transformations

Leveling up returns a new object:

```python
new_character, result = level_up(character, rng=rng)
```

---

### Uniform Data Model

All characters always include:

- `spell_slots`
- `thief_skills`
- `turn_undead`

Even if unused — avoids branching logic and keeps everything consistent.

---

### Deterministic Behavior

All randomness is injected:

```python
DiceRoller(seed=42)
```

This enables reproducible results and reliable tests.

---

## License

Copyright Jason Tennant, 2026.

Distributed under the terms of the MIT license.

---

## Credits / Legal

Basic Fantasy RPG is an open tabletop RPG by Chris Gonnerman and distributed
under the terms of the **Creative Commons Attribution-ShareAlike 4.0
International License**.

This project is a fan-made utility and is not affiliated with the original
authors or publishers.
