import json
import pathlib

from ..models.models import Destination

FILE_PATH = "data/Destination.json"


class DestinationStorage:
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
            return [Destination.from_dict(emp) for emp in data]

    def add(entity: Destination):
        pass
