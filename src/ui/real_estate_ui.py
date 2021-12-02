from src.ui.abstract_menu import AbstractMenu
from src.logic.real_estate_logic import RealEstateLogic
from src.ui.creation_menu import CreationMenu, EditingMenu
from src.models.models import RealEstate


class RealEstateMenu(AbstractMenu):
    def show(self):
        '''This function shows the menu for Real Estate '''
        print("--- Real Estate Menu ---")
        print("1. Register a new real estate")
        print("2. Find a real estate")
        print("3. Display list of real estate")
        print("b. Back")
        print("q. Quit")

    def handle_input(self, command):
        '''This function handles input for the RealEstateMenu'''
        if command == "1":
            return CreationMenu(RealEstate)
        elif command == "2":
            return RealEstateSearch()
        elif command == "3":
            return RealEstateListMenu()
        elif command == "b":
            return "back"
        elif command == "q":
            return "quit"

    def display_all_real_estate(self):
        '''Display a list of all the real estate'''
        print(f"{'--- List of Real Estate ---':^52}")
        print("-" * 52)
        print(f"| {'ID':^3} | {'Address':^21} | {'Real Estate Number':^18} |")
        print("-" * 52)
        for real_est in RealEstateLogic.get_real_estate_list():
            print(
                f"| {real_est.id:<3} | {real_est.address:<21} | {real_est.real_estate_number:<18} |"
            )
        print("-" * 52)
        print()


class RealEstateListMenu(RealEstateMenu):
    def show(self):
        '''Displays a menu that filters display of real estate list '''
        print("--- Display list of Real Estate ---")
        print("1. All real estate")
        print("2. By address")
        print("3. By destination")
        print("b. Back")
        print("q. Quit")

    def handle_input(self, command):
        '''This function handles input for the RealEstateListMenu'''
        if command == "1":
            self.display_all_real_estate()
            return BackQuitMenu()
        elif command == "2":
            self.display_real_estate_by_address()
            return BackQuitMenu()
        elif command == "3":
            self.display_real_estate_by_dest
            return BackQuitMenu()
        elif command == "b":
            return "back"
        elif command == "q":
            return "quit"

    def display_real_estate_by_address(self):
        '''This function displays a list of real estate filtered by a address, i.e. displays only the real estates by a certain address.'''
        self.print_addresses()
        address_input = input("Enter address to see Real Estate: ")

        is_address = RealEstateLogic.address_check(address_input)

        while not is_address:
            print("Sorry did not find address, try again.")
            address_input = input("Enter address to see Real Estate: ")

            is_address = RealEstateLogic.address_check(address_input)
    
        print(f"{'--- List of Real Estate by Address ---':^52}")
        print("-" * 52)
        print(f"| {'ID':^3} | {'Address':^21} | {'Real Estate Number':^18} |")
        print("-" * 52)
        for real_est in RealEstateLogic.get_real_estate_list():
            if real_est.address.lower() == address_input.lower():
                print(
                    f"| {real_est.id:<3} | {real_est.address:<21} | {real_est.real_estate_number:<18} |"
                )
        print("-" * 52)
        print()
        
    def display_real_estate_by_dest(self):
        '''This function displays a list of real estate filtered by a destination, i.e. displays only the real estates by a certain destination.'''

        pass

    def print_addresses(self):
        '''This function prints all possible addresses that a real estate can have.'''
        list_of_addresses = RealEstateLogic.get_address_list()
        print(f"{'--- List of Addresses ---':^25}")
        print("-" * 25)
        print(f"| {'Addresses':^21} |")
        print("-" * 25)
        for address in list_of_addresses:
            print(
                f"| {address:<21} |"
            )
        print("-" * 25)
        print()
    

class RealEstateSearch(RealEstateMenu):
    def show(self):
        '''Displays a menu that gives option how to search for a Real Estate '''
        print("--- Find a Real Estate ---")
        print("1. By ID")
        print("2. By real estate number")
        print("b. Back")
        print("q. Quit")

    def handle_input(self, command):
        if command == "1":
            self.find_real_estate_by_id()
            return ChangingMenu()
        elif command == "2":
            self.find_real_estate_by_re_num()
            return ChangingMenu()
        elif command == "b":
            return "back"
        elif command == "q":
            return "quit"

    def find_real_estate_by_id(self): # To-Do: Need to create a id_check function.
        '''This function finds the Real Estate given the ID inputed and prints it. '''
        print(f"{'--- Find Real Estate by ID ---':^52}")
        self.display_all_real_estate()
        print()

        id_input = int(input("Enter ID to choose a Real Estate: "))

        is_id = RealEstateLogic.id_check(id_input)

        while not is_id:
            print("Sorry did not find address, try again.")
            id_input = int(input("Enter ID to choose Real Estate: "))

            is_id = RealEstateLogic.id_check(id_input)

        for real_est in RealEstateLogic.get_real_estate_list():
            if real_est.id == id_input:
                print(real_est)

        print()

    def find_real_estate_by_re_num(self):
        '''This function finds the Real Estate given the Real Estate Number inputed and prints it. '''
        print(f"{'--- Find Real Estate by Real Estate Number ---':^52}")
        self.display_all_real_estate()
        print()

        re_num_input = input("Enter ID to choose a Real Estate: ")

        for real_est in RealEstateLogic.get_real_estate_list():
            if real_est.real_estate_number.lower() == re_num_input.lower():
                print(real_est)

        print()


class ChangingMenu(AbstractMenu):
    def show(self):
        '''Menu for changing information.'''
        print("1. Change Infromation")
        print("b. Back")
        print("q. Quit")
    
    def handle_input(self, command):
        '''Handles the input for ChangingMenu'''
        if command == "1":
            # return EditingMenu()
            pass
        elif command == "b":
            return "back"
        elif command == "q":
            return "quit"

class BackQuitMenu(AbstractMenu):
    def show(self):
        '''Menu for only back and quit'''
        print("b. Back")
        print("q. Quit")
    
    def handle_input(self, command):
        '''Handles the input for BackQuitMenu'''
        if command == "b":
            return "back"
        elif command == "q":
            return "quit"

