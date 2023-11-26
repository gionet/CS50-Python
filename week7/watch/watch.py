import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    url = re.search(r'(src=")?(https?://)?(www\.)?youtube\.com/(embed/)?(.+?)"', s)
    if url:
        convert = "https://youtu.be/" + url.group(5)
        return convert
    
    else:
        return None

if __name__ == "__main__":
    main()
