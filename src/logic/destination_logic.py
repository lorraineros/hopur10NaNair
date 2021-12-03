
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


