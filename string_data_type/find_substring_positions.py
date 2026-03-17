# File Name: find_substring_positions.py
# Author: Tejas Shete
# Purpose: To Find Positions of Substrings and Total Number of Occurences in given String

print("\n-----Program To Find Positions and Occurences of Substrings-----\n")
s=input("Enter Main String: ")
subs=input("Enter Sub String: ")

if subs == "":
    print("Substring cannot be Empty")
else:
    main=s.lower()
    sub=subs.lower()
    

    n=len(main)
    count = 0
    pos=0

    while True:
        i=main.find(sub,pos,n) #Here even if n is not used its ok Because find() automatically searches till end
        if i==-1:
            break
        #Here there can be Else but as per 
        #Industry Standard after break else is not used
        print("Found at Index:",i)
        count = count+1
        pos=i+len(sub)

    print("Total Number of Occurences: ",count)

    if count == 0:
        print("Main String Does not contain Entered Substring")

#If Overlapping logic needed then use pos=i+1
    