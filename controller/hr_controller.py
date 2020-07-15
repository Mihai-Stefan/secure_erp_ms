import copy
from model.util import *
from model.util import get_date
from view import terminal as view
from model.data_manager import *
from view.terminal import *
from model.hr.hr import *



def list_employees():
    cls()
    print_table(hr_list, HEADERS)


def add_employee():
    list_employees()
    new_employee = []
    new_id = generate_id()
    new_employee.append(new_id)
    for element in HEADERS[1:]:
        if element == HEADERS[2]:
            inf = get_date()
        elif element == HEADERS[4]: 
            min = 0
            max = 8
            message = f"(insert numbers between {min} and {max})"
            inf = check_if_number(HEADERS[4],min,max,message)    
        else:
            inf = get_input(element)
        new_employee.append(inf)
    hr_list.append(new_employee)
    list_employees()
    write_table_to_file(DATAFILE, hr_list, separator=';')
    wait_enter()


def update_employee():
    view.print_error_message("Not implemented yet.")


def delete_employee():
    view.print_error_message("Not implemented yet.")


def get_oldest_and_youngest():
    
    birthday_dates = list_birthdates()

    birthday_dates.sort()

    oldest = birthday_dates[0]
    youngest = birthday_dates[-1]

    for i in range(len(hr_list)):
        if hr_list[i][2] == str(oldest):
            print(f"{hr_list[i][1]} is the oldest employee")
        if hr_list[i][2] == str(youngest):
            print(f"{hr_list[i][1]} is the youngest employee")



def get_average_age():
    birthday_strings = list_separated_strings_birthdays()
    sum_age = 0
    for i in range(len(birthday_strings)):
        YEAR = int(birthday_strings[i][0])
        MONTH = int(birthday_strings[i][1])
        DAY = int(birthday_strings[i][2])
        age = calculate_age(datetime.date(YEAR,MONTH,DAY))
        sum_age += age
    age_average = sum_age / len(birthday_strings)
    age_average = int(age_average) 
    print(f"The average employee age is {age_average} years")



    


def next_birthdays():
    view.print_error_message("Not implemented yet.")


def count_employees_with_clearance():
    view.print_error_message("Not implemented yet.")


def count_employees_per_department():
    view.print_error_message("Not implemented yet.")


def run_operation(option):
    if option == 1:
        list_employees()
        wait_enter()
    elif option == 2:
        add_employee()
    elif option == 3:
        update_employee()
    elif option == 4:
        delete_employee()
    elif option == 5:
        get_oldest_and_youngest()
        wait_enter()
    elif option == 6:
        get_average_age()
        wait_enter()
    elif option == 7:
        next_birthdays()
    elif option == 8:
        count_employees_with_clearance()
    elif option == 9:
        count_employees_per_department()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List employees",
               "Add new employee",
               "Update employee",
               "Remove employee",
               "Oldest and youngest employees",
               "Employees average age",
               "Employees with birthdays in the next two weeks",
               "Employees with clearance level",
               "Employee numbers by department"]
    view.print_menu("Human resources", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
