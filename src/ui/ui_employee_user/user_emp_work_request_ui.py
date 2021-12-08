from src.models.models import WorkReport
from src.ui.creation_menu import CreationMenu
from src.ui.work_request_ui import FindWorkRequestMenu, WorkRequestMenu


class WorkRequestMenuUserEmp(WorkRequestMenu):
    """This class is for work request menu user employe"""
    def show(self):
        print("--- Work Request Menu ---")
        print("1. Register a new work report")
        print("2. Find work request")
        print("b. Back")
        print("q. Quit")

    def handle_input(self, command):
        """This function handles input for work request menu user employe"""
        if command == "1":
            return CreationMenu(WorkReport)
        elif command == "2":
            return EmpFindWorkRequestMenu()
        elif command == "b":
            return "back"
        elif command == "q":
            return "quit"


class EmpFindWorkRequestMenu(
    FindWorkRequestMenu
):  # To-Do: Add a function that allows to register a work report on a work request
    """This class is for employe to find work request"""
    def show(self):
        return super().show()

    def handle_input(self, command): # This handle_input can't be the same as for the Manager because the Employee is not allowed to change the work requests.
        """This function handels input for employe finde work reuqest menu"""
        return super().handle_input(command)
        """
        if command == "1":
            print("Find Work by ID:")
            print()
            self.display_all_works()
            self.find_work_by_id()
            return BackQuitMenu()
        elif command == "2":
            print("Find Work by Real Estate:")
            print()
            RealEstateMenu().display_all_real_estate()
            self.display_work_by_real_estate()
            self.find_work_by_id()
            return BackQuitMenu()
        elif command == "3":
            print("Find Work by Employee:")
            print()
            EmployeeMenu().display_all_employees()
            self.display_work_by_employee()
            self.find_work_by_id()
            return BackQuitMenu()
        elif command == "4":
            print("Find Work by Contractor:")
            print()
            ContractorMenu().display_all_contractors()
            self.display_work_by_contractor()
            self.find_work_by_id()
            return BackQuitMenu()
        elif command == "5":
            print("Find Work by Date:")
            print()
            self.display_all_works()
            self.display_work_by_date()
            self.find_work_by_id()
            return BackQuitMenu()
        elif command == "6":
            print("Find Work by Period:")
            print()
            self.display_all_works()
            self.find_work_by_period()
            self.find_work_by_id()
            return BackQuitMenu()
        elif command == "b":
            return "back"
        elif command == "q":
            return "quit"
        """
