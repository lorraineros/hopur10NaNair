from typing import Type

from src.logic.logic_api import LogicAPI
from src.models.models import Model
from src.ui.editing_menu import EditingMenu


class CreationMenu(EditingMenu):
    def __init__(self, model: Type[Model]):
        super().__init__(LogicAPI().get_new(model))
        self.transient_options = dict(
            enumerate(self.transients, 1 + len(self.variables))
        )

    def name(self):
        return f"{self.entity.model_name().lower()} creation menu"
