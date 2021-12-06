from src.ui.employee_ui import EmployeeMenu, FindEmployee
from src.logic.logic_api import LogicAPI
from src.ui.common_menus import BackQuitMenu

class EmployeeMenuUserEmp(EmployeeMenu):
    def show(self):
        print("1. Find an employee")
        print("2. Display list of employees")
        print("b. Back")
        print("q. Quit")

    def handle_input(self, command):
        if command == "1":
            return FindEmployeeUserEmp()
        elif command == "2":
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


class FindEmployeeUserEmp(FindEmployee):
    def show(self):
        return super().show()

    def handle_input(self, command):
        if command == "1":
            print("Find Employee by ID:")
            print()
            self.display_all_employees()
            self.find_employee_by_id()
            return BackQuitMenu()
        elif command == "2":
            print("Find Employee by Destination:")
            print()
            self.display_employees_by_dest()
            self.find_employee_by_id()
            return BackQuitMenu()
        elif command == "b":
            return "back"
        elif command == "q":
            return "quit"
