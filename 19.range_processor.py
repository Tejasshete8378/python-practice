'''
File Name: 19_range_processor.py
Author: Tejas Shete
Purpose: To Create a Intelligent Range Processor
'''

'''Write a program that asks the user for a Start number and an End number.
Generate a sequence of all numbers between the start and end (inclusive).
Filter the sequence to keep only numbers that are:Divisible by 3 OR Divisible by 5.
Transform the data: Take these filtered numbers and create a new list where each number is squared.
Display:
The original filtered numbers (before squaring).
The final squared list.
The average of the squared numbers.'''

print('\n','*'*30,"Welcome to the Intelligent Range Processor",'*'*30,'\n')

start=int(input("Enter Start Number: "))
end=int(input('\n'"Enter End Number: "))
 
sequence=[i for i in range(start,end+1)]

print('\n',f"Range from {start} to {end}: {sequence} ")