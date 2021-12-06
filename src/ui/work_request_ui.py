from src.models.models import Contractor, Employee, WorkRequest
from src.logic.logic_api import LogicAPI
from src.logic.contractor_logic import ContractorLogic
from src.ui.abstract_menu import AbstractMenu, SimpleMenu
from src.logic.work_request_logic import WorkRequestLogic
from src.logic.work_report_logic import WorkReportLogic
from src.logic.employee_logic import EmployeeLogic
from src.ui.common_menus import CreationMenu


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


class WorkRequestMenu2(AbstractMenu):
    def show(self):
        print("--- Work Request Menu ---")
        print("1. Register a new work request")
        print("2. Find work request")
        print("b. Back")
        print("q. Quit")

    def handle_input(self, command):
        if command == "1":
            # return CreationMenu(models.WorkRequest)
            pass
        elif command == "2":
            return FindWorkRequestMenu()
        elif command == "b":
            return "back"
        elif command == "q":
            return "quit"

    def display_all_works(self):
        print(f"{'--- Find Work Request ---':^138}")
        print("-" * 138)
        print(
            f"| {'ID':^2} | {'Title':^43} | {'Real estate':^11} |  {'Employee':^19} |  {'Contractor':^19} | {'From':^10} | {'To':^10} |"
        )
        print("-" * 138)
        for work in WorkRequestLogic.get_list():
            for emp in EmployeeLogic.get_list():
                for (contr_id, contr) in LogicAPI().get_all(Contractor).items():
                    if work.employee == emp.id and work.contractor == contr.id:
                        print(
                            f"| {work.id:<2} | {work.title:<43} | {work.real_estate:<11} | {emp.id}. {emp.name:<17} | {contr.id}. {contr.name:<17} | {work.start_date:<7} | {work.end_date:<7} |"
                        )
        print("-" * 138)

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


class FindWorkRequestMenu(WorkRequestMenu):
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
            self.display_all_works()
            self.find_work_by_real_estate()
            self.find_work_by_id()
            return ChangingMenu()
        elif command == "3":
            print("Find Work by Employee:")
            print()
            self.display_all_works()
            self.find_work_by_employee()
            self.find_work_by_id()
            return ChangingMenu()
        elif command == "4":
            print("Find Work by Contractor:")
            print()
            self.display_all_works()
            self.find_work_by_contractor()
            self.find_work_by_id()
            return ChangingMenu()
        elif command == "5":
            print("Find Work by Date:")
            print()
            self.display_all_works()
            self.find_work_by_date()
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
        id = input("\nEnter id to choose a work request: ")
        is_id = LogicAPI().work_id_check(id)

        while not is_id:
            print("Sorry did not find work request, try again.")
            id = input("Enter id to choose a work request: ")
            is_id = LogicAPI().work_id_check(id)

        work = LogicAPI().get(WorkRequest, int(id))
        self.print_work(work)

    def find_work_by_real_estate(self):
        real_est = input("\nEnter real estate address to choose a work request: ")

        print(f"{'--- List of Work Requests by {} ---':^138}".format(real_est.upper()))
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
                        and work.real_estate.lower() == real_est.lower()
                    ):
                        print(
                            f"| {work.id:<2} | {work.title:<43} | {work.real_estate:<11} | {emp.id}. {emp.name:<17} | {contr.id}. {contr.name:<17} | {work.start_date:<7} | {work.end_date:<7} |"
                        )
        print("-" * 138)

    def find_work_by_employee(self):
        emp_id = input("\nEnter employee id to choose a work request: ")

        emp = LogicAPI().get(Employee, int(emp_id))
        print(f"{'--- List of Work Requests by {} ---':^138}".format(emp.name))
        print("-" * 138)
        print(
            f"| {'ID':^2} | {'Title':^43} | {'Real estate':^11} |  {'Employee':^19} |  {'Contractor':^19} | {'From':^10} | {'To':^10} |"
        )
        print("-" * 138)
        for work in WorkRequestLogic.get_list():
            for emp in EmployeeLogic.get_list():
                for (contr_id, contr) in LogicAPI().get_all(Contractor).items():
                    if (
                        work.employee == emp.id == int(emp_id)
                        and work.contractor == contr.id
                    ):
                        print(
                            f"| {work.id:<2} | {work.title:<43} | {work.real_estate:<11} | {emp.id}. {emp.name:<17} | {contr.id}. {contr.name:<17} | {work.start_date:<7} | {work.end_date:<7} |"
                        )
        print("-" * 138)

    def find_work_by_contractor(self):
        contr_id = input("\nEnter contractor id to choose a work request: ")

        contr = LogicAPI().get(Contractor, int(contr_id))
        print(f"{'--- List of Work Requests by {} ---':^138}".format(contr.name))
        print("-" * 138)
        print(
            f"| {'ID':^2} | {'Title':^43} | {'Real estate':^11} |  {'Employee':^19} |  {'Contractor':^19} | {'From':^10} | {'To':^10} |"
        )
        print("-" * 138)
        for work in WorkRequestLogic.get_list():
            for emp in EmployeeLogic.get_list():
                for (contr_id, contr) in LogicAPI().get_all(Contractor).items():
                    if work.employee == emp.id and work.contractor == contr.id == int(
                        contr_id
                    ):
                        print(
                            f"| {work.id:<2} | {work.title:<43} | {work.real_estate:<11} | {emp.id}. {emp.name:<17} | {contr.id}. {contr.name:<17} | {work.start_date:<7} | {work.end_date:<7} |"
                        )
        print("-" * 138)

    def find_work_by_date(self):
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

    def find_work_by_period(self):
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


