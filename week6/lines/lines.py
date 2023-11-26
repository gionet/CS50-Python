import sys

def main():
    if len(sys.argv) > 2:
        print('Too many command-line arguments')
        sys.exit(1)

    elif len(sys.argv) < 2:
        print('Too few command-line arguments')
        sys.exit(1)

    else:
        try:
            check_python_file()
            with open(sys.argv[1], "r") as file:
                lines = file.readlines()
                print(count_LOC(lines))

        except FileNotFoundError:
            print('File does not exist')
            sys.exit(1)


def check_python_file():
    if sys.argv[1][-3:] != '.py':
        print('Not a python file')
        sys.exit(1)

def count_LOC(lines):
    count = 0

    for line in lines:
        line = line.strip()
        if line:
            if line[0] == '#':
                continue
            else:
                count += 1

    return count

if __name__ == '__main__':
    main()
