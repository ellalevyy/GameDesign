import random
winning_number =random.randint(1, 20)

for current_attempt in range (10):
    guess_input= int(input("please guess the winning number"))  
    if winning_number == guess_input:
        print("You win")
        exit()
    else:
        print("try again")

print("you lost")