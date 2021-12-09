import dataclasses
from datetime import date

from src.logic.logic_api import LogicAPI
from src.models.models import Model
from src.ui.abstract_menu import HelpfulMenu
from src.ui.list_menu import IdPickerMenu


class EditingMenu(HelpfulMenu):
    """This class is for editing menu"""

    def __init__(self, entity: Model):
        self.entity = entity
        self.constants = []
        self.variables = []
        for field in dataclasses.fields(entity):
            if field.metadata.get("autoinit") or (
                not self.is_manager and not field.metadata.get("employee_can_edit")
            ):
                self.constants.append(field)
            else:
                self.variables.append(field)

        self.transients = []
        self.options = {(i + 1): v for i, v in enumerate(self.variables)}

    def show(self):
        """This function shows fields to edit"""

        if self.constants:
            max_const_len = max(len(prop.name) for prop in self.constants) + 1
            print("Constant properties:")
            for field in self.constants:
                # get pretty name for property
                name = field.metadata.get("pretty_name", field.name)
                print(f"{name:<{max_const_len}}", end="")
                # show property if it has a value
                if field.name in dir(self.entity) and getattr(self.entity, field.name):
                    print(f"= {getattr(self.entity, field.name)}", end="")
                print()
            print()
        if self.variables:
            max_var_len = max(len(prop.name) for prop in self.variables) + 1
            print("Modifiable properties:")
            for (i, field) in self.options.items():
                # get pretty name for property
                name = field.metadata.get("pretty_name", field.name)
                print(
                    f"{str(i) + '.':<{3 if len(self.options) > 9 else 2}} {name:<{max_var_len}}",
                    end="",
                )

                # show property if it has a value
                if getattr(self.entity, field.name):
                    if field.metadata.get("hidden"):
                        print(f"= ******", end="")
                    else:
                        print(f"= {getattr(self.entity, field.name)}", end="")
                print()
            print()
        if self.transients:
            print("Creation parameters:")

        if self.variables or self.transients:
            print("c. Confirm changes")
        super().show()

    def _help_message(self):
        return f"""
Help message:
    To change a modifiable property input:
    > <property number> <new value>

    For example, to change the {self.options[1].name} property to Angela Merkel, you would write:
    > 1 Angela Merkel

    Because the {self.options[1].name} property is number 1 in the list above
    
    If the the property is a statement like Is Employee a Manager? input either "True" or "False" 
    """

    

    def handle_input(self, command: str):
        """This function handles input editing menu"""
        self._user_message = ""
        (str_option, _sep, arg) = command.partition(" ")
        option = int(str_option) if str_option.isdigit() else None
        if option in self.options and arg:
            if self.options[option].type is bool:
                if arg.lower() in ["1", "t", "true"]:
                    setattr(self.entity, self.options[option].name, True)
                    return "self"
                elif arg.lower() in ["0", "f", "false"]:
                    setattr(self.entity, self.options[option].name, False)
                    return "self"
            elif self.options[option].type is date:
                try:
                    setattr(
                        self.entity, self.options[option].name, date.fromisoformat(arg)
                    )
                    return "self"
                except ValueError as e:
                    self._user_message = e
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
            LogicAPI().set(self.entity)
            return "back"
        return super().handle_input(command)


def id_validator(string: str):
    if string.isdigit():
        return True
    else:
        print("Invalid ID")


def date_validator(string: str):
    year, month, day = string.split("-")
    isValidDate = True
    try:
        date.datetime(int(year), int(month), int(day))
    except ValueError:
        isValidDate = False
    if isValidDate:
        return
    else:
        print("Input date is not valid..")
