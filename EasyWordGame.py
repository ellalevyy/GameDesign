#ELLA-ROSE

#we are creating a list of words
#randomly selecting a list word of words
#randomly select a word from the list of words

import random, os
os.system('cls')
print("guess a word  one letter at a time")
words=["keyboard", "CPU", "storage", "ports", "OpperatingSystems "]
name= input("What is your name?")
answer=input(name+ " , Do you want to play the game?")  
while 'y' in answer:
    word=random.choice(words)
    word=word.lower()
    print(word)
    turns=len(word)+2
    check = True
    guesses= ' '
    while(turns>0 and check):
        for letter in word:
            if letter in guesses:
                print(letter, end=" ")
                if len(guesses)==len(word):
                    check = False
            else:
                print("_", end= " ")
        newGuess=input ("\n please enter a letter")
        if newGuess in word:
            guesses += newGuess
            print("good guess")
        else:    
            turns -=-1
            print("sorry guess again")

    answer=input(name + "Do you want to play again? ")        
print(name + ", Thank you for playing")





