"""
In a file called grocery.py, implement a program that prompts the user for items, one per line, until the user inputs control-d (which is a common way of ending one’s input to a program). Then output the user’s grocery list in all uppercase, sorted alphabetically by item, prefixing each line with the number of times the user inputted that item. No need to pluralize the items. Treat the user’s input case-insensitively.
"""
def main():
    grocery = {}
    while True:
        try:
            item = input().upper()
            if item in grocery:
                grocery[item] += 1
            else:
                grocery[item] = 1
        except EOFError:
            # Sort the dictionary by key in alphabetical order
            for item in sorted(grocery):
                print(f"{grocery[item]} {item}")
            break

main()

