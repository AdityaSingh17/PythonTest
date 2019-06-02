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

obj = mclass()                                                          #object creation (initialization)
print(obj.a)                                                            #print the initial value
obj.mfunc()                                                             #call the method to change value of the function

"""
The class methods or the __init__() must have a parameter (the first in argument list) that refers to the current instance of the class.
The parameter "self" in the above example is one such name, the reference may be given any legal variable name.
"""

#The __init__() is a built-in function that is automatically called when the object is being created. It is used to initialize the object or perform important necessary functions.


class stu:
    def __init__(self,name,usn):                                        #We are creating a constructor. Used to initilize class variables.
        self.name = name
        self.usn = usn

    def __del__(self):                                                  #Destructor, it is called automatically when scope is over or the variable is reassigned with another value.
        print("I am destructed :((")

print("direct passing")
a = stu("adi",19)
print(a.name,a.usn)

print("passing user inputs")
x = str(input("Enter the student name : "))
y = int(input("Enter the student usn : "))

a = stu(x,y)                            #same as stu.__init__(a,x,y)    
print(a.name,a.usn)

#a = 45                 This will call the destructor
#print(a)               First the destructor is printed, then this a value(45) is printed.

a.name = "ADITYA SINGH"                                                  #modifying object values
print(a.name,a.usn)

del a.name                                                               #deleting object values
print(a.usn)            #since we deleted the name, calling a.name will raise errors

del a                                                                    #deleting the object
#print(a.name,a.usn)    will cause errors.

"""
INHERITANCE
"""
class zclass:                                                          
    a=10                                                                
    def mfunc(self):                                                    
        print("the value stored in a is ="+str(self.a))                 

class nclass(zclass):                                   #nclass will inherit mclass
        print("Hello, i am in class nclass")
        
a = nclass()                            #made object for SUBCLASS, it will have access to methods and functions of both derived class and the base class.
a.mfunc()
#First the print of nclass is called, then the mfunc() of zclass is called.
#If the subclass has no constructor, it calls the base class' constructor.