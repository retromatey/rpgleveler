"""
Class name definitions for the application.

This module defines the canonical set of supported character classes using a
string-based enumeration. It also provides utilities for parsing user input
(e.g., from CLI arguments) into validated enum values.

The enum values are lowercase strings to align with CLI input and external
representations.

Example:
    >>> parse_class_name("cleric")
    <ClassName.CLERIC: 'cleric'>

    >>> parse_class_name("invalid")
    Traceback (most recent call last):
        ...
    ValueError: Invalid class name: invalid
"""

from enum import StrEnum, auto


class ClassName(StrEnum):
    """
    Enumeration of supported character classes.

    This enum uses `StrEnum` so that each member behaves like a string, making
    it convenient for CLI parsing, serialization, and comparison.

    Values are automatically generated as lowercase strings matching the member
    names.

    Members:
        CLERIC: Cleric class
        FIGHTER: Fighter class
        MAGIC_USER: Magic-user class
        THIEF: Thief class
    """
    CLERIC = auto()
    FIGHTER = auto()
    MAGIC_USER = "magic-user"
    THIEF = auto()


def parse_class_name(class_name: str) -> ClassName:
    """
    Parse a string into a `ClassName` enum value.

    This function is intended for use at system boundaries (e.g., CLI input),
    where user-provided strings must be validated and converted into
    strongly-typed enum values.

    Args:
        class_name: The input string representing a class name.

    Returns:
        A corresponding `ClassName` enum value.

    Raises:
        ValueError: If the input does not match any valid class name.

    Example:
        >>> parse_class_name("fighter")
        <ClassName.FIGHTER: 'fighter'>
    """
    try:
        return ClassName(class_name)
    except ValueError:
        raise ValueError(f"Invalid class name: {class_name}")
