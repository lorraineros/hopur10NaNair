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
