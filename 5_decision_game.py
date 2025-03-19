#Decision game: you have to take a decision and based on your luck, your lifebar will increase or decrease. The goal is to pass all the scenes before your lifebar goes to 0.
import random
import time

scenes=[
    "You found a magic lamp. Do you want to rub it? (Y/N)",
    "An old sorcerer asked for help. Do you want to help him? (Y/N)",
    "You found a misterous castle in the fog. Do you want to enter? (Y/N)",
    "There is a path of souls. Do you want to follow them? (Y/N)",
    "You entered a bar and a man asked to make business? Do want to continue? (Y/N)"
]

startGame = input("Hello adventurer, do you want to write your own story? (Y/N)").upper()
if startGame == "Y":
    lifeBar = 100
    numScenes = 0
    name = input("Type your name to read your destiny...")
    print("\n\nHello " + name + " welcome to the ancient lands of the dark world.")
    print("This was a beautiful place of light before the lord of the chaos took every soul and land. I'm just an old witcher.")
    print("However, you're the last hope, please take this time pendant, go to the past and write a new future!")
    print("...")
    print("The time pendant is shining in the deep darkness. A gate was opened and you crossed it.")
    print("...\n\n")
    time.sleep(1)
    while lifeBar>0 and numScenes <6:
        numScenes += 1
        sceneNumber = random.randint(0,4)
        print("Scene#"+str(numScenes))
        print(scenes[sceneNumber])
        option = input()
        luck = random.randint(0,10)
        if luck > 5:
            lifeBar += luck
            print("Great! Your life has increased in " + str(luck))
        else:
            lifeBar -= luck*random.randint(1,20)
            print("Wrong election! Your lost part of your vitality")
        if lifeBar < 0:
            lifeBar = 0
        print("Life bar: " + str(lifeBar))
    if lifeBar == 0:
        print("The adventure has finished for now. Be brave and try again!")
    else:
        print("You did it! The future is never written in stone!")    