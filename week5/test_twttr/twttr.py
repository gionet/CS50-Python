def main():
    user_input = input("Input: ")

    print("Output:", shorten(user_input))

def shorten(word):
    vowels = ["a", "e", "i", "o", "u"]
    for i in word:
        if i.lower() in vowels:
            word = word.replace(i, "")
    return word

if __name__ == "__main__":
    main()
