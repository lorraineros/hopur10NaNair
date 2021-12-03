
from src.storage.destination_storage import DestinationStorage


class DestinationLogic:
    def get_destination_list(self):
        return DestinationStorage.get_all()

    def get_address_list(self):
        '''Gets a list of addresses for all real estate'''
        list_of_addresses = []
        for dest in DestinationLogic.get_destination_list():
            if dest.address not in list_of_addresses:
                list_of_addresses.append(dest.address)

        return list_of_addresses

    def address_check(address_input):
        '''Checks if the address that was inputed is valid.'''
        list_of_addresses = DestinationLogic.get_address_list()

        if address_input in list_of_addresses:
            return True
        else:
            return False

    def id_check(id_input):
        '''Checks if the ID that was inputed is valid.'''
        for dest in DestinationLogic.get_destination_list():
            if str(dest.id) == str(id_input):
                return True
        return False

