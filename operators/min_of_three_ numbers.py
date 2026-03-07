# This function takes three numbers (a, b, c) as input
# and returns the smallest value using a conditional expression
def find_minimum(a,b,c):
    return a if a<b and a<c else b if b<c else c

num1 = int(input("Enter First Number:"))
num2 = int(input("Enter Second Number:"))
num3 = int(input("Enter Third Number:"))

# Calling the function 
# and storing the returned minimum value in minimum_value
minimum_value = find_minimum(num1, num2, num3)

print("Minimum Value:", minimum_value)
