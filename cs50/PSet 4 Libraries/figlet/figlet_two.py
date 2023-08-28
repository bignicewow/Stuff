import sys
import random
from pyfiglet import Figlet

def main():
    figlet = Figlet()
    new_font = validator(figlet)
    figlet.setFont(font=new_font)
    sentence = input("Input: ")
    print(figlet.renderText(sentence))
            
    
def validator(figlet):
    font_list = figlet.getFonts()

    if len(sys.argv) == 1:
        random.shuffle(font_list)
        new_font = font_list[0]
        return new_font
    elif len(sys.argv) == 3:
         if (sys.argv[1] == "-f" or sys.argv[1] == "--font") and sys.argv[2] in font_list:
              new_font = sys.argv[2]
              return new_font
         else:
              sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")



main()
    