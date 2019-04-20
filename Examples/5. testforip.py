"""
Program to take inputs from user and make the input into a list
"""
tlist=[]

for i in range(5):
    print("enter values")
    x=input()
    tlist.append(int(x))

print(tlist)