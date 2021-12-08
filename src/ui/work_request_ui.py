from src.logic.logic_api import LogicAPI
from src.models.models import Contractor, Employee, RealEstate, WorkReport, WorkRequest
from src.ui.abstract_menu import SimpleMenu
from src.ui.common_menus import BackQuitMenu, ChangingMenu
from src.ui.creation_menu import CreationMenu
from src.ui.contractor_ui import ContractorMenu
from src.ui.employee_ui import EmployeeMenu
from src.ui.list_menu import EditPickerMenu
from src.ui.real_estate_ui import RealEstateMenu
from datetime import datetime


class WorkRequestMenu(SimpleMenu):
    @property
    def header(self):
        return "--- Work requests ---"

    @property
    def options(self):
        return [
            ("Register a new work request", CreationMenu, WorkRequest),
            ("Find work request", FindWorkRequestMenu),
            ("List of work requests", EditPickerMenu, WorkRequest),
        ]

    def display_all_work_requests(self):
        print()
        print(f"{'--- List of Work Requests ---':^94}")
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

    def display_all_work_reports(self):
        print()
        print(f"{'--- List of Work Reports ---':^114}")
        print("-" * 114)
        print(
            f"| {'ID':^2} | {'Work Request':^48} | {'Employee':^21} | {'Contractor':^16} | {'Date':^11} |"
        )
        print("-" * 114)
        for (workr_id, workr) in LogicAPI().get_all(WorkReport).items():
            work_request = LogicAPI().get(WorkRequest, workr.work_request_id)
            emp = LogicAPI().get(Employee, workr.employee_id)
            contr = LogicAPI().get(Contractor, workr.contractor_id)
            print(
                f"| {workr.id:<2} | {workr.work_request_id:<2} | {work_request.title:<43} | {emp.name:<21} | {contr.name:<16} | {workr.date:<11} |"
            )
        print("-" * 114)

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

    def print_work_report(self, workr):
        employee = LogicAPI().get(Employee, workr.employee_id)
        contractor = LogicAPI().get(Contractor, workr.contractor_id)
        if workr.ready:
            is_ready = "Yes"
        else:
            is_ready = "No"
        print(
            """
ID: {}
Employee: {}
Contractors: {}
Contractor's fee: {}
Description: {}
Material Cost: {}
Date: {}
Ready: {}
Comment: {}
        """.format(
                workr.id,
                employee.name,
                contractor.name,
                workr.contractors_fee,
                workr.description,
                workr.material_cost,
                workr.date,
                is_ready,
                workr.comment,
            )
        )
    def approve_work(self, work, work_report_list):
        approve_input = input("Do you want to accept work report (Y/N)? ")
    
        if approve_input.lower() == "y":
            id = input("Enter id to choose a work report: ")
            is_id = LogicAPI().work_report_id_check(id)

            while not is_id:
                print("Sorry did not find work request, try again.")
                id = input("Enter id to choose a work report: ")
                is_id = LogicAPI().work_report_id_check(id)

            ready = True
            for workr in work_report_list:
                workr = LogicAPI().get(WorkReport, int(id))
                if not workr.ready:
                    ready = False
            
            print()
            if ready:
                work.is_open = 0 # Need to change the value of is_open in json file
                print("Work report is approved successfully!")
            else:
                print("Work report is not ready to approve")
            print()

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
            self.display_all_work_requests()
            #self.display_all_work_reports()
            self.find_work_by_id()
            return ChangingMenu()
        elif command == "2":
            print("Find Work by Real Estate:")
            print()
            RealEstateMenu().display_all_real_estate()
            real_est_input = self.real_estate_input()

            work_report_exist_emp = LogicAPI().real_est_work_check(real_est_input)
            if not work_report_exist_emp:
                print(
                    "There is no work request for {}.".format(
                        real_est_input.real_estate_number
                    )
                )
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
            self.display_all_work_requests()
            self.display_all_work_reports()
            self.display_work_by_date()
            self.find_work_by_id()
            return ChangingMenu()
        elif command == "6":
            print("Find Work by Period:")
            print()
            self.display_all_work_requests()
            self.display_all_work_reports()
            self.find_work_by_period()
            self.find_work_by_id()
            return ChangingMenu()
        elif command == "b":
            return "back"
        elif command == "q":
            return "quit"

    def find_work_by_id(self):
        id = input("Enter work request id to choose a work request: ")
        is_id = LogicAPI().work_id_check(id)

        while not is_id:
            print("Sorry did not find work request, try again.")
            id = input("Enter id to choose a work request: ")
            is_id = LogicAPI().work_id_check(id)

        work = LogicAPI().get(WorkRequest, int(id))
        print()
        print(f"--- Work Request ---")
        self.print_work_request(work)

        work_report_list = []
        for (workr_id, workr) in LogicAPI().get_all(WorkReport).items():
            if workr.work_request_id == int(id):
                work_report_list.append(workr_id)

        if work_report_list:
            print(f"--- Work Report ---")
            for work_report in work_report_list:
                workr = LogicAPI().get(WorkReport, int(work_report))
                self.print_work_report(workr)
            self.approve_work(work, work_report_list)
    
    def convert_to_datetime(self, work):
        year, month, day = work.start_date.split("-")
        date_start = datetime(int(year), int(month), int(day))
        year_end, month_end, day_end = work.end_date.split("-")
        date_end = datetime(int(year_end), int(month_end), int(day_end))
        return date_start, date_end
    
    def period_input(self):
        start_date = input("Enter start date (YYYY-MM-DD): ")
        end_date = input("Enter end date (YYYY-MM-DD): ")
        start_year, start_month, start_day = start_date.split("-")
        end_year, end_month, end_day = end_date.split("-")
        start = datetime(int(start_year), int(start_month), int(start_day))
        end = datetime(int(end_year),int(end_month), int(end_day))
        return start_date, end_date, start, end

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
        by_time_range = input("Do you want to display work done in a specific time range(Y/N)? ")
        print()
        if by_time_range.lower() == "y":
            self.display_work_by_real_estate_in_time_range(real_est)
        else:
            print(
                f"{'--- List of Work Requests by {} ---':^94}".format(
                    real_est.real_estate_number
                )
            )
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

    def display_work_by_real_estate_in_time_range(self, real_est):
        start_date, end_date, start, end = self.period_input()
        print(
            f"{'--- List of Work Requests by {} in time range {} - {} ---'}".format(
                real_est.real_estate_number, start_date, end_date
            )
        )
        print("-" * 94)
        print(
            f"| {'ID':^2} | {'Title':^43} | {'Real estate':^11} | {'From':^11} | {'To':^11} |"
        )
        print("-" * 94)
        for (work_id, work) in LogicAPI().get_all(WorkRequest).items():
            date_start, date_end = self.convert_to_datetime(work)
            if work.real_estate == real_est.real_estate_number and start <= date_start <= end and start <= date_end <= end:
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
        by_time_range = input("Do you want to display work done in a specific time range(Y/N)? ")
        print()
        if by_time_range.lower() == "y":
            self.display_work_by_employee_in_time_range(emp)
        else:
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

    def display_work_by_employee_in_time_range(self, emp):
        start_date, end_date, start, end = self.period_input()
        print(
            f"{'--- List of Work Requests by {} in time range {} - {} ---'}".format(
                emp.name, start_date, end_date
            )
        )
        print("-" * 94)
        print(
            f"| {'ID':^2} | {'Title':^43} | {'Real estate':^11} | {'From':^11} | {'To':^11} |"
        )
        print("-" * 94)
        for (work_id, work) in LogicAPI().get_all(WorkRequest).items():
            for (workr_id, workr) in LogicAPI().get_all(WorkReport).items():
                date_start, date_end = self.convert_to_datetime(work)
                if workr.employee_id == emp.id and work_id == workr.work_request_id and start <= date_start <= end and start <= date_end <= end:
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
        by_time_range = input("Do you want to display work done in a specific time range(Y/N)? ")
        print()
        if by_time_range.lower() == "y":
            self.display_work_by_contractor_in_time_range(contr)
        else:
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

    def display_work_by_contractor_in_time_range(self, contr):
        start_date, end_date, start, end = self.period_input()
        print(
            f"{'--- List of Work Requests by {} in time range {} - {} ---'}".format(
                contr.name, start_date, end_date
            )
        )
        print("-" * 94)
        print(
            f"| {'ID':^2} | {'Title':^43} | {'Real estate':^11} | {'From':^11} | {'To':^11} |"
        )
        print("-" * 94)
        for (work_id, work) in LogicAPI().get_all(WorkRequest).items():
            for (workr_id, workr) in LogicAPI().get_all(WorkReport).items():
                date_start, date_end = self.convert_to_datetime(work)
                if workr.contractor_id == contr.id and work_id == workr.work_request_id and start <= date_start <= end and start <= date_end <= end:
                    print(
                        f"| {work.id:<2} | {work.title:<43} | {work.real_estate:<11} | {work.start_date:<11} | {work.end_date:<11} |"
                    )
        print("-" * 94)

    def display_work_by_date(self):
        date = input("Enter work report date to choose a work request (YYYY-MM-DD): ")

        print(f"{'--- List of Work Requests by {} ---':^94}".format(date))
        print("-" * 94)
        print(
            f"| {'ID':^2} | {'Title':^43} | {'Real estate':^11} | {'From':^11} | {'To':^11} |"
        )
        print("-" * 94)
        for (work_id, work) in LogicAPI().get_all(WorkRequest).items():
            for (work_id, workr) in LogicAPI().get_all(WorkReport).items():
                if work.id == workr.work_request_id and workr.date == date:
                    print(
                        f"| {work.id:<2} | {work.title:<43} | {work.real_estate:<11} | {work.start_date:<11} | {work.end_date:<11} |"
                    )
        print("-" * 94)

    def find_work_by_period(self):  # To-Do: Need to rethink the dates for work request!
        start_date, end_date, start, end = self.period_input()
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
            date_start, date_end = self.convert_to_datetime(work)
            if start <= date_start <= end and start <= date_end <= end:
                print(
                    f"| {work.id:<2} | {work.title:<43} | {work.real_estate:<11} | {work.start_date:<11} | {work.end_date:<11} |"
                )
        print("-" * 94)
