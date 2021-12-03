from src.ui.employee_ui import EmployeeListMenu, EmployeeMenu, FindEmployee


class EmployeeMenuUserEmp(EmployeeMenu):
    def show(self):
        print("1. Find an employee")
        print("2. Display list of employees")
        print("b. Back")
        print("q. Quit")

    def handle_input(self, command):
        if command == "1":
            return FindEmployee()
        elif command == "2":
            return EmployeeListMenu()
        elif command == "b":
            return "back"
        elif command == "q":
            return "quit"