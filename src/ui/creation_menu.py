import dataclasses
from typing import Type

from src.logic.logic_api import LogicAPI
from src.models.models import Model
from src.ui.abstract_menu import AbstractMenu


class CreationMenu(AbstractMenu):
    def __init__(self, model: Type[Model]):
        self.model = model
        # TODO: do proper default initialization or find a better solution
        self.builder = {field.name: None for field in dataclasses.fields(model)}
        self.fields = [field for field in dataclasses.fields(model)]
        self.options = dict(
            map(
                lambda tup: (str(tup[0] + 1), tup[1]),
                enumerate(
                    filter(
                        lambda field: not field.metadata.get("autoinit"), self.fields
                    )
                ),
            )
        )

    def show(self):
        print("Choose a property to edit: ")
        max_prop_len = max(len(prop.name) for prop in self.fields) + 1
        for (i, prop) in enumerate(
            filter(lambda field: not field.metadata.get("autoinit"), self.fields)
        ):
            # print(prop)
            print(f"{i+1}. {prop.name:<{max_prop_len}}", end="")
            if prop.name in self.builder and not self.builder[prop.name] is None:
                print(f"= {self.builder[prop.name]}", end="")
            print()
        print()
        print("c. Confirm creation")
        print()
        print("b. Back (discard changes)")
        print("q. Quit (discard changes)")

    def handle_input(self, command):
        if command in self.options:
            print(self.options[command])
            return EditingMenu(self.options[command], self.builder)
        if command == "c":
            LogicAPI().create(self.model.from_dict(self.builder))
            return "back"
        if command == "b":
            return "back"
        if command == "q":
            return "quit"


class EditingMenu(AbstractMenu):
    def __init__(self, prop, builder):
        self.prop = prop
        self.builder = builder

    def show(self):
        print(f"Input a new value for {self.prop.name}")

    def handle_input(self, command):
        self.builder[self.prop.name] = command
        return "back"
