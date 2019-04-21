"""
Tuple is a collection which is ordered and UNCHANGEABLE. Allows duplicate members.
Tuples are written in round brackets ()
"""
mtup = ("apple","banana","mango","banana","orange")  #alter mtup=tuple(("apple","banana",....))  #here the tuple() is a constructor to create tuples
print(mtup)
print(mtup[1])                                      #to print a specific element from tuple

#mtup[1] = "mangoessss"                              #tuple values cannot be changed,error will be give
print(mtup)                                         #prints the unchanged tuple

for x in mtup:                                      #loop through a tuple
    print(x)

if "mangoessss" in mtup :                           #check for item in tuple
    print("'Mangoesss exists'")
    print(mtup.index("mangoesss"))                  #print the index of element
else:
    print("mangoesss does not exist!")

y=mtup.count("banana")                               #to count occurences of an element
print("the occurence of banana is "+str(y))

y="banana"                                           #alter for above, in place of directly giving , the value is given indirectly through a variable!
x=mtup.count(y)
print("the occurence of banana is "+str(x))
print("the occurence of banana is "+str(y))

x=len(mtup)
print(x)

#we cannot add items to tuple, once its been created! 
#also we cannot remove items from tuples, but we can delete the entire tuple !

del mtup
#print(mtup)        will raise an error! coz mtup existance is deleted!
