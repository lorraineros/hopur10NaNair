#!/usr/bin/env python3

from src.storage.employee_storage import EmployeeStorage
from src.ui.ui import App


if __name__ == "__main__":
    app = App()
    EmployeeStorage.get_all()
    print("Thank you for using NaNAir")
