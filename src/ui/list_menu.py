import dataclasses
import os
import shutil
from typing import Type

from src.logic.logic_api import LogicAPI
from src.models.models import M
from src.ui.abstract_menu import AbstractMenu
from src.ui.common_menus import EditingMenu


class ListMenu(AbstractMenu):
    def __init__(self, model: Type[M]):
        self.model = model
        self.data = LogicAPI().get_all(model)
        self.term_size = shutil.get_terminal_size()
        self.options = {
            field.name: chr(ord("A") + i)
            + ". "
            + field.metadata.get("pretty_name", field.name)
            for i, field in enumerate(dataclasses.fields(self.model))
        }
        self.assistance = False

    def show(self):
        self._update_term_size()
        # calculate column widths
        column_widths = {
            field.name: len(self.options[field.name])
            for field in dataclasses.fields(self.model)
        }
        for k in column_widths:
            for entity in self.data.values():
                value = str(getattr(entity, k))
                column_widths[k] = max(column_widths[k], *map(len, value.split("\n")))

        # figure out which fields to show
        fields_to_show = []
        total_width = 1
        for field in dataclasses.fields(self.model):
            next_thing = (2 + column_widths[field.name]) + 1
            if total_width + next_thing <= self.term_size.columns:
                total_width += next_thing
                fields_to_show.append(field)

        # top border
        self._draw_border(
            "\u256D", "\u2500", "\u252C", "\u256E", fields_to_show, column_widths
        )

        # header
        line = "\u2502"
        for field in fields_to_show:
            prop = self.options[field.name]
            line += f" {prop:<{column_widths[field.name]}} " + "\u2502"
        print(line)

        # header/body separator
        self._draw_border(
            "\u251C", "\u2500", "\u253C", "\u2524", fields_to_show, column_widths
        )

        # table contents
        for entity in self.data.values():
            line = "\u2502"
            for field in fields_to_show:
                prop = getattr(entity, field.name)
                next_thing = f" {prop:<{column_widths[field.name]}} " + "\u2502"
                if len(line + next_thing) <= self.term_size.columns:
                    if type(prop) is str:
                        line += f" {prop:<{column_widths[field.name]}} " + "\u2502"
                    else:
                        line += f" {prop:>{column_widths[field.name]}} " + "\u2502"
            print(line)

        # bottom border
        self._draw_border(
            "\u2570", "\u2500", "\u2534", "\u256F", fields_to_show, column_widths
        )
        print()
        print("h. Help")
        print()
        print("b. Back")
        print("q. Quit")

    def handle_input(self, command: str):
        if command.isdigit() and LogicAPI().get(self.model, int(command)):
            return EditingMenu(LogicAPI().get(self.model, int(command)))
        if command == "h":
            self.assistance = True
            return "self"
        if command == "b":
            return "back"
        if command == "q":
            return "quit"

    @staticmethod
    def _draw_border(start, fill, split, end, fields_to_show, column_widths):
        line = start
        for field in fields_to_show:
            line += fill * (2 + column_widths[field.name]) + split
        print(line[:-1] + end)

    def _update_term_size(self):
        self.term_size = shutil.get_terminal_size()
        if self.term_size.columns == 0 or self.term_size.lines == 0:
            self.term_size = os.terminal_size((80, 24))
