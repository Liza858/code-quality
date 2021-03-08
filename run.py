import argparse
from pathlib import Path

from application_config import ApplicationConfig
from application_config import ToolType
from reviewers.perform_review import perform_and_print_review


def add_cli_arguments(parser: argparse.ArgumentParser) -> None:
    parser.add_argument('tool',
                        help='Tool name',
                        choices=list(ToolType),
                        type=ToolType)

    parser.add_argument('path',
                        type=lambda value: Path(value).absolute(),
                        help='Path to file or directory to inspect.')


def main() -> None:
    parser = argparse.ArgumentParser()
    add_cli_arguments(parser)

    args = parser.parse_args()
    config = ApplicationConfig(tool=args.tool)
    perform_and_print_review(args.path, config)


if __name__ == '__main__':
    main()
