from ..storage.contractor_storage import ContractorStorage


class ContractorLogic:

    def get_list(self):
        return ContractorStorage.get_all()

    def id_check(self, id_input): 
        '''Checks if the ID that was inputed is valid.'''
        for contr in self.get_list():
            if str(contr.id) == str(id_input):
                return True
        return False
