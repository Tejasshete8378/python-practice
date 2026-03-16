# File Name: find_smallest_of_two_numbers.py
# Author: Tejas Shete
# Purpose: To Find smallest of Two given numbers

print("\n-----Program to Find smallest of Two given numbers-----\n")

num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))

if num1<num2:
    print(f"Number {num1} is smaller than {num2}")
elif num2<num1:
    print(f"Number {num2} is smaller than {num1}")
else:
    print("Both numbers are equal")
        
