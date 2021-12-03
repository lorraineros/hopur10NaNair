from src.ui.work_request_ui import *

class EmpWorkRequestMenu(WorkRequestMenu):
    def show(self):
        print("--- Work Request Menu ---")
        print("1. Register a new work report")
        print("2. Find work request")
        print("b. Back")
        print("q. Quit")

    def handle_input(self, command):
        if command == "1":
            # return CreationMenu(models.WorkReport)
            pass
        elif command == "2":
            return FindWorkRequestMenu()
        elif command == "b":
            return "back"
        elif command == "q":
            return "quit"
