#Ella-Rose levy
#learnng how to use while loops

#place instructions of your game
import os, random
os.system('cls')
name=input("what is your name? ")
print( "hi, ", name)
answer= input("Would you like to play my game ")
while ('y' in answer):
    randy=random
    counter=0
    guess=input("please enter a integer")
    while(guess != randy):
        guess=int(guess)
        guess = randy
        print("I was here")
        #try and except so to convert  the guess 
        #if check
        #end loop
    answer=input("Do you want to play again ")
print("thank you for playing, ", name)