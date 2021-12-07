from src.ui.contractor_ui import ContractorMenu
from src.ui.common_menus import BackQuitMenu


class ContractorMenuUserEmp(ContractorMenu):
    def show(self):
        print("1. Find a contractor")
        print("2. Display list of contractors")
        print("b. Back")
        print("q. Quit")

    def handle_input(self, command):
        if command == "1":
            self.display_all_contractors()
            self.find_contractor()
            return BackQuitMenu()
        elif command == "2":
            self.display_all_contractors()
            return BackQuitMenu()
        elif command == "b":
            return "back"
        elif command == "q":
            return "quit"