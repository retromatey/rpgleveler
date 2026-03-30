# API Overview

This section documents the core modules of the **rpgleveler** engine.

The API is designed to be **modular, deterministic, and easy to integrate**
into other tools, scripts, or game systems.

---

## Package Structure

The project is organized into a few key areas:

### Core (`rpgleveler.core`)

Fundamental data models and shared types.

- `Character` — Primary character data model
- `LevelUpResult` — Structured result of a level-up operation
- Enums and shared types (e.g., `ClassName`, `Race`)

---

### Engine (`rpgleveler.engine`)

The heart of the leveling system.

- `leveler.py` — Orchestrates the full level-up process
- `advancement.py` — XP thresholds and level eligibility
- `hit_points.py` — Hit point gain logic

This layer contains **no hardcoded tables**, only logic.

---

### IO (`rpgleveler.io`)

Serialization and file handling.

- Load characters from JSON
- Save characters to JSON

---

## Design Philosophy

The API follows a few key principles:

### 1. Pure Transformations

Leveling up does **not mutate** the original character.

```python
new_character, result = level_up(character, rng=rng)
```

---

### 2. Uniform Data Model

All characters always have all fields:

- `spell_slots` → always present (zeros if unused)
- `thief_skills` → always present (zeros if unused)
- `turn_undead` → always present (`None` if unused)

This avoids conditional logic and keeps everything predictable.

---

### 3. Deterministic by Design

All randomness is injected via a `DiceRoller`.

```python
rng = DiceRoller(seed=42)
```

This allows:

- Reproducible results
- Stable tests
- Debuggable behavior

---

## Typical Usage

```python
from diceroller.core import DiceRoller
from rpgleveler.engine.leveler import level_up

rng = DiceRoller(seed=42)

new_character, result = level_up(character, rng=rng)
```

---

## Where to Go Next

- See **Core** modules for data structures
- See **Engine** modules for leveling logic
- See **CLI Reference** for command-line usage
