from src.models.models import Employee
from src.storage.storage import StorageAPI
from ..storage.employee_storage import EmployeeStorage


class EmployeeLogic:

    def get_list():
        return EmployeeStorage.get_all()

    def id_check(self, id_input):
        for (emp_id, emp) in StorageAPI().get_all(Employee).items():
            if str(emp.id) == str(id_input):
                return True
        return False

    def yes_no_check(self, yes_no_input):
        if str(yes_no_input).upper() == "Y" or str(yes_no_input).upper() == "N":
            return True
        return False
