from ..storage.work_report_storage import WorkReportStorage

class WorkReportLogic:
    def get_list():
        return WorkReportStorage.get_all()