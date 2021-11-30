from ..logic.work_request_logic import WorkRequestLogic


class WorkRequestMenu:
    def show(self):
        print("--- Work Request Menu ---")
        print("1. Register a new work request")
        print("2. Find work request")
        print("b. Back")
        print("q. Quit")

    def handle_input(self, command):
        if command == "1":
            pass
        elif command == "2":
            return FindWorkRequestMenu()
        elif command == "b":
            return "back"
        elif command == "q":
            return "quit"


class FindWorkRequestMenu:
    def show(self):
        #print("--- FIND WORK REQUEST MENU ---")
        print("1. By ID")
        print("2. By real estate")
        print("3. By employee")
        print("4. By contractor")
        print("5. By date")
        print("6. By period")
        print("b. Back")
        print("q. Quit")

    def handle_input(self, command):
        if command == "1":
            pass
        elif command == "2":
            pass
        elif command == "3":
            pass
        elif command == "4":
            pass
        elif command == "5":
            pass
        elif command == "6":
            pass
        elif command == "b":
            return "back"
        elif command == "q":
            return "quit"

