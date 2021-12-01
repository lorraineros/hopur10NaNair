import dataclasses

from src.models.models import Model
from src.ui.abstract_menu import AbstractMenu


class CreationMenu(AbstractMenu):
    @classmethod
    # def from(cls, model: Model):
    #     return lambda: cls(model)

    def __init__(self, model: Model):
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
        for (i, prop) in enumerate(
            filter(lambda field: not field.metadata.get("autoinit"), self.fields)
        ):
            # print(prop)
            print(f"{i+1}. {prop.name:<16}")
        print()
        print("b. Back")
        print("q. Quit")

    def handle_input(self, command):
        if command in self.options:
            print(self.options[command])
            return EditingMenu(self.options[command])
        if command == "q":
            return "quit"


class EditingMenu(AbstractMenu):
    def __init__(self, prop):
        self.prop = prop

    def show(self):
        print(f"Editing {self.prop.name}")

    def handle_input(self, command):
        self.prop
