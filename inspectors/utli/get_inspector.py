from application_config import ToolType
from inspectors.base_inspector import BaseInspector
from inspectors.cohesion.cohesion import CohesionInspector
from inspectors.radon.radon import RadonInspector
from inspectors.wemake_python_styleguide.wemake_python_styleguide import WemakePythonStyleguideInspector


def get_inspector_for_tool_type(tool_type: ToolType) -> BaseInspector:
    if tool_type == ToolType.COHESION:
        return CohesionInspector()
    if tool_type == ToolType.WEMAKE_PYTHON_STYLEGUIDE:
        return WemakePythonStyleguideInspector()
    if tool_type == ToolType.RADON:
        return RadonInspector()
