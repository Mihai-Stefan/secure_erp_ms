import random
import string
import itertools
import datetime


def generate_id(number_of_small_letters=4,
                number_of_capital_letters=2,
                number_of_digits=2,
                number_of_special_chars=2,
                allowed_special_chars=r"_+-!"):

    small_letters = string.ascii_lowercase
    capital_letters = string.ascii_uppercase
    special_char = '_+-!'
    digits = string.digits
    id = []
    id.append(random.sample(small_letters, 4))
    id.append(random.sample(capital_letters, 2))
    id.append(random.sample(special_char, 2))
    id.append(random.sample(digits, 2))

    id = list(itertools.chain.from_iterable(id))
    random.shuffle(id)
    return ''.join(id)

def wait_enter():
    input("\npress enter to continue")

def get_date():
    isValid=False
    while not isValid:
        userIn = input("\nType Date yyyy-mm-dd > ")
        try:
            d = datetime.datetime.strptime(userIn, "%Y-%m-%d")
            isValid = True
        except:
            print("Please try again!")
    return str(d.date())

def check_if_number(what_to_insert, min, max):
    isValid = False
    while not isValid:
        userIn = input(f"\n    {what_to_insert} (insert numbers between {min} and {max-1}): > ")
        if userIn.isdigit() == True:
            if int(userIn) in range(min, max):
                isValid = True

        else:
            print("Please insert a number! ")
            wait_enter()

    return str(userIn)


