import sys
import csv
import os
from PIL import Image, ImageOps

def main():
    check_comment_line_arg()

    try:
        check_file_type()
        with Image.open(sys.argv[1]) as muppet:
            size = shirt_on(muppet)

    except FileNotFoundError:
        print('Input does not exist')
        sys.exit(1)

def check_comment_line_arg():
    if len(sys.argv) > 3:
            print('Too many command-line arguments')
            sys.exit(1)

    elif len(sys.argv) < 3:
            print('Too few command-line arguments')
            sys.exit(1)
    else:
        return

def check_file_type():
    file_types = ['.jpg', '.jpeg', '.png']

    root_ext_before = os.path.splitext(sys.argv[1])
    root_ext_after = os.path.splitext(sys.argv[2])

    if root_ext_after[1] not in file_types:
        print('Invalid output')
        sys.exit(1)

    if root_ext_before[1] != root_ext_after[1]:
        print('Input and output have different extensions')
        sys.exit(1)

def shirt_on(muppet):
    muppet_size = muppet.size
    print(f'Muppet Size:', muppet_size)
    shirt = Image.open("shirt.png")
    size = shirt.size
    print(f'Shirt Size:', size)

    after_file = ImageOps.fit(muppet, size)
    after_file.paste(shirt, shirt)

    after_file.save(sys.argv[2])

    return after_file

if __name__ == '__main__':
    main()
