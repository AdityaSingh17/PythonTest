"""
Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
A  dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.
"""
tdic = {
            #key      : value,
            "orange"  : "orange",                      #comma required 
            "apple"   : "red",
            "banana"  : "yellow"                        #comma not required for the last one
       }
print(tdic)
"""
alter to create a new dictionary

tdict = dict(apple="red",orange="orange",banana="yellow") 
#keys are not string literals
# = sign is used to assign value to key
"""

x=tdic["apple"]                                         #the value for key apple is stored in x
print(x)

x=tdic.get("apple")                                     #alter for above
print(x)

tdic["banana"]  = "black"                                #change value for key
print(tdic)

for x in tdic:
    print(x)                                                #print all keys of dictionary

for x in tdic:
    print(tdic[x])                                          #print all values 

#alter for values
# for x in tdic.values(): print(x)

for x,y in tdic.items():
    print(x,y)                                              #print all items(keys and values) #The key value pairs are a list of tuples!


if "apple" in tdic:
    print("yes exists")

#if "red" in tdic:                                             cant search for values alone
 #   print("yes value exists")

print(len(tdic))                                            #prints the total number of key value pairs


tdic["strawberry"]="pink"                    #alter tdic.update({"strawberry":"pink"})               #adding a new key-value pair
print(tdic)

tdic.pop("apple")                   #alter del tdic["apple"]                         #removes item with specified key
print(tdic)

print(str(tdic.popitem()))                                                #removes the last inserted item

sdic=tdic.copy()                                                          #copies tdic to sdic
print(sdic)

#alter to copy
"""
sdic = dict(tdict)
"""

tdic.clear()                                                               #clears 
print(tdic)                                                                #no error

del tdic
#print(tdic)    will cause error

#to create a dictionary from specified key-value pairs

x=('apple','mango','banana')
y=0

tdic = dict.fromkeys(x,y)
print(tdic)

#if y not initialised, the value is "none"
 
tdic = dict.fromkeys(x)
print(tdic)

x=tdic.keys()                               #x is a list containing the keys
print(x)

x=tdic.values                               #x now is a list of values
print(x)

x=tdic.items()                               #x is now a tuple for key value pairs 
print(x)                                     #op : dict_items([('key','value'),('key','value')...])

dic = dict()
dicti = dict()
print(dic)
x=2
dicti[x]=dict.get(dic,x,0)+1                         #get(KEY,DEFAULT) #if key exists, add one to its value, or else make a new key with DEFAULT value.
print(dicti)
#The get() will not give traceback if key is not present in the dictionary, infact it will make one if it doesnt already exists.