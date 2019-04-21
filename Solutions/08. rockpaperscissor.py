"""
To design a two player rock paper scissors game, by asking the user for input and the other player is the computer.
"""
def comp(ip1,ip2):
    print(str(ip1))
    print(str(ip2))
    if (ip1 == ["rock"] and ip2 == ["paper"]):                  # ["rock"] is a list element, since ip1 is a list element. Similarly others.
        print("USER WINS!")
    elif (ip1 == ["paper"] and ip2 == ["scissor"]):
        print("COMPUTER WINS!")
    elif (ip1 == ["rock"] and ip2 == ["scissor"]):
        print("USER WINS!")
    elif (ip1 == ["paper"] and ip2 == ["rock"]):
        print("COMPUTER WINS!")
    elif (ip1 == ["scissor"] and ip2 == ["rock"]):
        print("COMPUTER WINS!")
    elif (ip1 == ["scissor"] and ip2 == ["paper"]):
        print("USER WINS!")
    elif (ip1 == ip2):                                              #this statement is being printed.
        print("TIE")

import random
ai=["rock","paper","scissor"]
while(1):                                                           #infinite loop.
    aiip=(random.sample(ai,1))                                      #since the random() generates a list, #here ai becomes a sequence(list) and we select one element out of it.
    uip=[(input("Enter rock/paper/scissor : "))]                    #we converted the user ip also as a list.
    print("USER ENTERED : "+str(uip))
    print("COMPUER SELECTED : "+str(aiip))
    comp(uip,aiip)                                                  #function call
    x=int(input("Press 1 to exit : "))
    if(x==1):
        break
    

"""
#produces correct output.
ls = ["apple"]
print(ls)
if ["apple"] == ls:                                     #["apple"] becomes a list variable that is compared to the list directly.
    print("true")

#produces incorrect output.
ls = ["apple"]
print(ls)
if "apple" == ls:                                       #string cannot be compared to the list.
    print("true")
"""