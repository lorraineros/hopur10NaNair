from src.models.models import WorkReport, WorkRequest
from src.ui.abstract_menu import SimpleMenu
from src.ui.creation_menu import CreationMenu
from src.ui.list_menu import EditPickerMenu


class WorkRequestMenu(SimpleMenu):
    @property
    def header(self):
        return "--- Work Request Menu ---"

    @property
    def options(self):
        if self.is_manager:
            return [
                ("Register a new work request", CreationMenu, WorkRequest),
                ("List of work requests", EditPickerMenu, WorkRequest),
                ("List of work reports", EditPickerMenu, WorkReport),
            ]
        else:
            return [
                ("Register a new work report", CreationMenu, WorkReport),
                ("List of work requests", EditPickerMenu, WorkRequest),
                ("List of work reports", EditPickerMenu, WorkReport),
            ]

    def name(self):
        return f"Work Request Menu"


#     def display_all_work_requests(self):
#         print()
#         print(f"{'--- List of Work Requests ---':^80}")
#         print("-" * 80)
#         print(
#             f"| {'ID':^3} | {'Title':^43} | {'Real estate':^11} | {'Date':^10} |"
#         )
#         print("-" * 80)
#         for (work_id, work) in LogicAPI().get_all(WorkRequest).items():
#             print(
#                 f"| {work.id:<3} | {work.title:<43} | {work.real_estate:<11} | {work.date} |"
#             )
#         print("-" * 80)

#     def display_all_work_reports(self):
#         print()
#         print(f"{'--- List of Work Reports ---':^114}")
#         print("-" * 114)
#         print(
#             f"| {'ID':^3} | {'Work Request':^48} | {'Employee':^21} | {'Contractor':^16} | {'Date':^11} |"
#         )
#         print("-" * 114)
#         for (workr_id, workr) in LogicAPI().get_all(WorkReport).items():
#             work_request = LogicAPI().get(WorkRequest, workr.work_request_id)
#             emp = LogicAPI().get(Employee, workr.employee_id)
#             contr = LogicAPI().get(Contractor, workr.contractor_id)
#             print(
#                 f"| {workr.id:<3} | {workr.work_request_id:<3} | {work_request.title:<43} | {emp.name:<21} | {contr.name_of_company:<16} | {workr.date:<11} |"
#             )
#         print("-" * 114)

#     def print_work_request(self, work):
#         if work.is_open:
#             state = "Open"
#         else:
#             state = "Close"
#         print(
#             """
# Title: {}
# Location: {}
# Real Estate: {}
# Priority: {}
# State: {}
# Description: {}
#         """.format(
#                 work.title,
#                 work.location,
#                 work.real_estate,
#                 work.priority,
#                 state,
#                 work.description,
#             )
#         )

#     def print_work_report(self, workr):
#         employee = LogicAPI().get(Employee, workr.employee_id)
#         contractor = LogicAPI().get(Contractor, workr.contractor_id)
#         if workr.done:
#             is_ready = "Ready"
#         else:
#             is_ready = "Not ready"
#         print(
#             """
# ID: {}
# Employee: {}
# Contractors: {}
# Contractor's fee: {}
# Description: {}
# Material Cost: {}
# Date: {}
# State: {}
# Comment: {}
#         """.format(
#                 workr.id,
#                 employee.name,
#                 contractor.name,
#                 workr.contractors_fee,
#                 workr.description,
#                 workr.material_cost,
#                 workr.date,
#                 is_ready,
#                 workr.comment,
#             )
#         )
#     def approve_work(self, work, work_report_list):
#         approve_input = input("Do you want to accept work report (Y/N)? ")

#         if approve_input.lower() == "y":
#             id = input("Enter id to choose a work report: ")
#             is_id = LogicAPI().work_report_id_check(id)

#             while not is_id:
#                 print("Sorry did not find work request, try again.")
#                 id = input("Enter id to choose a work report: ")
#                 is_id = LogicAPI().work_report_id_check(id)

#             ready = True
#             for workr in work_report_list:
#                 workr = LogicAPI().get(WorkReport, int(id))
#                 if not workr.done:
#                     ready = False

#             if ready:
#                 work.is_open = 0 # To-Do: Need to change the value of is_open in json file
#                 comment = input("Enter comment: ")
#                 workr.comment = comment # To-Do: Need to change the value of comment in json file
#                 print("Work report is approved successfully!")
#             else:
#                 print("Work report is not ready to approve")
#             print()
#         else:
#             print()

