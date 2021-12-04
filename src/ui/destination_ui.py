from src.ui.abstract_menu import AbstractMenu
from src.logic.destination_logic import DestinationLogic
from src.ui.creation_menu import CreationMenu
from src.models.models import Destination
from src.ui.common_menus import BackQuitMenu

class DestinationMenu(AbstractMenu):
    def show(self):
        print("""
--- Destination Menu ---
1. List of all destinations   
2. Add new Destination
3. Delete destination 

q. Quit
b. Back
        """)


    def handle_input(self, command):
            if command == '1':
                self.list_of_all_destinations()
                return BackQuitMenu()
            elif command == '2':
                pass
                # return CreationMenu(Destination)
            elif command == '3':
                self.delete_destination()
            elif command == "b":
                return "back"
            elif command == "q":
                return "quit"


    def list_of_all_destinations(self):
        print(f"{'--- List of Destinations ---':^34}")
        print("-" * 52)
        print(f"| {'ID':^3} | {'Name':^21} | {'Country':^18} ")
        print("-" * 52)
        for destination in DestinationLogic.get_destination_list():
            print(
                f"| {destination.id:<3} | {destination.name:<21} | {destination.country:<18} |"
            )
        print("-" * 52)
        print()

    def delete_destination(self):
        print("""
--- Delete a Destination ---
1. By ID   
2. By Name  

q. Quit
b. Back
                """)
