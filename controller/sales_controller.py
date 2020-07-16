from model.util import *
from view import terminal as view
from model.data_manager import *
from view.terminal import *


DATAFILE = "model/sales/sales.csv"
HEADERS = ["Id", "Customer", "Product", "Price", "Date"]
sales_list = (read_table_from_file(DATAFILE, separator=';'))


ID = 0   # avoid magic numbers
CUSTOMER = 1
PRODUCT = 2
PRICE = 3
DATE = 4

def format_sales_list(sales_list):   # format price as float with two decimals
    for index in range(len(sales_list)):
        price = float(sales_list[index][PRICE])
        price = "{:10.2f}".format(price)
        sales_list[index][PRICE] = price
    return sales_list

sales_list = format_sales_list(sales_list)


def list_transactions():
    table = sales_list
    headers = HEADERS
    cls()
    print_table(table, headers)


def add_transaction():
    list_transactions()
    new_transaction = []
    new_id = generate_id()
    new_transaction.append(new_id)
    for element in HEADERS[1:]:
        inf = get_input(element)
        new_transaction.append(inf)
    sales_list.append(new_transaction)
    list_transactions()
    write_table_to_file(DATAFILE, sales_list, separator=';')
    wait_enter()


def update_transaction():
    list_transactions()
    upd_index = int(get_input("Line number of record to update")) - 1
    update_transaction = []
    update_transaction.append(sales_list[upd_index][ID])
    k = 1
    for element in HEADERS[1:]:
        inf = get_input(element)
        if inf == '':
            update_transaction.append(sales_list[upd_index][k])
        else:
            update_transaction.append(inf)
        k += 1
    sales_list[upd_index] = update_transaction
    list_transactions()
    write_table_to_file(DATAFILE, sales_list, separator=';')
    wait_enter()


def delete_transaction():
    list_transactions()
    del_index = int(get_input("Line number of record to delete"))
    del sales_list[del_index-1]
    list_transactions()
    write_table_to_file(DATAFILE, sales_list, separator=';')
    wait_enter()


def get_biggest_revenue_transaction():
    biggest_revenue_transaction = 0.00
    count_id = -1
    for i_d, customer, product, price, date in sales_list:
        price = float(price)
        if price > biggest_revenue_transaction:
            biggest_revenue_transaction = price
            count_id += 1
    brc_list = sales_list[count_id]
    brc_list_to_print = []
    brc_list_to_print.append(brc_list)
    print_message("The biggest revenue transaction is:")
    print_table(brc_list_to_print, HEADERS)
    wait_enter()


def get_biggest_revenue_product():
    products_dict = {}
    for i_d, customer, product, price, date in sales_list:
        if product in products_dict.keys():
            products_dict[product] += float(price)
        else:
            products_dict[product] = float(price)
    # sorting dictionary after values
    VALUES = 1
    list_of_tupples = sorted(products_dict.items(), key=lambda x: x[VALUES])
    product, biggest_revenue = list_of_tupples[-1]  # the last is the biggest
    biggest_revenue = "{:.2f}".format(biggest_revenue)
    print_message(f"The product with the biggest revenue is > {product}\n    And the revenue is {biggest_revenue}")
    wait_enter()


def count_transactions_between():
    initial_date = get_input("Input initial date in format yyyy-mm-dd")
    final_date = get_input("Input initial date in format yyyy-mm-dd")
    transaction_count = 0
    for i_d, customer, product, price, date in sales_list:
        if initial_date <= date <= final_date:
            transaction_count += 1
    list_transactions()
    print_message(f"  The number of transaction betveen {initial_date} and {final_date} > {transaction_count}")
    wait_enter()


def sum_transactions_between():
    initial_date = get_input("Input initial date in format yyyy-mm-dd")
    final_date = get_input("Input initial date in format yyyy-mm-dd")
    transaction_sum = 0
    for i_d, customer, product, price, date in sales_list:
        if initial_date <= date <= final_date:
            transaction_sum += float(price)
    list_transactions()
    formated_transaction_sum = "{:10.2f}".format(transaction_sum)
    print_message(f"  The total sum fot transaction betveen {initial_date} and {final_date} > {formated_transaction_sum}")
    wait_enter()


def run_operation(option):
    if option == 1:
        list_transactions()
        wait_enter()
    elif option == 2:
        add_transaction()
    elif option == 3:
        update_transaction()
    elif option == 4:
        delete_transaction()
    elif option == 5:
        get_biggest_revenue_transaction()
    elif option == 6:
        get_biggest_revenue_product()
    elif option == 7:
        count_transactions_between()
    elif option == 8:
        sum_transactions_between()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List transactions",
               "Add new transaction",
               "Update transaction",
               "Remove transaction",
               "Get the transaction that made the biggest revenue",
               "Get the product that made the biggest revenue altogether",
               "Count number of transactions between",
               "Sum the price of transactions between"]
    view.print_menu("Sales", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