"""
class FindWork(AbstractMenu):
    def show(self):
        print(f"{'--- Find Work Request ---':^138}")
        self.print_list()

    def handle_input(self, command):
        if command == "b":
            return "back"
        elif command == "q":
            return "quit"
        else:
            print("Invalid option\n")
            return "back"

    def print_list(self):
        print("-" * 138)
        print(
            f"| {'ID':^2} | {'Title':^43} | {'Real estate':^11} |  {'Employee':^19} |  {'Contractor':^19} | {'From':^10} | {'To':^10} |"
        )
        print("-" * 138)
        for work in WorkRequestLogic.get_list():
            for emp in EmployeeLogic.get_list():
                for (contr_id, contr) in LogicAPI().get_all(Contractor).items():
                    if work.employee == emp.id and work.contractor == contr.id:
                        print(
                            f"| {work.id:<2} | {work.title:<43} | {work.real_estate:<11} | {emp.id}. {emp.name:<17} | {contr.id}. {contr.name:<17} | {work.start_date:<7} | {work.end_date:<7} |"
                        )
        print("-" * 138)


class FindWorkByID(FindWork):
    def show(self):
        super().show()
        id = input("\nEnter id to choose a work request: ")
        self.print_filtered_list(id)
        print()
        print("b. Back")
        print("q. Quit")
        edit = input("\nDo you want to edit work request (Y/N)? ")
        accept = input("\nDo you want to accept work report (Y/N)? ")

    def handle_input(self, command):
        return super().handle_input(command)

    def print_list(self):
        return super().print_list()

    def print_filtered_list(self, id):
        print(f"{'--- Find Work Request by ID ---':^115}")
        print("-" * 115)
        print(
            f"| {'ID':^2} | {'Title':^43} | {'Location':^28} | {'Priority':^20} | {'Repeat':^6} |"
        )
        print("-" * 115)
        for work in WorkRequestLogic.get_list():
            if work.id == int(id):
                print(
                    f"| {work.id:<2} | {work.title:<43} |  {work.location:<27} | {work.priority:<20} | {work.repeated_work:<6} |"
                )
        print("-" * 115)
        print()
        print(f"{'--- Work Report ---':^76}")
        print("-" * 76)
        print(
            f"| {'ID':^2} | {'Employee':^20} | {'Contractor':^18} | {'From':^10} | {'To':^10} |"
        )
        print("-" * 76)
        for workr in WorkReportLogic.get_list():
            for emp in EmployeeLogic.get_list():
                if workr.work_request_id == int(id) and workr.employee_id == emp.id:
                    print(
                        f"| {workr.work_request_id:<2} | {emp.id}. {emp.name:<17} |  {workr.contractors:<17} | {workr.start_date:<7} | {workr.end_date:<7} |"
                    )
                    print("-" * 76)
                    print(f"| {'Description':^72} |")
                    print("-" * 76)
                    print(f"{workr.description:^72}")
        print("-" * 76)


class FindWorkByRealEstate(FindWork):
    def show(self):
        super().show()
        real_est = input("\nEnter real estate address to choose a work request: ")
        self.print_filtered_list(real_est)
        print()
        print("b. Back")
        print("q. Quit")

    def handle_input(self, command):
        return super().handle_input(command)

    def print_list(self):
        return super().print_list()

    def print_filtered_list(self, real_est):
        print(f"{'--- Find Work Request by Real Estate ---':^115}")
        print("-" * 115)
        print(
            f"| {'ID':^2} | {'Title':^43} | {'Location':^28} | {'Priority':^20} | {'Repeat':^6} |"
        )
        print("-" * 115)
        for work in WorkRequestLogic.get_list():
            if work.real_estate.lower() == real_est.lower():
                print(
                    f"| {work.id:<2} | {work.title:<43} |  {work.location:<27} | {work.priority:<20} | {work.repeated_work:<6} |"
                )
        print("-" * 115)


class FindWorkByEmployee(FindWork):
    def show(self):
        super().show()
        emp_id = input("\nEnter employee id to choose a work request: ")
        self.print_filtered_list(emp_id)
        print()
        print("b. Back")
        print("q. Quit")

    def handle_input(self, command):
        return super().handle_input(command)

    def print_list(self):
        return super().print_list()

    def print_filtered_list(self, emp_id):
        print(f"{'--- Find Work Request by Employee ---':^115}")
        print("-" * 115)
        print(
            f"| {'ID':^2} | {'Title':^43} | {'Location':^28} | {'Priority':^20} | {'Repeat':^6} |"
        )
        print("-" * 115)
        for work in WorkRequestLogic.get_list():
            if work.employee == int(emp_id):
                print(
                    f"| {work.id:<2} | {work.title:<43} |  {work.location:<27} | {work.priority:<20} | {work.repeated_work:<6} |"
                )
        print("-" * 115)


class FindWorkByContractor(FindWork):
    def show(self):
        super().show()
        contr_id = input("\nEnter contractor id to choose a work request: ")
        self.print_filtered_list(contr_id)
        print()
        print("b. Back")
        print("q. Quit")

    def handle_input(self, command):
        return super().handle_input(command)

    def print_list(self):
        return super().print_list()

    def print_filtered_list(self, contr_id):
        print(f"{'--- Find Work Request by Contractor ---':^115}")
        print("-" * 115)
        print(
            f"| {'ID':^2} | {'Title':^43} | {'Location':^28} | {'Priority':^20} | {'Repeat':^6} |"
        )
        print("-" * 115)
        for work in WorkRequestLogic.get_list():
            if work.contractor == int(contr_id):
                print(
                    f"| {work.id:<2} | {work.title:<43} |  {work.location:<27} | {work.priority:<20} | {work.repeated_work:<6} |"
                )
        print("-" * 115)


class FindWorkByDate(FindWork):
    def show(self):
        super().show()
        date = input("Enter date to choose a work request (YYYY-MM-DD): ")
        self.print_filtered_list(date)
        print()
        print("b. Back")
        print("q. Quit")

    def handle_input(self, command):
        return super().handle_input(command)

    def print_list(self):
        return super().print_list()

    def print_filtered_list(self, date):
        print(f"{'--- Find Work Request by Date ---':^115}")
        print("-" * 115)
        print(
            f"| {'ID':^2} | {'Title':^43} | {'Location':^28} | {'Priority':^20} | {'Repeat':^6} |"
        )
        print("-" * 115)
        for work in WorkRequestLogic.get_list():
            if work.start_date == date or work.end_date == date:
                print(
                    f"| {work.id:<2} | {work.title:<43} |  {work.location:<27} | {work.priority:<20} | {work.repeated_work:<6} |"
                )
        print("-" * 115)


class FindWorkByPeriod(FindWork):
    def show(self):
        super().show()
        start_date = input("Enter start date (YYYY-MM-DD): ")
        end_date = input("Enter end date (YYYY-MM-DD): ")
        self.print_filtered_list(start_date, end_date)
        print()
        print("b. Back")
        print("q. Quit")

    def handle_input(self, command):
        return super().handle_input(command)

    def print_list(self):
        return super().print_list()

    def print_filtered_list(self, start_date, end_date):
        print(f"{'--- Find Work Request by Period ---':^115}")
        print("-" * 115)
        print(
            f"| {'ID':^2} | {'Title':^43} | {'Location':^28} | {'Priority':^20} | {'Repeat':^6} |"
        )
        print("-" * 115)
        for work in WorkRequestLogic.get_list():
            if work.start_date == start_date and work.end_date == end_date:
                print(
                    f"| {work.id:<2} | {work.title:<43} |  {work.location:<27} | {work.priority:<20} | {work.repeated_work:<6} |"
                )
        print("-" * 115)
"""
