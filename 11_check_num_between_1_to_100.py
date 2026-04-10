# File Name: check_num_between_1_to_100.py
# Author: Tejas Shete
# Purpose: To Check whether the entered number lies between 1 to 100

print("\n-----Program to check Whether Entered Number lies between 1 to 100-----\n")

num = int(input("Enter Number: "))

if 1<=num<=100:
    print(f"{num} lies between 1 to 100")
else:
    print(f"{num} does not lie between 1 to 100")    