import argparse
import sys
from importlib.metadata import PackageNotFoundError, version

from diceroller.core import CustomRandom, DiceRoller


def _project_version() -> str:
    try:
        return version("rpgleveler")  # must match [project].name in pyproject.toml
    except PackageNotFoundError:
        return "unknown"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="rpgleveler",
        description="Basic Fantasy Character Leveler CLI",
    )
    parser.add_argument("--version", action="version", version=_project_version())
    return parser.parse_args()


def exit_with_error(message: str, args: argparse.Namespace) -> None:
    #prefix = "[verbose] " if args.verbose else ""
    prefix = ""
    print(f"{prefix}{message}", file=sys.stderr)
    sys.exit(2)


def create_dice_roller(seed: int | None) -> DiceRoller:
    if seed is None:
        return DiceRoller()
    else:
        custom_random = CustomRandom(seed)
        return DiceRoller(custom_random)


def main() -> None:
    #args = parse_args()
    parse_args()
    rng = create_dice_roller(None)
    print(f"You rolled a {rng.roll('1d20')}")


if __name__ == "__main__":
    main()
