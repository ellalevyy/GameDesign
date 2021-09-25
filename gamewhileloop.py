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
    tries_left=10
    guess=input("please enter a integer")
    while(tries_left >=1):
        try:
            guess=int(guess)
            check=True
        except ValueError:
            check=False
        if(check):
            if guess==randy:
                print("You win!")
                break
            else: 
                tries_left -=1
                if tries_left >0:
                    print("sorry try again. " + str(tries_left) + " tries left")
                
                    guess=input("Try a new integer")

                else:
                    print("you lost")
               

        else:
            tries_left -=1
            print( "Sorry you need to try another number. You have " +str(tries_left) + " tries left")
          
            guess=input("Try a new integer")
            

    
        
        #try and except so to convert  the guess 
        #if check
        #end loop
    answer=input("Do you want to play again ")
print("thank you for playing, ", name)