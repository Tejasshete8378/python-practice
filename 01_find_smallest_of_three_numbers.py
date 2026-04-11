# File Name: 01_find_smallest_of_three_numbers.py
# Author: Tejas Shete
# Purpose: To find Smallest of given Three numbers

print("\n-----Program to find Smallest of given Three Numbers-----")

num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))
num3 = int(input("Enter Third Number: "))

if num1==num2==num3:
    print(f"All Three Numbers are Equal")
elif num1<num2 and num1<num3:
    print(f"Number {num1} is smallest")
elif num2<num1 and num2<num3 :
    print(f"Number {num2} is smallest")
else:
    print(f"Number {num3} is smallest")
    
    