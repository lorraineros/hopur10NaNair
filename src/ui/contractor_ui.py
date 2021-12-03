from src.logic.logic_api import LogicAPI
from src.ui.abstract_menu import AbstractMenu
from ..logic.contractor_logic import ContractorLogic
from src.ui.common_menus import BackQuitMenu, ChangingMenu


class ContractorMenu(AbstractMenu):
    def show(self):
        print("1. Register a new contractor")
        print("2. Find a contractor")
        print("3. Display list of contractors")
        print("b. Back")
        print("q. Quit")

    def handle_input(self, command):
        if command == "1":
            # return CreationMenu(models.Contractor)
            pass
        elif command == "2":
            self.display_all_contractors()
            self.find_contractor()
            return ChangingMenu()
        elif command == "3":
            self.display_all_contractors()
            return BackQuitMenu()
        elif command == "b":
            return "back"
        elif command == "q":
            return "quit"

    def display_all_contractors(self):
        print(f"{'--- List of Contractor ---':^45}")
        print("-" * 45)
        print(
            f"| {'ID':^3} | {'Name':^16} | {'Location':^16} |"
        )
        print("-" * 45)
        for contr in LogicAPI.contractor_list():
            print(f"| {contr.id:<3} | {contr.name:<16} | {contr.location:<16} |")
        print("-" * 45)
        print()

    def find_contractor(self):
        id_input = input("Enter ID to choose a contractor: ")
        is_id = LogicAPI.contractor_id_check(id_input)

        while not is_id:
            print("Sorry did not find address, try again.")
            id_input = input("Enter ID to choose a contractor: ")
            is_id = LogicAPI.contractor_id_check(id_input)

        for contr in LogicAPI.contractor_list():
            if contr.id == int(id_input):
                print(contr)

        print()


