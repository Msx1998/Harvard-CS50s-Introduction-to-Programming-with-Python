"""
The U.S. Food & Drug Adminstration (FDA) offers downloadable/printable posters that “show nutrition information for the 20 most frequently consumed raw fruits … in the United States. Retail stores are welcome to download the posters, print, display and/or distribute them to consumers in close proximity to the relevant foods in the stores.”

In a file called nutrition.py, implement a program that prompts consumers users to input a fruit (case-insensitively) and then outputs the number of calories in one portion of that fruit, per the FDA’s poster for fruits, which is also available as text. Capitalization aside, assume that users will input fruits exactly as written in the poster (e.g., strawberries, not strawberry). Ignore any input that isn’t a fruit.
"""


def main():
    check(input("Item: "))


def check(n):
    j = n.lower()
    if j == "apples" or j == "apple":
        print("130")
    elif j == "avocados" or j == "avocado":
        print("50")
    elif j == "bananas" or j == "banana":
        print("110")
    elif j == "cantaloupe" or j == "cantaloupes":
        print("50")
    elif j == "grapefruit" or j == "grapefruits":
        print("60")
    elif j == "grapes" or j == "grape":
        print("90")
    elif j == "Honeydew melon" or j == "honeydew melons":
        print("50")
    elif j == "kiwifruit" or j == "kiwifruits":
        print("90")
    elif j == "lemons" or j == "lemon":
        print("15")
    elif j == "limes" or j == "lime":
        print("20")
    elif j == "nectarines" or j == "nectarine":
        print("60")
    elif j == "oranges" or j == "orange":
        print("80")
    elif j == "peaches" or j == "peach":
        print("60")
    elif j == "pears" or j == "pear":
        print("100")
    elif j == "pineapple" or j == "pineapples":
        print("50")
    elif j == "plums" or j == "plum":
        print("70")
    elif j == "strawberries" or j == "strawberry":
        print("50")
    elif j == "sweet cherries" or j == "sweet cherry":
        print("100")
    elif j == "tangerines" or j == "tangerine":
        print("50")
    elif j == "watermelon" or j == "watermelons":
        print("80")
    else:
        print("")


main()
