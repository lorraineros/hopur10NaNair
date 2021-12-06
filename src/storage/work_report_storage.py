import json

from ..models.models import WorkReport


FILE_PATH = "data/WorkReport.json"


class WorkReportStorage:
    @staticmethod
    def get(id: int):
        with open(FILE_PATH, encoding="utf-8") as file:
            data = json.load(file)
            print("This is the work report storage")
            print(data[id])

    @staticmethod
    def get_all():
        with open(FILE_PATH, 'r', encoding="utf-8", ) as file:
            data = json.load(file)
            return [WorkReport.from_dict(work) for work in data]

    def add(entity: WorkReport):
        pass