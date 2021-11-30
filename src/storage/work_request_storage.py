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
        pass

    def add(entity: WorkRequest):
        pass
