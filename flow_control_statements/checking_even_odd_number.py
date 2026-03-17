# File Name: checking_even_odd_number.py
# Author: Tejas Shete
# Purpose: To Create a Program to chek whether the Entered Number is Even or Odd

print("\n-----Program to Check whether Entered Number is Even or Odd-----\n")

num = int(input("Enter Number: "))

if num%2 == 0:
    print(f"{num} is an Even Number")
else:
    print(f"{num} is an Odd Number")    