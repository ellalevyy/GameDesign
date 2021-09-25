#ellarose levy
#9-24

import os, random
os.system('cls')

fruits=["banana" , "apple" , "barries","mango", "orange"]
print(fruits)

name=input("what is your name? ")
print( "hi, ", name)
print("Intructions: This is my game. Please enter a fruit. If you are correct you win! if you lose try again! ")
answer= input("Would you like to play my game ")


while ('y' in answer):
    randy=random.choice(fruits)
    tries_left=5
    guess= str(input("guess a word. "))
    print(guess.lower())    
    while (tries_left >=1):
        if guess==randy:
            print("you win!")
            break
        else:
            tries_left -=1
            if tries_left >0:

                print("sorry, try again. You have " + str(tries_left) + " tries left")
                guess = input("Try a new fruit")
                
            else: 
                print("You lost")
    answer=input("Do you want to play again" )
print("Thank you for playing")

