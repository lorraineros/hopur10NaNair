import json
from typing import Dict, Type

from src.models.models import Model
from src.utilities.singleton import Singleton


class StorageAPI(metaclass=Singleton):
    # def __init__(self):
    #     self.storages: Dict[Type[Model], str] = {
    #         Contractor: "data/Contractor.json",
    #         Employee: "data/Employee.json",
    #     }

    def get(self, model: Type[Model], id: int):
        with open(f"data/{model.__name__}.json", encoding="utf-8") as file:
            data = json.load(file)
            print("This is the work request storage")
            return model.from_dict(data[id])

    def get_all(self, model: Type[Model]):
        with open(f"data/{model.__name__}.json", encoding="utf-8") as file:
            data = json.load(file)
            return [model.from_dict(entity) for entity in data]
