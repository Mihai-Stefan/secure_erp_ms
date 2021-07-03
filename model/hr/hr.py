""" Human resources (HR) module

Data table structure:
    - id (string)
    - name (string)
    - birth date (string): in ISO 8601 format (like 1989-03-21)
    - department (string)
    - clearance level (int): from 0 (lowest) to 7 (highest)
"""

from model import data_manager, util
from model.data_manager import *
from model.util import *


DATAFILE = "model/hr/hr.csv"
HEADERS = ["Id", "Name", "Date of birth", "Department", "Clearance"]

hr_list = (read_table_from_file(DATAFILE, separator=';'))

ID = 0   # avoid magic numbers
NAME = 1
BIRTH_DAY = 2
DEPARTMENT = 3
CLEARANCE = 4

def list_birthdates():
    birthdays = []
    birthdays_sorted = []
    birthday_dates = []
    for i in range(len(hr_list)):
        birthdays.append(hr_list[i][2])

    for date in birthdays:
        date_object = datetime.datetime.strptime(date, "%Y-%m-%d")
        date_date = date_object.date()
        birthday_dates.append(date_date)

    return birthday_dates

def list_separated_strings_birthdays():
    birthdays = []
    birthdays_separated = []
    for i in range(len(hr_list)):
        birthdays.append(hr_list[i][2])
    for j in birthdays:
        birthday = j.split("-")
        birthdays_separated.append(birthday)
    
    return birthdays_separated

def calculate_age(birthdate):
    today = datetime.date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    
    return age

