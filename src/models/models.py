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
