''' 
File Name: 16_string_snake_case.py 
Author: Tejas Shete
Probme Statement: Write a Python program that takes a user's string and repeats it a 
specific number of times, but applies different "styles" based on whether the current count 
is even, odd, or a multiple of five.

1) takes a user's string
2) repeats it a specific number of times,
3) applies different "styles" based on even, odd, or a multiple of five.
'''

print('\n','*'*30,"Welcome to the Program of Strings",'*'*30,'\n')

text = input("Enter String: ")

repeat = int(input("Enter Number of times you want to Repeat the String: "))

if repeat<0:
      print("Invalid Input, Please Enter Positive Number Greater than Zero")
else:
    i=1
    while i<=repeat:
        
        # Priority 1: Check Multiple of 5 First
        if i%5 == 0:
            print(f"Line {i}: {text.capitalize()}")
        
        # Priority 2: Check Even
        elif i%2 == 0:
            print(f"Line {i}: {text.upper()}")
        
        # Priority 3: Check Odd (Everything Else)    
        else:
            print(f"Line {i}: {text.lower()}")
        i=i+1

print('\n','-'*40,"Thank You",'-'*40,'\n')