# class FindWorkRequestMenu(WorkRequestMenu):
#     def show(self):
#         print("--- Find Work Menu ---")
#         print("1. By ID")
#         print("2. By real estate")
#         print("3. By employee")
#         print("4. By contractor")
#         print("5. By date")
#         print("6. By period")
#         print("b. Back")
#         print("q. Quit")

#     def handle_input(self, command):
#         if command == "1":
#             print("Find Work by ID:")
#             print()
#             self.display_all_work_requests()
#             #self.display_all_work_reports()
#             self.find_work_by_id()
#             return ChangingMenu()
#         elif command == "2":
#             print("Find Work by Real Estate:")
#             print()
#             RealEstateMenu().display_all_real_estate()
#             real_est_input = self.real_estate_input()

#             work_report_exist_emp = LogicAPI().real_est_work_check(real_est_input)
#             if not work_report_exist_emp:
#                 print(
#                     "There is no work request for {}.".format(
#                         real_est_input.real_estate_number
#                     )
#                 )
#                 print()
#                 return BackQuitMenu()

#             print()
#             self.display_work_by_real_estate(real_est_input)
#             return ChangingMenu()
#         elif command == "3":
#             print("Find Work by Employee:")
#             print()
#             EmployeeMenu().display_all_employees()
#             emp_input = self.emp_input()

#             work_report_exist_emp = LogicAPI().emp_work_check(emp_input)
#             if not work_report_exist_emp:
#                 print("There is no work request for {}.".format(emp_input.name))
#                 print()
#                 return BackQuitMenu()

#             print()
#             self.display_work_by_employee(emp_input)
#             return ChangingMenu()
#         elif command == "4":
#             print("Find Work by Contractor:")
#             print()
#             ContractorMenu().display_all_contractors()
#             contr_input = self.contr_input()

#             work_report_exist_contr = LogicAPI().contr_work_check(contr_input)
#             if not work_report_exist_contr:
#                 print("There is no work request for {}.".format(contr_input.name))
#                 print()
#                 return BackQuitMenu()

#             print()
#             self.display_work_by_contractor(contr_input)
#             return ChangingMenu()
#         elif command == "5":
#             print("Find Work by Date:")
#             print()
#             self.display_all_work_requests()
#             self.display_all_work_reports()
#             self.display_work_by_date()
#             return ChangingMenu()
#         elif command == "6":
#             print("Find Work by Period:")
#             print()
#             self.display_all_work_requests()
#             self.display_all_work_reports()
#             self.find_work_by_period()
#             return ChangingMenu()
#         elif command == "b":
#             return "back"
#         elif command == "q":
#             return "quit"

#     def find_work_by_id(self):
#         id = input("Enter work request id to choose a work request: ")
#         is_id = LogicAPI().work_id_check(id)

#         while not is_id:
#             print("Sorry did not find work request, try again.")
#             id = input("Enter id to choose a work request: ")
#             is_id = LogicAPI().work_id_check(id)

#         work = LogicAPI().get(WorkRequest, int(id))
#         print()
#         print(f"--- Work Request ---")
#         self.print_work_request(work)

#         work_report_list = []
#         for (workr_id, workr) in LogicAPI().get_all(WorkReport).items():
#             if workr.work_request_id == int(id):
#                 work_report_list.append(workr_id)

#         if work_report_list:
#             print(f"--- Work Report ---")
#             for work_report in work_report_list:
#                 workr = LogicAPI().get(WorkReport, int(work_report))
#                 self.print_work_report(workr)
#             self.approve_work(work, work_report_list)

#     def period_input(self):
#         start_date = input("Enter start date (YYYY-MM-DD): ")
#         end_date = input("Enter end date (YYYY-MM-DD): ")
#         start_year, start_month, start_day = start_date.split("-")
#         end_year, end_month, end_day = end_date.split("-")
#         start = datetime(int(start_year), int(start_month), int(start_day)).date()
#         end = datetime(int(end_year),int(end_month), int(end_day)).date()
#         print()
#         return start_date, end_date, start, end

#     def real_estate_input(self):
#         real_est_id = input("Enter real estate ID to choose a work request: ")
#         is_real_est_id = LogicAPI().real_estate_id_check(real_est_id)

#         while not is_real_est_id:
#             print("Sorry did not find Real Estate, try again.")
#             real_est_id = input("Enter real estate ID to choose a work request: ")
#             is_real_est_id = LogicAPI().real_estate_id_check(real_est_id)

#         real_est = LogicAPI().get(RealEstate, int(real_est_id))
#         return real_est

