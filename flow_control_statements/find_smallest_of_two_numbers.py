# File Name: find_smallest_of_two_numbers.py
# Author: Tejas Shete
# Purpose: To Find smallest of Two given numbers

print("\n-----Program to Find smallest of Two given numbers-----\n")

num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))

if num1<num2:
    print("Number {} is smaller than {}" .format(num1,num2))
else:
    print("Number {} is smaller than {}" .format(num2,num1))
    
