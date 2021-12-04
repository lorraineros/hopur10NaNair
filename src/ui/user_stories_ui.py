




from src.ui.abstract_menu import AbstractMenu


class UserStoriesMenu(AbstractMenu):
    def show(self):
        print("--- User Stories Menu ---")
        print("1. Register a new user story")
        print("2. Find user story")
        print("3. Display list of user story")
        print("b. back")
        print("q. quit")

    def handle_input(self,command):
        if command == 1:
            pass 
        elif command == 2:
            return UserStoriesSearch()
        elif command == 3:
            return UserStoriesMenu()
        elif command == "b":
            return "back"
        elif command == "q":
            return "quit"

class UserStoriesSearch:
    def show(self):
        print("--- Find User Stories ---")
        print()
        inp = input("Choose a Find User Stories")

    def handle_input(self, inp):
        pass


class DestinationMenu:
    def show(self):
        print("--- Destination Menu ---")
        print("1. Register a new Destination menu")
        print("2. Find Destination menu")
        print("3. Display Destination value")
        print("b. back")
        print("q. quit")

    def handle_input(self,common):
        if common == 1:
            pass
        elif common == 2:
            return DestinationMenu()
        elif common == 3:
            return DestinationSearch()
        elif common == "b": 
            return "back"
        elif common == "q":
            return "quit"

class DestinationSearch:
    def show(self):
        print("--- Finde Destination ---")
        print()
        inp = input("Chose a Destination")
    def handle_input(self, inp):
        pass


