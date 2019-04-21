"""
Program to demonstrate the following
-> if
-> else-if
-> else-if ladder
-> while loop
-> for loop
-> break and continue statements
"""

"""
if
else if
else if ladder
"""
a=10
b=11
c=12

if a>b & a>c :                                  #alter if a>b and a>c:          #for and both must be true, for or one must be true
    print("a is greatest")
elif b>a & b>c :
    print("b is greatest")
else:
    print("c is greatest")


if a<b : print("a is smaller")                  #short hand if

print("a is greater") if a>b else print("b is greater")            #if condtion true, left is executed, else right


"""
while loop
"""
i=1                                                     #for while we need to initialise the variable before iteration
while i<5:
    print(i)
    i+=1                                                #increment statement

#break and continue have the same meaning as in other languages!


"""
for loop
"""
ls = ["apple","mango","banana","orange"]
for x in ls:
    print(x)                                            #looping through a list


x="aditya singh"
for y in x:
    print(y)                                             #strings are nothing but character arrays,prints char by char


for x in range(6):                            #starts from 0(by default) to 6-1, increments by 1(by default).
     print(x)

for x in range(10,30,3):                       #starts from 10 to 30-1, increments by 3.
    print(x)

for x in range(4):
    print(x)
else:
    print("loop terminated")                   #default statement that is executed once the loop is terminated, termination should not be by break or continue.


for x in range(4):
    for y in range(3):
        print(x,y)                              #nested loops