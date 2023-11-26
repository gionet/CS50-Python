def main():
    user_input = input("Input: ")

    vowels = ["a", "e", "i", "o", "u"]
    for i in user_input:
        if i.lower() in vowels:
            user_input = user_input.replace(i, "")

    print(f"Output: {user_input}")

if __name__ == "__main__":
    main()