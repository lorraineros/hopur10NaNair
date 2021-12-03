from src.ui.abstract_menu import AbstractMenu


class ChangingMenu(AbstractMenu):
    def show(self):
        '''Menu for changing information.'''
        print("c. Change Infromation")
        print("b. Back")
        print("q. Quit")
    
    def handle_input(self, command):
        '''Handles the input for ChangingMenu'''
        if command == "c":
            # return EditingMenu()
            pass
        elif command == "b":
            return "back"
        elif command == "q":
            return "quit"

class BackQuitMenu(AbstractMenu):
    def show(self):
        '''Menu for only back and quit'''
        print("b. Back")
        print("q. Quit")
    
    def handle_input(self, command):
        '''Handles the input for BackQuitMenu'''
        if command == "b":
            return "back"
        elif command == "q":
            return "quit"