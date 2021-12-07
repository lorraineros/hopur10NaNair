from src.models.models import WorkRequest
from src.storage.storage import StorageAPI
from ..storage.work_request_storage import WorkRequestStorage


class WorkRequestLogic:
    def get_list():
        return WorkRequestStorage.get_all()

    def id_check(self, id_input):
        for (work_id, work) in StorageAPI().get_all(WorkRequest).items():
            if str(work.id) == str(id_input):
                return True
        return False

    def yes_no_check(self, yes_no_input):
        if str(yes_no_input).upper() == "Y" or str(yes_no_input).upper() == "N":
            return True
        return False
    
    def real_est_work_check(self, real_est):
        for (work_id, work) in StorageAPI().get_all(WorkRequest).items():
            if work.real_estate == real_est.real_estate_number:
                return True
        return False


