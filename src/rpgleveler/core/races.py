"""
Race definitions for the application.

This module defines the canonical set of supported character races using a
string-based enumeration. It also provides a helper function for parsing and
validating user input (e.g., from CLI arguments).

The enum values are lowercase strings to align with CLI input and external
representations.

Example:
    ```
    >>> parse_race("elf")
    <Race.ELF: 'elf'>

    >>> parse_race("orc")
    Traceback (most recent call last):
        ...
    ValueError: Invalid race: orc
    ```
"""

from enum import StrEnum, auto


class Race(StrEnum):
    """
    Enumeration of supported character races.

    This enum uses `StrEnum` so that each member behaves like a string, making
    it convenient for CLI parsing, serialization, and comparison.

    Values are automatically generated as lowercase strings matching the member
    names.

    Members:
        - DWARF: Dwarf race
        - ELF: Elf race
        - HALFLING: Halfling race
        - HUMAN: Human race
    """
    DWARF = auto()
    ELF = auto()
    HALFLING = auto()
    HUMAN = auto()


def parse_race(race: str) -> Race:
    """
    Parse a string into a `Race` enum value.

    This function is intended for use at system boundaries (e.g., CLI input),
    where user-provided strings must be validated and converted into
    strongly-typed enum values.

    Args:
        race: The input string representing a character race.

    Returns:
        A corresponding `Race` enum value.

    Raises:
        ValueError: If the input does not match any valid race.

    Example:
        ```
        >>> parse_race("human")
        <Race.HUMAN: 'human'>
        ```
    """
    try:
        return Race(race)
    except ValueError:
        raise ValueError(f"Invalid race: {race}")
