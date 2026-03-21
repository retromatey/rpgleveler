"""
Shared literal type definitions for rpgleveler.

This module contains canonical string literals used across the project to ensure
consistency and type safety when referencing core game concepts.

Currently includes:
    - ClassName: Supported Basic Fantasy character classes
    - RaceName: Supported Basic Fantasy character races

Notes:
    - These literals should be reused across all modules to avoid duplication
      and string mismatches.
    - Values are lowercase and normalized for internal consistency.
"""

from __future__ import annotations

from typing import Literal

ClassName = Literal["cleric", "fighter", "magic-user", "thief"]
"""Canonical lowercase identifiers for supported character classes."""

RaceName = Literal["dwarf", "elf", "halfling", "human"]
"""Canonical lowercase identifiers for supported character races."""
