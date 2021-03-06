import datetime
from abc import abstractmethod
from dataclasses import dataclass, field
from typing import Any, Dict, TypeVar

M = TypeVar("M")


@dataclass
class Model:
    id: int = field(
        default=int(),
        metadata={"autoinit": True, "required": True, "pretty_name": "ID"},
    )

    @classmethod
    def from_dict(cls, dictionary: Dict[str, Any]):
        return cls(**dictionary)

    @classmethod
    def model_name(cls):
        return cls.__name__

    @abstractmethod
    def short_name(self):
        pass

    @classmethod
    def command(cls):
        return cls.__name__

    @classmethod
    def mentioned_by(cls):
        return []


@dataclass
class BaseEmployee(Model):
    name: str = field(
        default="",
        metadata={"pretty_name": "Name", "required": True},
    )
    phone: str = field(
        default="",
        metadata={"pretty_name": "Phone number", "required": True},
    )

    def short_name(self):
        return f"{self.id}. {self.name}"


@dataclass
class Employee(BaseEmployee):
    home_address: str = field(
        default="",
        metadata={"pretty_name": "Home address", "required": True},
    )
    gsm: str = field(
        default="",
        metadata={"pretty_name": "GSM"},
    )
    email: str = field(
        default="",
        metadata={"pretty_name": "Email"},
    )
    is_manager: bool = field(
        default=False,
        metadata={"pretty_name": "Is Employee a Manager? "},
    )
    work_destination: int = field(
        default=int(),
        metadata={"pretty_name": "Destination ID", "id": lambda: Destination},
    )

    def __post_init__(self):
        self.is_manager = bool(self.is_manager)

    @classmethod
    def command(cls):
        return "emp"

    @classmethod
    def mentioned_by(cls):
        return [WorkReport]


@dataclass
class Contractor(BaseEmployee):
    name_of_company: str = field(
        default="",
        metadata={"pretty_name": "Name of company", "required": True},
    )
    working_hours: str = field(
        default="",
        metadata={"pretty_name": "Working Hours", "required": True},
    )
    location: int = field(
        default=0,
        metadata={
            "pretty_name": "Location",
            "id": lambda: Destination,
            "required": True,
        },
    )

    def short_name(self):
        return f"{self.id}. {self.name_of_company}"

    @classmethod
    def command(cls):
        return "con"

    @classmethod
    def mentioned_by(cls):
        return [WorkReport]


@dataclass
class WorkRequest(Model):
    title: str = field(
        default="",
        metadata={"pretty_name": "Title", "required": True},
    )
    real_estate: int = field(
        default=0,
        metadata={
            "pretty_name": "Real Estate ID",
            "required": True,
            "id": lambda: RealEstate,
        },
    )
    date: datetime.date = field(
        default=datetime.date.today(),
        metadata={"pretty_name": "Date", "derived": True, "required": True},
    )
    priority: str = field(
        default="",
        metadata={"pretty_name": "Priority", "required": True},
    )
    is_open: bool = field(
        default=True,
        metadata={"pretty_name": "Is it Open?", "required": True},
    )
    description: str = field(
        default="",
        metadata={"pretty_name": "Description", "required": True},
    )
    start_date: datetime.date = field(
        default=None,
        metadata={"pretty_name": "Start date", "initializer": True, "required": True},
    )
    end_date: datetime.date = field(
        default=None,
        metadata={"pretty_name": "End date", "initializer": True, "required": True},
    )
    repeat_period: datetime.timedelta = field(
        default=None,
        metadata={
            "pretty_name": "Repeat period",
            "initializer": True,
            "required": True,
        },
    )

    def __post_init__(self):
        if not isinstance(self.date, datetime.date):
            self.date = datetime.date.fromisoformat(self.date)

    @classmethod
    def model_name(cls):
        return "Work request"

    def short_name(self):
        return f"{self.id}. {self.title}"

    @classmethod
    def command(cls):
        return "req"

    @classmethod
    def mentioned_by(cls):
        return [WorkReport]


@dataclass
class WorkReport(Model):
    work_request_id: int = field(
        default=int(),
        metadata={
            "pretty_name": "Work Request ID",
            "required": True,
            "id": lambda: WorkRequest,
            "employee_can_edit": True,
        },
    )
    date: datetime.datetime = field(
        default=datetime.datetime.now(),
        metadata={"pretty_name": "Date"},
    )
    employee_id: int = field(
        default=int(),
        metadata={
            "pretty_name": "Employee ID",
            "required": True,
            "id": lambda: Employee,
            "employee_can_edit": True,
        },
    )
    contractor_id: int = field(
        default=int(),
        metadata={
            "pretty_name": "Contractor ID",
            "id": lambda: Contractor,
            "employee_can_edit": True,
        },
    )
    contractors_fee: str = field(
        default="",
        metadata={"pretty_name": "Contractor's fee", "employee_can_edit": True},
    )
    description: str = field(
        default="",
        metadata={"pretty_name": "Description", "employee_can_edit": True},
    )
    material_cost: str = field(
        default="",
        metadata={"pretty_name": "Material cost", "employee_can_edit": True},
    )
    done: bool = field(
        default=False,
        metadata={"pretty_name": "Done", "employee_can_edit": True},
    )
    comment: str = field(
        default="",
        metadata={"pretty_name": "Comment"},
    )

    def __post_init__(self):
        self.done = bool(self.done)
        if not isinstance(self.date, datetime.datetime):
            self.date = datetime.datetime.fromisoformat(self.date)

    @classmethod
    def model_name(cls):
        return "Work report"

    @classmethod
    def command(cls):
        return "rep"

    def short_name(self):
        return f"{self.id}. {self.title}"


@dataclass
class RealEstate(Model):
    address: str = field(
        default="",
        metadata={"pretty_name": "Address", "required": True},
    )
    real_estate_number: str = field(
        default="",
        metadata={"pretty_name": "Real Estate Number", "required": True},
    )
    location: int = field(
        default=int(),
        metadata={"pretty_name": "Location ID", "id": lambda: Destination},
    )
    condition: str = field(
        default="",
        metadata={"pretty_name": "Condition"},
    )
    facilities: str = field(
        default="",
        metadata={"pretty_name": "Facilities"},
    )
    type_of_real_estate: str = field(
        default="",
        metadata={"pretty_name": "Type of Real Estate"},
    )
    rooms: int = field(
        default=0,
        metadata={"pretty_name": "Rooms"},
    )
    size: int = field(
        default=0,
        metadata={"pretty_name": "Size"},
    )

    def short_name(self):
        return f"{self.id}. {self.real_estate_number}"

    @classmethod
    def model_name(cls):
        return "Real Estate"

    @classmethod
    def command(cls):
        return "rea"

    @classmethod
    def mentioned_by(cls):
        return [WorkRequest]


@dataclass
class Destination(Model):
    name: str = field(
        default="",
        metadata={"pretty_name": "Name", "required": True},
    )
    country: str = field(
        default="",
        metadata={"pretty_name": "Country", "required": True},
    )

    def short_name(self):
        return f"{self.id}. {self.country}"

    @classmethod
    def command(cls):
        return "dst"

    @classmethod
    def mentioned_by(cls):
        return [Employee, Contractor, RealEstate]
