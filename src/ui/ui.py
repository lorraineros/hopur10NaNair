import os
from typing import List

from src.logic.logic_api import LogicAPI
from src.ui.abstract_menu import AbstractMenu, SimpleMenu
from src.ui.common_menus import BackQuitMenu, ChangingMenu

from ..ui.contractor_ui import ContractorMenu
from ..ui.destination_ui import DestinationMenu
from ..ui.employee_ui import EmployeeMenu
from ..ui.real_estate_ui import RealEstateMenu
from ..ui.work_request_ui import WorkRequestMenu


class App:
    def __init__(self):
        self.logic = LogicAPI()
        self.stack: List[AbstractMenu] = [MainMenu()]

    def run(self):
        while True:
            # if type(self.stack[-1]) == type(ChangingMenu()) or type(self.stack[-1]) == type(BackQuitMenu()):
            #     pass
            # else:
            #     os.system("cls" if os.name == "nt" else "clear")
            self.stack[-1].show()
            print()
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
            else:
                print("I did not understand that dave, try again")
                print()


class MainMenu(SimpleMenu):
    is_root = True

    @property
    def header(self):
        return """
        _   _       _   _      _    _
       | \ | | __ _| \ | |    / \  (_)_ __
       |  \| |/ _` |  \| |   / _ \ | | '__|
       | |\  | (_| | |\  |  / ___ \| | |
       |_| \_|\__,_|_| \_| /_/   \_\_|_|

--------------- Welcome to NaN Air ---------------
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
