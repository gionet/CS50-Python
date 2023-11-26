def main():

    storage = dict()

    while True:
        try:
            userInput = input().upper()
            if userInput in storage:
                storage[userInput] += 1
            else:
                storage[userInput] = 1
        except EOFError:
            for i in sorted(storage):
                print(storage[i], i)
            break

if __name__ == "__main__":
    main()