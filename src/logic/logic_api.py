from typing import Dict, List, Type, TypeVar
from src.logic.employee_logic import EmployeeLogic
from src.logic.destination_logic import DestinationLogic
from src.logic.contractor_logic import ContractorLogic
from src.logic.real_estate_logic import RealEstateLogic
from src.logic.work_request_logic import WorkRequestLogic
from src.storage.storage import StorageAPI
from src.utilities.singleton import Singleton
from ..storage.employee_storage import EmployeeStorage
from src.models.models import M, Model


class LogicAPI(metaclass=Singleton):
    def __init__(self):
        self.storage = StorageAPI()

    def get(self, model: Type[M], id: int) -> M:
        return self.storage.get(model, id)

    def get_all(self, model: Type[M]) -> Dict[int, M]:
        return self.storage.get_all(model)

    def create(self, model: Model):
        self.storage.create(model)

    def flush_to_disk(self):
        self.storage.flush_to_disk()

    def employee_list(self):
        return EmployeeStorage().get_all()

    def address_list(self):
        return RealEstateLogic().get_address_list()

    def address_check(self, address_input):
        return RealEstateLogic().address_check(address_input)

    def real_estate_id_check(self, real_estate_id_input):
        return RealEstateLogic().id_check(real_estate_id_input)

    def re_num_check(self, re_num_input):
        return RealEstateLogic().re_num_check(re_num_input)

    def contractor_id_check(self, contractor_id_input):
        return ContractorLogic().id_check(contractor_id_input)

    def dest_check(self, dest_input):
        return DestinationLogic().dest_check(dest_input)
    
    def employee_id_check(self, employee_id):
        return EmployeeLogic().id_check(employee_id)
    
    def work_id_check(self, work_id):
        return WorkRequestLogic().id_check(work_id)

    def yes_no_check(self, yes_no_input):
        return EmployeeLogic().yes_no_check(yes_no_input)
