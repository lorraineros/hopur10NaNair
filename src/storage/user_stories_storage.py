import json

from ..models.models import UserStories

FILE_PATH = "data/User_stories.json"


class User_stories_Storage:
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
            return [UserStories.from_dict(emp) for emp in data]

    def add(entity: UserStories):
        pass
