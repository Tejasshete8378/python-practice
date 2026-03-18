# File Name: print_characters_of_string_index_wise.py
# Auther : Tejas Shete
# Purpose : To Print Characters of a String Index Wise

print("\n-----Program to Print Characters of a String Index Wise-----\n")

text = input("Enter String: ")

if text == '':
    print("String Cannot be Empty")
else:
    for i, ch in enumerate(text): #enumerate(iterable, start=0) 
        print(f"Character '{ch}' is present at index {i}")
   
    