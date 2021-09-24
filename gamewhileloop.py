#Ella-Rose levy
#learnng how to use while loops

#place instructions of your game
import os, random
os.system('cls')
name=input("what is your name? ")
print( "hi, ", name)
answer= input("Would you like to play my game ")
while ('y' in answer):
    randy=random.randrange(1,10)
    counter=0
    guess=input("please enter a integer")
    print(randy)
    while(guess != randy):
        try:
            guess=int(guess)
            guess = randy
            check=True
        except ValueError:
            check=False
        if(check):
            if guess==randy:
                print("You win!")
                break
            else: 
                print("sorry try again")

        else:
            print("sorry try again")
            counter +=1
            

    
        
        #try and except so to convert  the guess 
        #if check
        #end loop
    answer=input("Do you want to play again ")
print("thank you for playing, ", name)