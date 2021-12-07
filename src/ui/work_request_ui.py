from src.models.models import Contractor, Employee, RealEstate, WorkRequest
from src.logic.logic_api import LogicAPI
from src.ui.abstract_menu import SimpleMenu
from src.logic.work_request_logic import WorkRequestLogic
from src.logic.employee_logic import EmployeeLogic
from src.ui.common_menus import CreationMenu, ChangingMenu
from src.ui.real_estate_ui import RealEstateMenu
from src.ui.employee_ui import EmployeeMenu
from src.ui.contractor_ui import ContractorMenu


class WorkRequestMenu(SimpleMenu):
    @property
    def header(self):
        return "--- Work requests ---"

    @property
    def options(self):
        return [
            ("Register a new work request", CreationMenu, WorkRequest),
            ("Find work request", FindWorkRequestMenu),
        ]

    def display_all_works(self):
        print(f"{'--- List of Work Request ---':^66}")
        print("-" * 66)
        print(
            f"| {'ID':^2} | {'Title':^43} | {'Real estate':^11} |"
        )
        print("-" * 66)
        for (work_id, work) in LogicAPI().get_all(WorkRequest).items():
            print(
                f"| {work.id:<2} | {work.title:<43} | {work.real_estate:<11} |"
            )
        print("-" * 66)

    def print_work(self, work):
        employee = LogicAPI().get(Employee, work.employee)
        contractor = LogicAPI().get(Contractor, work.contractor)
        print(
            """
Title: {}
Location: {}
Real Estate: {}
Employee: {}
Contractor: {}
Priority: {}
Description: {}
        """.format(
                work.title,
                work.location,
                work.real_estate,
                employee.name,
                contractor.name,
                work.priority,
                work.description,
            )
        )


