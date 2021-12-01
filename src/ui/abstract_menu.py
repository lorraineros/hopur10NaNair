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
