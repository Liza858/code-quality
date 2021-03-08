from dataclasses import dataclass
from typing import List

from inspectors.issue import Issue


@dataclass
class ReviewResult:
    issues: List[Issue]
