from src.ui.real_estate_ui import RealEstateMenu, RealEstateSearch
from src.ui.common_menus import BackQuitMenu


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