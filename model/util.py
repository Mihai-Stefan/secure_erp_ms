import random
import string
import itertools


def generate_id(number_of_small_letters=4,
                number_of_capital_letters=2,
                number_of_digits=2,
                number_of_special_chars=2,
                allowed_special_chars=r"_+-!"):
    #return 'T!uq6-b4Yq'

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



