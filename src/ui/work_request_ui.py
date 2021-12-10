from src.models.models import WorkReport, WorkRequest
from src.ui.abstract_menu import SimpleMenu
from src.ui.creation_menu import CreationMenu
from src.ui.list_menu import EditPickerMenu


class WorkRequestMenu(SimpleMenu):
    @property
    def header(self):
        return "--- Work Request Menu ---"

    @property
    def options(self):
        if self.is_manager:
            return [
                ("Register a new work request", CreationMenu, WorkRequest),
                ("List of work requests", EditPickerMenu, WorkRequest),
                ("List of work reports", EditPickerMenu, WorkReport)
            ]
        else:
            return[
                ("Register a new work report", CreationMenu, WorkReport),
                ("List of work requests", EditPickerMenu, WorkRequest),
                ("List of work reports", EditPickerMenu, WorkReport)
            ]
    def name(self):
        return f"Work Request Menu"
