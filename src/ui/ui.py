# from ui import *
from ..ui.employee_ui import EmployeeMenu
from ..ui.contractor_ui import ContractorMenu
from ..models import models
import dataclasses


class App:
    def __init__(self):

        self.stack = [MainMenu()]

    def run(self):
        while True:
            self.stack[-1].show()
            print()
            inp = input("> ")
            print()
            choice = self.stack[-1].handle_input(inp)
            if choice is None:
                print("I did not understand that dave, try again")
                print()
            elif choice == "back":
                self.stack.pop()
            elif choice == "quit":
                break
            else:
                self.stack.append(choice)


class MainMenu:
    def show(self):
        print("1. Employee")
        print("2. Real Estate")
        print("3. Work request")
        print("4. Contractor")
        print("5. Destination")
        print("q. Quit")

    def handle_input(self, command):
        if command == "1":
            return EmployeeMenu()
        elif command == "2":
            return RealEstateMenu()
        elif command == "3":
            return WorkRequestMenu()
        elif command == "4":
            return ContractorMenu()
        elif command == "5":
            return DestinationMenu()
        elif command == "q":
            return "quit"


class CreationMenu:
    def __init__(self, model):
        self.fields = [field.name for field in dataclasses.fields(model)]

    def show(self):
        print(self.fields)
        print()
        print("b. Back")
        print("q. Quit")

    def handle_input(self, command):
        if command == "q":
            return "quit"

