import argparse
import sys
from importlib.metadata import PackageNotFoundError, version

from diceroller.core import CustomRandom, DiceRoller

from rpgleveler.cli.handlers import handle_level_up


def _project_version() -> str:
    try:
        # Must match [project].name in pyproject.toml
        return version("rpgleveler")
    except PackageNotFoundError:
        return "unknown"


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="rpgleveler",
        description="Basic Fantasy Character Leveler CLI",
    )

    parser.add_argument("input_file", help="Path to character JSON file")

    parser.add_argument(
        "--version",
        action="version",
        version=_project_version(),
    )

    parser.add_argument(
        "--seed",
        type=int,
        help="Seed for deterministic dice rolls",
    )

    parser.add_argument(
        "--out",
        type=str,
        help="Write output to file instead of stdout",
    )

    return parser.parse_args(argv)


def create_dice_roller(seed: int | None) -> DiceRoller:
    if seed is None:
        return DiceRoller()
    return DiceRoller(CustomRandom(seed))


def main(argv: list[str] | None = None) -> None:
    args = parse_args(argv)

    try:
        rng = create_dice_roller(args.seed)

        handle_level_up(
            input_path=args.input_file,
            rng=rng,
            output_path=args.out,
        )

    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        sys.exit(2)


if __name__ == "__main__": # pragma: no cover
    main()
