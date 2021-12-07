import re
from dataclasses import dataclass
from typing import Any


@dataclass
class RegexFilter:
    field: str
    regex: str

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        entity = args[0]
        prop = getattr(entity, self.field)
        return re.search(self.regex, prop)
