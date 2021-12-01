from ..logic.work_request_logic import WorkRequestLogic
from ..logic.employee_logic import EmployeeLogic


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
        self.print_list()
        id = int(input("\nEnter id to choose a work request: "))
        self.print_filtered_list(id)
        print()
        print("b. Back")
        print("q. Quit")
        edit = input("\nDo you want to edit work request (Y/N)? ")
        

    def handle_input(self, command):
        if command == "b":
            return "back"
        elif command == "q":
            return "quit"
        else:
            print("Invalid ID\n")
            return "back"

    def print_list(self):
        print("-"*52)
        print(f"| {'ID':^2} | {'Title':^43} |")
        print("-"*52)
        for work in WorkRequestLogic.get_list():
            print(f"| {work.id:<2} | {work.title:<43} |")
        print("-"*52)

    def print_filtered_list(self,id):
        print("-"*52)
        print(f"| {'ID':^2} | {'Title':^43} |")
        print("-"*52)
        for work in WorkRequestLogic.get_list():
            if work.id == id:
                print(f"| {work.id:<2} | {work.title:<43} | ")
        print("-"*52)
        
class FindWorkByRealEstate:
    def show(self):
        print(f"{'--- Find Work Request by Real Estate ---':^78}")
        self.print_list()
        real_est = input("\nEnter real estate to choose a work request: ")
        self.print_filtered_list(real_est)
        print()
        print("b. Back")
        print("q. Quit")

    def handle_input(self, command):
        if command == "b":
            return "back"
        elif command == "q":
            return "quit"
    
    def print_list(self):
        print("-"*78)
        print(f"| {'Real estate':^28} | {'Title':^43} |")
        print("-"*78)
        for work in WorkRequestLogic.get_list():
            print(f"| {work.real_estate:<28} | {work.title:<43} |")
        print("-"*78)

    def print_filtered_list(self, real_est):
        print("-"*78)
        print(f"| {'Real estate':^28} | {'Title':^43} |")
        print("-"*78)
        for work in WorkRequestLogic.get_list():
            if work.real_estate.lower() == real_est.lower():
                print(f"| {work.real_estate:<28} | {work.title:<43} |")
        print("-"*78)

class FindWorkByEmployee:
    def show(self):
        print(f"{'--- Find Work Request by Employee ---':^72}")
        self.print_list()
        emp_id = int(input("\nEnter employee id to choose a work request:  "))
        self.print_filtered_list(emp_id)
        print()
        print("b. Back")
        print("q. Quit")

    def handle_input(self, command):
        if command == "b":
            return "back"
        elif command == "q":
            return "quit"

    def print_list(self):
        print("-"*72)
        print(f"| {'Employee':^22} | {'Title':^43} |")
        print("-"*72)
        for work in WorkRequestLogic.get_list():
            for emp in EmployeeLogic.get_list():
                if work.employee == emp.id:
                    print(f"| {work.employee:<2} | {emp.name:<17} | {work.title:<43} |")
        print("-"*72)
    
    def print_filtered_list(self, emp_id):
        print("-"*72)
        print(f"| {'Employee':^22} | {'Title':^43} |")
        print("-"*72)
        for work in WorkRequestLogic.get_list():
            for emp in EmployeeLogic.get_list():
                if work.employee == emp.id == emp_id:
                    print(f"| {work.employee:<2} | {emp.name:<17} | {work.title:<43} |")
        print("-"*72)

class FindWorkByContractor:
    def show(self):
        print("--- Find Work Request by Contractor ---")
        print("\n(Display list of work requests)\n")
        inp = input("\nEnter contractor to choose a work request: ")

    def handle_input(self, inp):
        if inp == "b":
            return "back"
        elif inp == "q":
            return "quit"

class FindWorkByDate:
    def show(self):
        print("--- Find Work Request by Date ---")
        print("\n(Display list of work requests)\n")
        inp = input("Enter date to choose a work request: ")

    def handle_input(self, command):
        if command == "b":
            return "back"
        elif command == "q":
            return "quit"

class FindWorkByPeriod:
    def show(self):
        print("--- Find Work Request by Period ---")
        print("\n(Display list of work requests)\n")
        inp = input("Enter period to choose a work request: ")

    def handle_input(self, command):
        if command == "b":
            return "back"
        elif command == "q":
            return "quit"