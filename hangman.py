import os, random
os.system('cls')

possible_words=["keyboard", "printer", "motherboared", "cpu", "cooling fan", "storange"]
name=input("what is your name? ")
print( "hi, ", name)
word=random.choice(possible_words)
word=word.lower()
for letter in word:
    print("_", end=" ") 
guessed_letters = word


print(word[1])


