from dataclasses import dataclass, field
import json
from typing import Dict, Any, MutableSet, TypeVar
import dataclasses
import datetime
M = TypeVar("M")


@dataclass
class Id:
    idx: int = 0
    model: str = ""

    def __bool__(self):
        return bool(self.idx) or bool(self.model)


@dataclass
class Model:
    id: Id = field(default=Id(), metadata={"autoinit": True})

    @classmethod
    def from_dict(cls, dictionary: Dict[str, Any]):
        return cls(**dictionary)


@dataclass
class BaseEmployee(Model):
    name: str = field(default="")
    phone: str = field(default="")


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
    work_destination: Id = field(default=Id())


def id_validator(string: str):
    if string.isdigit():
        return True
    else:
        print("Invalid ID")

def date_validator(string: str):
    day, month, year = string.split('-')
    isValidDate = True
    try:
        datetime.datetime(int(year), int(month), int(day))
    except ValueError:
        isValidDate = False
    if(isValidDate):
        return
    else:
        print("Input date is not valid..")

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


@dataclass
class WorkReport(Model):
    work_request_id: Id = field(default=Id())
    employee_id: Id = field(default=Id())
    contractor_id: Id = field(default=Id())
    contractors_fee: str = field(default="")
    description: str = field(default="")
    material_cost: str = field(default="")
    date: str = field(default="")
    ready: bool = field(default=False)
    comment: str = field(default="")


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
    destination: Id = field(default=Id())

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
    id: Id = field(default=Id())
    name: str = field(default="", metadata={"pretty_name": "Name", "required": True})
    country: str = field(
        default="", metadata={"pretty_name": "Country", "required": True}
    )

    def __str__(self):
        return """
        Id: {}
        Name: {} 
        """.format(
            self.id, self.name
        )
