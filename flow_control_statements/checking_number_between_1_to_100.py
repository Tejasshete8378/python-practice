# File Name : checking_number_between_1_to_100.py
# Author : Tejas Shete
# Purpose : To Check whether entered number is between 1 to 100

print("\n-----Program to Check number between 1 to 100-----\n")
num = int(input("Enter Number: "))

if 1<=num<=100:
    print("Entered Number {} lies between 1 to 100" .format(num))
else:
    print("Entered Number {} does not lies between 1 to 100" .format(num))
