import json
import pathlib

from ..models.models import Contractor


FILE_PATH = "data/Contractor.json"


class ContractorStorage:
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
            return [Contractor.from_dict(contr) for contr in data]

    def add(entity: Contractor):
        pass
