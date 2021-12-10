from src.logic.logic_api import LogicAPI
from src.models.models import Contractor, Destination
from src.ui.abstract_menu import AbstractMenu, SimpleMenu
from src.ui.common_menus import BackQuitMenu, ChangingMenu
from src.ui.creation_menu import CreationMenu
from src.ui.list_menu import EditPickerMenu


class ContractorMenu(SimpleMenu):
    """This class is for contract menu"""
    @property
    def header(self):
        return "--- Contractor Menu ---"

    @property
    def options(self):
        if self.is_manager:
            return [
                ("Register a new contractor", CreationMenu, Contractor),
                ("List of contractors", EditPickerMenu, Contractor)
            ]
        else:
            return[
                ("List of contractors", EditPickerMenu, Contractor)
            ]
    
    def name(self):
        return f"Contractor Menu"
            
    # def show(self):
    #     print("1. Register a new contractor")
    #     print("2. Display list of contractors")
    #     print("b. Back")
    #     print("q. Quit")

    # def handle_input(self, command):
    #     """This function handles input for contractor menu"""
    #     if command == "1":
    #         return CreationMenu(Contractor)
    #     elif command == "2":
    #         return EditPickerMenu(Contractor)
    #     elif command == "b":
    #         return "back"
    #     elif command == "q":
    #         return "quit"

#     def display_all_contractors(self):
#         """This function displays all contractors"""
#         print(f"{'--- List of Contractor ---':^45}")
#         print("-" * 45)
#         print(f"| {'ID':^3} | {'Name':^16} | {'Location':^16} |")
#         print("-" * 45)
#         for (contr_id, contr) in LogicAPI().get_all(Contractor).items():
#             contr_location = LogicAPI().get(Destination, contr.location)
#             print(f"| {contr.id:<3} | {contr.name_of_company:<16} | {contr_location.name:<16} |")
#         print("-" * 45)
#         print()

#     def find_contractor(self):
#         """This function helps finding specific all contractors"""
#         id_input = input("Enter ID to choose a contractor: ")
#         is_id = LogicAPI().contractor_id_check(id_input)

#         while not is_id:
#             print("Sorry did not find address, try again.")
#             id_input = input("Enter ID to choose a contractor: ")
#             is_id = LogicAPI().contractor_id_check(id_input)

#         contr = LogicAPI().get(Contractor, int(id_input))
#         self.print_contractor(contr)
#         print()

#     def print_contractor(self, contr):
#         """This function prints contractors"""
#         contr_location = LogicAPI().get(Destination, contr.location)
#         print(
#             """
# ID: {}
# Name: {}
# Name of Contact: {}
# Phone Number: {}
# Working hours: {}
# Location: {}
#         """.format(
#                 contr.id,
#                 contr.name,
#                 contr.name_of_contact,
#                 contr.phone,
#                 contr.working_hours,
#                 contr_location.name,
#             )
#         )