class FindWorkRequestMenu(WorkRequestMenu): # To-Do: Create a function that checks if there is a work request for inputed filter and if not print No Work Request for filter
    def show(self):
        print("--- Find Work Request Menu ---")
        print("1. By ID")
        print("2. By real estate")
        print("3. By employee")
        print("4. By contractor")
        print("5. By date")
        print("6. By period")
        print("b. Back")
        print("q. Quit")

    def handle_input(self, command):
        if command == "1":
            print("Find Work by ID:")
            print()
            self.display_all_works()
            self.find_work_by_id()
            return ChangingMenu()
        elif command == "2":
            print("Find Work by Real Estate:")
            print()
            RealEstateMenu().display_all_real_estate()
            self.display_work_by_real_estate()
            self.find_work_by_id()
            return ChangingMenu()
        elif command == "3":
            print("Find Work by Employee:")
            print()
            EmployeeMenu().display_all_employees()
            self.display_work_by_employee()
            self.find_work_by_id()
            return ChangingMenu()
        elif command == "4":
            print("Find Work by Contractor:")
            print()
            ContractorMenu().display_all_contractors()
            self.display_work_by_contractor()
            self.find_work_by_id()
            return ChangingMenu()
        elif command == "5":
            print("Find Work by Date:")
            print()
            self.display_all_works()
            self.display_work_by_date()
            self.find_work_by_id()
            return ChangingMenu()
        elif command == "6":
            print("Find Work by Period:")
            print()
            self.display_all_works()
            self.find_work_by_period()
            self.find_work_by_id()
            return ChangingMenu()
        elif command == "b":
            return "back"
        elif command == "q":
            return "quit"

    def find_work_by_id(self):
        id = input("Enter id to choose a work request: ")
        is_id = LogicAPI().work_id_check(id)

        while not is_id:
            print("Sorry did not find work request, try again.")
            id = input("Enter id to choose a work request: ")
            is_id = LogicAPI().work_id_check(id)

        work = LogicAPI().get(WorkRequest, int(id))
        self.print_work(work)

    def display_work_by_real_estate(self):
        real_est_id = input("Enter real estate ID to choose a work request: ")
        is_real_est_id = LogicAPI().real_estate_id_check(real_est_id)

        while not is_real_est_id:
            print("Sorry did not find Real Estate, try again.")
            real_est_id = input("Enter real estate ID to choose a work request: ")
            is_real_est_id = LogicAPI().real_estate_id_check(real_est_id)

        real_est = LogicAPI().get(RealEstate, int(real_est_id))
        print()
        print(f"{'--- List of Work Requests by {} ---':^66}".format(real_est.real_estate_number))
        print("-" * 66)
        print(
            f"| {'ID':^2} | {'Title':^43} | {'Real estate':^11} |"
        )
        print("-" * 66)
        for (work_id, work) in LogicAPI().get_all(WorkRequest).items():
            if work.real_estate == real_est.real_estate_number:
                print(
                    f"| {work.id:<2} | {work.title:<43} | {work.real_estate:<11} |"
                )
        print("-" * 66)

    def display_work_by_employee(self):
        emp_id = input("Enter employee id to choose a work request: ")
        is_emp_id = LogicAPI().employee_id_check(emp_id)

        while not is_emp_id:
            print("Sorry, did not find employee, try again.")
            emp_id = input("Enter employee id to choose a work request: ")
            is_emp_id = LogicAPI().employee_id_check(emp_id)

        emp = LogicAPI().get(Employee, int(emp_id))
        print()
        print(f"{'--- List of Work Requests by {} ---':^85}".format(emp.name))
        print("-" * 85)
        print(
            f"| {'ID':^2} | {'Title':^43} | {'Real estate':^11} | {'Employee':^15} |"
        )
        print("-" * 85)
        for (work_id, work) in LogicAPI().get_all(WorkRequest).items():
            if work.employee == emp.id:
                print(
                    f"| {work.id:<2} | {work.title:<43} | {work.real_estate:<11} | {emp.name:<15} |"
                )        
        print("-" * 85)

    def display_work_by_contractor(self):
        contr_id = input("Enter contractor id to choose a work request: ")
        is_contr_id = LogicAPI().contractor_id_check(contr_id)

        while not is_contr_id:
            print("Sorry, did not find contractor, try again.")
            contr_id = input("Enter contractor id to choose a work request: ")
            is_contr_id = LogicAPI().contractor_id_check(contr_id)

        contr = LogicAPI().get(Contractor, int(contr_id))
        print(f"{'--- List of Work Requests by {} ---':^84}".format(contr.name))
        print("-" * 84)
        print(
            f"| {'ID':^2} | {'Title':^43} | {'Real estate':^11} | {'Contractor':^15} |"
        )
        print("-" * 84)
        for (work_id, work) in LogicAPI().get_all(WorkRequest).items():
            if work.contractor == contr.id:
                print(
                    f"| {work.id:<2} | {work.title:<43} | {work.real_estate:<11} | {contr.name:<15} |"
                ) 
        print("-" * 84)

    def display_work_by_date(self): # To-Do: Need to rethink the dates for work request!
        date = input("Enter date to choose a work request (YYYY-MM-DD): ")

        print(f"{'--- List of Work Requests by {} ---':^138}".format(date))
        print("-" * 138)
        print(
            f"| {'ID':^2} | {'Title':^43} | {'Real estate':^11} |  {'Employee':^19} |  {'Contractor':^19} | {'From':^10} | {'To':^10} |"
        )
        print("-" * 138)
        for work in WorkRequestLogic.get_list():
            for emp in EmployeeLogic.get_list():
                for (contr_id, contr) in LogicAPI().get_all(Contractor).items():
                    if (
                        work.employee == emp.id
                        and work.contractor == contr.id
                        and (work.start_date == date or work.end_date == date)
                    ):
                        print(
                            f"| {work.id:<2} | {work.title:<43} | {work.real_estate:<11} | {emp.id}. {emp.name:<17} | {contr.id}. {contr.name:<17} | {work.start_date:<7} | {work.end_date:<7} |"
                        )
        print("-" * 138)

    def find_work_by_period(self): # To-Do: Need to rethink the dates for work request!
        start_date = input("Enter start date (YYYY-MM-DD): ")
        end_date = input("Enter end date (YYYY-MM-DD): ")

        print(
            f"{'--- List of Work Requests by {} - {} ---':^138}".format(
                start_date, end_date
            )
        )
        print("-" * 138)
        print(
            f"| {'ID':^2} | {'Title':^43} | {'Real estate':^11} |  {'Employee':^19} |  {'Contractor':^19} | {'From':^10} | {'To':^10} |"
        )
        print("-" * 138)
        for work in WorkRequestLogic.get_list():
            for emp in EmployeeLogic.get_list():
                for (contr_id, contr) in LogicAPI().get_all(Contractor).items():
                    if (
                        work.employee == emp.id
                        and work.contractor == contr.id
                        and work.start_date == start_date
                        and work.end_date == end_date
                    ):
                        print(
                            f"| {work.id:<2} | {work.title:<43} | {work.real_estate:<11} | {emp.id}. {emp.name:<17} | {contr.id}. {contr.name:<17} | {work.start_date:<7} | {work.end_date:<7} |"
                        )
        print("-" * 138)


