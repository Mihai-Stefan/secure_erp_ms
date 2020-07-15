import os
import copy

def cls(): 
    os.system('cls' if os.name == 'nt' else 'clear') 


def print_menu(title, list_options):
    """Prints options in standard menu format like this:

    Main menu:
    (1) Store manager
    (2) Human resources manager
    (3) Inventory manager
    (0) Exit program

    Args:
        title (str): the title of the menu (first row)
        list_options (list): list of the menu options (listed starting from 1, 0th element goes to the end)
    """
    cls()
    menu_str = f"    {title}"
    print(menu_str, '\n')
    for counter, menu_item in enumerate(list_options):
        print(f"    {counter}. {menu_item}")
 





def print_message(message):
    """Prints a single message to the terminal.

    Args:
        message: str - the message
    """
    pass


def print_general_results(result, label):
    """Prints out any type of non-tabular data.
    It should print numbers (like "@label: @value", floats with 2 digits after the decimal),
    lists/tuples (like "@label: \n  @item1; @item2"), and dictionaries
    (like "@label \n  @key1: @value1; @key2: @value2")
    """
    pass


# /--------------------------------\
# |   id   |   product  |   type   |
# |--------|------------|----------|
# |   0    |  Bazooka   | portable |
# |--------|------------|----------|
# |   1    | Sidewinder | missile  |
# \-----------------------------------/
def print_table(table, headers):
    """Prints tabular data like above.

    Args:
        table: list of lists - the table to print out
    """
    cls()
    prinable_table = copy.deepcopy(table)
    prinable_table.insert(0, headers)
    length_elements = [[len(x) for x in prinable_table[i]] for i in range(len(prinable_table))]
    off_set = 6
    longest_element = [0 for x in range(len(headers))]
    for len_element in length_elements:
        for index, char in enumerate(len_element):
            if int(char) > longest_element[index]:
                longest_element[index] = int(char) + off_set
    chart = ['-' * int(x) for x in longest_element]
    print(f'      /{"-".join(chart)}\ ')
    print('      ', end = '')
    for index, employee in enumerate(prinable_table):
        string = ""
        for i in range(len(employee)):
            string += "|" + employee[i].center(longest_element[i])
        print(string + '|')
        if index == len(prinable_table) - 1:
            print(f'      \{"-".join(chart)}/')
        else:
            print(f'      |{"|".join(chart)}|')   
            print(f"{'{:4}'.format(index + 1)}", end ='  ')


def get_input(label):
    """Gets single string input from the user.

    Args:
        label: str - the label before the user prompt
    """
    user_input = input(f"\n    {label} >  ")
    return user_input


def get_inputs(labels):
    """Gets a list of string inputs from the user.

    Args:
        labels: list - the list of the labels to be displayed before each prompt
    """
    pass


def print_error_message(message):
    """Prints an error message to the terminal.

    Args:
        message: str - the error message
    """
    pass


'''
print_table([['pF5v4wG_e_', 'Dr. Strangelove', 'strangelove@rgv453.grer', '1'], 
['k0_JUq+8hk', 'Kim', 'supremeleader@dfs.vfsdfv', '0'], 
['l4x__QmU8r', 'Unknown', '---', '0'], 
['P7+5Ggza!n', 'Known', 'ping@me', '1']])
'''