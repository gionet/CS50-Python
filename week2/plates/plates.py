def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if not (2 <= len(s) <= 6 and s[0:2].isalpha()):
        return False

    if len(s) > 2 and not (s[2:].isalnum() or s[2:].isdigit() or s[2:].isalpha()):
        return False

    stack = []
    for i in s[2:]:
        if i.isdigit():
            stack.append(i)
            if s[2:][s[2:].index(i):].isdigit() and i != '0':
                return True
            else:
                return False

    return True

    # if 6 >= len(s) >= 2 and s[0:2].isalpha() and s.isalnum():
    #     for char in s:
    #         if char.isdigit():
    #             index = s.index(char)
    #             if s[index:].isdigit() and int(char) != 0:
    #                 return True
    #             else:
    #                 return False
    #     return True

if __name__ == "__main__":
    main()
