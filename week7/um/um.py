import re
import sys


def main():
    print(count(input("Text: ")))

def count(s):
    regex = r"(\bum\b)"
    if match := re.findall(regex, s,  re.IGNORECASE):
        total = len(match)
        return total

if __name__ == "__main__":
    main()
