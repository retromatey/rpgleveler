from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

# Special turn undead result values.
type TurnResult = int | Literal["T", "D"] | None


@dataclass(frozen=True)
class TurnUndead:
    """
    Immutable container for turn undead results.

    Each field represents the effectiveness of turning a specific undead type.

    Values:
        - int: Target number to roll on d20 (lower is better)
        - "T": Automatic success (turn)
        - "D": Destroy undead
        - None: Cannot affect this undead type

    Attributes:
        skeleton: Turn result for skeletons
        zombie: Turn result for zombies
        ghoul: Turn result for ghouls
        wight: Turn result for wights
        wraith: Turn result for wraiths
        mummy: Turn result for mummies
        spectre: Turn result for spectres
        vampire: Turn result for vampires
    """
    skeleton: TurnResult
    zombie: TurnResult
    ghoul: TurnResult
    wight: TurnResult
    wraith: TurnResult
    mummy: TurnResult
    spectre: TurnResult
    vampire: TurnResult

    def to_dict(self) -> dict[str, int | str | None]:
        return vars(self)

    @classmethod
    def from_dict(cls, data: dict[str, int | Literal['T','D'] | None]) -> TurnUndead:
        return cls(**data)

