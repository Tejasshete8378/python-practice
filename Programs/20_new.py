# File Name: 20_new.py
# Author: 
# Purpose:

'''CTL Challenge #1
Now it is your turn to build your logic.

Problem Statement:
Instead of just summing the numbers, write a function that takes a list of numbers and returns a dictionary 
containing three keys:

sum: The total sum of the numbers.
even_count: The count of even numbers in the list.
average: The arithmetic mean of the list.

Constraints:
You must use a list comprehension to filter the even numbers.
Do not use the built-in sum() function for the sum key; implement your own loop logic.
Handle the case where the list might be empty to avoid a "division by zero" error when calculating the average.'''

print('\n','*'*30,"Welcome to the Program",'*'*30,'\n')

l1 = eval(input("Enter List: "))

if len(l1) != 0:
    l2 = [i for i in l1 if i % 2 == 0]
    
    total = 0

    for i in l1:
        total = total + i 

    avg = total/len(l1)

    data = {'Even Numbers': l2, 'Sum of all Numbers': total, 'Average of all Numbers': avg}
 
    print('\n',data,'\n')

else:
    print("List is Empty, Please enter List\n")
    
print('*'*30,"Thank You",'*'*30)

