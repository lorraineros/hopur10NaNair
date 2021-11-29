import json

from ..models.models import Employee


FILE_PATH = "data/Employee.json"


class EmployeeStorage:
    @staticmethod
    def get(id: int):
        with open(FILE_PATH, encoding="utf-8") as file:
            data = json.load(file)
            print("This is the employee storage")
            print(data[id])

    @staticmethod
    def get_all():
        pass

    def add(entity: Employee):
        pass
