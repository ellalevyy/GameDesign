#Ella-Rose levy
#learnng how to use while loops


import random, os
os.system('cls')
#function to update dashes and letters
def updateWord(word, guesses, letCount):
    for letter in word:
        if letter in guesses:
            print(letter,end=" ")
            letCount+=1
        else:
            print('_', end=' ')
    return letCount
#define function for Menu
name= input("What is your name? ")
#lists of worlds for guessing    
animals=["tiger", "elephant", "cat", "dog", "cow", "frog"]
fruits=["banana", "strawberries", "Cherry", "grape", "orange", "apple"]
compParts=["keyboard", "Monitors", "computer","trackpad", "case","Operating System"]

maxScore=0 #to store highest Score


def Menu():
    check = True
    while check:
        print("You are playing hangman. Please select a category you want to play.")
        print("Type one letter at a time to guess the word.")
        print("########################################")
    ## put instructions right above menu
        print("#                MENU                  #")
        print("#                                      #")
        print("#       1. Animals                     #")
        print("#       2. Computer PArts              #")
        print("#       3. Fruits                      #")
        print("#       4. ScoreBoard                  #")
        print("#       5. Exit                        #")
        print("#    To play the game select 1-4       #")
        print("#       To exit select 5               #")
        print("########################################")
        print()
        sel=input("What would you like to do? ")
       
        #Checks to see if the number entered is a real number     
        print(sel)
        try:
            sel=int(sel)
            check=False
        except ValueError:
            print("Please enter a number")
    
    
    # add the Try and except before you force sel to be an int
    
    return sel

#Function to select the Word
def selWord(sel):
    if sel == 1:
        word= random.choice(animals)
    elif sel ==2:
        word= random.choice(compParts)
    else: 
        word= random.choice(fruits)
    return word
    
#Plays the game
def Run_Through(sel, name, maxScore):
    word= selWord(sel)
    word = word.lower()
    wordCount=len(word)
    turns= wordCount+2  #depending on the lenght if the word
    print(name, " Good Luck! you have", turns, "turns left") 
    letCount=0 #variable to check if the user guessed the word
    guesses=''
    score=0
    updateWord(word, guesses, letCount)

    #Checking the letters the player has entered
    #This loop continuing until the player guess all the letters or runs out of turns
    while turns > 0 and letCount<wordCount:
        print()
        newguess=input (name + " Give me a letter ")
        newguess= newguess.lower()
        if newguess in word:
            guesses += newguess
            
            print("you guessed one letter ")
        else:
            turns -=1
            print("Sorry, you have ", turns, "turns left")
        letCount=0
        letCount= updateWord(word, guesses, letCount)
    
    #if your new score is higher it will replace the old lower score
    score=3*wordCount+5*turns
    if score > maxScore:
        maxScore=score
    print(maxScore)
    return maxScore





#openes save file for reading
# f=open("save.txt","r+")
# userData=[]
# #splits each line into name, highscore, and number
# for line in f.readlines():
#     splitLine=line.split("\t")
#     print(splitLine)
#     splitLine[2].replace("\n", "")
#     splitLine[2]=int(splitLine[2])
#     userData.append(splitLine)
# #deletes the file
# f.seek(0)
# f.truncate()


sel=Menu()
#Shows the result of selection 
while sel<5:
    if sel==1 or sel==2 or sel==3:
        maxScore=Run_Through(sel, name, maxScore) 
    if sel==4:
#prints the newest high score in save.txt
        file = open("save.txt","r")
        for line in file.readlines():
            print(line.strip('\n'))
        input('Are you ready to return to the menu? ')
        
    
    sel=Menu()
    
    if sel==5:
        f=open("save.txt", 'a')
        f.write (name + "\t Highest score:\t"+str(maxScore)+"\n")
        f.close()
        exit()
#checks to see if the current player has played before and ubdates the new highscore
# didFindUser=False
# for user in userData:
#     if user[0] == name:
#         didFindUser=True
#         if user[2] <= maxScore:
#             user[2] = maxScore

# #Opened txt file for writting 
# f=open("save.txt","w")

# #If user was not found, this write the user's name into the highscore list
# if didFindUser is False:
#     f.write (name + "\t Highest score:\t"+str(maxScore)+"\n")

#prints information of past players
# for user in userData:
#     f.write(user[0])
#     f.write("\t")
#     f.write(user[1])
#     f.write("\t")
#     f.write(str(user[2]))
#     f.write("\n")
    