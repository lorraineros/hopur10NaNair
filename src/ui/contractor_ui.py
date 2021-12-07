from src.logic.logic_api import LogicAPI
from src.models.models import Contractor, Destination
from src.ui.abstract_menu import AbstractMenu
from src.ui.common_menus import BackQuitMenu, ChangingMenu
from src.ui.creation_menu import CreationMenu


class ContractorMenu(AbstractMenu):
    def show(self):
        print("1. Register a new contractor")
        print("2. Find a contractor")
        print("3. Display list of contractors")
        print("b. Back")
        print("q. Quit")

    def handle_input(self, command):
        if command == "1":
            return CreationMenu(Contractor)
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
        print(f"| {'ID':^3} | {'Name':^16} | {'Location':^16} |")
        print("-" * 45)
        for (contr_id, contr) in LogicAPI().get_all(Contractor).items():
            contr_location = LogicAPI().get(Destination, contr.location)
            print(f"| {contr.id:<3} | {contr.name:<16} | {contr_location.name:<16} |")
        print("-" * 45)
        print()

    def find_contractor(self):
        id_input = input("Enter ID to choose a contractor: ")
        is_id = LogicAPI().contractor_id_check(id_input)

        while not is_id:
            print("Sorry did not find address, try again.")
            id_input = input("Enter ID to choose a contractor: ")
            is_id = LogicAPI().contractor_id_check(id_input)

        contr = LogicAPI().get(Contractor, int(id_input))
        self.print_contractor(contr)
        print()

    def print_contractor(self, contr):
        contr_location = LogicAPI().get(Destination, contr.location)
        print(
            """
ID: {}
Name: {}
Name of Contact: {}
Phone Number: {}
Working hours: {}
Location: {}
        """.format(
                contr.id,
                contr.name,
                contr.name_of_contact,
                contr.phone,
                contr.working_hours,
                contr_location.name,
            )
        )
