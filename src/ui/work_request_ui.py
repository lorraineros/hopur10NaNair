from src.logic.contractor_logic import ContractorLogic
from src.ui.abstract_menu import AbstractMenu
from ..logic.work_request_logic import WorkRequestLogic
from ..logic.employee_logic import EmployeeLogic

PRINT_LIST = f"| {'ID':^2} | {'Title':^43} | {'Location':^28} | {'Priority':^20} | {'Repeat':^6} |"

class WorkRequestMenu(AbstractMenu):
    def show(self):
        print("--- Work Request Menu ---")
        print("1. Register a new work request")
        print("2. Find work request")
        print("b. Back")
        print("q. Quit")

    def handle_input(self, command):
        if command == "1":
            # return CreationMenu(models.WorkRequest)
            pass
        elif command == "2":
            return FindWorkRequestMenu()
        elif command == "b":
            return "back"
        elif command == "q":
            return "quit"


class FindWorkRequestMenu(AbstractMenu):
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

class FindWork(AbstractMenu):
    def handle_input(self, command):
        if command == "b":
            return "back"
        elif command == "q":
            return "quit"
        else:
            print("Invalid option\n")
            return "back"

    def print_list(self):
        print("-" * 115)
        print(f"| {'ID':^2} | {'Title':^43} | {'Real estate':^11} |  {'Employee':^19} | {'From':^10} | {'To':^10} |")
        print("-" * 115)
        for work in WorkRequestLogic.get_list():
            for emp in EmployeeLogic.get_list():
                if work.employee == emp.id:
                    print(f"| {work.id:<2} | {work.title:<43} | {work.real_estate:<11} | {emp.id}. {emp.name:<17} | {work.start_date:<7} | {work.end_date:<7} |")
        print("-" * 115)

class FindWorkByID(FindWork):
    def show(self):
        print(f"{'--- Find Work Request by ID ---':^112}")
        self.print_list()
        id = int(input("\nEnter id to choose a work request: "))
        self.print_filtered_list(id)
        print()
        print("b. Back")
        print("q. Quit")
        edit = input("\nDo you want to edit work request (Y/N)? ")

    def handle_input(self, command):
        return super().handle_input(command)

    def print_list(self):
        return super().print_list()

    def print_filtered_list(self, id):
        print("-" * 115)
        print(f"| {'ID':^2} | {'Title':^43} | {'Location':^28} | {'Priority':^20} | {'Repeat':^6} |")
        print("-" * 115)
        for work in WorkRequestLogic.get_list():
            if work.id == id:
                print(f"| {work.id:<2} | {work.title:<43} |  {work.location:<27} | {work.priority:<20} | {work.repeated_work:<6} |")
        print("-" * 115)


class FindWorkByRealEstate(FindWork):
    def show(self):
        print(f"{'--- Find Work Request by Real Estate ---':^78}")
        self.print_list()
        real_est = input("\nEnter real estate to choose a work request: ")
        self.print_filtered_list(real_est)
        print()
        print("b. Back")
        print("q. Quit")

    def handle_input(self, command):
        return super().handle_input(command)

    def print_list(self):
        return super().print_list()

    def print_filtered_list(self, real_est):
        print("-" * 115)
        print(f"| {'ID':^2} | {'Title':^43} | {'Location':^28} | {'Priority':^20} | {'Repeat':^6} |")
        print("-" * 115)
        for work in WorkRequestLogic.get_list():
            if work.real_estate.lower() == real_est.lower():
                print(f"| {work.id:<2} | {work.title:<43} |  {work.location:<27} | {work.priority:<20} | {work.repeated_work:<6} |")
        print("-" * 115)

class FindWorkByEmployee(FindWork):
    def show(self):
        print(f"{'--- Find Work Request by Employee ---':^72}")
        self.print_list()
        emp_id = int(input("\nEnter employee id to choose a work request:  "))
        self.print_filtered_list(emp_id)
        print()
        print("b. Back")
        print("q. Quit")

    def handle_input(self, command):
        return super().handle_input(command)

    def print_list(self):
        return super().print_list()

    def print_filtered_list(self, emp_id):
        print("-" * 115)
        print(f"| {'ID':^2} | {'Title':^43} | {'Location':^28} | {'Priority':^20} | {'Repeat':^6} |")
        print("-" * 115)
        for work in WorkRequestLogic.get_list():
            if work.employee == emp_id:
                print(f"| {work.id:<2} | {work.title:<43} |  {work.location:<27} | {work.priority:<20} | {work.repeated_work:<6} |")
        print("-" * 115)

class FindWorkByContractor(AbstractMenu):
    def show(self):
        print("--- Find Work Request by Contractor ---")
        #self.print_list()
        inp = input("\nEnter contractor to choose a work request: ")

    def handle_input(self, command):
        return super().handle_input(command)
    
    """
    def print_list(self):
        print("-" * 72)
        print(f"| {'Employee':^22} | {'Title':^43} |")
        print("-" * 72)
        for contr in ContractorLogic.get_list():
            print(f"| {contr.name_of_contact:<25} | {contr.name:<30} | {contr.title:<43} |")
        print("-" * 72)

    def print_filtered_list(self, emp_id):
        print("-" * 72)
        print(f"| {'Employee':^22} | {'Title':^43} |")
        print("-" * 72)
        for work in WorkRequestLogic.get_list():
            for emp in EmployeeLogic.get_list():
                if work.employee == emp.id == emp_id:
                    print(f"| {work.employee:<2} | {emp.name:<17} | {work.title:<43} |")
        print("-" * 72)
"""

class FindWorkByDate(FindWork):
    def show(self):
        print("--- Find Work Request by Date ---")
        self.print_list()
        date = input("Enter date to choose a work request: ")
        self.print_filtered_list(date)
        print()
        print("b. Back")
        print("q. Quit")

    def handle_input(self, command):
        return super().handle_input(command)
    
    def print_list(self):
        return super().print_list()

    def print_filtered_list(self, date):
        print("-" * 115)
        print(f"| {'ID':^2} | {'Title':^43} | {'Location':^28} | {'Priority':^20} | {'Repeat':^6} |")
        print("-" * 115)
        for work in WorkRequestLogic.get_list():
            if work.start_date == date or work.end_date == date:
                print(f"| {work.id:<2} | {work.title:<43} |  {work.location:<27} | {work.priority:<20} | {work.repeated_work:<6} |")
        print("-" * 115)

class FindWorkByPeriod(FindWork):
    def show(self):
        print("--- Find Work Request by Period ---")
        self.print_list()
        start_date = input("Enter start date to choose a work request: ")
        end_date = input("Enter end date to choose a work request: ")
        self.print_filtered_list(start_date, end_date)
        print()
        print("b. Back")
        print("q. Quit")

    def handle_input(self, command):
        return super().handle_input(command)

    def print_list(self):
        return super().print_list()

    def print_filtered_list(self, start_date, end_date):
        print("-" * 115)
        print(f"| {'ID':^2} | {'Title':^43} | {'Location':^28} | {'Priority':^20} | {'Repeat':^6} |")
        print("-" * 115)
        for work in WorkRequestLogic.get_list():
            if work.start_date == start_date and work.end_date == end_date:
                print(f"| {work.id:<2} | {work.title:<43} |  {work.location:<27} | {work.priority:<20} | {work.repeated_work:<6} |")
        print("-" * 115)