import copy
from model.util import *
from view import terminal as view
from model.data_manager import *
from view.terminal import *



DATAFILE = "model/crm/crm.csv"
HEADERS = ["id", "name", "email", "subscribed"]
crm_list = (read_table_from_file(DATAFILE, separator=';'))


    
def list_customers():
    table = crm_list
    headers = HEADERS
    cls()
    print_table(table, headers)


def add_customer():
    list_customers()
    new_customer = []
    new_id = generate_id()
    new_customer.append(new_id)
    for element in HEADERS[1:]:
        inf = get_input(element)
        new_customer.append(inf)
    crm_list.append(new_customer)
    list_customers()
    write_table_to_file(DATAFILE, crm_list, separator=';')
    wait_enter()



def update_customer():
    view.print_error_message("Not implemented yet.")


def delete_customer():
    list_customers()
    del_index = get_input()


def get_subscribed_emails():
    view.print_error_message("Not implemented yet.")


def run_operation(option):
    if option == 1:
        list_customers()
        wait_enter()
    elif option == 2:
        add_customer()
    elif option == 3:
        update_customer()
    elif option == 4:
        delete_customer()
    elif option == 5:
        get_subscribed_emails()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List customers",
               "Add new customer",
               "Update customer",
               "Remove customer",
               "Subscribed customer emails"]
    view.print_menu("Customer Relationship Management", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)


