#File Name:  read_multiple_values_in_single_line.py
#Author: Tejas Shete
#Purpose: To Read multiple values in single line and perform oprations

# Read two integers from a single line input
a,b = (int(x) for x in input("Enter two numbers: ").split())

print("Product is: ",a*b)