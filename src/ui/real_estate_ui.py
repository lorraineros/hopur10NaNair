from src.logic.logic_api import LogicAPI
from src.models.models import Destination, RealEstate
from src.ui.abstract_menu import AbstractMenu, SimpleMenu
from src.ui.common_menus import BackQuitMenu, ChangingMenu
from src.ui.creation_menu import CreationMenu
from src.ui.destination_ui import DestinationMenu
from src.ui.list_menu import EditPickerMenu


class RealEstateMenu(SimpleMenu):
    @property
    def header(self):
        return "--- Real Estate ---"
    
    @property
    def options(self):
        if self.is_manager:
            return [
                ("Register a new real estate", CreationMenu, RealEstate),
                ("List of real estate", EditPickerMenu, RealEstate),
            ]
        else:
            return[
                ("List of real estate", EditPickerMenu, RealEstate)
            ]


    # def show(self):
    #     """This function shows the menu for Real Estate"""
    #     print("--- Real Estate Menu ---")
    #     print("1. Register a new real estate")
    #     print("2. Display list of real estate")
    #     print("b. Back")
    #     print("q. Quit")

    # def handle_input(self, command):
    #     """This function handles input for the RealEstateMenu"""
    #     if command == "1":
    #         return CreationMenu(RealEstate)
    #     elif command == "2":
    #         return EditPickerMenu(RealEstate)
    #     elif command == "b":
    #         return "back"
    #     elif command == "q":
    #         return "quit"

    # def display_all_real_estate(self):
    #     """Display a list of all the real estate"""
    #     print(f"{'--- List of Real Estate ---':^70}")
    #     print("-" * 70)
    #     print(
    #         f"| {'ID':^3} | {'Address':^21} | {'Real Estate Number':^18} | {'Destination':^15} |"
    #     )
    #     print("-" * 70)
    #     for (real_est_id, real_est) in LogicAPI().get_all(RealEstate).items():
    #         dest = LogicAPI().get(Destination, real_est.destination)
    #         print(
    #             f"| {real_est.id:<3} | {real_est.address:<21} | {real_est.real_estate_number:<18} | {dest.name:<15} |"
    #         )
    #     print("-" * 70)
    #     print()

    # def print_addresses(self):
    #     """This function prints all possible addresses that a real estate can have."""
    #     list_of_addresses = LogicAPI().address_list()
    #     print(f"{'--- List of Addresses ---':^30}")
    #     print("-" * 30)
    #     print(f"| {'ID':^2} | {'Addresses':^21} |")
    #     print("-" * 30)
    #     for i in range(len(list_of_addresses)):
    #         address = list_of_addresses[i]
    #         print(f"| {i+1:<2} | {address:<21} |")
    #     print("-" * 30)
    #     print()

    # def display_real_estate_by_dest(self):
    #     """This function displays a list of real estate filtered by a destination, i.e. displays only the real estates by a certain destination."""
    #     DestinationMenu().list_of_all_destinations()
    #     dest_input = input("Enter Destination ID to filter Real Estate: ")
    #     is_dest = LogicAPI().dest_check(dest_input)

    #     while not is_dest:
    #         print("Sorry did not find Destination ID, try again.")
    #         dest_input = input("Enter Destination ID to filter Real Estate: ")
    #         is_dest = LogicAPI().dest_check(dest_input)

    #     dest = LogicAPI().get(Destination, int(dest_input))

    #     print()
    #     print(f"{'--- List of Real Estate by {} ---':^70}".format(dest.name))
    #     print("-" * 70)
    #     print(
    #         f"| {'ID':^3} | {'Address':^21} | {'Real Estate Number':^18} | {'Destination':^15} |"
    #     )
    #     print("-" * 70)
    #     for (real_est_id, real_est) in LogicAPI().get_all(RealEstate).items():
    #         if real_est.destination == int(dest_input):
    #             dest = LogicAPI().get(Destination, real_est.destination)
    #             print(
    #                 f"| {real_est.id:<3} | {real_est.address:<21} | {real_est.real_estate_number:<18} | {dest.name:<15} |"
    #             )
    #     print("-" * 70)
    #     print()

