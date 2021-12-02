
from src.logic.destination_logic  import DestinationLogic


# python3 -m src.main

class DestinationMenu:
    def __init__(self):
        self.options = """
        ---Destination Menu---
        1. List of all destinations   
        2. Add new Destination
        3. Find a Destination
        4. Delete destination 
        
        q. Quit
        b. Back
        """

    def draw_options(self):
        """This shows a Menu """
        print(self.options)
        self.user_input()

    def user_input(self):
        while True:
            print()
            command = input("> ")
            print()
            if command == '1':
                self.list_destinations()
            elif command == '2':
                 self.change_destination_info()
            elif command == '3':
                 self.add_destination()
            elif command == '4':
                 self.delete_destination()
            elif command == "b":
                return "back"
            elif command == "q":
                return "quit"
            else:
                print("Invalid option, try again!")

    def list_destinations(self):
        print(f"{'--- List of Destinations ---':^34}")
        print("-" * 34)
        print(f"| {'ID':^3} | {'Name':^21} | ")
        print("-" * 34)
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
