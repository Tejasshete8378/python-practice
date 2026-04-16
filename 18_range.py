# File Name:
# Author: Tejas Shete

'''
Write a Python program that asks the user for a range (a start and an end number). The program should then iterate through that range and perform the following:

Filter: Identify whether each number is Even or Odd.

Categorize: Store these numbers into two separate lists: even_numbers and odd_numbers.

Analyze: Calculate the sum of the odd numbers and the count of the even numbers.

Report: Display the final lists and the calculated metrics to the user.
'''

print('\n','*'*30,"Welcome to the program",'*'*30,'\n')

start = int(input("Enter Starting Number: "))
end = int(input("Enter Ending Number: "))

even_number=[]
odd_number=[]

for i in range(start,end+1):
    if i%2 == 0:
        even_number.append(i)
    else:
        odd_number.append(i)

print(f"List of Even Numbers from the Range {start,end} provided: {even_number}")
print(f"List of Odd Numbers from the Range {start,end} provided: {odd_number} ")

print('\n',"Do you want see Sum: ")
print("Press 1 to see the sum of Even Numbers")
print("Press 2 to see the sum of Odd Numbers",'\n')

choice = int(input("Please enter your choice: "))

even_sum = 0
odd_sum = 0

if choice == 1:
    
    for i in even_number:
        even_sum = even_sum + i
    print(f"Sum of Even Numbers of Range{start,end}: {even_sum}")
elif choice == 2:
    
    for i in odd_number:
        odd_sum = odd_sum + i
    print(f"Sum of Odd Numbers of Range{start,end}: {odd_sum}")

print('\n','*'*30,"Thank You",'*'*30,'\n')

