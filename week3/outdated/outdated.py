def main():

    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    while True:
        userInput = input("Date: ")

        if "/" in userInput:
            try:
                month, day, year = map(int, userInput.strip().split('/'))

            except:
                continue

        elif "," in userInput:
            try:
                userInput = userInput.replace(',', '')
                month, day, year = userInput.split(' ')
            except:
                continue

            if month not in months:
                continue

            else:
                month = months.index(month) + 1

        else:
            continue

        if int(month) > 12 or int(day) > 31:
            continue
        else:
            break

    print(f"{year}-{int(month):02}-{int(day):02}", end="")


if __name__ == "__main__":
    main()