import os, random
os.system('cls')

words=["keyboard", "printer", "motherboared", "cpu", "cooling fan", "storange"]
name=input("what is your name? ")
answer=input(name+ " , Do you want to play the game?") 
print( "hi, ", name)
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
#for letter in word:
    #print= "_", end= " "
   # print(fdashes) 
   # print()
#guessed_letters = word


#print(word[1])


