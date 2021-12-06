from abc import abstractmethod, abstractproperty
from typing import List
from src.logic.logic_api import LogicAPI
from src.ui.abstract_menu import AbstractMenu, SimpleMenu
from ..ui.real_estate_ui import RealEstateMenu
from ..ui.employee_ui import EmployeeMenu
from ..ui.contractor_ui import ContractorMenu
from ..ui.work_request_ui import WorkRequestMenu
from ..ui.destination_ui import DestinationMenu
#from ..ui.user_stories_ui import UserStoriesMenu
from ..models import models


class App:
    def __init__(self):
        self.logic = LogicAPI()
        self.stack: List[AbstractMenu] = [MainMenu()]

    def run(self):
        while True:
            self.stack[-1].show()
            print()
            inp = input("> ")
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
