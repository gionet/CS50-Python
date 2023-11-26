import random

def main():
    while True:
        try:
            level = int(input('Level: '))
            if level <= 0:
                continue
            else:
                random_number = random.randint(1, level)
                break

        except ValueError:
            continue

    while True:
        try:
            guesses = int(input('Guess: '))
            if guesses <= 0:
                raise ValueError
            elif guesses > random_number:
                print('Too large!')
            elif guesses < random_number:
                print('Too small!')
            else:
                print('Just right!')
                break

        except ValueError:
            continue




if __name__ == "__main__":
    main()