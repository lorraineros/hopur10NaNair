from dataclasses import dataclass


@dataclass
class Id:
    value: int


@dataclass
class BaseEmployee:
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
    destination: str
    real_estate: str
    description: str
    priority: str
    repeated_work: int


@dataclass
class RealEstate:
    id: Id
    address: str
    type_of_real_estate: str
    size: int
    condition: str
    facilities: str