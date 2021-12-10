from src.models.models import Contractor
from src.ui.abstract_menu import SimpleMenu
from src.ui.creation_menu import CreationMenu
from src.ui.list_menu import EditPickerMenu


class ContractorMenu(SimpleMenu):
    '''The Menu for Contractor'''

    @property
    def header(self):
        return "--- Contractor Menu ---"

    @property
    def options(self):
        if self.is_manager:
            return [
                ("Register a new contractor", CreationMenu, Contractor),
                ("List of contractors", EditPickerMenu, Contractor),
            ]
        else:
            return [("List of contractors", EditPickerMenu, Contractor)]

    def name(self):
        return f"Contractor Menu"
