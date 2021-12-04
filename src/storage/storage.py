import json
from typing import Dict, Type

from src.models.models import *
from src.utilities.singleton import Singleton


class StorageAPI(metaclass=Singleton):
    def __init__(self):
        models = [Employee, Contractor, RealEstate, Destination]
        self.storages: Dict[Type[Model], Any] = {
            model: Storage(model) for model in models
        }

    def get(self, model: Type[Model], id: int):
        return self.storages[model].get(id)

    def get_all(self, model: Type[M]) -> Dict[int, M]:
        return self.storages[model].get_all()

    def add(self, entity: Model):
        # TODO
        pass


class Storage:
    def __init__(self, model: Type[Model]):
        self.model = model
        self.loaded = False
        self.modified = False
        self.file_name = f"new_data/{self.model.__name__}.json"

        self.data = {}

    def get(self, id: int):
        self.ensure_loaded()
        return self.data[id]

    def get_all(self):
        self.ensure_loaded()
        return self.data

    def ensure_loaded(self):
        if not self.loaded:
            self.load()

    def load(self):
        with open(self.file_name, encoding="utf-8") as file:
            raw_dict = json.load(file)
            self.next_id = raw_dict["next_id"]
            self.data = {
                int(id): self.model.from_dict(v) for (id, v) in raw_dict["data"].items()
            }
        self.loaded = True

    def store(self):
        with open(self.file_name, "w", encoding="utf-8") as file:
            file.write(json.dumps(self.data))
        self.modified = False
