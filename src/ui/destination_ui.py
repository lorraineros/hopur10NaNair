from src.logic.logic_api import LogicAPI
from src.models.models import Destination
from src.ui.abstract_menu import AbstractMenu, SimpleMenu
from src.ui.common_menus import BackQuitMenu
from src.ui.creation_menu import CreationMenu
from src.ui.list_menu import EditPickerMenu


class DestinationMenu(SimpleMenu):
    """This class controls destination menu"""
    @property
    def header(self):
        return "--- Destination Menu ---"

    @property
    def options(self):
        if self.is_manager:
            return [
                ("Register a new destination", CreationMenu, Destination),
                ("List of destinations", EditPickerMenu, Destination)
            ]
        else:
            return[
                ("List of destinations", EditPickerMenu, Destination)
            ]
    
    def name(self):
        return f"Destination Menu"

#     def show(self):
#         print(
#             """
# --- Destination Menu ---
# 1. Register a new destination   
# 2. List of all destinations 

# q. Quit
# b. Back
#         """
#         )

#     def handle_input(self, command):
#         """This function handles input for AbstractMenu"""

#         if command == "1":
#             return CreationMenu(Destination)
#         elif command == "2":
#             return EditPickerMenu(Destination)
#         elif command == "b":
#             return "back"
#         elif command == "q":
#             return "quit"

    # def list_of_all_destinations(self):
    #     """This function handles input for list of all destinations"""
    #     print(f"{'--- List of Destinations ---':^51}")
    #     print("-" * 51)
    #     print(f"| {'ID':^2} | {'Name':^21} | {'Country':^18} |")
    #     print("-" * 51)
    #     for (dest_id, destination) in LogicAPI().get_all(Destination).items():
    #         print(
    #             f"| {destination.id:<2} | {destination.name:<21} | {destination.country:<18} |"
    #         )
    #     print("-" * 51)
    #     print()
