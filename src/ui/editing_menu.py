import dataclasses
import os
from datetime import date, timedelta

from src.logic.logic_api import LogicAPI
from src.logic.filters import IdFilter
from src.models.models import Model, RealEstate, WorkReport
from src.ui.abstract_menu import HelpfulMenu
from src.ui.list_menu import EditPickerMenu, IdPickerMenu


class EditingMenu(HelpfulMenu):
    """This class is for editing menu"""

    def __init__(self, entity: Model):
        super().__init__()
        self.entity = entity
        self.constants = []
        self.variables = []
        self.transients = []
        for field in dataclasses.fields(entity):
            if field.metadata.get("autoinit") or (
                not self.is_manager and not field.metadata.get("employee_can_edit")
            ):
                self.constants.append(field)
            elif field.metadata.get("initializer"):
                self.transients.append(field)
            elif field.metadata.get("derived"):
                pass  # don't display derived values
            else:
                self.variables.append(field)

        self.variable_options = dict(enumerate(self.variables, 1))
        self.transient_options = {}

    def name(self):
        if self.is_manager or isinstance(self.entity, WorkReport):
            return f"Editing {self.entity.model_name()}"
        else:
            return f"{self.entity.model_name()}"

    def show(self):
        """This function shows fields to edit"""

        print(f"Properties of a {self.entity.model_name()}")

        if self.constants:
            max_const_len = max(len(field.name) for field in self.constants) + 1
            print("Constant properties:")
            self.show_props(max_const_len, enumerate(self.constants), False)
            print()

        max_var_len = (
            max(
                [0]
                + [
                    len(field.metadata.get("pretty_name", field.name))
                    for field in (self.variables + self.transients)
                ]
            )
            + 1
        )
        if self.variable_options:
            print("Modifiable properties:")
            self.show_props(max_var_len, self.variable_options.items(), True)
            print()

        if self.transient_options:
            print("Creation parameters:")
            self.show_props(max_var_len, self.transient_options.items(), True)
            print()

        extra_print = False
        for model in self.entity.mentioned_by():
            for field in dataclasses.fields(model):
                ref = field.metadata.get("id")
                if (
                    ref
                    and ref() == type(self.entity)
                    and [
                        ent
                        for ent in LogicAPI().get_all(model).values()
                        if getattr(ent, field.name) == self.entity.id
                    ]
                ):
                    extra_print = True
                    print(f"{model.command()}. Show a list of {model.model_name()}")
        if extra_print:
            print()

        if self.variables or self.transients:
            print("c. Confirm changes")
        super().show()

    def show_props(self, max_prop_len, options, modifiable):
        extra_padding = 3 if len(self.variables) + len(self.transients) >= 10 else 2
        for (i, field) in options:
            # get pretty name for property
            name = field.metadata.get("pretty_name", field.name)
            prop_lhs = ""
            if modifiable:
                prop_lhs = f"{str(i) + '.':<{extra_padding}} "
            prop_lhs += f"{name:<{max_prop_len}}"
            print(prop_lhs, end="")

            # show property if it has a value
            if getattr(self.entity, field.name):
                if field.metadata.get("hidden"):
                    print(f"= ******", end="")
                else:
                    prop = str(getattr(self.entity, field.name)).splitlines()
                    print(f"= {prop[0]}", end="")
                    for line in prop[1:]:
                        print()
                        print(
                            f"{' '*len(prop_lhs)}  {line}",
                            end="",
                        )
            print()

    def _help_message(self):
        return f"""
Help message:
    To change a modifiable property input:
    > <property number> (space between) <new value>

    For example, to change the {self.options[1].name} " "property to Angela Merkel, you would write:
    > 1 Angela Merkel

    Because the {self.options[1].name} property " "is number 1 in the list above

    If the the property is a statement like Is Employee a Manager? input either "True" or "False"
    """

    def handle_input(self, command: str):
        """This function handles input editing menu"""
        for model in self.entity.mentioned_by():
            for field in dataclasses.fields(model):
                ref = field.metadata.get("id")
                if (
                    ref  # if field is an ID field
                    and ref() == type(self.entity)  # and references the right model
                    and command == model.command()  # and it's command was input
                    and [
                        ent
                        for ent in LogicAPI().get_all(model).values()
                        if getattr(ent, field.name) == self.entity.id
                    ]
                ):
                    next_menu = EditPickerMenu(model)
                    next_menu.filters.append(IdFilter(field, self.entity.id))
                    return next_menu
        self.options = self.variable_options | self.transient_options
        (str_option, _sep, arg) = command.partition(" ")
        option = int(str_option) if str_option.isdigit() else None
        # handle property changing commands
        if option in self.options and arg:
            set_option = lambda val: (
                setattr(self.entity, self.options[option].name, val),
                "self",
            )[1]
            if self.options[option].type is bool:
                if arg.lower() in ["1", "t", "true"]:
                    return set_option(True)
                elif arg.lower() in ["0", "f", "false"]:
                    return set_option(False)
            elif self.options[option].type is date:
                try:
                    return set_option(date.fromisoformat(arg))
                except ValueError as e:
                    self._user_message = (
                        str(e) + os.linesep + "Valid format: yyyy-mm-dd" + os.linesep
                    )
            elif self.options[option].type is timedelta:
                (number, _, duration) = arg.partition(" ")
                if arg.lower() in ["day", "daily"]:
                    return set_option(timedelta(days=1))
                elif arg.lower() in ["week", "weekly"]:
                    return set_option(timedelta(days=7))
                elif arg.lower() in ["month", "monthly"]:
                    return set_option(timedelta(days=30))
                elif duration and number.isdigit():
                    if duration in ["day", "days"]:
                        return set_option(timedelta(days=int(number)))
                    elif duration in ["week", "weeks"]:
                        return set_option(timedelta(days=7 * int(number)))
                    elif duration in ["month", "months"]:
                        return set_option(timedelta(days=30 * int(number)))
                    else:
                        self._user_message = (
                            "Invalid format, it should be like this: '3 weeks'"
                            + os.linesep
                        )
                else:
                    self._user_message = (
                        "Invalid format, valid options are: day, week, month"
                        + os.linesep
                    )

            elif self.options[option].type is str:
                setattr(self.entity, self.options[option].name, arg)
                return "self"
            elif self.options[option].type is int:
                if not self.options[option].metadata.get("id") and arg.isdigit():
                    setattr(self.entity, self.options[option].name, arg)
                    return "self"
            # Invalid command return nothing
            return
        if option in self.options and self.options[option].metadata.get("id"):
            # field is an ID, open a list to pick it
            # a somewhat high risk play
            self.message_from_child = lambda message: setattr(
                self.entity, self.options[option].name, message.messages["id"]
            )
            return IdPickerMenu(self.options[option].metadata.get("id")())
        if command == "c":
            for field in dataclasses.fields(self.entity):
                if not bool(getattr(self.entity, field.name)) and field.metadata.get(
                    "required"
                ):
                    self._user_message += (
                        f"Missing/invalid value for {field.metadata.get('pretty_name', field.name)}"
                        + os.linesep
                    )
            if LogicAPI().set(self.entity):
                return "back"
            else:
                return "self"
        return super().handle_input(command)
