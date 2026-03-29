"""
Hit point gain calculation for Basic Fantasy RPG.

This module implements the rules for determining how many hit points a character
gains when advancing to the next level.

Unlike most progression systems in this package, hit point gains are
**logic-driven** rather than table-driven. The hit dice tables define the
structure of the roll, but additional rules must be applied dynamically based on
level, race, and Constitution modifier.

Overview:
    - Hit dice expressions are retrieved from the data layer via
      `get_hit_dice()`.
    - Expressions are parsed into roll components (dice count, die size, and
      bonus).
    - Dice rolling is delegated to a provided `DiceRoller` instance.
    - Additional rules (racial caps, Constitution modifiers, fixed gains) are
      applied according to Basic Fantasy RPG rules.

Rules Implemented:
    Levels 1–9:
        - Roll hit dice based on class progression (e.g., "1d8", "3d6+1").
        - Apply Constitution modifier.
        - Minimum gain is 1 hit point.

    Levels 10+:
        - Use fixed bonus from hit dice expression (e.g., "9d8+3" → gain 3).
        - Constitution modifier is NOT applied.

    Racial Restrictions:
        - Elves and Halflings cannot roll hit dice larger than d6.
        - Any larger die (e.g., d8) is capped at d6 before rolling.

Design Notes:
    - This module is deterministic given the injected RNG.
    - No mutation occurs; functions return computed values only.
    - Parsing and rule application are separated for testability.
"""
import re

from diceroller.core import DiceRoller

from rpgleveler.core import Race
from rpgleveler.data import get_hit_dice
from rpgleveler.shared import Character


def _parse_hit_dice(expr: str) -> tuple[int, int, int]:
    """
    Parse a hit dice expression like '3d6+2' into components.

    Returns:
        (num_dice, die_size, bonus)
    """
    match = re.fullmatch(r"(\d+)d(\d+)(?:\+(\d+))?", expr)
    if not match:
        raise ValueError(f"Invalid hit dice expression: {expr}")

    num_dice = int(match.group(1))
    die_size = int(match.group(2))
    bonus = int(match.group(3) or 0)

    return num_dice, die_size, bonus


def _apply_racial_cap(die_size: int, race: Race) -> int:
    """
    Apply racial hit die caps.

    Elves and Halflings cannot roll above d6.
    """
    if race in {Race.ELF, Race.HALFLING}:
        return min(die_size, 6)
    return die_size


def _get_con_modifier(character: Character) -> int:
    """
    Retrieve Constitution modifier.

    Assumes ability_mods already contains it.
    """
    return character.ability_mods.get("CON", 0)


def roll_hp_gain(character: Character, rng: DiceRoller) -> int:
    """
    Calculate hit points gained when a character levels up.

    This function determines the hit point increase for a character advancing
    to their next level, applying all relevant game rules including hit dice
    progression, racial restrictions, and Constitution modifiers.

    The calculation path depends on the resulting level:

    - Levels 1–9:
        - Roll hit dice based on class progression.
        - Apply Constitution modifier.
        - Enforce a minimum gain of 1 hit point.

    - Levels 10+:
        - Use the fixed bonus from the hit dice expression.
        - Constitution modifier is not applied.
        - Enforce a minimum gain of 1 hit point.

    Racial adjustments:
        - Elves and Halflings cannot roll dice larger than d6.
        - Larger dice are reduced to d6 before rolling.

    Args:
        character:
            The character being leveled up.
        rng:
            A DiceRoller instance used to perform dice rolls.

    Returns:
        int:
            The number of hit points gained (minimum of 1).

    Raises:
        ValueError:
            If the hit dice expression is invalid.

    Notes:
        - The calculation uses the *next* level (current level + 1).
        - Dice rolling is delegated to the provided RNG for testability.
        - This function does not modify the character.
    """
    level = character.level + 1  # gaining next level

    expr = get_hit_dice(character.class_name, level)
    num_dice, die_size, bonus = _parse_hit_dice(expr)

    # Post-9th level → fixed gain only
    if level >= 10:
        return max(1, bonus)

    # Apply racial cap
    die_size = _apply_racial_cap(die_size, character.race)
    expr = f"1d{die_size}"

    # Roll dice
    roll_total = rng.roll(expr)

    # Apply CON modifier
    con_mod = _get_con_modifier(character)

    total = roll_total + con_mod

    return max(1, total)
