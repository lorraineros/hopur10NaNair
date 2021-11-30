#from ..logic.real_estate_logic import RealEstateLogic
#from ..ui.ui import CreationMenu


class RealEstateMenu:
    def show(self):
        print("--- Real Estate Menu ---")
        print("1. Register a new real estate")
        print("2. Find a real estate")
        print("3. Display list of real estate")
        print("b. Back")
        print("q. Quit")

    def handle_input(self, command):
        if command == "1":
            pass
        elif command == "2":
            return RealEstateSearch()
        elif command == "3":
            return RealEstateListMenu()
        elif command == "b":
            return "back"
        elif command == "q":
            return "quit"


class RealEstateListMenu:
    def show(self):
        print("--- List of Real Estate ---")
        #print(RealEstateLogic.get_list())
        print()
        print("b. Back")
        print("q. Quit")

    def handle_input(self, command):
        if command == "b":
            return "back"
        elif command == "q":
            return "quit"


class RealEstateSearch:
    def show(self):
        print("--- Find a Real Estate ---")
        #print(RealEstateLogic.get_list())
        print()
        inp = input("Choose a real estate from list: ")

    def handle_input(self, inp):
        pass

