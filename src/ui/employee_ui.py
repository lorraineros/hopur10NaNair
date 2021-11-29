from ..logic.employee_logic import EmployeeLogic


class EmployeeMenu:
    def show(self):
        print("1. Register a new employee")
        print("2. Find an employee")
        print("3. Display list of employees")
        print("b. Back")
        print("q. Quit")

    def handle_input(self, command):
        if command == "1":
            return CreationMenu(models.Employee)
        elif command == "2":
            pass
        elif command == "3":
            return EmployeeListMenu()
        elif command == "b":
            return "back"
        elif command == "q":
            return "quit"


class EmployeeListMenu:
    def show(self):
        print(EmployeeLogic.get_list())
        print()
        print("b. Back")
        print("q. Quit")

    def handle_input(self, command):
        if command == "b":
            return "back"
        elif command == "q":
            return "quit"
