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
    mobile_number: str
    address: str


@dataclass
class Employee(BaseEmployee):
    phone_number: str
    email_address: str
    workplace: Id


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
class RealEstate:
    id: Id
    address: str
    real_estate_number: str
    condition: str
    facilities: str
    type_of_real_estate: str
    rooms: int
    size: int