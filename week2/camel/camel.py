def main():

    user_input = input("camelCase: ")

    for letter in user_input:
        if letter.isupper():
            user_input = user_input.replace(letter, '_' + letter.lower())

    print(f"snake_case: {user_input}")

if __name__ == "__main__":
    main()
