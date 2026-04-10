# File Name: 05_program_to_print_sum_of_two_numbers.py
# Author:    Tejas Shete
# Purpose:   To take two numbers and print their Sum

print('Welcome to the Program to print sum of Two Numbers')
print()

num1 = float(input("Enter First Number: "))
num2 = float(input("Enter Second Number: "))

total = num1 + num2

print('\n' + '-'*20)
print(f'The Sum = {total:.2f}') #.2f limit output to 2 decimal places
print('-'*20)