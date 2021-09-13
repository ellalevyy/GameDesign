#Ella-Rose Levy
#09-13-21
import os

os.system('cls')
userInput=input("type somthing ")

try:
    int(userInput)
    check=True
except ValueError:
    check=False

if(check):
    #I will be back
    print()
else:
    print(len(userInput))
for i in userInput:
    print(i)

if len(userInput>3):
print(userInput[3])

#This is about data types
#how strings work