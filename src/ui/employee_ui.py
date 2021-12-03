from src.models.models import Employee
from src.ui.abstract_menu import AbstractMenu
from src.ui.creation_menu import CreationMenu
from ..logic.employee_logic import EmployeeLogic
from ..logic.destination_logic import DestinationLogic


class EmployeeMenu(AbstractMenu):
    def show(self):
        print("1. Register a new employee")
        print("2. Find an employee")
        print("3. Display list of employees")
        print("b. Back")
        print("q. Quit")

    def handle_input(self, command):
        if command == "1":
            return CreationMenu(Employee)
        elif command == "2":
            return FindEmployee()
        elif command == "3":
            return EmployeeListMenu()
        elif command == "b":
            return "back"
        elif command == "q":
            return "quit"


class EmployeeListMenu(AbstractMenu):
    def show(self):
        dest = input("Do you want to display a list of employees by destination (Y/N)?")
        if dest.upper() == "Y":
            print(f"{'--- List of Employee ---':^50}")
            print("-" * 50)
            print(f"| {'ID':^3} | {'Name':^21} | {'Destination':^16} |")
            print("-" * 50)
            for emp in EmployeeLogic.get_list():
                for dest in DestinationLogic.get_destination_list():
                    if emp.work_destination == dest.id:
                        print(f"| {emp.id:<3} | {emp.name:<21} | {dest.id}. {dest.country:<14}|")
            print("-" * 50)
            print()
            print("b. Back")
            print("q. Quit")
        else:
            print(f"{'--- List of Employee ---':^61}")
            print("-" * 61)
            print(f"| {'ID':^3} | {'Name':^21} | {'Email':^27} |")
            print("-" * 61)
            for emp in EmployeeLogic.get_list():
                print(f"| {emp.id:<3} | {emp.name:<21} | {emp.email:<27} |")
            print("-" * 61)
            print()
            print("b. Back")
            print("q. Quit")

    def handle_input(self, command):
        if command == "b":
            return "back"
        elif command == "q":
            return "quit"

class FindEmployee(EmployeeMenu):
    def show(self):
        print(f"{'--- Find an employee ---':^29}")
        self.print_list()
        id = int(input("\nEnter id to choose an employee: "))
        self.print_filtered_list(id)
        print()
        print("b. Back")
        print("q. Quit")
        edit = input("\nDo you want to edit the employee (Y/N)? ")

    def print_list(self):
        print("-" * 29)
        print(f"| {'ID':^2} | {'Employee':^20} |")
        print("-" * 29)
        for emp in EmployeeLogic.get_list():
            print(f"| {emp.id:<2} | {emp.name:<20} |")
        print("-" * 29)
    
    def print_filtered_list(self, id):
        print("-" * 78)
        print(f"| {'ID':^2} | {'Employee':^20} | {'Email':^28} | {'GSM':^15} |")
        print("-" * 78)
        for emp in EmployeeLogic.get_list():
            if emp.id == id:
                print(f"| {emp.id:<2} | {emp.name:<20} |  {emp.email:<27} | {emp.gsm:<15} |")
        print("-" * 78)
