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
    Calculate hit points gained when leveling up.

    Rules:
        - Levels 1–9: roll hit dice + CON modifier
        - Levels 10+: fixed bonus only (no CON modifier)
        - Elves/Halflings cap die size at d6
        - Minimum gain is 1 HP
    """
    level = character.level + 1  # gaining next level

    expr = get_hit_dice(character.class_name, level)
    num_dice, die_size, bonus = _parse_hit_dice(expr)

    # Post-9th level → fixed gain only
    if level >= 10:
        return max(1, bonus)

    # Apply racial cap
    die_size = _apply_racial_cap(die_size, character.race)
    expr = f"{num_dice}d{die_size}"

    # Roll dice
    roll_total = rng.roll(expr)

    # Apply CON modifier
    con_mod = _get_con_modifier(character)

    total = roll_total + con_mod

    return max(1, total)
