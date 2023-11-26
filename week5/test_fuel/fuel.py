def main():

    while True:
        userInput = input("Fraction: ")
        try:
            x = convert(userInput)
            break

        except(ValueError, ZeroDivisionError):
            pass

    print(gauge(x))

def convert(fraction):
        x, y = fraction.split('/')
        x, y = int(x), int(y)

        if y == 0:
            raise ZeroDivisionError
        if x > y:
            raise ValueError

        decimal = round((x / y) * 100)
        return decimal

def gauge(percentage):
    if percentage >= 99:
        return("F")
    elif percentage <= 1:
        return("E")
    else:
        return(f'{percentage}%')


if __name__ == "__main__":
    main()
