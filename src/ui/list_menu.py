import dataclasses
from typing import Type
from src.logic.logic_api import LogicAPI
from src.models.models import M
from src.ui.abstract_menu import AbstractMenu


class ListMenu(AbstractMenu):
    def __init__(self, model: Type[M]):
        self.model = model
        self.data = LogicAPI().get_all(model)

    def show(self):
        options = {
            field.name: str(i) + ". " + field.metadata.get("pretty_name", field.name)
            for i, field in enumerate(dataclasses.fields(self.model))
        }
        # calculate column widths
        column_widths = {
            field.name: len(
                str(i) + ". " + field.metadata.get("pretty_name", field.name)
            )
            for i, field in enumerate(dataclasses.fields(self.model))
        }
        for k in column_widths:
            for entity in self.data.values():
                if len(str(getattr(entity, k))) > column_widths[k]:
                    column_widths[k] = len(str(getattr(entity, k)))

        # top border
        self._draw_border("\u256D", "\u2500", "\u252C", "\u256E", column_widths)

        # header
        line = "\u2502"
        for field in dataclasses.fields(self.model):
            prop = field.metadata.get("pretty_name", field.name)
            line += f" {prop:<{column_widths[field.name]}} " + "\u2502"
        print(line)

        # header/body separator
        self._draw_border("\u251C", "\u2500", "\u253C", "\u2524", column_widths)

        # table contents
        for entity in self.data.values():
            line = "\u2502"
            for field in dataclasses.fields(self.model):
                prop = getattr(entity, field.name)
                line += f" {prop:<{column_widths[field.name]}} " + "\u2502"
            print(line)

        # bottom border
        self._draw_border("\u2570", "\u2500", "\u2534", "\u256F", column_widths)

    def handle_input(self, command):
        pass

    def _draw_border(self, start, fill, split, end, column_widths):
        line = start
        for field in dataclasses.fields(self.model):
            line += fill * (2 + column_widths[field.name]) + split
        print(line[:-1] + end)
