""" Customer Relationship Management (CRM) module

Data table structure:
    - id (string)
    - name (string)
    - email (string)
    - subscribed (int): Is subscribed to the newsletter? 1: yes, 0: no
"""


from model.data_manager import *

DATAFILE = "model/crm/crm.csv"
HEADERS = ["id", "name", "email", "subscribed"]
ID = 0   # avoid magic numbers
NAME = 1
EMAIL = 2
SUBSRIBED = 3

crm_list = (read_table_from_file(DATAFILE, separator=';'))
