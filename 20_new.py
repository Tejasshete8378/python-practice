# File Name: 20_new.py
# Author: 
# Purpose:

'''CTL Challenge #1
Now it is your turn to build your logic.

Problem Statement:
Take List of Numbers and do the following operations.

sum: The total sum of the numbers.
even_count: The count of even numbers in the list.
average: The arithmetic mean of the list.

Constraints:
You must use a list comprehension to filter the even numbers.
Do not use the built-in sum() function for the sum key; implement your own loop logic.
Handle the case where the list might be empty to avoid a "division by zero" error when calculating the average.'''

import ast

print('\n','*'*30,"Welcome to the Program",'*'*30,'\n')

user_input = input("Enter List of Numbers: ")

l2 = []
total = 0
avg = 0

# Check whether Input is provided or not 
if not user_input.strip():
    print("No Input Provided\n")
else:
    # Covert User String into List 
    # ast.literal_eval converts string to integer list so no need to convert it to int
    l1 = ast.literal_eval(user_input)

    #Check whether List is Empty or Not
    if len(l1) == 0:
        print("List is Empty")
    else:
       
        # 1) Using list comprehension to filter the even numbers.
        l2 = [i for i in l1 if i % 2 == 0]

        # 2) Using Own logic to calculate sum    
       
        for i in l1:
            total = total + i 

        # 3) "Division by zero" error already handled.
        avg = total/len(l1)

    data = {'Even Numbers': l2, 'Sum of all Numbers': total, 'Average of all Numbers': avg}
 
    print('\n',data,'\n')
  
print('*'*30,"Thank You",'*'*30)

