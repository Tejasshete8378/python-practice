'''
File Name: 19_range_processor.py
Author: Tejas Shete
Purpose: To Create a Intelligent Range Processor
'''

'''Write a program that asks the user for a Start number and an End number.
Generate a sequence of all numbers between the start and end (inclusive) in Forward Direction.
Generate a sequence of all numbers between the start and end (inclusive) in Backward Direction.
Filter the sequence to keep only numbers that are:Divisible by 3 OR Divisible by 5.
Transform the data: Take these filtered numbers and create a new list where each number is squared.
Display:
The original filtered numbers (before squaring).
The final squared list.
The average of the squared numbers.'''

print('\n','*'*30,"Welcome to the Intelligent Range Processor",'*'*30,'\n')

start=int(input("Enter Start Number: "))
end=int(input('\n'"Enter End Number: "))
 
filtered_nums=[i for i in range(start,end+1) if i%3 == 0 or i%5 == 0]

if not filtered_nums:
    print('\n',"No Numbers found Divisible by 3 or 5 in this range")
else:
    squared_nums = [i**2 for i in filtered_nums]

    avg = sum(squared_nums)/len(squared_nums)

print()

print("Sequence in Ascending Order: ",end=' ')
for i in range(start,end+1):
    print(i,end=' ')

print()

print("\nSequence in Descending Order: ",end=' ')   
for i in range(end,start-1,-1):
    print(i,end=' ')

print('\n')
print(f"List of Numbers Divisible by 3 or 5: {filtered_nums}")

print()

print(f"Square of Numbers Divisible by 3 or 5: {squared_nums}")

print()

print(f"Average of Squared Numbers: {avg}")

print()

print('*'*30,"Thank You",'*'*30,'\n')

