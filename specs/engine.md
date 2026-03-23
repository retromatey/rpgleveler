Implement the logic for src/rpgleveler/engine/progression.py.

Context:
- This module provides a thin abstraction over static data tables located in src/rpgleveler/data/.
- It must not contain hardcoded game rules beyond simple table lookups and composition.
- All functions are pure and must not mutate inputs.

Requirements:
- Follow the constraints defined in AGENTS.md.
- Do not modify function signatures.
- Do not move logic into other modules.
- Keep implementations minimal and table-driven.
- Preserve immutability (especially for returned dicts).

Functions to implement:
- get_attack_bonus
- get_saving_throws
- apply_saving_throw_modifiers
- get_spell_slots
- get_thief_skills
- get_turn_undead

Behavior expectations:
- Table lookups should raise KeyError for invalid class or level.
- get_spell_slots returns None for non-caster classes.
- get_thief_skills returns None for non-thief classes.
- get_turn_undead returns None for non-cleric classes.
- apply_saving_throw_modifiers:
  - returns a new dict
  - adds race-based modifiers to base values
  - returns base unchanged if race has no modifiers

Testing:
- Run only relevant tests:
  pytest tests/unit/engine/test_progression.py tests/unit/data

Quality gates:
- ruff check .
- mypy src

Constraints:
- Do not introduce new dependencies.
- Do not change test files unless they are clearly incorrect.
- Do not implement unrelated modules.

Output:
- List files modified
- Summarize implementation approach
- Confirm test results (pass/fail)
- Note any assumptions or ambiguities in rules


---


