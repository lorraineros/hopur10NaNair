from ..storage.employee_storage import EmployeeStorage


class LogicAPI:
    def employee_list(self):
        return EmployeeStorage.get_all()
