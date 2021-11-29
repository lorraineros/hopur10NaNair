from ..storage.employee_storage import EmployeeStorage


class EmployeeLogic:
    def get_list():
        return EmployeeStorage.get_all()
