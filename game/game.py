"""
In a file called game.py, implement a program that:

Prompts the user for a level, . If the user does not input a positive integer, the program should prompt again.
Randomly generates an integer between 1 and , inclusive, using the random module.
Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again.
If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
If the guess is larger than that integer, the program should output Too large! and prompt the user again.
If the guess is the same as that integer, the program should output Just right! and exit.
"""
from random import randint

while True:
    try:
        x = input("Level: ")
        x = int(x)
        if x >= 0:
            x = randint(1, x)
            z = input("Guess: ")
            z = int(z)
            if z < x:
                print("Too small!")
            elif z > x:
                print("Too large!")
            else:
                print("Just right!")
                break
    except ValueError:
        print("Invalid input")
