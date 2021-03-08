from typing import List

from inspectors.issue import Issue


def parse_flake8(cls, output: str) -> List[Issue]:
    issues = []
    lines = output.split("\n")[:-1]
    for line in lines:
        parts = line.split(' ', maxsplit=2)
        file, line_number, column_number, _ = tuple(parts[0].split(':', maxsplit=3))
        code = parts[1]
        text = parts[2]

        issues.append(Issue(
            category=cls.get_issue_category(code),
            text=text,
            file=file,
            line_number=int(line_number),
            column_number=int(column_number)
        ))

    return issues
