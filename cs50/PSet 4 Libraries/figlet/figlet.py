"""
Expects zero or two command-line arguments:
Zero if the user would like to output text in a random font.
Two if the user would like to output text in a specific font, in which case the first of the two should be -f or --font, and the second of the two should be the name of the font.
Prompts the user for a str of text.
Outputs that text in the desired font.
"""

import sys
import random
from pyfiglet import Figlet

def main():
    figlet = Figlet()
    font_list = figlet.getFonts()
    
    if len(sys.argv) == 1:
        random.shuffle(font_list)
        figlet.setFont(font=font_list[0])
        sentence = input("Input: ")
        print(figlet.renderText(sentence))
            
    elif len(sys.argv) == 3:
        if sys.argv[1] == "-f" or sys.argv[1] == "--font":
            if sys.argv[2] in font_list:
                figlet.setFont(font=sys.argv[2])
                sentence = input("Input: ")
                print(figlet.renderText(sentence))
                
            else:
                sys.exit("Invalid usage")
                
        else:
            sys.exit("Invalid usage")
            
    else:
        sys.exit("Invalid usage")


main()
    
    