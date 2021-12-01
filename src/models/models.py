from dataclasses import dataclass
import json
from typing import Dict, Any
import dataclasses


@dataclass
class Id:
    value: int

@dataclass
class Model:
    id: Id

    @classmethod
    def from_dict(cls, dictionary: Dict[str, Any]):
        return cls(**dictionary)

@dataclass
class BaseEmployee(Model):
    name: str
    home_address: str
    phone: str
    


@dataclass
class Employee(BaseEmployee):
    gsm: str
    email: str
    work_destination: Id


@dataclass
class WorkRequest(Model):
    title: str
    location: str
    real_estate: str
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

@dataclass
class Contractor(BaseEmployee):
    name_of_contact: str
    working_hours: str
    location: str
