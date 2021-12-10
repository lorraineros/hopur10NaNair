import datetime
import re
from abc import abstractmethod
from dataclasses import Field, dataclass
from typing import Union

from src.models.models import Model


@dataclass
class AbstractFilter:
    field: Field

    @abstractmethod
    def __call__(self, entity: Model) -> bool:
        pass


@dataclass
class DateFilter(AbstractFilter):
    date: Union[datetime.date, datetime.datetime]

    def __call__(self, entity: Model) -> bool:
        prop = getattr(entity, self.field.name)
        return self.date == prop

    def __str__(self):
        return f"""Filtering enteries in the "{self.field.metadata['pretty_name']} by {self.date}"""


@dataclass
class PeriodFilter(AbstractFilter):
    start_date: Union[datetime.date, datetime.datetime]
    end_date: Union[datetime.date, datetime.datetime]

    def __call__(self, entity: Model) -> bool:
        prop = getattr(entity, self.field.name)
        return self.start_date <= prop and prop <= self.end_date

    def __str__(self):
        return f"""Filtering enteries in the "{self.field.metadata['pretty_name']} by {self.start_date} and {self.end_date}"""


@dataclass
class RegexFilter(AbstractFilter):
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


@dataclass
class IdFilter(AbstractFilter):
    id: int

    def __call__(self, entity: Model) -> bool:
        return getattr(entity, self.field.name) == self.id
