from src.models.models import Employee
from src.ui.abstract_menu import AbstractMenu
from src.ui.creation_menu import CreationMenu
from ..logic.employee_logic import EmployeeLogic


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
            pass
        elif command == "3":
            return EmployeeListMenu()
        elif command == "b":
            return "back"
        elif command == "q":
            return "quit"


class EmployeeListMenu(AbstractMenu):
    def show(self):
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
