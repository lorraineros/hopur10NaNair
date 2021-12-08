import dataclasses

from src.logic.logic_api import LogicAPI
from src.models.models import Id, Model
from src.ui.abstract_menu import AbstractMenu
from src.ui.list_menu import IdPickerMenu
from src.ui.utilities import MessageToParent


class EditingMenu(AbstractMenu):
    def __init__(self, entity: Model):
        self.entity = entity
        self.constants = [
            field
            for field in dataclasses.fields(entity)
            if field.metadata.get("autoinit")
        ]
        self.variables = [
            field
            for field in dataclasses.fields(entity)
            if not field.metadata.get("autoinit")
        ]
        self.options = {(i + 1): v for i, v in enumerate(self.variables)}
        self.assistance = False  # help was taken :(

    def show(self):
        max_const_len = max(len(prop.name) for prop in self.constants) + 1
        max_var_len = max(len(prop.name) for prop in self.variables) + 1

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
        print("Modifiable properties:")
        for (i, field) in self.options.items():
            # get pretty name for property
            name = field.metadata.get("pretty_name", field.name)
            print(
                f"{str(i) + '.':<{3 if len(self.options) > 9 else 2}} {name:<{max_var_len}}",
                end="",
            )

            # show property if it has a value
            if field.name in dir(self.entity) and getattr(self.entity, field.name):
                print(f"= {getattr(self.entity, field.name)}", end="")
            print()
        print()
        print("c. Confirm changes")
        print()
        print("h. Help")
        print("b. Back (discard changes)")
        print("q. Quit (discard changes)")
        if self.assistance:
            print()
            print("Help message:")
            print("\tTo change a modifiable property input:")
            print("> <property number> <new value>")
            print()
            print(
                f"\tFor example, to change the {self.options[1].name} "
                "property to Angela Merkel, you would write:"
            )
            print("> 1 Angela Merkel")
            print()
            print(
                f"\tBecause the {self.options[1].name} property "
                "is number 1 in the list above"
            )

    def handle_input(self, command: str):
        # if option in self.options and self.options[option].type is Id:
        #     pass
        #     # TODO: return ListMenu(self.options[option].metadata.get("model_ref"))
        self.assistance = False
        (str_option, _sep, arg) = command.partition(" ")
        option = int(str_option) if str_option.isdigit() else None
        if option in self.options:
            if arg:
                if self.options[option].type is int:
                    if date_validator(arg):
                        setattr(self.entity, self.options[option].name, arg)
                    else:
                        print("error")
                elif self.options[option].type is str:
                    print("error")
            elif self.options[option].metadata.get("id"):
                # a somewhat high risk play
                self.message_from_child = lambda message: setattr(
                    self.entity, self.options[option].name, message.messages["id"]
                )
                return IdPickerMenu(self.options[option].metadata.get("model")())
        if option in self.options and arg:
            setattr(self.entity, self.options[option].name, arg)
            return "self"
        if command == "c":
            LogicAPI().set(self.entity)
            return "back"
        if command == "h":
            self.assistance = True
            return "self"
        if command == "b":
            return "back"
        if command == "q":
            return "quit"


def id_validator(string: str):
    if string.isdigit():
        return True
    else:
        print("Invalid ID")


def date_validator(string: str):
    year, month, day = string.split("-")
    isValidDate = True
    try:
        datetime.datetime(int(year), int(month), int(day))
    except ValueError:
        isValidDate = False
    if isValidDate:
        return
    else:
        print("Input date is not valid..")
