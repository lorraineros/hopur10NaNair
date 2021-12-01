import json

from ..models.models import WorkRequest


FILE_PATH = "data/WorkRequest.json"


class WorkRequestStorage:
    @staticmethod
    def get(id: int):
        with open(FILE_PATH, encoding="utf-8") as file:
            data = json.load(file)
            print("This is the work request storage")
            print(data[id])

    @staticmethod
    def get_all():
        with open(FILE_PATH, 'r', encoding="utf-8", ) as file:
            data = json.load(file)
            return [WorkRequest.from_dict(work) for work in data]

    def add(entity: WorkRequest):
        pass
