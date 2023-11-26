import inflect

p = inflect.engine()

def main():

    mylist = []

    while True:
        try:
            userInput = input('Name: ')
            mylist.append(userInput)

        except EOFError:
            break

    output = p.join(mylist)
    print(f'Adieu, adieu, to {output}')

if __name__ == "__main__":
    main()