from ..storage.real_estate_storage import RealEstateStorage


class RealEstateLogic:
    def get_real_estate_list():
        return RealEstateStorage.get_all()

    def get_address_list():
        '''Gets a list of addresses for all real estate'''
        list_of_addresses = []
        for real_est in RealEstateLogic.get_real_estate_list():
            if real_est.address not in list_of_addresses:
                list_of_addresses.append(real_est.address)
        
        return list_of_addresses

    def address_check(address_input):
        '''Checks if the address that was inputed is valid.'''
        list_of_addresses = RealEstateLogic.get_address_list()
        
        if address_input in list_of_addresses:
            return True
        else:
            return False

    def id_check(id_input): # To-Do: Need to make invalid if id_input not int / or have both as str
        '''Checks if the ID that was inputed is valid.'''
        for real_est in RealEstateLogic.get_real_estate_list():
            if int(real_est.id) == id_input:
                return True
        return False