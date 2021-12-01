from ..logic.work_request_logic import WorkRequestLogic


class WorkRequestMenu:
    def show(self):
        print("--- Work Request Menu ---")
        print("1. Register a new work request")
        print("2. Find work request")
        print("b. Back")
        print("q. Quit")

    def handle_input(self, command):
        if command == "1":
            #return CreationMenu(models.WorkRequest)
            pass
        elif command == "2":
            return FindWorkRequestMenu()
        elif command == "b":
            return "back"
        elif command == "q":
            return "quit"


class FindWorkRequestMenu:
    def show(self):
        print("--- Find Work Request Menu ---")
        print("1. By ID")
        print("2. By real estate")
        print("3. By employee")
        print("4. By contractor")
        print("5. By date")
        print("6. By period")
        print("b. Back")
        print("q. Quit")

    def handle_input(self, command):
        if command == "1":
            return FindWorkByID()
        elif command == "2":
            return FindWorkByRealEstate()
        elif command == "3":
            return FindWorkByEmployee()
        elif command == "4":
            return FindWorkByContractor()
        elif command == "5":
            return FindWorkByDate()
        elif command == "6":
            return FindWorkByPeriod()
        elif command == "b":
            return "back"
        elif command == "q":
            return "quit"


class FindWorkByID:
    def show(self):
        print(f"{'--- Find Work Request by ID ---':^52}")
        print("-"*52)
        print(f"| {'ID':^2} | {'Title':^43} |")
        print("-"*52)
        for work in WorkRequestLogic.get_list():
            print(f"| {work.id:<2} | {work.title:<43} |")
        print("-"*52)
        id = int(input("Enter id to choose a work request: "))

        print("-"*52)
        print(f"| {'ID':^2} | {'Title':^43} |")
        print("-"*52)
        for work in WorkRequestLogic.get_list():
            if work.id == id:
                print(f"| {work.id:<2} | {work.title:<43} | ")
        print("-"*52)

    def handle_input(self, command):
        if command == "b":
            return "back"
        elif command == "q":
            return "quit"
        else:
            print("Invalid ID\n")
            return "back"

class FindWorkByRealEstate:
    def show(self):
        print("--- Find Work Request by Real Estate ---")
        print("-"*46)
        print(f"| {'Real estate':^40} | {'Title':^43} |")
        print("-"*46)
        for work in WorkRequestLogic.get_list():
            print(f"| {work.real_estate:<40} | {work.title:<43} |")
        print("-"*46)
        inp = str(input("Choose a work request: "))

    def handle_input(self, command):
        if command == "b":
            return "back"
        elif command == "q":
            return "quit"

class FindWorkByEmployee:
    def show(self):
        print("--- Find Work Request by Employee ---")
        print("\n(Display list of work requests)\n")
        inp = input("Choose a work request: ")

    def handle_input(self, command):
        if command == "b":
            return "back"
        elif command == "q":
            return "quit"

class FindWorkByContractor:
    def show(self):
        print("--- Find Work Request by Contractor ---")
        print("\n(Display list of work requests)\n")
        inp = input("Choose a work request: ")

    def handle_input(self, inp):
        if inp == "b":
            return "back"
        elif inp == "q":
            return "quit"

class FindWorkByDate:
    def show(self):
        print("--- Find Work Request by Date ---")
        print("\n(Display list of work requests)\n")
        inp = input("Choose a work request: ")

    def handle_input(self, command):
        if command == "b":
            return "back"
        elif command == "q":
            return "quit"

class FindWorkByPeriod:
    def show(self):
        print("--- Find Work Request by Period ---")
        print("\n(Display list of work requests)\n")
        inp = input("Choose a work request: ")

    def handle_input(self, command):
        if command == "b":
            return "back"
        elif command == "q":
            return "quit"