def main():

    user_input = (input("Expression: "))
    expression = user_input.split(" ")
    
    x = float(expression[0])
    y = expression[1]
    z = float(expression[2])

    operators(x , y , z)


def operators(num1, operator, num2):
    match operator:
        case "+":
            print(num1 + num2)
        case "-":
            print(num1 - num2)
        case "*":
            print(num1 * num2)
        case "/":
            print(num1 / num2)
        case _:
            print("Invalid operator, try again!")


if __name__ == "__main__":
    main()