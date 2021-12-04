from src.storage.user_stories_storage import UserStories

class UserStories:
    def user_stories_list(self):
        return UserStories.get_all()

    def get_address_list(self):
        list_of_addresses = []
        for user_stor in self.get_user_stories_list():
            if user_stor not in list_of_addresses:
                list_of_addresses.append(user_stor.address)


        return list_of_addresses

    
    def address_check(self, address_input):
        list_of_address = self.get_address_list()

        if address_input in list_of_address:
            return True 
        else:
            return False

    
    def id_check(self, id_input):
        for user_stor in self.get_user_stories_list():
            if str(user_stor.id) == str(id_input):
                return True
        return False

    def re_num_check(self, us_num_input):
        for user_stor in self.get_stories_list():
            if user_stor.real_estate_number.lower() == us_num_input.lower():
                return True
        return False
