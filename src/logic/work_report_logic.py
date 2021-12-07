from src.models.models import WorkReport
from src.storage.storage import StorageAPI
from ..storage.work_report_storage import WorkReportStorage

class WorkReportLogic:
    def get_list():
        return WorkReportStorage.get_all()
    
    def id_check(self, id_input):
        for (work_id, work) in StorageAPI().get_all(WorkReport).items():
            if str(work.id) == str(id_input):
                return True
        return False

    def yes_no_check(self, yes_no_input):
        if str(yes_no_input).upper() == "Y" or str(yes_no_input).upper() == "N":
            return True
        return False
    
    def emp_work_check(self, emp):
        for (work_id, work) in StorageAPI().get_all(WorkReport).items():
            if work.employee == emp.id:
                return True
        return False


    def contr_work_check(self, contr):
        for (work_id, work) in StorageAPI().get_all(WorkReport).items():
            if work.contractor == contr.id:
                return True
        return False