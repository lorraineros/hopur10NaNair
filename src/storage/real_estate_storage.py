import json
import pathlib

from ..models.models import RealEstate


FILE_PATH = "data/RealEstate.json"


class RealEstateStorage:
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
            return [RealEstate.from_dict(emp) for emp in data]

    def add(entity: RealEstate):
        pass
