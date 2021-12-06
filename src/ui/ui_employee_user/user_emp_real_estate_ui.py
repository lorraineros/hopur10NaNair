from src.ui.real_estate_ui import RealEstateMenu, RealEstateSearch
from src.ui.common_menus import BackQuitMenu
from src.logic.logic_api import LogicAPI


class RealEstateMenuUserEmp(RealEstateMenu):
    def show(self):
        '''This function shows the menur for Real Estate'''
        print("--- Real Estate Menu ---")
        print("1. Find a real estate")
        print("2. Display list of real estate")
        print("b. Back")
        print("q. Quit")

    def handle_input(self, command):
        if command == "1":
            return RealEstateSearchUserEmp()
        elif command == "2":
            yes_no_input = input("Do you want to display a list of real estate by destination (Y/N)? ")
            is_yes_no = LogicAPI().yes_no_check(yes_no_input)

            while not is_yes_no:
                print("Sorry, did not understand that, try again.")
                yes_no_input = input("Do you want to display a list of real estate by destination (Y/N)? ")
                is_yes_no = LogicAPI().yes_no_check(yes_no_input)
            print()

            if yes_no_input.upper() == "Y":
                self.display_real_estate_by_dest()
            elif yes_no_input.upper() == "N":
                self.display_all_real_estate()
                
            return BackQuitMenu()
        elif command == "b":
            return "back"
        elif command == "q":
            return "quit"

class RealEstateSearchUserEmp(RealEstateSearch):
    def show(self):
        return super().show()

    def handle_input(self, command):
        if command == "1":
            print(f"{'--- Find Real Estate by ID ---':^52}")
            self.display_all_real_estate()
            print()
            self.find_real_estate_by_id()
            return BackQuitMenu()
        elif command == "2":
            print(f"{'--- Find Real Estate by Real Estate Number ---':^52}")
            self.display_all_real_estate()
            print()
            self.find_real_estate_by_re_num()
            return BackQuitMenu()
        elif command == "3":
            print(f"{'--- Find Real Estate by Address ---':^52}")
            print()
            self.find_real_estate_by_address()
            self.find_real_estate_by_id()
            return BackQuitMenu()
        elif command == "4":
            pass
        elif command == "b":
            return "back"
        elif command == "q":
            return "quit"