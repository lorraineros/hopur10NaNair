

from src.models.models import RealEstate
from src.storage.real_estate_storage import RealEstateStorage
from src.storage.storage import StorageAPI


class RealEstateLogic:
    def get_real_estate_list(self):
        return RealEstateStorage.get_all()

    def get_address_list(self):
        '''Gets a list of addresses for all real estate'''
        list_of_addresses = []
        for (real_est_id, real_est) in StorageAPI().get_all(RealEstate).items():
            if real_est.address not in list_of_addresses:
                list_of_addresses.append(real_est.address)
        
        return list_of_addresses

    def address_check(self, address_input):
        '''Checks if the address that was inputed is valid.'''
        list_of_addresses = self.get_address_list()
        
        if address_input in list_of_addresses:
            return True
        else:
            return False

    def id_check(self, id_input): 
        '''Checks if the ID that was inputed is valid.'''
        for (real_est_id, real_est) in StorageAPI().get_all(RealEstate).items():
            if str(real_est.id) == str(id_input):
                return True
        return False

    def re_num_check(self, re_num_input):
        '''Checks if the Real Estate Number that was inputed is valid.'''
        for (real_est_id, real_est) in StorageAPI().get_all(RealEstate).items():
            if real_est.real_estate_number == re_num_input:
                return True
        return False