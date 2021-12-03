from src.logic.real_estate_logic import RealEstateLogic
from src.storage.storage import StorageAPI
from ..storage.employee_storage import EmployeeStorage
from src.models.models import Model


class LogicAPI:
    def __init__(self):
        self.storage = StorageAPI()

    def create(self, model: Model):
        pass

    def employee_list(self):
        return EmployeeStorage().get_all()

    def real_estate_list():
        return RealEstateLogic().get_real_estate_list()

    def address_list():
        return RealEstateLogic().get_address_list()

    def address_check(address_input):
        return RealEstateLogic().address_check(address_input)

    def id_check(id_input):
        return RealEstateLogic().id_check(id_input)

    def re_num_check(re_num_input):
        return RealEstateLogic().re_num_check(re_num_input)