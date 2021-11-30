from ..storage.work_request_storage import WorkRequestStorage


class WorkRequestLogic:
    def get_list():
        return WorkRequestStorage.get_all()
