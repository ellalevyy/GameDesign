#Ella-Rose lEcy
#9-17
#learning abt random function and an introduction to list (array)

import os, random
os.system('cls')
for i in range(10):
    randy = random.randint(3,5)
    print(randy)
    randy2 = random.random()
    randy2 *=10000
    print(int(randy2))

    #arrays in py are called lists
fruits=["banana" , "apple" , "barries","mango"]
print(fruits)
numbers=[1,2,3,4,5]
print(numbers)
    #index = random.randint(o,2)
   # print(fruits[index])
word= random.choice(fruits)
print(word)
num=random.choice(numbers)
print(num)