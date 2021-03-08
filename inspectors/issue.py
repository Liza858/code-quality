from dataclasses import dataclass
from enum import Enum, unique


@unique
class IssueType(Enum):
    SYSTEM = 'SYSTEM'
    NAMING = 'NAMING'
    COMPLEXITY = 'COMPLEXITY'
    CONSISTENCY = 'CONSISTENCY'
    BEST_PRACTICES = 'BEST_PRACTICES'
    REFACTORING = 'REFACTORING'
    OOP = 'OOP'
    COHESION = 'COHESION'
    CYCLOMATIC_COMPLEXITY = 'CYCLOMATIC_COMPLEXITY'
    MAINTAINABILITY_INDEX = 'MAINTAINABILITY_INDEX'


@dataclass
class Issue:
    file: str
    category: IssueType
    text: str
    line_number: int
    column_number: int
