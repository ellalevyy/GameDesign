#learning python collection 

#list
import os, random

name = ["alex", "jack", "marry", "ellen", "peter", "ray",]
print(name[1])
print(name)
#printing with a loop
for nam in name:
    print(nam, end= " ")
print("\n these are all the names! \n")
#going in reverse
print(name[-1])
print(name[-2])
#range of index
print(name[2:5])

if "ellen" in name:
    print("you win")
else:
    print("sorry,you are wrong")

#length of array
print(len(name))
#add elements ussing appends
name.append("owen")
print(name)
name.insert(4, "joan")
print(name)

#copy a list to another list

othername =name[2:6].copy()
print(othername)

comparts=["keyboard", "printer", "motherboared", "cpu", "cooling fan", "storange"]
words=random.choice(comparts)
words=words.lower()
guess=input("try again")
while(guess != words):
    guess=guess.lower()
    if guess not in words:
        print("You are right")
    else:
        print("You are wrong")
        guess= input("guess the word i am thinking")
    print(Thankyou)
