from pathlib import Path
from typing import List, Optional

from inspectors.base_inspector import BaseInspector
from inspectors.issue import Issue, IssueType
from inspectors.utli.parse_flake8 import parse_flake8
from inspectors.wemake_python_styleguide.wemake_python_styleguide import run_in_subprocess

cohesion_issues_code_prefix_by_type = {
    IssueType.COHESION: "H601"
}


class CohesionInspector(BaseInspector):

    @classmethod
    def inspect(cls, path: Path) -> List[Issue]:
        command = [
            'flake8',
            '--select', 'H601',
            str(path)
        ]

        output = run_in_subprocess(command)
        return cls.parse(output)

    @classmethod
    def get_issue_category(cls, error_code: str) -> Optional[IssueType]:
        if error_code.startswith(cohesion_issues_code_prefix_by_type[IssueType.COHESION]):
            return IssueType.COHESION

        return None

    @classmethod
    def parse(cls, output: str) -> List[Issue]:
        return parse_flake8(cls, output)
