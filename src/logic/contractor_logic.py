from src.models.models import Contractor
from src.storage.storage import StorageAPI
from ..storage.contractor_storage import ContractorStorage


class ContractorLogic:

    def id_check(self, id_input): 
        '''Checks if the ID that was inputed is valid.'''
        for (contr_id, contr) in StorageAPI().get_all(Contractor).items():
            if str(contr.id) == str(id_input):
                return True
        return False
