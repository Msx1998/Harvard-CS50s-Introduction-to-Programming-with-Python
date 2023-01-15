"""
FIGlet, named after Frank, Ian, and Glen’s letters, is a program from the early 1990s for making large letters out of ordinary text, a form of ASCII art:

In a file called figlet.py, implement a program that:

Expects zero or two command-line arguments:
Zero if the user would like to output text in a random font.
Two if the user would like to output text in a specific font, in which case the first of the two should be -f or --font, and the second of the two should be the name of the font.
Prompts the user for a str of text.
Outputs that text in the desired font.
If the user provides two command-line arguments and the first is not -f or --font or the second is not the name of a font, the program should exit via sys.exit with an error message.
"""
import sys
from pyfiglet import Figlet

figlet = Figlet()

if len(sys.argv) == 0:
    print(figlet.renderText(input("Enter a word: ")))
elif len(sys.argv) == 3:
    if (sys.argv[1] in ['-f', '--font']) and (sys.argv[2] in figlet.getFonts()):
        figlet.setFont(font=sys.argv[2])
        print(figlet.renderText(input("Enter a word: ")))
    else:
        sys.exit("Invalid input")
else:
    sys.exit("Invalid input")
