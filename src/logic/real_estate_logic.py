from ..storage.real_estate_storage import RealEstateStorage


class RealEstateLogic:
    def get_list():
        return RealEstateStorage.get_all()