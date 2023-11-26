def main():

    while True:
        x = input("Fraction: ")
        try:
            x, y = x.split('/')
            x, y = int(x), int(y)
            if x > y:
                continue

            return calculation(x, y)
        except (ValueError, ZeroDivisionError):
            pass

def calculation(numerator, denominator):

    percentage = round((numerator / denominator) * 100)

    if percentage >= 99:
        print("F")
    elif percentage <= 1:
        print("E")
    else:
        print(f"{percentage}%")


if __name__ == "__main__":
    main()
