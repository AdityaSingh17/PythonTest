"""
To create a class containing members and methods, create objects of a class and use methods to alter the member values.
"""

class mclass:                                                           #class definition
    a=10                                                                #member variable
    def mfunc(self):                                                    #member function, the "self" parameter refers to the current instance of the class.
        print("the value stored in a is ="+str(self.a))                 #self is like "this" pointer in c/c++
        print("enter new value for a ")
        self.a = input()
        print("new value of a = "+str(self.a))

obj = mclass()                                                          #object creation
print(obj.a)                                                            #print the initial value
obj.mfunc()                                                             #call the method to change value of the function

"""
The class methods or the __init__() must have a parameter (the first in argument list) that refers to the current instance of the class.
The parameter "self" in the above example is one such name, the reference may be given any legal variable name.
"""

#The __init__() is a built-in function that is automatically called when the object is being created. It is used to initialize the object or perform important necessary functions.


class stu:
    def __init__(abc,name,usn):                                         #abc is the reference name
        abc.name = name
        abc.usn = usn

print("direct passing")
a = stu("adi",19)
print(a.name,a.usn)

print("passing user inputs")
x = str(input("Enter the student name : "))
y = int(input("Enter the student usn : "))

a = stu(x,y)
print(a.name,a.usn)
        
a.name = "ADITYA SINGH"                                                  #modifying object values
print(a.name,a.usn)

del a.name                                                               #deleting object values
print(a.usn)            #since we deleted the name, calling a.name will raise errors

del a                                                                    #deleting the object
#print(a.name,a.usn)    will cause errors.