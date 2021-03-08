import abc
from pathlib import Path
from typing import List

from inspectors.issue import Issue


class BaseInspector(abc.ABC):
    @abc.abstractmethod
    def inspect(self, path: Path) -> List[Issue]:
        raise NotImplementedError
