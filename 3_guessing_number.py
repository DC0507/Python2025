import random
print("Welcome to the guessing game!")
random_num = random.randint(1, 100)
while True:
    print("Please enter a number between 1 and 100:")
    num = int(input())
    if num == random_num:
        print("Congratulations! You guessed the number!")
        break
    elif num < random_num:
        print("Too low! Try again!")
    else:
        print("Too high! Try again!")