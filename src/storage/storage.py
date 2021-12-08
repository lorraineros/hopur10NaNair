import json
import dataclasses
from datetime import datetime, date
from typing import Dict, Type

from src.models.models import *
from src.utilities.singleton import Singleton


class StorageAPI(metaclass=Singleton):
    def __init__(self):
        models = [
            Employee,
            Contractor,
            RealEstate,
            Destination,
            WorkReport,
            WorkRequest,
        ]
        self.storages: Dict[Type[Model], Storage] = {
            model: Storage(model) for model in models
        }

    def get(self, model: Type[Model], id: int):
        return self.storages[model].get(id)

    def get_all(self, model: Type[M]) -> Dict[int, M]:
        return self.storages[model].get_all()

    def next_id(self, model: Type[M]):
        return self.storages[model].next_id

    def set(self, entity: Model):
        self.storages[type(entity)].set(entity)

    def flush_to_disk(self):
        for storage in filter(lambda s: s.modified, self.storages.values()):
            storage.store()


class Storage:
    def __init__(self, model: Type[Model]):
        self.model = model
        self.loaded = False
        self.modified = False
        self.file_name = f"new_data/{self.model.__name__}.json"
        self._next_id = 0

        self.data = {}

    @property
    def next_id(self):
        self._ensure_loaded()
        return self._next_id

    def get(self, id: int):
        self._ensure_loaded()
        return self.data[id]

    def get_all(self):
        self._ensure_loaded()
        return self.data

    def set(self, entity: Model):
        self.data[entity.id] = entity
        if self._next_id == entity.id:
            self._next_id += 1
        self.modified = True

    def _ensure_loaded(self):
        if not self.loaded:
            self.load()

    def load(self):
        with open(self.file_name, encoding="utf-8") as file:
            raw_dict = json.load(file)
            self._next_id = raw_dict["next_id"]
            self.data = {
                int(id): self.model.from_dict(v) for (id, v) in raw_dict["data"].items()
            }
        self.loaded = True

    def store(self):
        class IsoDateEncoder(json.JSONEncoder):
            def default(self, obj):
                if isinstance(obj, date):
                    return obj.isoformat()
                return super().default(obj)

        with open(self.file_name, "w", encoding="utf-8") as file:
            json.dump(
                {
                    "next_id": self._next_id,
                    "data": {
                        k: dataclasses.asdict(entity) for k, entity in self.data.items()
                    },
                },
                file,
                indent=" " * 4,
                cls=IsoDateEncoder,
            )
        self.modified = False
