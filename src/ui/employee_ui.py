from src.models.models import Employee
from src.ui.abstract_menu import SimpleMenu
from src.ui.creation_menu import CreationMenu
from src.ui.list_menu import EditPickerMenu


class EmployeeMenu(SimpleMenu):
    @property
    def header(self):
        return "--- Employee Menu ---"

    @property
    def options(self):
        if self.is_manager:
            return [
                ("Register a new employee", CreationMenu, Employee),
                ("List of employees", EditPickerMenu, Employee)
            ]
        else:
            return[
                ("List of employees", EditPickerMenu, Employee)
            ]

    def name(self):
        return f"Employee Menu"


    