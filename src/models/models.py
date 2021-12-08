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
    id: int = field(default=int(), metadata={"autoinit": True, "required": True})

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
    name: str = field(default="", metadata={"required": True})
    phone: str = field(default="", metadata={"required": True})

    def short_name(self):
        return self.name


@dataclass
class Employee(BaseEmployee):
    home_address: str = field(default="", metadata={"required": True})
    password: str = field(
        default="", metadata={"pretty_name": "Password", "required": True}
    )
    gsm: str = field(default="", metadata={"pretty_name": "Gsm", "required": False})
    email: str = field(default="", metadata={"pretty_name": "Email", "required": False})
    is_manager: bool = field(default=False)
    home_address: str = field(
        default="", metadata={"pretty_name": "Home Address", "required": True}
    )
    work_destination: int = field(
        default=int(), metadata={"id": True, "model": lambda: Destination}
    )






@dataclass
class WorkRequest(Model):
    title: str = field(default="", metadata={"pretty_name": "Title", "required": True})
    location: str = field(
        default="", metadata={"pretty_name": "Location", "required": True}
    )
    real_estate: str = field(
        default="", metadata={"pretty_name": "Real Estate", "required": True}
    )
    start_date: datetime.date = field(
        default="", metadata={"pretty_name": "Start Date", "required": False}
    )
    end_date: str = field(
        default="", metadata={"pretty_name": "End Date", "required": False}
    )
    description: str = field(
        default="", metadata={"pretty_name": "Description", "required": True}
    )
    priority: str = field(
        default="", metadata={"pretty_name": "Priority", "required": False}
    )
    repeated_work: str = field(
        default="none", metadata={"pretty_name": "Repeat", "required": False}
    )
    repeated_work: datetime.timedelta = field(default=datetime.timedelta(days=7))
    is_open: bool = field(default=True)

    @classmethod
    def model_name(cls):
        return "Work request"

    def short_name(self):
        return self.title


@dataclass
class WorkReport(Model):
    work_request_id: int = field(
        default=int(), metadata={"id": True, "model": lambda: WorkRequest}
    )
    employee_id: int = field(
        default=int(), metadata={"id": True, "model": lambda: Employee}
    )
    contractor_id: int = field(
        default=int(), metadata={"id": True, "model": lambda: Contractor}
    )
    contractors_fee: str = field(
        default="", metadata={"pretty_name": "Contractor's fee", "required": False}
    )
    description: str = field(
        default="", metadata={"pretty_name": "Description", "required": False}
    )
    material_cost: str = field(
        default="", metadata={"pretty_name": "Material cost", "required": False}
    )
    date: str = field(default="")
    ready: bool = field(default=False)
    comment: str = field(default="")

    @classmethod
    def model_name(cls):
        return "Work report"


@dataclass
class RealEstate(Model):
    address: str = field(
        default="", metadata={"pretty_name": "Address", "required": True}
    )
    real_estate_number: str = field(
        default="", metadata={"pretty_name": "Real Estate Number", "required": True}
    )
    condition: str = field(
        default="", metadata={"pretty_name": "Condition", "required": False}
    )
    facilities: str = field(
        default="", metadata={"pretty_name": "Facilities", "required": False}
    )
    type_of_real_estate: str = field(
        default="", metadata={"pretty_name": "Type of Real Estate", "required": False}
    )
    rooms: int = field(default=0)
    size: int = field(default=0)
    destination: int = field(
        default=int(), metadata={"id": True, "model": lambda: WorkRequest}
    )

    def short_name(self):
        return self.address

    def __str__(self):
        return """
Address: {}        
Real Estate Number: {}
Condition: {}
Facilities: {}
Type of Real Estate: {}
Rooms: {}
Size: {} """.format(
            self.address,
            self.real_estate_number,
            self.condition,
            self.facilities,
            self.type_of_real_estate,
            self.rooms,
            self.size,
        )


@dataclass
class Contractor(BaseEmployee):
    name_of_contact: str = field(
        default="", metadata={"pretty_name": "Name Of Contact", "required": True}
    )
    working_hours: str = field(
        default="", metadata={"pretty_name": "Location", "required": True}
    )
    location: int = field(default=0)

    def __str__(self):
        return """
ID: {}
Name: {}
Name of contact: {}
Phone number: {}
Working hours: {}
Location: {}""".format(
            self.id,
            self.name,
            self.name_of_contact,
            self.phone,
            self.working_hours,
            self.location,
        )


@dataclass
class Destination(Model):
    name: str = field(default="", metadata={"pretty_name": "Name", "required": True})
    country: str = field(
        default="", metadata={"pretty_name": "Country", "required": True}
    )

    def short_name(self):
        return self.name

    def __str__(self):
        return """
        Id: {}
        Name: {} 
        """.format(
            self.id, self.name
        )
