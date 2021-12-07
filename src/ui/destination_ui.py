from src.logic.logic_api import LogicAPI
from src.models.models import Destination
from src.ui.abstract_menu import AbstractMenu
from src.ui.common_menus import BackQuitMenu
from src.ui.creation_menu import CreationMenu


class DestinationMenu(AbstractMenu):
    """This class contrlos destination menu"""

    def show(self):
        print(
            """
--- Destination Menu ---
1. List of all destinations   
2. Add new Destination 

q. Quit
b. Back
        """
        )

    def handle_input(self, command):
        """This function handles input for AbstractMenu"""

        if command == "1":
            self.list_of_all_destinations()
            return BackQuitMenu()
        elif command == "2":
            return CreationMenu(Destination)
        elif command == "b":
            return "back"
        elif command == "q":
            return "quit"

    def list_of_all_destinations(self):
        """This function handles input for list of all destinations"""
        print(f"{'--- List of Destinations ---':^51}")
        print("-" * 51)
        print(f"| {'ID':^2} | {'Name':^21} | {'Country':^18} |")
        print("-" * 51)
        for (dest_id, destination) in LogicAPI().get_all(Destination).items():
            print(
                f"| {destination.id:<2} | {destination.name:<21} | {destination.country:<18} |"
            )
        print("-" * 51)
        print()
