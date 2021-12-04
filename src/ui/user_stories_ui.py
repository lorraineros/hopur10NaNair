

from src.ui.abstract_menu import AbstractMenu
from src.logic.user_stories_logic import UserStories



class UserStoriesMenu(AbstractMenu):
    def show(self):
        print("--- User Stories Menu ---")
        print("1. Register a new user story")
        print("2. Find user story")
        print("3. Display list of user stories")
        print("b. back")
        print("q. quit")

    def handle_input(self,command):
        if command == 1:
            pass 
        elif command == 2:
            return UserStoriesSearch()
        elif command == 3:
            self.list_of_all_user_stories()
        elif command == "b":
            return "back"
        elif command == "q":
            return "quit"

    def list_of_all_user_stories(self):
            print(f"{'--- List of all user stories ---':^34}")
            print("-" * 52)
            print(f"| {'ID':^3} | {'Name':^21} | {'Storie':^18} ")
            print("-" * 52)
            for user_stories in UserStories.get_destination_list():
                print(
                    f"| {user_stories.id:<3} | {user_stories.name:<21} | {user_stories.country:<18} |"
                )
            print("-" * 52)
            print()

    
class UserStoriesSearch:
    def show(self):
        print("--- Find User Stories ---")
        print()
        inp = input("Choose a Find User Stories")

    def handle_input(self, inp):
        pass






    def delete_user_stories(self):
        print("""
--- Delete a Destination ---
1. By ID   
2. By Name  

q. Quit
b. Back
                """)


    def handle_input(self,common):
        if common == 1:
            pass
        elif common == 2:
            return ListOfUserStories()
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


