
from src.storage.destination_storage import DestinationStorage


class DestinationLogic:
    def get_destination_list():
        return DestinationStorage.get_all()

    def dest_check(self, dest_input):
        for dest in DestinationLogic.get_destination_list():
            if str(dest.id) == str(dest_input):
                return True
        return False



