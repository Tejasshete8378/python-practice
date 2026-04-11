# File Name: 13_Find_Smallest_of_2_Numbers_(if n%2==0).py
# Author: Tejas Shete
# Purpose: To Find smallest of Two given numbers

'''

Q 3) Check whether given number is even or odd
Q 4) Check whether given number is in between 1 and 100(inclusive) (if n>=1 and n<=100)'''

print("\n-----Program to Find smallest of Two given numbers if First Number is Even-----\n")

num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))

if num1%2 == 0:
    if num1==num2:
        print("Both numbers are equal")
    else:
        smallest = min(num1,num2)
        print(f"The Smallest Number is: {smallest}")
else:
    print(f"{num1} is an ODD Number")
