from pathlib import Path

from application_config import ApplicationConfig
from inspectors.utli.get_inspector import get_inspector_for_tool_type
from reviewers.review_result import ReviewResult
from reviewers.util.print_review import print_review


def perform_and_print_review(path: Path, config: ApplicationConfig) -> None:
    if not path.exists():
        print(f'error! path {str(path)} doesn\'t exist')
        return
    if path.is_file():
        if not path.suffix == '.py':
            print(f'error! {str(path)} is not a python file')
            return

    inspector = get_inspector_for_tool_type(config.tool)
    issues = inspector.inspect(path)
    print_review(ReviewResult(issues))
