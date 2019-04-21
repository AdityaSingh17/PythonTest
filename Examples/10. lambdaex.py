"""
Program to demonstrate the usage of lambda functions.
A lambda function is a small anonymous function.
A lambda function can take any number of arguments, but can only have one expression.
"""

x = lambda a : a*2                                   #function_name = lambda arg1,arg2...,argn : expression
print(x(5))

x = lambda a,b : a*b                                 #2 arguments passed
print(x(10,20))

def myfunc(n):                                       #normal function definition
  return lambda a : a * n                            #lambda function in normal function

mydoubler = myfunc(2)                                #here "n" value is set
mytripler = myfunc(3)

print(mydoubler(11))                                 # "a" value is passed
print(mytripler(11))