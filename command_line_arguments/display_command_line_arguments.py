#File Name:  display_command_line_arguments.py
#Author: Tejas Shete
#Purpose: To Display Command Line Arguments

from sys import argv
print("Number of Command Line Arguments: ",len(argv))
print("List of Command Line Arguments: ",argv)
print("Command Line Arguments One by One: ")
for i in argv:
    print(i)
