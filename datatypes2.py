#trying again 

import os
os.system('cls')

#variables declear and initialize 
num = 30
print(type(num))
num = 6.7
print(type(num))
userInput=input("type somthing ")


#how to check for youe data

try:
    userInput=float(userInput)
    print(type(userInput))
    check=True
except ValueError:
    check=False
#using conditional statement if/else
if(check):
    print(num + userInput)
else:
    print("sorry i cant not add a number")
    
print(num/0)
