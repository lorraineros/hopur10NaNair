from dataclasses import dataclass, field
import json
from typing import Dict, Any
import dataclasses


@dataclass
class Id:
    value: int


@dataclass
class Model:
    id: Id = field(metadata={"autoinit": True})

    @classmethod
    def from_dict(cls, dictionary: Dict[str, Any]):
        return cls(**dictionary)


@dataclass
class BaseEmployee(Model):
    name: str
    phone: str


@dataclass
class Employee(BaseEmployee):
    home_address: str
    password: str
    gsm: str
    email: str
    is_manager: bool
    home_address: str
    work_destination: Id


@dataclass
class WorkRequest(Model):
    title: str
    location: str
    real_estate: str
    employee: int
    contractor: int
    start_date: str
    end_date: str
    description: str
    priority: str
    repeated_work: int


@dataclass
class RealEstate(Model):
    address: str
    real_estate_number: str
    condition: str
    facilities: str
    type_of_real_estate: str
    rooms: int
    size: int
    destination: Id

    def __str__(self):
        str = """ 
Address: {}        
Real Estate Number: {}
Condition: {}
Facilities: {}
Type of Real Estate: {}
Rooms: {}
Size: {} """.format(self.address, self.real_estate_number, self.condition, self.facilities, self.type_of_real_estate,
                    self.rooms, self.size)
        return str


@dataclass
class Contractor(BaseEmployee):
    name_of_contact: str
    working_hours: str
    location: int

    def __str__(self):
        str = """
ID: {}
Name: {}
Name of contact: {}
Phone number: {}
Working hours: {}
Location: {}""".format(self.id, self.name, self.name_of_contact, self.phone, self.working_hours, self.location)
        return str

@dataclass
class Destination(Model):
    id: Id
    name: str
    country: str

    def __str__(self):
        str = """
        Id: {}
        Name: {} 
        """. format(self.id, self.name)
        return str