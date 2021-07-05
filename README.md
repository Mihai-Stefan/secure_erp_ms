# SECURE ERP

**Team project:**  2 programmers \* 4 work days >> 8 Man-Days

**Technology/Language used:** 100% Python, Console I/O



**Enterprise Resource Planning (ERP)** is the integrated management of main business processes, often in real time and mediated by software and technology.
Keep track of customers, transactions and employees.
The data is kept in CSV files [client request].



## Client [school] requirements:

* The client want to see a solution that is *super secure*: a short and clean codebase that works on local files, strictly on offline computers. 

* They require a highly modularized structure

* Create a variant of the MVC (model-view-controller) architecture for terminal and local data files.

* Do not spend much time on input checking. This time it is not a problem if a badly formatted data breaks your code.



## Description:

**CRM module** = Customer Relationship Management Module

1 - Add new customer

2 - Print all the customers

3 - Edit customer [by ID]

4 - Delete a customer [by ID]

5 - Subscribed customer emails [emails list of subscribed customers]



**Sales module**

1 … 4 - Provide basic CRUD operations for transactions.

5 - Get the transaction that made the biggest revenue.

6 - Get the product that made the biggest revenue altogether.

7 - Count number of transactions between two given dates.

8 - Sum the price of transactions between two given dates.



**HR module**

1...4 - Provide basic CRUD operations.

5 - Return the names of the oldest and the youngest employees as a tuple.

6 - Return the average age of employees.

7 - Return the names of employees having birthdays within the two weeks starting from the given date.

8 - Return the number of employees with at least the given clearance level.

9 - Return the number of employees per department in a dictionary (like `{'dep1': 5, 'dep2': 11}`).



## Usage samples

Main menu and exit from app:

![00_main](\images\00_main.jpg)



CRM ( Customer Relationship Management )  module:

![01_crm](\images\01_crm.jpg)



Sales module:

![02_sales](\images\02_sales.jpg)



HR ( Human Resources ) module:

![03_hr](\images\03_hr.jpg)
