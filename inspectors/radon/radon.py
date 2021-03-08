import json
from dataclasses import dataclass
from pathlib import Path
from typing import List

from common.subprocess_runner import run_in_subprocess
from inspectors.base_inspector import BaseInspector
from inspectors.issue import Issue, IssueType


@dataclass
class RadonRules:
    MIN_CYCLOMATIC_COMPLEXITY = 'C'
    MIN_MAINTAINABILITY_INDEX = 'B'


class RadonInspector(BaseInspector):

    @classmethod
    def inspect(cls, path: Path) -> List[Issue]:
        command_cc = [
            'radon', 'cc',
            '-s', '-j',
            '-n', RadonRules.MIN_CYCLOMATIC_COMPLEXITY,
            str(path)
        ]

        command_mi = [
            'radon', 'mi',
            '-s', '-j',
            '-n', RadonRules.MIN_MAINTAINABILITY_INDEX,
            str(path)
        ]

        output_cc = run_in_subprocess(command_cc)
        output_mi = run_in_subprocess(command_mi)

        return cls.parse_cc(output_cc) + cls.parse_mi(output_mi)

    @classmethod
    def parse_cc(cls, output: str) -> List[Issue]:
        result = json.loads(output)
        issues = []
        for file in result:
            errors = result[file]
            for error in errors:
                issues.append(Issue(
                    category=IssueType.CYCLOMATIC_COMPLEXITY,
                    text=f'{error["type"]} {error["name"]} '
                         f'has high cyclomatic complexity={error["complexity"]} ({error["rank"]}/A)',
                    file=file,
                    line_number=int(error["lineno"]),
                    column_number=int(error["col_offset"])
                ))

        return issues

    @classmethod
    def parse_mi(cls, output: str) -> List[Issue]:
        result = json.loads(output)
        issues = []
        for file in result:
            error = result[file]
            issues.append(Issue(
                category=IssueType.MAINTAINABILITY_INDEX,
                text=f'file has low maintainability index={int(error["mi"])} ({error["rank"]}/A)',
                file=file,
                line_number=0,
                column_number=0
            ))

        return issues
