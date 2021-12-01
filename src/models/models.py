from dataclasses import dataclass
import json
from typing import Dict, Any
import dataclasses


@dataclass
class Id:
    value: int

class Model:
    @classmethod
    def from_dict(cls, dictionary: Dict[str, Any]):
        return cls(**dictionary)

@dataclass
class BaseEmployee(Model):
    id: Id
    name: str
    home_address: str
    phone_number: str
    


@dataclass
class Employee(BaseEmployee):
    gsm: str
    email: str
    work_destination: Id


@dataclass
class WorkRequest:
    id: Id
    title: str
    location: str
    real_estate: str
    description: str
    priority: str
    repeated_work: int


@dataclass
class RealEstate(Model):
    id: Id
    address: str
    real_estate_number: str
    condition: str
    facilities: str
    type_of_real_estate: str
    rooms: int
    size: int

@dataclass
class Contractor:
    id: Id
    name: str
    name_of_contact: str
    mobile_number: str
    working_hours: str
    location: str