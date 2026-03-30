# Character Leveling

This page explains how the `rpgleveler` engine processes a character leveling up.

---

## Overview

Leveling up is implemented as a **pure transformation**:

- The original character is **not modified**
- A **new Character object** is returned
- A **LevelUpResult** summarizes what changed

This makes the system:

- Easy to test
- Predictable
- Safe to use in pipelines or simulations

---

## Level-Up Flow

When a character is leveled up, the engine performs the following steps:

1. **Validate eligibility**
2. **Determine next level**
3. **Roll hit point gain**
4. **Retrieve progression data**
5. **Build updated character**
6. **Return result summary**

---

## Step-by-Step Breakdown

### 1. Validation

The engine checks:

- The character is below max level (20)
- The character has enough XP for the next level

```python
can_level_up(character)
```

If not, a `LevelUpError` is raised.

---

### 2. Determine Next Level

```python
new_level = character.level + 1
```

---

### 3. Hit Point Gain

Hit points are calculated using:

- Class hit dice
- Constitution modifier
- Racial caps (Elf/Halfling → max d6)
- Fixed gains after level 9

```python
hp_gained = roll_hp_gain(character, rng)
```

Rules:

- Minimum gain is always **1 HP**
- CON modifier applies only before level 10

---

### 4. Progression Updates

The engine retrieves updated values from data tables:

```python
get_attack_bonus(...)
get_saving_throws(...)
get_spell_slots(...)
get_thief_skills(...)
get_turn_undead(...)
```

### Important Design Choice

All classes receive **all data structures**, even if unused:

- Fighters still have `spell_slots` (all zeros)
- Clerics still have `thief_skills` (all zeros)
- Non-clerics have `turn_undead` (all `None`)

This avoids conditional logic and keeps the system uniform.

---

### 5. Build New Character

A new character is created using:

```python
dataclasses.replace(...)
```

Only level-dependent fields are updated:

- `level`
- `hp`
- `attack_bonus`
- `saving_throws`
- `spell_slots`
- `thief_skills`
- `turn_undead`

Everything else remains unchanged.

---

### 6. Result Summary

A `LevelUpResult` object captures:

- Old vs new level
- HP gained
- Updated combat stats
- Updated class features

This is useful for:

- CLI output
- Logging
- UI display

---

## Example

### Input Character

```json
{
  "class": "fighter",
  "level": 1,
  "xp": 2200,
  "hp": 8
}
```

### After Level-Up

```json
{
  "level": 2,
  "hp": 13,
  "attack_bonus": 1
}
```

### Result Summary

```python
LevelUpResult(
    old_level=1,
    new_level=2,
    hp_gained=5,
    new_hp_total=13,
    ...
)
```

---

## Deterministic Leveling (Seeds)

You can control randomness using a seed:

```bash
rpgleveler character.json --seed 42
```

This guarantees:

- Same HP rolls
- Reproducible results
- Stable tests

---

## Design Principles

### Pure Functions

- No mutation of input objects

### Immutable Data

- Tables use `MappingProxyType`

### Uniform Data Model

- All classes share the same structure

### Separation of Concerns

- XP logic → `advancement.py`
- Tables → `data/`
- HP logic → `hit_points.py`
- Orchestration → `leveler.py`

---

## Why This Matters

This architecture allows you to:

- Chain tools together (your CLI vision 👀)
- Run simulations safely
- Serialize/deserialize easily
- Extend the system without breaking things

---

## TL;DR

Leveling up is:

> Validate → Roll HP → Lookup tables → Build new character → Return result

Clean, predictable, and testable.
