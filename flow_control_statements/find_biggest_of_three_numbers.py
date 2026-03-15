#File Name:  find_biggest_of_three_numbers.py
#Author: Tejas Shete
#Purpose: To Find Biggest of Three Numbers

print("\n------Program to Find Biggest of Three Numbers------\n")
num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))
num3 = int(input("Enter Third Number: "))


if num1>num2 and num1>num3:
    print("Biggest Number: ", num1)
elif num2>num3:
    print("Biggest Number: ", num2)
else:
    print("Biggest Number: ", num3)        