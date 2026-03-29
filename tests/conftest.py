from pathlib import Path

import pytest

from rpgleveler.core import (
    AbilityScores,
    Character,
    ClassName,
    Race,
    SavingThrowData,
    SpellSlots,
    ThiefSkills,
    TurnUndead,
)


def pytest_collection_modifyitems(config, items):
    for item in items:
        parts = Path(item.fspath).parts

        if "unit" in parts:
            item.add_marker(pytest.mark.unit)
        elif "integration" in parts:
            item.add_marker(pytest.mark.integration)


@pytest.fixture
def character_factory():
    """
    Factory fixture for creating valid Character instances in tests.

    This fixture provides a fully-populated default Character object that can be
    customized via keyword overrides. It is intended to reduce boilerplate in
    tests while ensuring all required fields are present and valid.

    The returned factory function accepts any Character field as a keyword
    argument and will override the default value.

    Returns:
        Callable[..., Character]:
            A function that constructs a Character instance with optional
            overrides.

    Example:
        Create a default character:
            def test_default_character(character_factory):
                char = character_factory()
                assert char.level == 1

        Override specific fields:
            def test_custom_level(character_factory):
                char = character_factory(level=5, xp=20000)
                assert char.level == 5

        Test level-up behavior:
            def test_level_up(character_factory):
                char = character_factory(level=1, xp=3000)
                new_char, result = level_up(char, rng=my_rng)
                assert new_char.level == 2

        Create a different class:
            def test_magic_user(character_factory):
                char = character_factory(class_name=ClassName.MAGIC_USER)
                assert char.class_name == ClassName.MAGIC_USER

    Notes:
        - All required Character fields are pre-populated with sensible
          defaults.
        - Overrides are shallow (no deep merging of nested objects).
        - Enum values (ClassName, Race) should be used instead of strings.
        - This fixture is best suited for unit tests. For integration tests,
          consider using JSON-based test data.
    """
    def _build_character(**overrides):
        base = {
            "name": "Thorin",
            "race": Race.DWARF,
            "class_name": ClassName.FIGHTER,
            "level": 1,
            "xp": 0,

            "abilities": AbilityScores(
                STR=16, DEX=12, CON=15, INT=10, WIS=11, CHA=9
            ),

            "ability_mods": {
                "STR": 2,
                "DEX": 0,
                "CON": 1,
                "INT": 0,
                "WIS": 0,
                "CHA": -1,
            },

            "hp": 10,
            "ac": 15,
            "attack_bonus": 1,

            "inventory": [],
            "money_gp": 0,

            "saving_throws": SavingThrowData(
                death_ray_or_poison=12,
                magic_wands=13,
                paralysis_or_petrify=14,
                dragon_breath=15,
                spells=17,
            ),

            "spell_slots": SpellSlots(0, 0, 0, 0, 0),
            "thief_skills": ThiefSkills(0, 0, 0, 0, 0, 0, 0, 0),
            "turn_undead": TurnUndead(*(None,) * 8),
        }

        base.update(overrides)
        return Character(**base)

    return _build_character
