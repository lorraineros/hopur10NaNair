from src.models.models import Contractor, Employee, RealEstate, WorkRequest, WorkReport
from src.logic.logic_api import LogicAPI
from src.ui.abstract_menu import SimpleMenu
from src.logic.work_request_logic import WorkRequestLogic
from src.logic.employee_logic import EmployeeLogic
from src.logic.work_report_logic import WorkReportLogic
from src.ui.common_menus import BackQuitMenu, CreationMenu, ChangingMenu
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
        print(f"{'--- List of Work Request ---':^94}")
        print("-" * 94)
        print(
            f"| {'ID':^2} | {'Title':^43} | {'Real estate':^11} | {'From':^11} | {'To':^11} |"
        )
        print("-" * 94)
        for (work_id, work) in LogicAPI().get_all(WorkRequest).items():
            print(
                f"| {work.id:<2} | {work.title:<43} | {work.real_estate:<11} | {work.start_date:<11} | {work.end_date:<11} |"
            )
        print("-" * 94)

    def print_work_request(self, work):
        print(
            """
Title: {}
Location: {}
Real Estate: {}
Priority: {}
Description: {}
        """.format(
                work.title,
                work.location,
                work.real_estate,
                work.priority,
                work.description,
            )
        )
    
    def print_work_report(self, work):
        employee = LogicAPI().get(Employee, work.employee_id)
        contractor = LogicAPI().get(Contractor, work.contractor_id)
        print(
            """
Employee: {}
Contractors: {}
Contractor's fee: {}
Description: {}
Material Cost: {}
Date: {}
Ready: {}
Comment: {}
        """.format(
                employee.name,
                contractor.name,
                work.contractors_fee,
                work.description,
                work.material_cost,
                work.date,
                work.ready,
                work.comment,
            )
        )


