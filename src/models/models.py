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
class BaseWorkRequest:
    id: Id
    real_estate: str
    mobile_number: str
    address: str


@dataclass
class Employee(BaseEmployee):
    phone_number: str
    email_address: str
    workplace: Id

@dataclass
class WorkRequest(BaseWorkRequest):
    phone_number: str
    email_address: str
    workplace: Id