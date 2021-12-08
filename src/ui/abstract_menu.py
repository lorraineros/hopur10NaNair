from abc import ABC, abstractmethod

from src.ui.utilities import MessageToParent


class AbstractMenu(ABC):
    is_root = False
    _inbox = None

    @abstractmethod
    def show(self):
        raise NotImplementedError(f"{self.__name__} doesn't implement .show()")

    @abstractmethod
    def handle_input(self, command):
        raise NotImplementedError(
            f"{self.__name__} doesn't implement .handle_input(command)"
        )

    def message_from_child(self, message: MessageToParent):
        self._inbox = message


class BasicNavigationMenu(AbstractMenu):
    def show(self):
        if not self.is_root:
            print("b. Back")
        print("q. Quit")

    def handle_input(self, command):
        if command == "b":
            return "back"
        elif command == "q":
            return "quit"


class SimpleMenu(BasicNavigationMenu):
    @property
    def header(self):
        return f"--- {self.__class__.__name__} ---"

    @property
    @abstractmethod
    def options(self):
        raise NotImplementedError

    def show(self):
        print(self.header)
        for (i, option) in enumerate(self.options):
            print(f"{i+1}. {option[0]}")
        print()
        super().show()

    def handle_input(self, command):
        if command.isdigit():
            choice = int(command) - 1
            if choice < len(self.options):
                if len(self.options[choice]) == 3:
                    return self.options[choice][1](self.options[choice][2])
                else:
                    return self.options[choice][1]()
        return super().handle_input(command)
