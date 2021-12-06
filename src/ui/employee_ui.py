from src.logic.employee_logic import EmployeeLogic
from src.logic.logic_api import LogicAPI
from src.models.models import Destination, Employee
from src.ui.abstract_menu import AbstractMenu
from src.ui.creation_menu import CreationMenu
from src.ui.common_menus import BackQuitMenu, ChangingMenu
from src.ui.destination_ui import DestinationMenu


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
            yes_no_input = input("Do you want to display a list of employees by destination (Y/N)? ")
            is_yes_no = LogicAPI().yes_no_check(yes_no_input)

            while not is_yes_no:
                print("Sorry, did not understand that, try again.")
                yes_no_input = input("Do you want to display a list of employees by destination (Y/N)? ")
                is_yes_no = LogicAPI().yes_no_check(yes_no_input)

            if yes_no_input.upper() == "Y":
                self.display_employees_by_dest()
            elif yes_no_input.upper() == "N":
                self.display_all_employees()
            
            return BackQuitMenu()
        elif command == "b":
            return "back"
        elif command == "q":
            return "quit"

    def display_all_employees(self):
        print(f"{'--- List of Employee ---':^61}")
        print("-" * 61)
        print(f"| {'ID':^3} | {'Name':^21} | {'Email':^27} |")
        print("-" * 61)
        for (emp_id, emp) in LogicAPI().get_all(Employee).items():
            print(f"| {emp.id:<3} | {emp.name:<21} | {emp.email:<27} |")
        print("-" * 61)
        print()

    def print_emp(self,emp):
        print("""
Name: {}
Home address: {}
Work Location: {}
Position: {}
Phone: {}
GSM: {}
Email: {}
        """.format(
            emp.name,
            emp.home_address,
            emp.work_destination,
            emp.is_manager,
            emp.phone,
            emp.gsm,
            emp.email
        ))

    def display_employees_by_dest(self):
        DestinationMenu().list_of_all_destinations()
        dest_input = input("Enter Destination ID to filter Employees: ")
        is_dest = LogicAPI().dest_check(dest_input)

        while not is_dest:
            print("Sorry did not find Destination ID, try again.")
            dest_input = input("Enter Destination ID to filter Employees: ")
            is_dest = LogicAPI().dest_check(dest_input)

        dest = LogicAPI().get(Destination, int(dest_input))

        print()
        print(f"{'--- List of Employees by {} ---':^61}".format(dest.name))
        print("-" * 61)
        print(f"| {'ID':^3} | {'Name':^21} | {'Email':^27} |")
        print("-" * 61)
        for (emp_id, emp) in LogicAPI().get_all(Employee).items():
            if emp.work_destination == int(dest_input):
                print(
                    f"| {emp.id:<3} | {emp.name:<21} | {emp.email:<27} |"
                )
        print("-" * 61)
        print()

class FindEmployee(EmployeeMenu):
    def show(self):
        print("--- Find an Employee ---")
        print("1. By ID")
        print("2. By destination")
        print("b. Back")
        print("q. Quit")

    def handle_input(self, command):
        if command == "1":
            print("Find Employee by ID:")
            print()
            self.display_all_employees()
            self.find_employee_by_id()
            return ChangingMenu()
        elif command == "2":
            print("Find Employee by Destination:")
            print()
            self.display_employees_by_dest()
            self.find_employee_by_id()
            return ChangingMenu()
        elif command == "b":
            return "back"
        elif command == "q":
            return "quit"

    def find_employee_by_id(self):
        id_input = input("Enter id to choose an employee: ")
        is_id = LogicAPI().employee_id_check(id_input)

        while not is_id:
            print("Sorry did not find employee, try again.")
            id_input = input("Enter id to choose an employee: ")
            is_id = LogicAPI().employee_id_check(id_input)
        
        emp = LogicAPI().get(Employee, int(id_input))
        self.print_emp(emp)

# class EmployeeListMenu(AbstractMenu):
#     def show(self):
#         dest = input("Do you want to display a list of employees by destination (Y/N)?")
#         if dest.upper() == "Y":
#             print(f"{'--- List of Employee ---':^50}")
#             print("-" * 50)
#             print(f"| {'ID':^3} | {'Name':^21} | {'Destination':^16} |")
#             print("-" * 50)
#             for (emp_id, emp) in LogicAPI().get_all(Employee).items():
#                 dest = LogicAPI().get(Destination, emp.work_destination)
#                 if dest:
#                     print(
#                         f"| {emp.id:<3} | {emp.name:<21} | {dest.id}. {dest.country:<14}|"
#                     )
#             print("-" * 50)
#             print()
#             print("b. Back")
#             print("q. Quit")
#         else:
#             print(f"{'--- List of Employee ---':^61}")
#             print("-" * 61)
#             print(f"| {'ID':^3} | {'Name':^21} | {'Email':^27} |")
#             print("-" * 61)
#             for emp in EmployeeLogic.get_list():
#                 print(f"| {emp.id:<3} | {emp.name:<21} | {emp.email:<27} |")
#             print("-" * 61)
#             print()
#             print("b. Back")
#             print("q. Quit")

#     def handle_input(self, command):
#         if command == "b":
#             return "back"
#         elif command == "q":
#             return "quit"


# class FindEmployee(EmployeeMenu):
#     def show(self):
#         print(f"{'--- Find an employee ---':^29}")
#         self.print_list()
#         id = int(input("\nEnter id to choose an employee: "))
#         self.print_filtered_list(id)
#         print()
#         print("b. Back")
#         print("q. Quit")
#         edit = input("\nDo you want to edit the employee (Y/N)? ")

#     def print_list(self):
#         print("-" * 29)
#         print(f"| {'ID':^2} | {'Employee':^20} |")
#         print("-" * 29)
#         for emp in EmployeeLogic.get_list():
#             print(f"| {emp.id:<2} | {emp.name:<20} |")
#         print("-" * 29)

#     def print_filtered_list(self, id):
#         print("-" * 78)
#         print(f"| {'ID':^2} | {'Employee':^20} | {'Email':^28} | {'GSM':^15} |")
#         print("-" * 78)
#         for emp in EmployeeLogic.get_list():
#             if emp.id == id:
#                 print(
#                     f"| {emp.id:<2} | {emp.name:<20} |  {emp.email:<27} | {emp.gsm:<15} |"
#                 )
#         print("-" * 78)

