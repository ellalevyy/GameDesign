import random
fruits=["banana", "apple" , "berries","mango", "orange"]
winning_word = fruits[random.randint(0, len(fruits)-1)]
print("please guess a fruit to win the game")
print(fruits)
while True:
    guess_input= input("please guess the correct word: ") 
    if winning_word == guess_input:
        print("You win")
        exit()
    else:
        print("try again")

