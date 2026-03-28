"""
Hit point progression logic for Basic Fantasy RPG.

This module encapsulates the rules for determining how many hit points a
character gains when advancing to a new level.

The primary responsibility of this module is to calculate hit point increases
based on class hit dice, ability modifiers, and game rules.

Structure:
    - roll_hp_gain: Calculates hit points gained during level-up

Notes:
    - Hit point progression is class-dependent (different hit dice).
    - Constitution modifiers may affect the final result.
    - Minimum gain rules (e.g., at least 1 HP per level) may apply.
    - This module is responsible for all HP-related calculations and should be
      used by the level-up engine instead of duplicating logic.
"""
from diceroller.core import DiceRoller

from rpgleveler.shared import Character


def roll_hp_gain(character: Character, rng: DiceRoller) -> int:
    """
    Calculate hit points gained when a character levels up.

    The number of hit points gained is determined by:
        - The character's class hit die
        - A random roll using the provided DiceRoller
        - Constitution modifier (if applicable)
        - Minimum gain rules (if enforced)

    Args:
        character:
            The character gaining a level.
        rng:
            A DiceRoller instance used to generate deterministic or random rolls.

    Returns:
        int:
            The number of hit points gained for this level-up.

    Notes:
        - This function does not modify the character directly.
        - The result should be applied by the level-up engine.
    """
    raise NotImplementedError
