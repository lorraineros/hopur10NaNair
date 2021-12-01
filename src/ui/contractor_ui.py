from ..logic.contractor_logic import ContractorLogic

class ContractorMenu:
    def show(self):
        print("1. Register a new contractor")
        print("2. Find a contractor")
        print("3. Display list of contractors")
        print("b. Back")
        print("q. Quit")

    def handle_input(self ,command):
        if command == "1":
            return CreationMenu(models.Contractor)
        elif command == "2":
            pass 
        elif command == "3":
            return ContractorMenu()
        elif command == "b":
            return "back"
        elif command == "q":
            return "quit"


class ContractorListMenu:
    def show(self):
        print(f"{'--- List of Contractor ---':^61}")
        print("-"*61)
        print(f"| {'ID':^3} | {'Name':^21} | {'Name of contact':^27} | {'Mobile_number':^27} | {'Working hours':^27} | {'Location':^27} |")
        print("-"*61)
        for contr in ContractorLogic.get_list():
            print(f"| {contr.id:<3} | {contr.name:<21} | {contr.email:<27} |")
        print("-"*61)
        print()
        print("b. Back")
        print("q. Quit")

    def handle_input(self, command):
        if command == "b":
            return "back"
        elif command == "q":
            return "quit"

