from src.storage.storage import StorageAPI
from ..storage.employee_storage import EmployeeStorage
from src.models.models import Model


class LogicAPI:
    def __init__(self):
        self.storage = StorageAPI()

    def create(self, model: Model):
        pass

    def employee_list(self):
        return EmployeeStorage.get_all()
