from dataclasses import dataclass, field
import json
from typing import Dict, Any, TypeVar
import dataclasses

M = TypeVar("M")


@dataclass
class Id:
    idx: int = 0
    model: str = ""


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
    home_address: str = field(default="")
    password: str = field(default="")
    gsm: str = field(default="")
    email: str = field(default="")
    is_manager: bool = field(default=False)
    home_address: str = field(default="")
    work_destination: Id = field(default=Id())


@dataclass
class WorkRequest(Model):
    title: str = field(default="")
    location: str = field(default="")
    real_estate: str = field(default="")
    employee: Id = field(default=Id())
    contractor: Id = field(default=Id())
    start_date: str = field(default="")
    end_date: str = field(default="")
    description: str = field(default="")
    priority: str = field(default="")
    repeated_work: int = field(default=0)


@dataclass
class RealEstate(Model):
    address: str = field(default="")
    real_estate_number: str = field(default="")
    condition: str = field(default="")
    facilities: str = field(default="")
    type_of_real_estate: str = field(default="")
    rooms: int = field(default=0)
    size: int = field(default=0)
    destination: Id = field(default=Id())

    def __str__(self):
        return """
Address: {}        
Real Estate Number: {}
Destination: {}
Condition: {}
Facilities: {}
Type of Real Estate: {}
Rooms: {}
Size: {} """.format(
            self.address,
            self.real_estate_number,
            self.destination,
            self.condition,
            self.facilities,
            self.type_of_real_estate,
            self.rooms,
            self.size,
        )


@dataclass
class Contractor(BaseEmployee):
    name_of_contact: str = field(default="")
    working_hours: str = field(default="")
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
    name: str = field(default="")
    country: str = field(default="")

    def __str__(self):
        return """
        Id: {}
        Name: {} 
        Country: {}
        """.format(
            self.id, 
            self.name,
            self.country
        )
