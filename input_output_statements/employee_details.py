# File Name : employee_details.py
# Author : Tejas Shete
# Purpose : Read employee details from the user and display them.

# Reading Employee Details
emp_no = int(input("Enter Employee Number: "))
emp_name = (input("Enter Employee Name: "))
emp_salary = float(input("Enter Employee Salary: "))
emp_address = (input("Enter Employee Address: "))
married_input = input("Is Employee Married? (True/False): ")

# Convert string input to boolean value
emp_married = married_input.strip().lower() == "true"

print("\n Employee Details are as follows: ")
print("\n Employee Number: ", emp_no)
print("\n Employee Name: ", emp_name)
print("\n Employee Salary: ", emp_salary)
print("\n Employee Adress: ", emp_address)
print("\n Employee Married: ", emp_married)