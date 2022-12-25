"""
CS50P 2022 Functions, Variables

String Section
"""
# name is the variable. print & input are the functions imposed on the variable
print("Hello World")
name = input(
    "What's your name? ").capitalize()  # you can add methods to the end of the input method that will format the string
print("Hello " + name)

# this overrides the end parameter by passing an empty string as an argument. This allows ths print to appear in one line even though there are two prints
print("Hello, ", end="")
print(name)

# here is string manipulation with a functional string
name = name.capitalize().strip().title()
print(f"Hello {name}")

"""
int section
"""

# add two ints
print(1 + 1)

# add two custom ints
x = input("What's x ?").strip()
y = input("What's y ?").strip()
print(f"Your answer is {x + y}")  # This does not work because you are concatenating strings
print(f"Your real answer is {int(x) + int(y)}")  # this works because now the type is defined

# nest two functions and then add
x = int(input("What's x ?").strip())
y = int(input("What's y ?").strip())
print(f"Your real answer is {x + y}")  # this works because the type is already defined during assignment

# one line best line
print(int(input("Whats x? ")) + int(input("whats y?")))

"""
float section
"""
print(float(input("Whats x? ")) + float(input("whats y?")))
# rounding to the nearest int
print(round(float(input("Whats x? ")) + float(input("whats y?"))))
# rounding using an f string
x = float(input("What's x? "))
y = float(input("What's y? "))
z = x / y
print(f"{z:.2f}")  # rounds 2 decimal places
"""
defining a custom function
"""


def hello():  # with no parameters
    print("hello")


hello()


def helloAgain(newName):  # with parameters
    print(f"hello, {newName}")


name = input("whats the name ")
helloAgain(name)  # calls the method and passes the parameter made in input


def helloAgain(to="world"):  # this sets a default string literal incase there is no passed argument
    print(f"hello, {to}")


helloAgain()

"""
using multiple defined functions
"""


def main():
    newestName = input("What is your name ")
    hello(newestName)


def hello(to="world"):
    print(f"hello, {to}")


main()  # what is unique here is that you can define functions in any order. However, you must call those functions after they have been defined.
"""
returning a value
"""


def anotherFunction():
    print(f"x squared is: " + str(square(int(input("What is x? ")))))


def square(n):
    return n * n  # n * n == n ** 2 == pow(n,2)


anotherFunction()
