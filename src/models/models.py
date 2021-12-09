import datetime
from abc import abstractmethod
from dataclasses import dataclass, field
from typing import Any, Dict, TypeVar

M = TypeVar("M")


@dataclass
class Id:
    idx: int = 0
    model: str = ""

    def __bool__(self):
        return bool(self.idx) or bool(self.model)


@dataclass
class Model:
    id: int = field(
        default=int(), 
        metadata={"autoinit": True, "required": True}
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


@dataclass
class BaseEmployee(Model):
    name: str = field(
        default="", 
        metadata={"pretty_name": "Name", "required": True}
        )
    phone: str = field(
        default="", 
        metadata={"pretty_name": "Phone number", "required": True}
        )

    def short_name(self):
        return self.name


@dataclass
class Employee(BaseEmployee):
    home_address: str = field( # Why are there two home_address?
        default="", 
        metadata={"required": True}
        ) 
    password: str = field(
        default="", 
        metadata={"pretty_name": "Password", "required": True}
        )
    gsm: str = field(
        default="", 
        metadata={"pretty_name": "GSM"}
        )
    email: str = field(
        default="", 
        metadata={"pretty_name": "Email"}
        )
    is_manager: bool = field(
        default=False, 
        metadata={"pretty_name": "Is Employee a Manager? ", "required": True}
        )
    home_address: str = field(
        default="", 
        metadata={"pretty_name": "Home Address", "required": True}
        )
    work_destination: int = field(
        default=int(), 
        metadata={"pretty_name": "Location","id": lambda: Destination}
        )

    def __post_init__(self):
        self.is_manager = bool(self.is_manager)


@dataclass
class Contractor(BaseEmployee):
    name_of_company: str = field(
        default="", 
        metadata={"pretty_name": "Name Of Company", "required": True}
        )
    working_hours: str = field(
        default="", 
        metadata={"pretty_name": "Working Hours"}
        )
    location: int = field(
        default=0, 
        metadata={"pretty_name": "Location"}
        )


@dataclass
class WorkRequest(Model):
    title: str = field(
        default="", 
        metadata={"pretty_name": "Title", "required": True}
        )
    location: str = field(
        default="", 
        metadata={"pretty_name": "Location", "required": True}
        )
    real_estate: int = field(
        default=0, 
        metadata={"pretty_name": "Real Estate", "required": True, "id": lambda: RealEstate},
        )
    date: datetime.date = field(
        default=datetime.date.today(), 
        metadata={"pretty_name": "Date", "required": True}
        )
    priority: str = field(
        default="", 
        metadata={"pretty_name": "Priority"}
        )
    is_open: bool = field(
        default=True, 
        metadata={"pretty_name": "Is it Open?", "required": True}
        )
    description: str = field(
        default="", 
        metadata={"pretty_name": "Description", "required": True}
        )

    def __post_init__(self):
        if not isinstance(self.date, datetime.date):
            self.date = datetime.date.fromisoformat(self.date)

    @classmethod
    def model_name(cls):
        return "Work request"

    def short_name(self):
        return self.title


@dataclass
class WorkReport(Model):
    work_request_id: int = field(
        default=int(), 
        metadata={"pretty_name": "Work Request ID", "required": True, "id": lambda: WorkRequest, "employee_can_edit": True}
        )
    employee_id: int = field(
        default=int(), 
        metadata={"pretty_name": "Employee ID", "required": True, "id": lambda: Employee, "employee_can_edit": True},
        )
    contractor_id: int = field(
        default=int(), 
        metadata={"pretty_name": "Contractor ID", "id": lambda: Contractor, "employee_can_edit": True}
        )
    contractors_fee: str = field(
        default="", 
        metadata={"pretty_name": "Contractor's fee", "employee_can_edit": True}
        )
    description: str = field(
        default="", 
        metadata={"pretty_name": "Description", "employee_can_edit": True}
        )
    material_cost: str = field(
        default="", 
        metadata={"pretty_name": "Material cost", "employee_can_edit": True}
        )
    done: bool = field(
        default=False, 
        metadata={"pretty_name": "Done", "employee_can_edit": True}
        )
    comment: str = field(
        default="", 
        metadata={"pretty_name": "Comment"}
        )
    # TODO: consider removal vvv
    date: datetime.datetime = field(default=datetime.datetime.now()) # <<< TODO: consider removal 
    # TODO: consider removal ^^^

    @classmethod
    def model_name(cls):
        return "Work report"


@dataclass
class RealEstate(Model):
    address: str = field(
        default="", 
        metadata={"pretty_name": "Address", "required": True}
        )
    real_estate_number: str = field(
        default="", 
        metadata={"pretty_name": "Real Estate Number", "required": True}
        )
    destination: int = field(
        default=int(), 
        metadata={"pretty_name": "Destination", "id": lambda: Destination},
        )
    condition: str = field(
        default="", 
        metadata={"pretty_name": "Condition"}
        )
    facilities: str = field(
        default="", 
        metadata={"pretty_name": "Facilities"}
        )
    type_of_real_estate: str = field(
        default="", 
        metadata={"pretty_name": "Type of Real Estate"}
        )
    rooms: int = field(
        default=0, 
        metadata={"pretty_name": "Rooms"}
        )
    size: int = field(
        default=0, 
        metadata={"pretty_name": "Size"}
        )

    @classmethod
    def model_name(cls):
        return "Real Estate"

    def short_name(self):
        return self.address


@dataclass
class Destination(Model):
    name: str = field(
        default="", 
        metadata={"pretty_name": "Name", "required": True}
        )
    country: str = field(
        default="", 
        metadata={"pretty_name": "Country", "required": True}
    )

    def short_name(self):
        return self.name

