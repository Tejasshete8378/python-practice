# File Name: 21_sum_of_numbers_inside_list.py
# Author: Tejas
# Purpose : To write a logic to do Sum of Numbers inside list without using inbuild sum function

import ast

print('\n','*'*30,'Welcome to the Program','*'*30,'\n')

total = 0

user_input = input("Enter List: ")
if not user_input.strip():
    print("No Input Provided")
else:
    l1 = ast.literal_eval(user_input)
    if len(l1) == 0:
        print("List is Empty")    
    else:
        
        for i in l1:
            total = total + i
        
print(f"Sum:{total}")

print('\n','*'*30,"Thank You",'*'*30,'\n')