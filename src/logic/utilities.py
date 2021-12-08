from abc import abstractmethod
import re
from dataclasses import dataclass
from typing import Any
import datetime

from src.models.models import Model


class AbstractFilter:
    @abstractmethod
    def __call__(self, entity: Model) -> bool:
        pass


@dataclass
class DateFilter(AbstractFilter):
    field: str
    date: datetime.date

    def __call__(self, entity: Model) -> bool:
        prop = getattr(entity, self.field)
        return self.date == prop


@dataclass
class PeriodFilter(AbstractFilter):
    field: str
    start_date: datetime.date
    end_date: datetime.date

    def __call__(self, entity: Model) -> bool:
        prop = getattr(entity, self.field)
        return self.start_date <= prop and prop <= self.end_date


@dataclass
class RegexFilter(AbstractFilter):
    field: str
    regex: str

    def __call__(self, entity: Model) -> bool:
        prop = getattr(entity, self.field)
        return bool(re.search(self.regex, prop))
