# Expects zero or two command-line arguments:
# Zero if the user would like to output text in a random font.
# Two if the user would like to output text in a specific font, in which case the first of the two should be -f or --font, and the second of the two should be the name of the font.
# Prompts the user for a str of text.
# Outputs that text in the desired font.

# Import Modules
import sys
from pyfiglet import Figlet
import random

# Prerequisites
figlet = Figlet()
ff = figlet.getFonts()

if len(sys.argv) == 1:
    user_input = input("Input: ")
    f_random = figlet.setFont(font=random.choice(ff))
    user_output = figlet.renderText(user_input)
    print(user_output)
elif len(sys.argv) == 3:
    if sys.argv[1] not in ["-f", "--font"]:
        sys.exit("Invalid usage")
    if sys.argv[2] not in ff:
        sys.exit("Invalid usage")
    else:
        user_input = input("Input: ")
        figlet.setFont(font=sys.argv[2])
        user_output = figlet.renderText(user_input)
        print(user_output)
else:
    sys.exit("Invalid usage")
