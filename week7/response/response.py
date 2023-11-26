import sys
from validator_collection import validators

def main():
    print(verify(input("Text: ")))

def verify(s):
    try:
    # regex = (r"^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$")
        email_address = validators.email(s, allow_empty = False)

    except ValueError:
        return "Invalid"

    return "Valid"

if __name__ == '__main__':
    main()