#     def print_real_estate(self, real_est):
#         destination = LogicAPI().get(Destination, real_est.destination)
#         print(
#             """
# Address: {}
# Real Estate Number: {}
# Destination: {}
# Condition: {}
# Facilities: {}
# Type of Real Estate: {}
# Rooms: {}
# Size: {} """.format(
#                 real_est.address,
#                 real_est.real_estate_number,
#                 destination.name,
#                 real_est.condition,
#                 real_est.facilities,
#                 real_est.type_of_real_estate,
#                 real_est.rooms,
#                 real_est.size,
#             )
#         )


# class RealEstateSearch(RealEstateMenu):
#     def show(self):
#         """Displays a menu that gives option how to search for a Real Estate"""
#         print("--- Find a Real Estate ---")
#         print("1. By ID")
#         print("2. By real estate number")
#         print("3. By address")
#         print("4. By destination")
#         print("b. Back")
#         print("q. Quit")

#     def handle_input(self, command):
#         if command == "1":
#             print(f"{'--- Find Real Estate by ID ---':^52}")
#             self.display_all_real_estate()
#             print()
#             self.find_real_estate_by_id()
#             return ChangingMenu()
#         elif command == "2":
#             print(f"{'--- Find Real Estate by Real Estate Number ---':^52}")
#             self.display_all_real_estate()
#             print()
#             self.find_real_estate_by_re_num()
#             return ChangingMenu()
#         elif command == "3":
#             print(f"{'--- Find Real Estate by Address ---':^52}")
#             print()
#             self.find_real_estate_by_address()
#             self.find_real_estate_by_id()
#             return ChangingMenu()
#         elif command == "4":
#             print(f"{'--- Find Real Estate by Destination ---':^52}")
#             print()
#             self.display_real_estate_by_dest()
#             self.find_real_estate_by_id()
#             return ChangingMenu()
#         elif command == "b":
#             return "back"
#         elif command == "q":
#             return "quit"

#     def find_real_estate_by_id(self):  # To-Do: Need to create a id_check function.
#         """This function finds the Real Estate given the ID inputed and prints it."""
#         id_input = input("Enter ID to choose a Real Estate: ")
#         is_id = LogicAPI().real_estate_id_check(id_input)

#         while not is_id:
#             print("Sorry did not find address, try again.")
#             id_input = input("Enter ID to choose Real Estate: ")
#             is_id = LogicAPI().real_estate_id_check(id_input)

#         real_est = LogicAPI().get(RealEstate, int(id_input))
#         self.print_real_estate(real_est)
#         # print(real_est)

#         print()

#     def find_real_estate_by_re_num(self):
#         """This function finds the Real Estate given the Real Estate Number inputed and prints it."""
#         re_num_input = input("Enter Real Estate Number to choose a Real Estate: ")
#         is_re_num = LogicAPI().re_num_check(re_num_input)

#         while not is_re_num:
#             print("Sorry did not find Real Estate Number, try again.")
#             re_num_input = input("Enter Real Estate Number to choose Real Estate: ")
#             is_re_num = LogicAPI().re_num_check(re_num_input)

#         for (real_est_id, real_est) in LogicAPI().get_all(RealEstate).items():
#             if real_est.real_estate_number == re_num_input:
#                 self.print_real_estate(real_est)
#                 # print(real_est)

#         print()

#     def find_real_estate_by_address(self):
#         """This function displays a list of real estate filtered by a address, i.e. displays only the real estates by a certain address."""
#         self.print_addresses()
#         address_input = input("Enter address ID to filter Real Estate: ")
#         address = LogicAPI().address_list()[int(address_input) - 1]
#         is_address = LogicAPI().address_check(address)

#         while not is_address:
#             print("Sorry did not find address, try again.")
#             address_input = input("Enter address to see Real Estate: ")
#             is_address = LogicAPI().address_check(address)

#         print(f"{'--- List of Real Estate by Address ---':^52}")
#         print("-" * 52)
#         print(f"| {'ID':^3} | {'Address':^21} | {'Real Estate Number':^18} |")
#         print("-" * 52)
#         for (real_est_id, real_est) in LogicAPI().get_all(RealEstate).items():
#             if real_est.address == address:
#                 print(
#                     f"| {real_est.id:<3} | {real_est.address:<21} | {real_est.real_estate_number:<18} |"
#                 )
#         print("-" * 52)
#         print()
