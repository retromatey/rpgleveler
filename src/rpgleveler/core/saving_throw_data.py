from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class SavingThrowData:
    """
    Immutable container for saving throw values.

    Each field represents the target number required to succeed on a d20 roll
    against a specific category of effect. Lower values indicate better saves.

    Attributes:
        death_ray_or_poison: Resistance to poison and instant-death effects
        magic_wands: Resistance to effects from magical wands
        paralysis_or_petrify: Resistance to paralysis and petrification effects
        dragon_breath: Resistance to breath weapons and area attacks
        spells: Resistance to general spell effects
    """
    death_ray_or_poison: int
    magic_wands: int
    paralysis_or_petrify: int
    dragon_breath: int
    spells: int

    def add(self, other: SavingThrowData) -> SavingThrowData:
        """
        Combine two saving throw datasets.

        This is primarily used to apply racial modifiers to base class values.

        Args:
            other: Another `SavingThrowData` instance to add.

        Returns:
            A new `SavingThrowData` instance with combined values.
        """
        return SavingThrowData(
            death_ray_or_poison=self.death_ray_or_poison + other.death_ray_or_poison,
            magic_wands=self.magic_wands + other.magic_wands,
            paralysis_or_petrify=self.paralysis_or_petrify + other.paralysis_or_petrify,
            dragon_breath=self.dragon_breath + other.dragon_breath,
            spells=self.spells + other.spells,
        )

    def to_dict(self) -> dict[str, int]:
        return vars(self)

    @classmethod
    def from_dict(cls, data: dict[str, int]) -> SavingThrowData:
        return cls(**data)
