import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
    regex = "([1][0-2]|[0-9]):?([0-5][0-9])? ([AP]M)"
    if time := re.search(r"^" + regex + " to " + regex + "$", s):
        t = time.groups()
        return f"{converted(t[:3])} to {converted(t[3:])}"

    else:
        raise ValueError


def converted(time):
    hours = int(time[0])
    minutes = 00

    if time[2] == "AM":
        if hours == 12:
            hours = 00
    else:
        if hours == 12:
            hours = 12
        else:
            hours += 12

    if time[1] is not None:
        minutes = int(time[1])

    return f"{hours:02}" + ":" + f"{minutes:02}"

if __name__ == "__main__":
    main()
