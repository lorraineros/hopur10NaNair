from ..storage.contractor_storage import ContractorStorage


class ContractorLogic:

    def get_list():
        return ContractorStorage.get_all()
