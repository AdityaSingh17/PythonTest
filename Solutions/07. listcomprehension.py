"""
An example to list comprehension, generate a list and create a new list that contains only the even numbers.
"""
import random
x = random.sample(range(1,50),10)                           #retruns a list of 10 random numbers bw 1 and 50
print(x)
y = [eg for eg in x if eg%2==0]                             #eg is appended into y ; for every eg belongs to x : such that eg%2==0
print(y)
