# Character JSON Format

The `rpgleveler` CLI operates on character data stored in JSON format.

This page describes the expected structure of that JSON file.

---

## Overview

A character JSON file represents the full state of a character, including:

- Core identity (name, class, race)
- Ability scores and modifiers
- Combat stats
- Progression data (XP, level)
- Class-specific features (spell slots, thief skills, etc.)

---

## Example

```json
{
  "name": "Thorin",
  "race": "dwarf",
  "class": "fighter",
  "level": 1,
  "xp": 2500,

  "abilities": {
    "STR": 16,
    "DEX": 12,
    "CON": 15,
    "INT": 10,
    "WIS": 11,
    "CHA": 9
  },

  "ability_mods": {
    "STR": 2,
    "DEX": 0,
    "CON": 1,
    "INT": 0,
    "WIS": 0,
    "CHA": -1
  },

  "hp": 10,
  "ac": 15,
  "attack_bonus": 1,

  "saving_throws": {
    "death_ray_or_poison": 12,
    "magic_wands": 13,
    "paralysis_or_petrify": 14,
    "dragon_breath": 15,
    "spells": 17
  },

  "spell_slots": {
    "level_1": 0,
    "level_2": 0,
    "level_3": 0,
    "level_4": 0,
    "level_5": 0
  },

  "thief_skills": {
    "open_locks": 0,
    "pick_pockets": 0,
    "find_traps": 0,
    "remove_traps": 0,
    "move_silently": 0,
    "climb_walls": 0,
    "hide_in_shadows": 0,
    "hear_noise": 0
  },

  "turn_undead": {
    "skeleton": null,
    "zombie": null,
    "ghoul": null,
    "wight": null,
    "wraith": null,
    "mummy": null,
    "spectre": null,
    "vampire": null
  },

  "money_gp": 50,
  "inventory": [
    "chain mail",
    "shield",
    "battle axe"
  ]
}
```

---

## Required Fields

| Field | Type           | Description                                |
|-------|----------------|--------------------------------------------|
| name  | string \| null | Character name                             |
| race  | string         | One of: dwarf, elf, halfling, human        |
| class | string         | One of: cleric, fighter, magic-user, thief |
| level | int            | Current level (1–20)                       |
| xp    | int            | Current experience points                  |

---

## Ability Scores

```json
"abilities": {
  "STR": int,
  "DEX": int,
  "CON": int,
  "INT": int,
  "WIS": int,
  "CHA": int
}
```

- Standard Basic Fantasy ability scores
- Typically range from 3–18

---

## Ability Modifiers

```json
"ability_mods": {
  "STR": int,
  "DEX": int,
  "CON": int,
  "INT": int,
  "WIS": int,
  "CHA": int
}
```

- Precomputed modifiers
- Used during level-up (e.g., CON affects HP)

---

## Combat Stats

| Field        | Type | Description        |
|--------------|------|--------------------|
| hp           | int  | Current hit points |
| ac           | int  | Armor class        |
| attack_bonus | int  | Attack modifier    |

---

## Saving Throws

```json
"saving_throws": {
  "death_ray_or_poison": int,
  "magic_wands": int,
  "paralysis_or_petrify": int,
  "dragon_breath": int,
  "spells": int
}
```

- Lower values are better
- Values depend on class and level

---

## Spell Slots

```json
"spell_slots": {
  "level_1": int,
  "level_2": int,
  "level_3": int,
  "level_4": int,
  "level_5": int
}
```

- Non-spellcasters should use all zeros

---

## Thief Skills

```json
"thief_skills": {
  "open_locks": int,
  "pick_pockets": int,
  "find_traps": int,
  "remove_traps": int,
  "move_silently": int,
  "climb_walls": int,
  "hide_in_shadows": int,
  "hear_noise": int
}
```

- Percent values (0–100+)
- Non-thieves should use all zeros

---

## Turn Undead

```json
"turn_undead": {
  "skeleton": int | "T" | "D" | null,
  "zombie": int | "T" | "D" | null,
  "ghoul": int | "T" | "D" | null,
  "wight": int | "T" | "D" | null,
  "wraith": int | "T" | "D" | null,
  "mummy": int | "T" | "D" | null,
  "spectre": int | "T" | "D" | null,
  "vampire": int | "T" | "D" | null
}
```

- int → roll target  
- "T" → automatic turn  
- "D" → destroy  
- null → no effect  

---

## Inventory and Wealth

```json
"money_gp": int
"inventory": string[]
```

---

## Notes

- All fields are expected to be present  
- Default values should be used for non-applicable abilities  
- The CLI does not modify the input file  
- Output will follow the same structure  
