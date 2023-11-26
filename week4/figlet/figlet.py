import sys
import random
from pyfiglet import Figlet

figlet = Figlet()
def main():

    if len(sys.argv) == 1:
        randompick = random.choice(figlet.getFonts())
        figlet.setFont(font=randompick)

    elif len(sys.argv) == 3 and sys.argv[1] in ['-f', '--font']:
        try:
            figlet.setFont(font=sys.argv[2])
        except:
            sys.exit(1)

    else:
        print("Invalid usage")
        sys.exit(1)

    userInput = input("Input: ")

    print("Output: ")
    print(figlet.renderText(userInput))

if __name__ == "__main__":
    main()