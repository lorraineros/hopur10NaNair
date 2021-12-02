
from src.logic.destination_logic  import DestinationLogic


# python3 -m src.main

class DestinationMenu:
    def __init__(self):
        self.options = """
        ---Destination Menu---
        1. List of all destinations 
        2. Change destination information  
        3. Add new Destination
        4. Delete destination 
        """

    def draw_options(self):
        print(self.options)
        self.user_input()

    def user_input(self):
        while True:
            print()
            command = input("> ")
            if command == '1':
                self.list_destinations()
            elif command == '2':
                 self.change_destination_info()
            elif command == '3':
                 self.add_destination()
            elif command == '4':
                 self.delete_destination()
            else:
                print("Invalid option, try again!")

    def list_destinations(self):
        print(f"{'--- List of Destinations ---':^52}")
        print("-" * 52)
        print(f"| {'ID':^3} | {'Name':^21} | ")
        print("-" * 52)
        for destination in DestinationLogic.get_destination_list():
            print(
                f"| {destination.id:<3} | {destination.name:<21} |"
            )


    def change_destination_info(self):
        print("--- Change destination Information ---")


    def add_destination(self):
        print("--- Add a new Destination ---")

    def delete_destination(self):
        print("--- Delete Destination ---")
