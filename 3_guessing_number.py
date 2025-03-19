#Guessing the number game.
import random
print("Welcome to the guessing game!")
random_num = random.randint(1, 100) #Generate a random integer number between 1 and 100, inclusive.
while True:
    num = int(input("Please enter a number between 1 and 100:"))
    if num == random_num:
        print("Congratulations! You guessed the number!")
        break
    elif num < random_num:
        print("Too low! Try again!")
    else:
        print("Too high! Try again!")