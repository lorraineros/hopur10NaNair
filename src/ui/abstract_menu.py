from abc import ABC, abstractmethod

from src.ui.utilities import MessageToParent

_is_manager = None


class IllegalArgumentException(ValueError):
    pass


class AbstractMenu(ABC):
    """This class is for abstrct menu"""

    is_root = False
    _inbox = None
    _user_message = ""

    @abstractmethod
    def show(self):
        if self._user_message:
            print()
            print(self._user_message)
            self._user_message = ""

    @abstractmethod
    def handle_input(self, command):
        pass

    @property
    def is_manager(self):
        return _is_manager

    @is_manager.setter
    def is_manager(self, value):
        global _is_manager
        if type(value) == bool:
            if _is_manager is None:
                _is_manager = value
            else:
                raise Exception("manager constant can't be changed after program start")
        else:
            raise IllegalArgumentException("is_manager must be a boolean")

    def name(self):
        return self.__class__.__name__

    def message_from_child(self, message: MessageToParent):
        self._inbox = message


class BasicNavigationMenu(AbstractMenu):
    """This class is for basic navigation menu"""

    @abstractmethod
    def show(self):
        if not self.is_root:
            print("b. Back")
        print("q. Quit")
        super().show()

    @abstractmethod
    def handle_input(self, command):
        """This function handles input for basic navigation menu"""
        if not self.is_root and command == "b":
            return "back"
        elif command == "q":
            return "quit"


class HelpfulMenu(BasicNavigationMenu):
    """An abstract menu class that represents
    a menu that displays a help message"""

    @abstractmethod
    def _help_message(self):
        pass

    @abstractmethod
    def show(self):
        print("h. Help")
        super().show()

    @abstractmethod
    def handle_input(self, command):
        """This function handles input for a helpful menu"""
        if command == "h":
            self._user_message = self._help_message()
            return "self"
        return super().handle_input(command)


class SimpleMenu(BasicNavigationMenu):
    """This class is for simple menu"""

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
        """This finction handles input for a simple menu"""
        if command.isdigit():
            choice = int(command) - 1
            if choice < len(self.options):
                if len(self.options[choice]) == 3:
                    return self.options[choice][1](self.options[choice][2])
                else:
                    return self.options[choice][1]()
        return super().handle_input(command)
