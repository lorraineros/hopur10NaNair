from abc import abstractmethod, abstractproperty
from typing import List
from src.logic.logic_api import LogicAPI
from src.ui.abstract_menu import AbstractMenu
from ..ui.real_estate_ui import RealEstateMenu
from ..ui.employee_ui import EmployeeMenu
from ..ui.contractor_ui import ContractorMenu
from ..ui.work_request_ui import WorkRequestMenu
from ..ui.destination_ui import DestinationMenu
from ..models import models
import dataclasses


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
                break
            elif choice == "self":
                continue
            elif issubclass(type(choice), models.Model):
                self.logic.create(choice)
            elif issubclass(type(choice), AbstractMenu):
                self.stack.append(choice)
            else:
                print("I did not understand that dave, try again")
                print()


class SimpleMenu(AbstractMenu):
    @property
    def header(self):
        return f"--- {self.__class__.__name__} ---"

    @property
    @abstractmethod
    def options(self):
        raise NotImplementedError

    def show(self):
        print(self.header)
        for (i, option) in enumerate(self.options):
            print(f"{i+1}. {option[0]}")
        print()
        if not self.is_root:
            print("b. Back")
        print("q. Quit")

    def handle_input(self, command):
        if command.isdigit():
            choice = int(command) - 1
            if choice < len(self.options):
                return self.options[choice][1]()
        elif command == "b":
            return "quit"
        elif command == "q":
            return "quit"


class MainMenu(SimpleMenu):
    is_root = True

    header = """
        _   _       _   _      _    _
       | \ | | __ _| \ | |    / \  (_)_ __
       |  \| |/ _` |  \| |   / _ \ | | '__|
       | |\  | (_| | |\  |  / ___ \| | |
       |_| \_|\__,_|_| \_| /_/   \_\_|_|

--------------- Welcome to NaN Air ---------------
"""

    options = [
        ("Employee", EmployeeMenu),
        ("Real Estate", RealEstateMenu),
        ("Work request", WorkRequestMenu),
        ("Contractor", ContractorMenu),
        ("Destination", DestinationMenu),
    ]
