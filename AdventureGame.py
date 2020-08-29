import random
import time


def print_pause(print_messages):
    print(print_messages)
    time.sleep(2)


def exhibitIntro():
    print_pause("You decided to camp on this beautiful sunny Day")
    print_pause("it was peaceful until you encountered a grizzly bear!")
    print_pause("Shrieking in fear, you rapidly ran away as it chases you")
    print_pause("After a while, you've come across two paths")
    print_pause("On your right, the path is dark, eerie and horrific")
    print_pause("On your left, the path is clear, colorful and bright")
    print()


def choosePath():
    path = ""
    while path != "1" and path != "2":
        path = input("Which path will you choose? (1 or 2): ")

    return path


def checkPath(chosenPath):
    print("You headed down the path")
    time.sleep(2)
    print("You began to slowly walked down the path you choose")
    time.sleep(2)
    print("you slowly start to shiver")
    print()
    time.sleep(2)

    correctPath = random.randint(1, 2)

    if chosenPath == str(correctPath):
        print("At the end of the road, you notice a shinning object")
        time.sleep(2)
        print("You found a gun at the end of the path ")
        time.sleep(2)
        print("you picked it up and went back to your camping site ")
        time.sleep(2)
        print("You have defeated the bear")

    else:
        print("you continue walking forward, then suddenly bears attacks you")
        time.sleep(2)
        print("Since you dont have anything to attack, you died")
        time.sleep(2)
        print("You start to fade away from the world as you lay on the ground")


def play_game():
    exhibitIntro()
    choice = choosePath()
    checkPath(choice)
    play_again()


def play_again():
    answer = " "
    answer = input("Please enter (yes/y) to restart and ( no/n ) to exit:")
    if answer == "yes" or answer == "y":
        play_game()
    elif answer == "no" or answer == "n":
        exit()
    else:
        play_again()

play_game()
