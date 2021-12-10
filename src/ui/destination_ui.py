from src.models.models import Destination
from src.ui.abstract_menu import SimpleMenu
from src.ui.creation_menu import CreationMenu
from src.ui.list_menu import EditPickerMenu


class DestinationMenu(SimpleMenu):
    '''The Menu for Destination'''

    @property
    def header(self):
        return "--- Destination Menu ---"

    @property
    def options(self):
        if self.is_manager:
            return [
                ("Register a new destination", CreationMenu, Destination),
                ("List of destinations", EditPickerMenu, Destination),
            ]
        else:
            return [("List of destinations", EditPickerMenu, Destination)]

    def name(self):
        return f"Destination Menu"


