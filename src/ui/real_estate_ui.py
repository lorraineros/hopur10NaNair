from src.ui.abstract_menu import AbstractMenu
from src.logic.real_estate_logic import RealEstateLogic
from src.ui.creation_menu import CreationMenu, EditingMenu
from src.models.models import RealEstate


class RealEstateMenu(AbstractMenu):
    def show(self):
        print("--- Real Estate Menu ---")
        print("1. Register a new real estate")
        print("2. Find a real estate")
        print("3. Display list of real estate")
        print("b. Back")
        print("q. Quit")

    def handle_input(self, command):
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
        print("--- Display list of Real Estate ---")
        print("1. All real estate")
        print("2. By address")
        print("3. By destination")
        print("b. Back")
        print("q. Quit")

    def handle_input(self, command):
        if command == "1":
            self.display_all_real_estate()
            return BackMenu()
        elif command == "2":
            self.display_real_estate_by_address()
            return BackMenu()
        elif command == "3":
            self.display_real_estate_by_dest
            return BackMenu()
        elif command == "b":
            return "back"
        elif command == "q":
            return "quit"

    def display_real_estate_by_address(self):
        self.print_addresses()
        address_input = input("Enter address to see Real Estate: ")

        is_address = self.address_check(address_input)

        while not is_address:
            self.print_addresses()
            print("Sorry did not find address, try again.")
            address_input = input("Enter address to see Real Estate: ")

            is_address = self.address_check(address_input)

    
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
        pass

    def print_addresses(self):
        list_of_addresses = []
        print(f"{'--- List of Addresses ---':^25}")
        print("-" * 25)
        print(f"| {'Addresses':^21} |")
        print("-" * 25)
        for real_est in RealEstateLogic.get_real_estate_list():
            if real_est.address not in list_of_addresses:
                list_of_addresses.append(real_est.address)        
                print(
                    f"| {real_est.address:<21} |"
                )
        print("-" * 25)
        print()
    
    def address_check(self, address_input):
        list_of_addresses = []
        for real_est in RealEstateLogic.get_real_estate_list():
            if real_est.address not in list_of_addresses:
                list_of_addresses.append(real_est.address)
        
        if address_input in list_of_addresses:
            return True
        else:
            return False


class RealEstateSearch(RealEstateMenu):
    def show(self):
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

    def find_real_estate_by_id(self):
        print(f"{'--- Find Real Estate by ID ---':^52}")
        self.display_all_real_estate()
        print()

        id_input = int(input("Enter ID to choose a Real Estate: "))

        for real_est in RealEstateLogic.get_real_estate_list():
            if real_est.id == id_input:
                print(real_est)

        print()

    def find_real_estate_by_re_num(self):
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
        print("1. Change Infromation")
        print("b. Back")
        print("q. Quit")
    
    def handle_input(self, command):
        if command == "1":
            # return EditingMenu()
            pass
        elif command == "b":
            return "back"
        elif command == "q":
            return "quit"

class BackMenu(AbstractMenu):
    def show(self):
        print("b. Back")
        print("q. Quit")
    
    def handle_input(self, command):
        if command == "b":
            return "back"
        elif command == "q":
            return "quit"

