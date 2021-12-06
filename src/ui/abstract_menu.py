from abc import ABC, abstractmethod


class AbstractMenu(ABC):
    is_root = False

    @abstractmethod
    def show(self):
        raise NotImplementedError(f"{self.__name__} doesn't implement .show()")

    @abstractmethod
    def handle_input(self, command):
        raise NotImplementedError(
            f"{self.__name__} doesn't implement .handle_input(command)"
        )


class SimpleMenu(AbstractMenu):
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
        if not self.is_root:
            print("b. Back")
        print("q. Quit")

    def handle_input(self, command):
        if command.isdigit():
            choice = int(command) - 1
            if choice < len(self.options):
                return self.options[choice][1]()
        elif command == "b":
            return "back"
        elif command == "q":
            return "quit"
