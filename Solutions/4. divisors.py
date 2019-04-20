"""
To get a number as user input and display a list of its divisors.
"""
x=int(input("Please enter a number : "))
ls=[]

for i in range(2,x):
    if x%i==0:
        ls.append(i)
    
print("The required list is ",ls)