"""
Program to demonstrate the decleration and usage of functions.
"""

def myfun():                                                #function definition
    print("hello world! (inside a function)")

myfun()                                                     #function call

def pint(x):                                                #functions with parameter
    print(x)

for i in range(5):
    pint(i)

def dval(x="india"):                                         #function with a default value
    print("my country is "+x)

dval()                                                       #default value will be used
dval("usa")                                                  #default value is overwritten
dval("france")

#if we pass a list to a function, it will be treated as a list ONLY in function, same with other datatypes.

def fivetable(x):                                            #function that returns a value, type casting can be done to change or specify return values.
    return 5*x

for i in range(1,11):
    print("5 * "+str(i)+" = "+str(fivetable(i)))

def fact(x):                                                  #RECURSION!
    if(x==1):
        return x 
    else:
        return(x*fact(x-1))
    
print(fact(5))