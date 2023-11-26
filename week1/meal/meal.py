import re

def main():
    time = input("What time is it? ")

    convert_time = convert(time)

    if 7 <= convert_time <= 8:
        print("breakfast time")

    elif 12 <= convert_time <= 13:
        print("lunch time")

    elif 18 <= convert_time <= 19:
        print("dinner time")

    else:
        return

def convert(time):
    match = re.search(r'(\d+:\d+)\s*(a\.m\.|p\.m\.)?', time)

    if match:
        time_str = match.group(1)
        period = match.group(2)
    else:
        print("Invalid input format!")
        return

    hours, minutes = map(int, time_str.split(":"))

    if period == "a.m.":
        if 0 <= hours < 12 and 0 <= minutes < 60:
            time = hours + (minutes / 60)
            return time
        else:
            print("Invalid hours or minutes!")

    elif period == "p.m.":
        if 0 <= hours < 12 and 0 <= minutes < 60:
            time = hours + 12 + (minutes / 60)
            return time
        else:
            print("Invalid hours or minutes!"   )

    elif period == None:
        if 0 <= hours < 24 and 0 <= minutes < 60:
            time = hours + (minutes / 60)
            return time
        else:
            print("Invalid hours or minutes!")

    else:
        print("Something went wrong...")


if __name__ == "__main__":
    main()