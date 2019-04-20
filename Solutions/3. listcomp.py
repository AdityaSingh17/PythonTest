"""
To get input from the user and create a list.
To get input from the user and print all items of the list less than that number.
(To create a new list containing these numbers)
"""

n=int(input("Enter the number of elements in list : "))
ls=[]
for i in range(n):
    x=int(input("Enter the element"))
    ls.append(x)

print("The list is\n",ls)

ip=int(input("Enter the value : "))

for i in ls:
    if(i<ip):
        print(i)

print([i for i in ls if i<ip])

"""
The for loop for printing may be written in a single line as
print([i for i in ls if i<5])
#This is called list comprehension.
Basic syntax :  [output] for [item] in [list] if [filter]
"""