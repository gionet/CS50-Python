import sys
import csv

def main():
    check_comment_line_arg()
    try:
        check_csv_file()
        with open(sys.argv[1], "r") as file:
            table = clean_data(file)

    except FileNotFoundError:
        print('File does not exist')
        sys.exit(1)

    with open(sys.argv[2], "w") as afterfile:
        fieldnames = ['first', 'last', 'house']
        writer = csv.DictWriter(afterfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(table)

def check_comment_line_arg():
    if len(sys.argv) > 3:
            print('Too many command-line arguments')
            sys.exit(1)

    elif len(sys.argv) < 3:
            print('Too few command-line arguments')
            sys.exit(1)
    else:
        return

def check_csv_file():
    if sys.argv[1][-4:] != '.csv':
        print('Before file a CSV file')
        sys.exit(1)

    if sys.argv[2][-4:] != '.csv':
        print('After file not a csv file')
        sys.exit(1)

def clean_data(before):
    lst = []

    writer = csv.DictReader(before)
    for line in writer:
        fn, ln = line['name'].split(',')
        fn, ln = fn.strip(), ln.strip()
        house = line['house']
        lst.append({'first':ln, 'last':fn, 'house':house})

    return lst

if __name__ == '__main__':
    main()
