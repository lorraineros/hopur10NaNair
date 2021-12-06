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

    def create(self, entity: Model):
        self.storages[type(entity)].create(entity)

    def flush_to_disk(self):
        for storage in filter(lambda s: s.modified, self.storages.values()):
            storage.store()


class Storage:
    def __init__(self, model: Type[Model]):
        self.model = model
        self.loaded = False
        self.modified = False
        self.file_name = f"new_data/{self.model.__name__}.json"
        self.next_id = 0

        self.data = {}

    def get(self, id: int):
        self._ensure_loaded()
        return self.data[id]

    def get_all(self):
        self._ensure_loaded()
        return self.data

    def create(self, entity: Model):
        entity.id = self.next_id
        self.data[self.next_id] = entity
        self.next_id += 1
        self.modified = True

    def _ensure_loaded(self):
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
            json.dump(
                {
                    "next_id": self.next_id,
                    "data": {k: dataclasses.asdict(v) for k, v in self.data.items()},
                },
                file,
                indent="    ",
            )
        self.modified = False
