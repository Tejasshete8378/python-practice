# Program to Find Maximum of Three Numbers

# This function takes three numbers (a, b, c) as input
# and returns the largest value using a conditional expression
def find_maximum(a,b,c):
    return a if a>b and a>c else b if b>c else c

num1 = int(input("Enter First Number:"))
num2 = int(input("Enter Second Number:"))
num3 = int(input("Enter Third Number:"))

# Calling the function 
# and storing the returned maximum value in maximum_value
maximum_value = find_maximum(num1,num2,num3)

print("Maximum Value:", maximum_value)
