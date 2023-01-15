"""
Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents and only accepts coins in these denominations: 25 cents, 10 cents, and 5 cents.

In a file called coke.py, implement a program that prompts the user to insert a coin, one at a time, each time informing the user of the amount due. Once the user has inputted at least 50 cents, output how many cents in change the user is owed. Assume that the user will only input integers, and ignore any integer that isn’t an accepted denomination.
"""
def main():
    x = 0
    while(x < 50):
        y = input("Enter a coin: ")
        y = int(y)
        if(isValid(y)): # Validation
            x += y
        if(x > 50):
            print(f"{x-50}") #Change
        else:
            print(f"{50-x}") # Remaining Balance


def isValid(n):
    return n == 25 or n == 10 or n == 5

main()
