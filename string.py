
import os
os.system('cls')

#string
print("hi")
print('hi')

multistring = """words worlds world
Word, words
word"""
print(multistring)

ab = "I love candy"
print(ab[1])

print(len(ab))

#slicing

a = "coding is fun"
print(a[2:8])

print(a[-8:-3])

#modifing

print(a.upper())
print(a.lower())

#string concenstartion 

d = "cat"
g = "is"
h = "soft"
f = d + g + h
print(f)

#formating

age= 16
txt = "My name is ella, and i am {}"
print(txt.format(age))

#escaping
txt = "I am coding \"aka\" trying."
print(txt)