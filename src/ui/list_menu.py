import dataclasses
import os
import shutil
from typing import List, Type

from src.logic.logic_api import LogicAPI
from src.logic.utilities import RegexFilter
from src.models.models import M
from src.ui.abstract_menu import BasicNavigationMenu
from src.ui.utilities import MessageToParent

# commented to prevent circular imports
# from src.ui.editing_menu import EditingMenu
# from src.ui.creation_menu import CreationMenu


class AbstractListMenu(BasicNavigationMenu):
    def __init__(self, model: Type[M]):
        self.model = model
        self.term_size = shutil.get_terminal_size()
        self.filters: List[RegexFilter] = []
        self.filter_options = {
            chr(ord("A") + i): field
            for i, field in enumerate(dataclasses.fields(self.model))
        }
        self.options = {
            field.name: chr(ord("A") + i)
            + ". "
            + field.metadata.get("pretty_name", field.name)
            for i, field in enumerate(dataclasses.fields(self.model))
        }
        self.assistance = False

    def show(self):
        entities = LogicAPI().get_filtered(self.model, self.filters)
        self._update_term_size()
        # calculate column widths
        column_widths = {
            field.name: len(self.options[field.name])
            for field in dataclasses.fields(self.model)
        }
        for k in column_widths:
            for entity in entities.values():
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
        column_widths = {field: column_widths[field.name] for field in fields_to_show}

        # top border
        self._draw_border("\u256D", "\u2500", "\u252C", "\u256E", column_widths)

        # header
        line = "\u2502"
        for (field, width) in column_widths.items():
            prop = self.options[field.name]
            line += f" {prop:<{width}} " + "\u2502"
        print(line)

        # header/body separator
        self._draw_border("\u251C", "\u2500", "\u253C", "\u2524", column_widths)

        # table contents
        for entity in entities.values():
            line = "\u2502"
            for (field, width) in column_widths.items():
                prop = getattr(entity, field.name)
                next_thing = f" {prop:<{width}} " + "\u2502"
                if len(line + next_thing) <= self.term_size.columns:
                    if type(prop) is int:
                        line += f" {prop:>{width}} " + "\u2502"
                    else:
                        line += f" {prop:<{width}} " + "\u2502"
            print(line)

        # bottom border
        self._draw_border("\u2570", "\u2500", "\u2534", "\u256F", column_widths)

        if self.filters:
            print()
            print("Active filters")
            for (i, filt) in enumerate(self.filters):
                print(f"r {i+1}. {filt}")
            print()
            print("r. Reset filters")

        print()
        print("h. Help")
        print(f"c. Create {self.model.model_name()}")
        print()
        super().show()

    def handle_input(self, command: str):
        self.assistance = False
        (str_option, _sep, arg) = command.partition(" ")
        if str_option in self.filter_options and arg:
            self.filters.append(RegexFilter(self.filter_options[str_option].name, arg))
            return "self"
        if str_option == "r":
            if arg:
                # if the argument is a valid int then remove that filter
                if arg.isdigit() and int(arg) > 0 and int(arg) <= len(self.filters):
                    self.filters.pop(int(arg) - 1)
                    return "self"
            else:
                # if only "r" is input then clear all filters
                self.filters.clear()
                return "self"
        if command == "c":
            from src.ui.creation_menu import CreationMenu

            return CreationMenu(self.model)
        if command == "h":
            self.assistance = True
            return "self"
        return super().handle_input(command)

    @staticmethod
    def _draw_border(start, fill, split, end, column_widths):
        line = start
        for (field, width) in column_widths.items():
            line += fill * (2 + width) + split
        print(line[:-1] + end)

    def _update_term_size(self):
        self.term_size = shutil.get_terminal_size()
        if self.term_size.columns == 0 or self.term_size.lines == 0:
            self.term_size = os.terminal_size((80, 24))


class EditPickerMenu(AbstractListMenu):
    def handle_input(self, command):
        if command.isdigit() and LogicAPI().get(self.model, int(command)):
            from src.ui.editing_menu import EditingMenu

            return EditingMenu(LogicAPI().get(self.model, int(command)))
        else:
            return super().handle_input(command)


class IdPickerMenu(AbstractListMenu):
    def handle_input(self, command):
        if command.isdigit() and LogicAPI().get(self.model, int(command)):
            return MessageToParent(id=int(command))
        return super().handle_input(command)