class FindWorkRequestMenu(WorkRequestMenu): 
    def show(self):
        print("--- Find Work Menu ---")
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
            real_est_input = self.real_estate_input()

            work_report_exist_emp = LogicAPI().real_est_work_check(real_est_input)
            if not work_report_exist_emp:
                print("There is no work request for {}.".format(real_est_input.real_estate_number))
                print()
                return BackQuitMenu()

            print()
            self.display_work_by_real_estate(real_est_input)
            self.find_work_by_id()
            return ChangingMenu()
        elif command == "3":
            print("Find Work by Employee:")
            print()
            EmployeeMenu().display_all_employees()
            emp_input = self.emp_input()

            work_report_exist_emp = LogicAPI().emp_work_check(emp_input)
            if not work_report_exist_emp:
                print("There is no work request for {}.".format(emp_input.name))
                print()
                return BackQuitMenu()

            print()
            self.display_work_by_employee(emp_input)
            self.find_work_by_id()
            return ChangingMenu()
        elif command == "4":
            print("Find Work by Contractor:")
            print()
            ContractorMenu().display_all_contractors()
            contr_input = self.contr_input()

            work_report_exist_contr = LogicAPI().contr_work_check(contr_input)
            if not work_report_exist_contr:
                print("There is no work request for {}.".format(contr_input.name))
                print()
                return BackQuitMenu()

            print()
            self.display_work_by_contractor(contr_input)
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
        print()
        print(f"--- Work Request ---")
        self.print_work_request(work)

        work_report_id = 0
        for (workr_id, workr) in LogicAPI().get_all(WorkReport).items():
            if workr.work_request_id ==int(id):
                work_report_id = workr_id
        
        if work_report_id:
            workr = LogicAPI().get(WorkReport, int(work_report_id))
            print(f"--- Work Report ---")
            self.print_work_report(workr)

    def real_estate_input(self):
        real_est_id = input("Enter real estate ID to choose a work request: ")
        is_real_est_id = LogicAPI().real_estate_id_check(real_est_id)

        while not is_real_est_id:
            print("Sorry did not find Real Estate, try again.")
            real_est_id = input("Enter real estate ID to choose a work request: ")
            is_real_est_id = LogicAPI().real_estate_id_check(real_est_id)

        real_est = LogicAPI().get(RealEstate, int(real_est_id))
        return real_est

    def display_work_by_real_estate(self, real_est):
        print(f"{'--- List of Work Requests by {} ---':^94}".format(real_est.real_estate_number))
        print("-" * 94)
        print(
            f"| {'ID':^2} | {'Title':^43} | {'Real estate':^11} | {'From':^11} | {'To':^11} |"
        )
        print("-" * 94)
        for (work_id, work) in LogicAPI().get_all(WorkRequest).items():
            if work.real_estate == real_est.real_estate_number:
                print(
                    f"| {work.id:<2} | {work.title:<43} | {work.real_estate:<11} | {work.start_date:<11} | {work.end_date:<11} |"
            )
        print("-" * 94)

    def emp_input(self):
        emp_id = input("Enter employee id to choose a work request: ")
        is_emp_id = LogicAPI().employee_id_check(emp_id)

        while not is_emp_id:
            print("Sorry, did not find employee, try again.")
            emp_id = input("Enter employee id to choose a work request: ")
            is_emp_id = LogicAPI().employee_id_check(emp_id)

        emp = LogicAPI().get(Employee, int(emp_id))
        return emp

    def display_work_by_employee(self, emp):
        print(f"{'--- List of Work Requests by {} ---':^94}".format(emp.name))
        print("-" * 94)
        print(
            f"| {'ID':^2} | {'Title':^43} | {'Real estate':^11} | {'From':^11} | {'To':^11} |"
        )
        print("-" * 94)
        for (work_id, work) in LogicAPI().get_all(WorkRequest).items():
            for (workr_id, workr) in LogicAPI().get_all(WorkReport).items():
                if workr.employee_id == emp.id and work_id == workr.work_request_id:
                    print(
                        f"| {work.id:<2} | {work.title:<43} | {work.real_estate:<11} | {work.start_date:<11} | {work.end_date:<11} |"
                )
        print("-" * 94)

    def contr_input(self):
        contr_id = input("Enter contractor id to choose a work request: ")
        is_contr_id = LogicAPI().contractor_id_check(contr_id)

        while not is_contr_id:
            print("Sorry, did not find contractor, try again.")
            contr_id = input("Enter contractor id to choose a work request: ")
            is_contr_id = LogicAPI().contractor_id_check(contr_id)

        contr = LogicAPI().get(Contractor, int(contr_id))
        return contr

    def display_work_by_contractor(self, contr):
        print(f"{'--- List of Work Requests by {} ---':^94}".format(contr.name))
        print("-" * 94)
        print(
            f"| {'ID':^2} | {'Title':^43} | {'Real estate':^11} | {'From':^11} | {'To':^11} |"
        )
        print("-" * 94)
        for (work_id, work) in LogicAPI().get_all(WorkRequest).items():
            for (workr_id, workr) in LogicAPI().get_all(WorkReport).items():
                if workr.contractor_id == contr.id and work_id == workr.work_request_id:
                    print(
                        f"| {work.id:<2} | {work.title:<43} | {work.real_estate:<11} | {work.start_date:<11} | {work.end_date:<11} |"
                )
        print("-" * 94)

    def display_work_by_date(self):
        date = input("Enter date to choose a work request (YYYY-MM-DD): ")

        print(f"{'--- List of Work Requests by {} ---':^94}".format(date))
        print("-" * 94)
        print(
            f"| {'ID':^2} | {'Title':^43} | {'Real estate':^11} | {'From':^11} | {'To':^11} |"
        )
        print("-" * 94)
        for (work_id, work) in LogicAPI().get_all(WorkRequest).items():
            if work.start_date == date or work.end_date == date:
                print(
                    f"| {work.id:<2} | {work.title:<43} | {work.real_estate:<11} | {work.start_date:<11} | {work.end_date:<11} |"
            )
        print("-" * 94)

    def find_work_by_period(self): # To-Do: Need to rethink the dates for work request!
        start_date = input("Enter start date (YYYY-MM-DD): ")
        end_date = input("Enter end date (YYYY-MM-DD): ")

        print(
            f"{'--- List of Work Requests by {} - {} ---':^94}".format(
                start_date, end_date
            )
        )
        print("-" * 94)
        print(
            f"| {'ID':^2} | {'Title':^43} | {'Real estate':^11} | {'From':^11} | {'To':^11} |"
        )
        print("-" * 94)
        for (work_id, work) in LogicAPI().get_all(WorkRequest).items():
            if work.start_date == start_date and work.end_date == end_date:
                print(
                    f"| {work.id:<2} | {work.title:<43} | {work.real_estate:<11} | {work.start_date:<11} | {work.end_date:<11} |"
            )
        print("-" * 94)


