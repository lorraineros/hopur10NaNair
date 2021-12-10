import datetime
import re
from abc import abstractmethod
from dataclasses import Field, dataclass
from typing import Union

from src.models.models import Model


@dataclass
class AbstractFilter:
    field: Field

    def __post_init__(self):
        self.pname = self.field.metadata.get("pretty_name", self.field.name)

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
        return (
            f'Only showing entries with the date {self.date} in column "{self.pname}"'
        )


@dataclass
class PeriodFilter(AbstractFilter):
    start_date: Union[datetime.date, datetime.datetime]
    end_date: Union[datetime.date, datetime.datetime]

    def __call__(self, entity: Model) -> bool:
        prop = getattr(entity, self.field.name)
        return self.start_date <= prop and prop <= self.end_date

    def __str__(self):
        return f"Only showing entries with dates from "

    '{self.start_date} to {self.end_date} in column "{self.pname}"'


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
        return f'Limiting the "{self.pname}" column to entries that match the regex: "{self.regex}"'


@dataclass
class IdFilter(AbstractFilter):
    id: int

    def __call__(self, entity: Model) -> bool:
        return getattr(entity, self.field.name) == self.id

    def __str__(self):
        return f"Only showing {self.pname} with the ID: {self.id}"