#     def display_work_by_real_estate(self, real_est):
#         by_time_range = input("Do you want to display work done in a specific time range(Y/N)? ")
#         print()
#         if by_time_range.lower() == "y":
#             self.display_work_by_real_estate_in_time_range(real_est)
#         else:
#             print(
#                 f"{'--- List of Work Requests by {} ---':^80}".format(
#                     real_est.real_estate_number
#                 )
#             )
#             print("-" * 80)
#             print(
#                 f"| {'ID':^3} | {'Title':^43} | {'Real estate':^11} | {'Date':^10} |"
#             )
#             print("-" * 80)
#             for (work_id, work) in LogicAPI().get_all(WorkRequest).items():
#                 if work.real_estate == real_est.real_estate_number:
#                     print(
#                         f"| {work.id:<3} | {work.title:<43} | {work.real_estate:<11} | {work.date} |"
#                     )
#             print("-" * 80)
#             self.find_work_by_id()

#     def display_work_by_real_estate_in_time_range(self, real_est):
#         start_date, end_date, start, end = self.period_input()
#         work_list = []
#         for (work_id, work) in LogicAPI().get_all(WorkRequest).items():
#             if work.real_estate == real_est.real_estate_number and start <= work.date <= end:
#                 work_list.append(work)
#         if work_list:
#             print(
#                 f"{'--- List of Work Requests by {} from {} to {} ---'}".format(
#                     real_est.real_estate_number, start_date, end_date
#                 )
#             )
#             print("-" * 80)
#             print(
#                 f"| {'ID':^3} | {'Title':^43} | {'Real estate':^11} | {'Date':^10} |"
#             )
#             print("-" * 80)
#             for work in work_list:
#                 print(
#                     f"| {work.id:<3} | {work.title:<43} | {work.real_estate:<11} | {work.date} |"
#                 )
#             print("-" * 80)
#             self.find_work_by_id()
#         else:
#             print("There is no work request for {} from {} to {}.".format(
#                 real_est.real_estate_number, start_date, end_date
#                 )
#             )
#             print()

#     def emp_input(self):
#         emp_id = input("Enter employee id to choose a work request: ")
#         is_emp_id = LogicAPI().employee_id_check(emp_id)

#         while not is_emp_id:
#             print("Sorry, did not find employee, try again.")
#             emp_id = input("Enter employee id to choose a work request: ")
#             is_emp_id = LogicAPI().employee_id_check(emp_id)

#         emp = LogicAPI().get(Employee, int(emp_id))
#         return emp

#     def display_work_by_employee(self, emp):
#         by_time_range = input("Do you want to display work done in a specific time range(Y/N)? ")
#         print()
#         if by_time_range.lower() == "y":
#             self.display_work_by_employee_in_time_range(emp)
#         else:
#             print(f"{'--- List of Work Requests by {} ---':^80}".format(emp.name))
#             print("-" * 80)
#             print(
#                 f"| {'ID':^3} | {'Title':^43} | {'Real estate':^11} | {'Date':^10} |"
#             )
#             print("-" * 80)
#             for (work_id, work) in LogicAPI().get_all(WorkRequest).items():
#                 for (workr_id, workr) in LogicAPI().get_all(WorkReport).items():
#                     if workr.employee_id == emp.id and work_id == workr.work_request_id:
#                         print(
#                             f"| {work.id:<3} | {work.title:<43} | {work.real_estate:<11} | {work.date} |"
#                         )
#             print("-" * 80)
#             self.find_work_by_id()

#     def display_work_by_employee_in_time_range(self, emp):
#         start_date, end_date, start, end = self.period_input()
#         work_list = []
#         for (work_id, work) in LogicAPI().get_all(WorkRequest).items():
#                 for (workr_id, workr) in LogicAPI().get_all(WorkReport).items():
#                     if workr.employee_id == emp.id and work_id == workr.work_request_id and start <= work.date <= end:
#                         work_list.append(work)
#         if work_list:
#             print(
#                 f"{'--- List of Work Requests by {} from {} to {} ---'}".format(
#                     emp.name, start_date, end_date
#                 )
#             )
#             print("-" * 80)
#             print(
#                 f"| {'ID':^3} | {'Title':^43} | {'Real estate':^11} | {'Date':^10} |"
#             )
#             print("-" * 80)
#             for work in work_list:
#                 print(
#                     f"| {work.id:<3} | {work.title:<43} | {work.real_estate:<11} | {work.date} |"
#                 )
#             print("-" * 80)
#             self.find_work_by_id()
#         else:
#             print("There is no work request for {} from {} to {}.".format(
#                 emp.name, start_date, end_date
#                 )
#             )
#             print()

