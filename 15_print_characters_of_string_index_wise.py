# File Name: print_characters_of_string_index_wise.py
# Auther : Tejas Shete
# Purpose : To Print Characters of a String Index Wise

'''print("\n-----Program to Print Characters of a String Index Wise-----\n")

text = input("Enter String: ")

print("Please select")

choice = int(input(""))

if text.strip() == '':
    print("String Cannot be Empty")
    exit()
for i,ch in enumerate(text): #enumerate(iterable, start=0)
    print(f"The Character {ch} is Present at Index {i}")
'''
print("\n-----Program to Print Characters of a String Index Wise as per User Demand-----\n")

text = input("Enter String: ")

print("\nPress 1 to Remove Spaces: \n")
print("\nPress 2 to Keep Spaces: \n")

choice1 = int(input("Enter Choice out of above 2 Options: "))

print("\nPress 3 to get Positive Index: \n")
print("\nPress 4 to get Negative Index: \n")

choice2 = int(input("Enter Choice out of above 2 Options: "))

if choice1 == 1 and choice2 == 3:
    new_text = "".join(text.split())
    for i,ch in enumerate(new_text):
        print(f"The Character {ch} is present at Index {i}")

elif choice1 == 1 and choice2 == 4:
    new_text = "".join(text.split())
    for i,ch in enumerate(new_text):
        print(f"The Character {ch} is present at Index {i-len(new_text)}")  

elif choice1 == 2 and choice2 == 3:
    for i,ch in enumerate(text, start=0):
        print(f"The Character {ch} is present at Index {i}")     

elif choice1 == 2 and choice2 == 4:
    for i,ch in enumerate(text, start=0):
        print(f"The Character {ch} is present at Index {i - len(text)}")

print("\n-----Thank You-----\n")   