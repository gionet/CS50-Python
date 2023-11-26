def main():
    user_input = input(str(""))
    substitutions = {
        ':)': '🙂',
        ':(': '🙁',
    }

    output = replace_characters(user_input, substitutions)
    print(output)

def replace_characters(text, substitutions):
    for char, replacement in substitutions.items():
        text = text.replace(char, replacement)
    return text

if __name__ == "__main__":
    main()