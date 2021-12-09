from abc import abstractmethod
import re
from dataclasses import Field, dataclass
from typing import Any
import datetime

from src.models.models import Model


class AbstractFilter:
    @abstractmethod
    def __call__(self, entity: Model) -> bool:
        pass


@dataclass
class DateFilter(AbstractFilter):
    field: Field
    date: datetime.date

    def __call__(self, entity: Model) -> bool:
        prop = getattr(entity, self.field.name)
        return self.date == prop


@dataclass
class PeriodFilter(AbstractFilter):
    field: Field
    start_date: datetime.date
    end_date: datetime.date

    def __call__(self, entity: Model) -> bool:
        prop = getattr(entity, self.field.name)
        return self.start_date <= prop and prop <= self.end_date


@dataclass
class RegexFilter(AbstractFilter):
    field: Field
    regex: str

    def __call__(self, entity: Model) -> bool:
        prop = str(getattr(entity, self.field.name))
        try:
            result = bool(re.search(self.regex, prop))
        except re.error:
            result = self.regex in prop
        return result

    def __str__(self):
        return f"""Filtering entries in the "{self.field.metadata['pretty_name']}" column by "{self.regex}" """
