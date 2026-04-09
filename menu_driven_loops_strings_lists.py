# File Name: menu_driven_loops_strings_lists.py
# Author: Tejas Shete
# Purpose: To Create a Program to Print the Characters of a Given String

print("\n-----Welcome to Menu Driven Program of Loops, Strings and Lists-----\n")

print("\n 1) Print Hello 10 Times\n")
print("\n 2) Display Numbers from 0 to 10\n")
print("\n 3) Display Odd Numbers from 0 to 20\n")
print("\n 4) Display Numbers form 10 to 01 in Descending Order\n")
print("\n 5) Calculate and Display the Sum of Elements in User provided List \n")
print("\n 6) Print Each Character of a Given String\n")
print("\n 7) Print Each Character of a Given Index along ith index\n")

option=int(input("\n Select Option from Above Given List: "))

if option == 1:
    s='Hello'
    a=1
    while a<=10:
        print(a,')',s)
        a=a+1
elif option == 2:
    for b in range(0,11):
        print(b, end=' ')
        b=b+1 
elif option == 3:
    print("\n Odd Numbers between 0 to 20 are as follows:\n")
    for c in range(21):
        if c%2!=0:
            print(c, end=' ') 
            c=c+1      
elif option == 4:
    d=10
    while d>0:
        print(d, end=' ')
        d=d-1
elif option == 5:
    e = list(map(int, input("Enter Numbers separated by Space: ").split()))
    total=0

    for i in e:
        total=total + i
    print(f"Sum = {total}")