#     def contr_input(self):
#         contr_id = input("Enter contractor id to choose a work request: ")
#         is_contr_id = LogicAPI().contractor_id_check(contr_id)

#         while not is_contr_id:
#             print("Sorry, did not find contractor, try again.")
#             contr_id = input("Enter contractor id to choose a work request: ")
#             is_contr_id = LogicAPI().contractor_id_check(contr_id)

#         contr = LogicAPI().get(Contractor, int(contr_id))
#         return contr

#     def display_work_by_contractor(self, contr):
#         by_time_range = input("Do you want to display work done in a specific time range(Y/N)? ")
#         print()
#         if by_time_range.lower() == "y":
#             self.display_work_by_contractor_in_time_range(contr)
#         else:
#             print(f"{'--- List of Work Requests by {} ---':^80}".format(contr.name_of_company))
#             print("-" * 80)
#             print(
#                 f"| {'ID':^3} | {'Title':^43} | {'Real estate':^11} | {'Date':^10} |"
#             )
#             print("-" * 80)
#             for (work_id, work) in LogicAPI().get_all(WorkRequest).items():
#                 for (workr_id, workr) in LogicAPI().get_all(WorkReport).items():
#                     if workr.contractor_id == contr.id and work_id == workr.work_request_id:
#                         print(
#                             f"| {work.id:<3} | {work.title:<43} | {work.real_estate:<11} | {work.date} |"
#                         )
#             print("-" * 80)
#             self.find_work_by_id()

#     def display_work_by_contractor_in_time_range(self, contr):
#         start_date, end_date, start, end = self.period_input()
#         work_list = []
#         for (work_id, work) in LogicAPI().get_all(WorkRequest).items():
#                 for (workr_id, workr) in LogicAPI().get_all(WorkReport).items():
#                     if workr.contractor_id == contr.id and work_id == workr.work_request_id and start <= work.date <= end:
#                         work_list.append(work)
#         if work_list:
#             print(
#                 f"{'--- List of Work Requests by {} from {} to {} ---'}".format(
#                     contr.name_of_company, start_date, end_date
#                 )
#             )
#             print("-" * 80)
#             print(
#                 f"| {'ID':^3} | {'Title':^43} | {'Real estate':^11} | {'Date':^10} |"
#             )
#             print("-" * 80)
#             for work in work_list:
#                 print(
#                     f"| {work.id:<3} | {work.title:<43} | {work.real_estate:<11} | {work.date} |"
#                 )
#             print("-" * 80)
#             self.find_work_by_id()
#         else:
#             print("There is no work request for {} from {} to {}.".format(
#                 contr.name_of_company, start_date, end_date
#                 )
#             )
#             print()

#     def date_input(self):
#         date = input("Enter date to choose a work request (YYYY-MM-DD): ")
#         year, month, day = date.split("-")
#         date = datetime(int(year), int(month), int(day)).date()
#         print()
#         return date

#     def display_work_by_date(self):
#         date = self.date_input()
#         work_list = []
#         for (work_id, work) in LogicAPI().get_all(WorkRequest).items():
#             if work.date == date:
#                 work_list.append(work)
#         if work_list:
#             print(f"{'--- List of Work Requests by {} ---':^80}".format(date))
#             print("-" * 80)
#             print(
#                 f"| {'ID':^3} | {'Title':^43} | {'Real estate':^11} | {'Date':^10} |"
#             )
#             print("-" * 80)
#             for work in work_list:
#                 print(
#                     f"| {work.id:<3} | {work.title:<43} | {work.real_estate:<11} | {work.date} |"
#                 )
#             print("-" * 80)
#             self.find_work_by_id()
#         else:
#             print("There is no work request for {}.".format(date))
#             print()

#     def find_work_by_period(self):
#         start_date, end_date, start, end = self.period_input()
#         work_list = []
#         for (work_id, work) in LogicAPI().get_all(WorkRequest).items():
#                 if start <= work.date <= end:
#                     work_list.append(work)
#         if work_list:
#             print(
#                 f"{'--- List of Work Requests by {} - {} ---':^80}".format(
#                     start_date, end_date
#                 )
#             )
#             print("-" * 80)
#             print(
#                 f"| {'ID':^3} | {'Title':^43} | {'Real estate':^11} | {'Date':^10} |"
#             )
#             print("-" * 80)
#             for work in work_list:
#                 print(
#                     f"| {work.id:<3} | {work.title:<43} | {work.real_estate:<11} | {work.date} |"
#                 )
#             print("-" * 80)
#             self.find_work_by_id()
#         else:
#             print("There is no work request from {} to {}.".format(
#                 start_date, end_date
#                 )
#             )
#             print()
