import dataclasses
from datetime import date
import os
import shutil
from typing import List, Type

from src.logic.logic_api import LogicAPI
from src.logic.utilities import DateFilter, PeriodFilter, RegexFilter
from src.models.models import M
from src.ui.abstract_menu import BasicNavigationMenu, HelpfulMenu
from src.ui.utilities import MessageToParent

# commented to prevent circular imports
# from src.ui.editing_menu import EditingMenu
# from src.ui.creation_menu import CreationMenu


class AbstractListMenu(HelpfulMenu):
    """This class contains menu functions"""

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
        self.sort_order = []

    def show(self):
        """This function shows menu based on display used"""
        # fetch data from storage
        entities = LogicAPI().get_filtered(self.model, self.filters)
        # sort data
        for (field, rev) in self.sort_order:
            entities.sort(key=lambda ent: getattr(ent, field), reverse=rev)

        self._update_term_size()
        # calculate column widths
        # start with the widths of the headers
        column_widths = {
            field.name: len(self.options[field.name])
            for field in dataclasses.fields(self.model)
        }
        # find the widest value
        for k in column_widths:
            for entity in entities:
                value = str(getattr(entity, k))
                column_widths[k] = max(column_widths[k], *map(len, value.split("\n")))
        # hidden fields have a length of 6
        for field in dataclasses.fields(self.model):
            if field.metadata.get("hidden"):
                column_widths[field.name] = max(column_widths[field.name], 6)

        # figure out which fields fit on the screen
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
            if self.sort_order and field.name == self.sort_order[-1][0]:
                line += "↑" if self.sort_order[-1][1] else "↓"
            else:
                line += " "
            line += f"{prop:<{width}} "
            line += "\u2502"
        print(line)

        # header/body separator
        self._draw_border("\u251C", "\u2500", "\u253C", "\u2524", column_widths)

        # table contents
        for entity in entities:
            line = "\u2502"
            for (field, width) in column_widths.items():
                prop = str(getattr(entity, field.name))
                next_thing = f" {prop:<{width}} " + "\u2502"
                if len(line + next_thing) <= self.term_size.columns:
                    if type(prop) is int:
                        line += f" {prop:>{width}} " + "\u2502"
                    elif field.metadata.get("hidden"):
                        line += f" {'******':<{width}} " + "\u2502"
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
        if self.is_manager:
            print(f"c. Create {self.model.model_name()}")
            print()
        super().show()

    def _help_message(self):
        return """
Help message:
    A column can be sorted by inputting the capital letter in it's header.
    A column can be filtered by inputting the capital letter in it's header,
    followed by a string that should be matched.
    If a column represents a date, the string should be a valid date in the format: yyyy-mm-dd
    A date column can receive a start and an end date seperated with a space, to show entries within a period: Start(yyyy-mm-dd) End(yyyy-mm-dd)

    All filters can be removed with the 'r' command.
    Individual filters can be removed by inputting 'r' followed by the number of the filter shown.
            """

    def handle_input(self, command: str):
        """This function handles input from menu"""
        self._user_message = ""
        (str_option, _, arg) = command.partition(" ")
        if str_option in self.filter_options and arg:  # Filtering
            chosen_column = self.filter_options[str_option]
            if chosen_column.type is date:
                (start, _, end) = arg.partition(" ")
                try:
                    if end:
                        self.filters.append(
                            PeriodFilter(
                                chosen_column,
                                date.fromisoformat(start),
                                date.fromisoformat(end),
                            )
                        )
                    else:
                        self.filters.append(
                            DateFilter(
                                chosen_column,
                                date.fromisoformat(start),
                            )
                        )
                except ValueError as e:
                    self._user_message = e
                    return
            else:
                self.filters.append(RegexFilter(self.filter_options[str_option], arg))
            return "self"
        elif str_option in self.filter_options:  # Sorting
            sort_target = self.filter_options[str_option].name

            if len(self.sort_order) > 0 and self.sort_order[-1][0] == sort_target:
                # toggle sort order
                self.sort_order[-1] = (sort_target, not self.sort_order[-1][1])
            elif (sort_target, False) in self.sort_order:
                self.sort_order.remove((sort_target, False))
                self.sort_order.append((sort_target, False))
            elif (sort_target, True) in self.sort_order:
                self.sort_order.remove((sort_target, True))
                self.sort_order.append((sort_target, True))
            else:
                self.sort_order.append((sort_target, False))
            return "self"
        elif str_option == "r":
            if arg:
                # if the argument is a valid int then remove that filter
                if arg.isdigit() and int(arg) > 0 and int(arg) <= len(self.filters):
                    self.filters.pop(int(arg) - 1)
                    return "self"
            else:
                # if only "r" is input then clear all filters
                self.filters.clear()
                return "self"
        elif command == "c" and self.is_manager:
            from src.ui.creation_menu import CreationMenu

            return CreationMenu(self.model)
        return super().handle_input(command)

    @staticmethod
    def _draw_border(start, fill, split, end, column_widths):
        """Function that draws border according to size of terminal"""
        line = start
        for (field, width) in column_widths.items():
            line += fill * (2 + width) + split
        print(line[:-1] + end)

    def _update_term_size(self):
        """Function that gets size of terminal"""
        self.term_size = shutil.get_terminal_size()
        if self.term_size.columns == 0 or self.term_size.lines == 0:
            self.term_size = os.terminal_size((80, 24))


class EditPickerMenu(AbstractListMenu):
    """This class is to edit to PickerMenu"""

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
