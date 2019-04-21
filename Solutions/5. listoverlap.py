"""
To generate a list that contains the common elements of two lists of different sizes, the returned list must not have duplicate items.
"""

ls1 = [1,2,3,3,5,4,5,7,9,0]
ls2 = [1,3,5,7,7,8,11,23,45,67,89]
ls3=[]

for x in ls1:                                                                      #this method will have duplicates.
    for y in ls2:
        if x==y:
            ls3.append(x)

print(ls3)

#write the same in one line and without duplicates.

print(list(dict.fromkeys([x for x in ls1 if x in ls2])))                        #dict.fromkeys is used to remove the duplicates
                                                                                #fromkeys() accepts a list as input, and the list() converts the dict into list.


# [ls3.add(x) for x in ls1 for y in ls2 if x == y] alter for the method( line 9-13 )

#  we can also generate the random list using the random function as shown below

import random
ls1 = random.sample(range(1,100),10)                                            #select 10 numbers from 1-100
ls2 = random.sample(range(1,100),15)

print(ls1)
print(ls2)
print(list(dict.fromkeys([x for x in ls1 if x in ls2])))    

