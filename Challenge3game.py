#Ella-Rose Levy
#This is Challenge 3
#game instructions 
import os, random
os.system('cls')
numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,]
num = random.choice(numbers)
for i in range(10):
    guess=input("guess an interger 1-20")
    try:
        guess=int(guess)
        check=True
    except ValueError:
        check=False 
    if (check):
        if guess==num: 
            print("you win")    
            break
        else:
            print("Sorry try again") 

print("Thank you for playing")

            