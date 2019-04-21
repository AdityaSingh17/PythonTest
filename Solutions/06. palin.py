"""
To get a string from user as input, and tell whether it is palindrome or not.
"""

x=str(input("Please enter the string : "))
print(x)
y = x[::-1]                                                 #gets a substring from start to end, -1 indicates that it comes from right to left(reads backwards)
print(x,y)
if x==y:                                                    #compares the two lists
    print("Palindrome!")
else:
    print("Not palindrome!")

"""
x[start:end:increment/decrement]    gives a sublist.
Since strings are lists of characters, it gives a substring.
If start index is not given it starts from starting by default, same with end.
The increment may be positive (left to right : forward) , or negative (right to left : backward)
"""

