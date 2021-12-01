import dataclasses

from src.models.models import Model
from src.ui.abstract_menu import AbstractMenu


class CreationMenu(AbstractMenu):
    # @classmethod
    # def from(cls, model: Model):
    #     return lambda: cls(model)

    def __init__(self, model: Model):
        self.builder = {}
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
            print(f"{i+1}. {prop.name:<18}", end="")
            if prop.name in self.builder:
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
            # TODO: Write self.builder to file
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
