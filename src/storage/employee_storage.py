import json

from ..models.models import Employee

FILE_PATH = "data/Employee.json"


class EmployeeStorage:
    @staticmethod
    def get(id: int):
        print("get")
        with open(FILE_PATH, encoding="utf-8") as file:
            data = json.load(file)
            print(data[id])

    @staticmethod
    def get_all():
        with open(FILE_PATH, 'r', encoding="utf-8", ) as file:
            data = json.load(file)
            return [Employee.from_dict(emp) for emp in data]

    def add(entity: Employee):
        pass
