

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


