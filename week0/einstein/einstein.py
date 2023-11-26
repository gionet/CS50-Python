def main():

    while True:
        try:
            m = int(input('m: '))
            break  # Exit the loop if input is a valid integer
        except ValueError:
            print('Please enter a valid number!')

    c = 300000000 ** 2
    E = m * c

    print(E)

if __name__ == "__main__":
    main()