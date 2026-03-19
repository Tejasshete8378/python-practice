Python enumerate() Function

Introduction

enumerate() is a built-in Python function used to iterate over an iterable while keeping track of the index position of each element.
It is commonly used with data types such as strings, lists, and tuples.
Normally, a loop returns only the element value.
Using enumerate(), both the index and the element can be accessed together.
_________________________________________________________________________________________________________________________________________
Syntax

enumerate(iterable, start=0)

•	iterable : A sequence such as string, list, or tuple

•	start : The starting index value (default is 0)
________________________________________
Example 1: Using enumerate() with a String
text = "CAT"

for i, ch in enumerate(text):
    print(i, ch)
Output
0 C
1 A
2 T
Here, i represents the index position and ch represents the character.
________________________________________
Example 2: Using enumerate() with a List
fruits = ["Apple", "Mango", "Banana"]

for i, fruit in enumerate(fruits):
    print(i, fruit)
Output
0 Apple
1 Mango
2 Banana
________________________________________
Example 3: Changing the Starting Index
text = "DOG"

for i, ch in enumerate(text, start=1):
    print(i, ch)
Output
1 D
2 O
3 G
________________________________________
Comparison Without Using enumerate()
text = "CAT"
i = 0

for ch in text:
    print(i, ch)
    i += 1
This approach requires manual handling of the index variable.
________________________________________
Advantages of enumerate()
•	Produces cleaner and more readable code
•	Eliminates the need for manual index management
•	Reduces the possibility of logical errors
•	Widely used in professional Python development
•	Frequently discussed in technical interviews
________________________________________
Conclusion
enumerate() is an efficient and recommended method for iterating through an iterable when both index and element values are required.

