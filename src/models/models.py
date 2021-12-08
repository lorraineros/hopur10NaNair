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
    name: str = field(default="", metadata={"pretty_name": "Name", "required": True})
    phone: str = field(
        default="", metadata={"pretty_name": "Phone number", "required": True}
    )

    def short_name(self):
        return self.name


@dataclass
class Employee(BaseEmployee):
    home_address: str = field(default="", metadata={"required": True})
    password: str = field(
        default="", metadata={"pretty_name": "Password", "required": True}
    )
    gsm: str = field(default="", metadata={"pretty_name": "GSM"})
    email: str = field(default="", metadata={"pretty_name": "Email"})
    is_manager: bool = field(default=False)
    home_address: str = field(
        default="", metadata={"pretty_name": "Home Address", "required": True}
    )
    work_destination: int = field(default=int(), metadata={"id": lambda: Destination})


@dataclass
class Contractor(BaseEmployee):
    name_of_company: str = field(
        default="", metadata={"pretty_name": "Name Of Company", "required": True}
    )
    working_hours: str = field(default="", metadata={"pretty_name": "Working Hours"})
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
class WorkRequest(Model):
    title: str = field(default="", metadata={"pretty_name": "Title", "required": True})
    location: str = field(
        default="", metadata={"pretty_name": "Location", "required": True}
    )
    real_estate: int = field(
        default=0,
        metadata={
            "pretty_name": "Real Estate",
            "required": True,
            "id": lambda: RealEstate,
        },
    )
    # TODO: consider removal vvv
    start_date: datetime.date = field(
        default=datetime.date.today(),
        metadata={"pretty_name": "Start Date"},
    )
    end_date: datetime.date = field(
        default=datetime.date.today(),
        metadata={"pretty_name": "End Date"},
    )
    repeated_work: datetime.timedelta = field(default=datetime.timedelta(days=7))
    # TODO: consider removal ^^^
    description: str = field(
        default="", metadata={"pretty_name": "Description", "required": True}
    )
    priority: str = field(default="", metadata={"pretty_name": "Priority"})
    is_open: bool = field(default=True, metadata={"required": True})

    def __post_init__(self):
        self.start_date = datetime.date.fromisoformat(self.start_date)
        self.end_date = datetime.date.fromisoformat(self.end_date)

    @classmethod
    def model_name(cls):
        return "Work request"

    def short_name(self):
        return self.title


@dataclass
class WorkReport(Model):
    work_request_id: int = field(
        default=int(), metadata={"required": True, "id": lambda: WorkRequest}
    )
    employee_id: int = field(
        default=int(),
        metadata={"required": True, "id": lambda: Employee},
    )
    contractor_id: int = field(default=int(), metadata={"id": lambda: Contractor})
    contractors_fee: str = field(
        default="", metadata={"pretty_name": "Contractor's fee"}
    )
    description: str = field(default="", metadata={"pretty_name": "Description"})
    material_cost: str = field(default="", metadata={"pretty_name": "Material cost"})
    # TODO: consider removal vvv
    date: datetime.datetime = field(default=datetime.datetime.now())
    # TODO: consider removal ^^^
    done: bool = field(default=False)
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
    destination: int = field(
        default=int(),
        metadata={"pretty_name": "Destination", "id": lambda: Destination},
    )
    condition: str = field(default="", metadata={"pretty_name": "Condition"})
    facilities: str = field(default="", metadata={"pretty_name": "Facilities"})
    type_of_real_estate: str = field(
        default="", metadata={"pretty_name": "Type of Real Estate"}
    )
    rooms: int = field(default=0, metadata={"pretty_name": "Rooms"})
    size: int = field(default=0, metadata={"pretty_name": "Size"})

    @classmethod
    def model_name(cls):
        return "Real Estate"

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
