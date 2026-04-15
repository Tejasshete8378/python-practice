'''
File Name: 17_selective_filter.py
 Author: Tejas Shete
 Problem Statement: Problem Statement:
Write a program that iterates through numbers from 1 to 50.
A) If the number is a multiple of 3, print it.
B) If the number is a multiple of 5, print it.
C) If it is a multiple of both 3 and 5, print the word "Bingo" instead of the number.'''

print('\n','*'*30,"Welcome to the Program",'*'*30,'\n')

for i in range(1,51):
    if i%3 == 0 and i%5 == 0:
        print(f"{i}: Bingo")
    elif i%3 == 0:
        print(f"Number {i} is multiple of 3")
    elif i%5 == 0:
        print(f"Number {i} is multiple of 5")
    
print('\n','*'*30,"Thank You",'*'*30,'\n')

