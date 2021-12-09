import os
from typing import List

from src.logic.logic_api import LogicAPI
from src.ui.abstract_menu import AbstractMenu, BasicNavigationMenu, SimpleMenu
from src.ui.utilities import MessageToParent

from ..ui.contractor_ui import ContractorMenu
from ..ui.destination_ui import DestinationMenu
from ..ui.employee_ui import EmployeeMenu
from ..ui.real_estate_ui import RealEstateMenu
from ..ui.work_request_ui import WorkRequestMenu

# from src.ui.ui_employee_user.user_emp_employee_ui import EmployeeMenuUserEmp
# from src.ui.ui_employee_user.user_emp_contractor_ui import ContractorMenuUserEmp
# from src.ui.ui_employee_user.user_emp_real_estate_ui import RealEstateMenuUserEmp
# from src.ui.ui_employee_user.user_emp_work_request_ui import WorkRequestMenuUserEmp


class App:
    def __init__(self):
        self.logic = LogicAPI()
        self.stack: List[AbstractMenu] = [UserControl()]

    def run(self):
        """This function runs the generic menues"""
        os.system("cls" if os.name == "nt" else "clear")
        while True:
            # if type(self.stack[-1]) == type(ChangingMenu()) or type(self.stack[-1]) == type(BackQuitMenu()):
            #     pass
            # else:
            #     os.system("cls" if os.name == "nt" else "clear")

            # Breadcrumb
            print(" -> ".join(menu.name() for menu in self.stack[1:]))
            print()
            self.stack[-1].show()
            print()
            # this handles an issue that occurs with when inputting
            # unicode characters and erasing them
            inp = ""
            while True:
                try:
                    inp = input("> ")
                    break
                except UnicodeDecodeError as e:
                    print(e)
                    continue

            print()
            choice = self.stack[-1].handle_input(inp)
            if choice == "back":
                self.stack.pop()
            elif choice == "quit":
                LogicAPI().flush_to_disk()
                break
            elif choice == "self":
                continue
            elif issubclass(type(choice), AbstractMenu):
                self.stack.append(choice)
            elif type(choice) is MessageToParent:
                self.stack.pop()
                self.stack[-1].message_from_child(choice)
            else:
                self.stack[
                    -1
                ]._user_message += "I did not understand that dave, try again"


class UserControl(BasicNavigationMenu):
    """This class defines userclass"""

    is_root = True

    def show(self):
        print("--- Please choose a user type ---")
        print("1. Manager")
        print("2. Employee")
        print("")
        super().show()

    def handle_input(self, command):
        """This finction handles input for a simple menu"""
        if command == "1":
            self.is_manager = True
            return MainMenu()
        elif command == "2":
            self.is_manager = False
            return MainMenu()
        else:
            return super().handle_input(command)


class MainMenu(SimpleMenu):
    """This class prints the main menu for maneger"""

    is_root = True

    @property
    def header(self):

        if self.is_manager:
            user = "Manager"
        else:
            user = "Employee"
        return f"""
╭──────────────────────────────────────────────────╮
│        _   _       _   _      _    _             │
│       | \ | | __ _| \ | |    / \  (_)_ __        │
│       |  \| |/ _` |  \| |   / _ \ | | '__|       │
│       | |\  | (_| | |\  |  / ___ \| | |          │
│       |_| \_|\__,_|_| \_| /_/   \_\_|_|          │
│                                                  │
│              ╭────────────────────╮              │
│              │ Welcome to NaN Air │              │
│              ├────────────────────┤              │
│              │   User: {user:<9}  │              │
│              ╰────────────────────╯              │
╰──────────────────────────────────────────────────╯
"""

    @property
    def options(self):
        return [
            ("Employee", EmployeeMenu),
            ("Real Estate", RealEstateMenu),
            ("Work request", WorkRequestMenu),
            ("Contractor", ContractorMenu),
            ("Destination", DestinationMenu),
        ]


# class MainMenuUserEmp(SimpleMenu):
#     """This class is the main menu for the employees"""

#     is_root = True

#     @property
#     def header(self):
#         return """
# ╭──────────────────────────────────────────────────╮
# │        _   _       _   _      _    _             │
# │       | \ | | __ _| \ | |    / \  (_)_ __        │
# │       |  \| |/ _` |  \| |   / _ \ | | '__|       │
# │       | |\  | (_| | |\  |  / ___ \| | |          │
# │       |_| \_|\__,_|_| \_| /_/   \_\_|_|          │
# │                                                  │
# │               ╭──────────────────╮               │
# │               │Welcome to NaN Air│               │
# │               ├──────────────────┤               │
# │               │  User: Employee  │               │
# │               ╰──────────────────╯               │
# ╰──────────────────────────────────────────────────╯
# """

#     @property
#     def options(self):
#         return [
#             ("Employee", EmployeeMenuUserEmp),
#             ("Real Estate", RealEstateMenuUserEmp),
#             ("Work request", WorkRequestMenuUserEmp),
#             ("Contractor", ContractorMenuUserEmp),
#         ]
