import sys
import csv
from tabulate import tabulate

def main():
    if len(sys.argv) > 2:
            print('Too many command-line arguments')
            sys.exit(1)

    elif len(sys.argv) < 2:
            print('Too few command-line arguments')
            sys.exit(1)

    else:
        try:
            check_csv_file()
            with open(sys.argv[1], "r") as file:
                table = tabulate_data(file)

        except FileNotFoundError:
            print('File does not exist')
            sys.exit(1)

    print(table)


def check_csv_file():
    if sys.argv[1][-4:] != '.csv':
        print('Not a CSV file')
        sys.exit(1)

def tabulate_data(table):
    list = []
    reader = csv.DictReader(table)

    for line in reader:
        list.append(line)

    return tabulate(list, headers="keys", tablefmt="grid")

if __name__ == '__main__':
    main()
