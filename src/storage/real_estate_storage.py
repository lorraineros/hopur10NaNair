import json

from ..models.models import RealEstate


FILE_PATH = "data/RealEstate.json"


class RealEstateStorage:
    @staticmethod
    def get(id: int):
        with open(FILE_PATH, encoding="utf-8") as file:
            data = json.load(file)
            print("This is the real estate storage")
            print(data[id])

    @staticmethod
    def get_all():
        pass

    def add(entity: RealEstate):
        pass
