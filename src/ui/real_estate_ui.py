from src.ui.abstract_menu import AbstractMenu
from ..logic.real_estate_logic import RealEstateLogic


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
            pass
        elif command == "2":
            return RealEstateSearch()
        elif command == "3":
            return RealEstateListMenu()
        elif command == "b":
            return "back"
        elif command == "q":
            return "quit"


class RealEstateListMenu(AbstractMenu):
    def show(self):
        print(f"{'--- List of Real Estate ---':^52}")
        self.print_list()
        print()
        print("b. Back")
        print("q. Quit")

    def handle_input(self, command):
        if command == "b":
            return "back"
        elif command == "q":
            return "quit"

    def print_list(self):
        print("-" * 52)
        print(f"| {'ID':^3} | {'Address':^21} | {'Real Estate Number':^18} |")
        print("-" * 52)
        for real_est in RealEstateLogic.get_list():
            print(
                f"| {real_est.id:<3} | {real_est.address:<21} | {real_est.real_estate_number:<18} |"
            )
        print("-" * 52)


class RealEstateSearch(AbstractMenu):
    def show(self):
        print("--- Find a Real Estate ---")
        print("1. By ID")
        print("2. By address")
        print("3. By destination")
        print("4. By real estate number")
        print("b. Back")
        print("q. Quit")

    def handle_input(self, command):
        if command == "1":
            return FindRealEstateByID()
        elif command == "2":
            return FindRealEstateByAddress()
        elif command == "3":
            return FindRealEstateByDest()
        elif command == "4":
            return FindRealEstateByRENum()
        elif command == "b":
            return "back"
        elif command == "q":
            return "quit"


class FindRealEstateByID(RealEstateListMenu):
    def show(self):
        print(f"{'--- Find Real Estate by ID ---':^52}")
        self.print_list()
        print()
        id_input = int(input("Enter ID to choose a Real Estate: "))

        self.print_list_by_id(id_input)
        print("b. Back")
        print("q. Quit")

    def print_list_by_id(self, id_input):
        print("-" * 52)
        print(f"| {'ID':^3} | {'Address':^21} | {'Real Estate Number':^18} |")
        print("-" * 52)
        for real_est in RealEstateLogic.get_list():
            if real_est.id == id_input:
                print(
                    f"| {real_est.id:<3} | {real_est.address:<21} | {real_est.real_estate_number:<18} |"
                )
        print("-" * 52)


class FindRealEstateByAddress(RealEstateListMenu):
    def show(self):
        print(f"{'--- Find Real Estate by Address ---':^52}")
        self.print_list()
        print()
        address_input = input("Enter address to see Real Estate: ")

        self.print_list_by_address(address_input)
        print("b. Back")
        print("q. Quit")

    def print_list_by_address(self, address_input):
        print("-" * 52)
        print(f"| {'ID':^3} | {'Address':^21} | {'Real Estate Number':^18} |")
        print("-" * 52)
        for real_est in RealEstateLogic.get_list():
            if real_est.address.lower() == address_input.lower():
                print(
                    f"| {real_est.id:<3} | {real_est.address:<21} | {real_est.real_estate_number:<18} |"
                )
        print("-" * 52)


class FindRealEstateByDest(RealEstateListMenu):
    def show(self):
        print(f"{'--- Find Real Estate by Destination ---':^52}")
        self.print_list()
        print()
        print("b. Back")
        print("q. Quit")


class FindRealEstateByRENum(RealEstateListMenu):
    def show(self):
        print(f"{'--- Find Real Estate by Real Estate Number ---':^52}")
        self.print_list()
        print()
        renum_input = input("Enter Real Estate Number to choose Real Estate: ")

        self.print_list_by_renum(renum_input)
        print("b. Back")
        print("q. Quit")

    def print_list_by_renum(self, renum_input):
        print("-" * 52)
        print(f"| {'ID':^3} | {'Address':^21} | {'Real Estate Number':^18} |")
        print("-" * 52)
        for real_est in RealEstateLogic.get_list():
            if real_est.real_estate_number.lower() == renum_input.lower():
                print(
                    f"| {real_est.id:<3} | {real_est.address:<21} | {real_est.real_estate_number:<18} |"
                )
        print("-" * 52)
