from pathlib import Path
from typing import List, Optional

from common.subprocess_runner import run_in_subprocess
from inspectors.base_inspector import BaseInspector
from inspectors.issue import Issue, IssueType
from inspectors.utli.parse_flake8 import parse_flake8

wps_issues_code_prefix_by_type = {
    IssueType.SYSTEM: "WPS0",
    IssueType.NAMING: "WPS1",
    IssueType.COMPLEXITY: "WPS2",
    IssueType.CONSISTENCY: "WPS3",
    IssueType.BEST_PRACTICES: "WPS4",
    IssueType.REFACTORING: "WPS5",
    IssueType.OOP: "WPS6",
}


class WemakePythonStyleguideInspector(BaseInspector):

    @classmethod
    def inspect(cls, path: Path) -> List[Issue]:
        command = [
            'flake8',
            '--select', 'WPS',
            str(path)
        ]

        output = run_in_subprocess(command)
        return cls.parse(output)

    @classmethod
    def get_issue_category(cls, error_code: str) -> Optional[IssueType]:
        if error_code.startswith(wps_issues_code_prefix_by_type[IssueType.SYSTEM]):
            return IssueType.SYSTEM
        if error_code.startswith(wps_issues_code_prefix_by_type[IssueType.NAMING]):
            return IssueType.NAMING
        if error_code.startswith(wps_issues_code_prefix_by_type[IssueType.COMPLEXITY]):
            return IssueType.COMPLEXITY
        if error_code.startswith(wps_issues_code_prefix_by_type[IssueType.CONSISTENCY]):
            return IssueType.CONSISTENCY
        if error_code.startswith(wps_issues_code_prefix_by_type[IssueType.BEST_PRACTICES]):
            return IssueType.BEST_PRACTICES
        if error_code.startswith(wps_issues_code_prefix_by_type[IssueType.REFACTORING]):
            return IssueType.REFACTORING
        if error_code.startswith(wps_issues_code_prefix_by_type[IssueType.OOP]):
            return IssueType.OOP

        return None

    @classmethod
    def parse(cls, output: str) -> List[Issue]:
        return parse_flake8(cls, output)
