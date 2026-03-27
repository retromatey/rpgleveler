"""
TODO: add comments
"""

from enum import StrEnum, auto


class Race(StrEnum):
    """
    TODO: add comments
    """
    DWARF = auto()
    ELF = auto()
    HALFLING = auto()
    HUMAN = auto()


def parse_race(race: str) -> Race:
    """
    TODO: add comments
    """
    try:
        return Race(race)
    except ValueError:
        raise ValueError(f"Invalid race: {race}")
