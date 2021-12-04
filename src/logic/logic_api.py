from src.logic.destination_logic import DestinationLogic
from src.logic.contractor_logic import ContractorLogic
from src.logic.real_estate_logic import RealEstateLogic
from src.storage.storage import StorageAPI
from src.utilities.singleton import Singleton
from ..storage.employee_storage import EmployeeStorage
from src.models.models import Model


class LogicAPI(metaclass=Singleton):
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

    def real_estate_id_check(real_estate_id_input):
        return RealEstateLogic().id_check(real_estate_id_input)

    def re_num_check(re_num_input):
        return RealEstateLogic().re_num_check(re_num_input)

    def contractor_list():
        return ContractorLogic().get_list()

    def contractor_id_check(contractor_id_input):
        return ContractorLogic().id_check(contractor_id_input)

    def dest_check(dest_input):
        return DestinationLogic().dest_check(dest_input)
