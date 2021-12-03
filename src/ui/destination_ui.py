
from src.ui.abstract_menu import AbstractMenu
from src.logic.destination_logic import DestinationLogic
from src.ui.creation_menu import CreationMenu
from src.models.models import Destination


class DestinationMenu(AbstractMenu):
    def show(self):
        '''This function shows the menu for Real Estate '''
        print("--- Destination ---")
        print("1. List of all destinations")
        print("2. Add new Destination")
        print("3. Delete Destination")
        print("b. Back")
        print("q. Quit")

    def handle_input(self, command):
        '''This function handles input for the RealEstateMenu'''
        if command == "1":
            pass
        elif command == "2":
            pass
        elif command == "3":
            pass
        elif command == "b":
            return "back"
        elif command == "q":
            return "quit"

    # def user_input(self):
    #     while True:
    #         print()
    #         command = input("> ")
    #         print()
    #         if command == '1':
    #             self.list_destinations()
    #         elif command == '2':
    #             pass
    #             # return CreationMenu(Destination)
    #         elif command == '3':
    #             self.delete_destination()
    #         elif command == "b":
    #             return "back"
    #         elif command == "q":
    #             return "quit"
    #         else:
    #             print("Invalid option, try again!")

    def list_destinations(self):
        print(f"{'--- List of Destinations ---':^34}")
        print("-" * 54)
        print(f"| {'ID':^3} | {'Name':^21} | {'Country':^18} ")
        print("-" * 52)
        for destination in DestinationLogic.get_destination_list():
            print(
                f"| {destination.id:<3} | {destination.name:<21} | {destination.country:<18} |"
            )

    def delete_destination(self):
        print("""
        --- Delete a Destination ---
        1. By ID   
        2. By Name  

        q. Quit
        b. Back
                """)
