import dataclasses
from copy import deepcopy
from typing import Dict, List, Optional, Type

from src.logic.filters import AbstractFilter
from src.models.models import M, Model, WorkReport, WorkRequest
from src.storage.storage import StorageAPI
from src.utilities.singleton import Singleton


class LogicAPI(metaclass=Singleton):
    def __init__(self):
        self.storage = StorageAPI()

    def get(self, model: Type[M], id: int) -> M:
        return self.storage.get(model, id)

    def get_a_that_references_b(self, a: Type[M], b: M) -> Optional[M]:
        for field in dataclasses.fields(a):
            ref = field.metadata.get("id")
            if ref and ref() == type(b):
                for (i, ays) in self.get_all(a).items():
                    if getattr(ays, field.name) == b.id:
                        return ays
                break
        return None

    def get_new(self, model: Type[M]) -> M:
        return model(id=self.storage.next_id(model))

    def get_all(self, model: Type[M]) -> Dict[int, M]:
        return self.storage.get_all(model)

    def get_filtered(self, model: Type[M], filters: List[AbstractFilter]) -> List[M]:
        result = list(self.get_all(model).values())
        for filt in filters:
            result = [entity for entity in result if filt(entity)]
        return result

    def set(self, entity: Model) -> bool:
        # check if required fields are all set
        for field in dataclasses.fields(entity):
            if not bool(getattr(entity, field.name)) and field.metadata.get("required"):
                return False
        if isinstance(entity, WorkRequest):
            print("its a workreq")
            current_date = entity.start_date
            while current_date < entity.end_date:
                new_entity = deepcopy(entity)
                # for field in dataclasses.fields(entity):
                #     if field.metadata.get("initializer"):
                new_entity.id = 0
                new_entity.date = current_date

                print(f"adding {new_entity}")
                self.storage.set(new_entity)
                current_date += entity.repeat_period
        else:
            self.storage.set(entity)
        return True

    def flush_to_disk(self):
        self.storage.flush_to_disk()

    def is_a_locked_work_request(self, entity) -> bool:
        if isinstance(entity, WorkRequest):  # if entity is a work request
            work_report = LogicAPI().get_a_that_references_b(
                WorkReport,
                entity,
            )  # get the work report that references it
            return bool(work_report) and work_report.done  # check if it's done
        return False
