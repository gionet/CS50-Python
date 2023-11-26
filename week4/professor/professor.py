import random

def main():

    math_questions = 10
    attempts = 3
    score = 0

    x = get_level()

    while math_questions != 0:
        math_questions -= 1
        attempts = 3
        num1 = generate_integer(x)
        num2 = generate_integer(x)

        while attempts > 0:
            try:
                answer = int(input(f'{num1} + {num2} = '))
            except ValueError:
                attempts -= 1
                print('EEE')
                continue

            if answer != question_generator(num1, num2):
                attempts -= 1
                print("EEE")
            else:
                attempts = 3
                score += 1
                break

        if attempts == 0:
            print(f'{num1} + {num2} =', question_generator(num1, num2))
            continue

    print(f'Score: {score}')


def get_level():
    while True:
        try:
            getlevel = int(input('Level: '))

            if getlevel not in range(1,4):
                raise ValueError
            else:
                return getlevel

        except ValueError:
            continue

def generate_integer(level):
    n = 10 ** level

    if level == 1:
        difficulty = random.randint(0, n-1)
    else:
        difficulty = random.randint(n/10, n-1)

    return difficulty

def question_generator(a, b):

    equation = a + b

    return equation


if __name__ == '__main__':
    main()