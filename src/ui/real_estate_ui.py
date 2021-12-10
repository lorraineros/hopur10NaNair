from src.models.models import RealEstate
from src.ui.abstract_menu import SimpleMenu
from src.ui.creation_menu import CreationMenu
from src.ui.list_menu import EditPickerMenu


class RealEstateMenu(SimpleMenu):
    @property
    def header(self):
        return "--- Real Estate Menu ---"
    
    @property
    def options(self):
        if self.is_manager:
            return [
                ("Register a new real estate", CreationMenu, RealEstate),
                ("List of real estate", EditPickerMenu, RealEstate),
            ]
        else:
            return[
                ("List of real estate", EditPickerMenu, RealEstate)
            ]

    def name(self):
        return f"Real Estate Menu"
