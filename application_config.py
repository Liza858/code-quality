from dataclasses import dataclass
from enum import Enum, unique


@unique
class ToolType(Enum):
    WEMAKE_PYTHON_STYLEGUIDE = 'wemake-python-styleguide'
    COHESION = 'cohesion'
    RADON = 'radon'


@dataclass
class ApplicationConfig:
    tool: ToolType
