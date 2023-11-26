import emoji

def main():

    userInput = input("Input: ")
    print('Output:', emoji.emojize(userInput, language='alias'))

if __name__ == "__main__":
    main()