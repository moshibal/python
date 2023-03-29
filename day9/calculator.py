from logo import logo


def add(n1, n2):
    return n1+n2


def subtract(n1, n2):
    return n1-n2


def multiply(n1, n2):
    return n1*n2


def divide(n1, n2):
    return n1/n2


operators = {"+": add, "-": subtract, "*": multiply, "/": divide}
# taking the inputs


def calculator():
    print(logo)
    num1 = float(input("provide first number: "))

    continue_operation = True
    while continue_operation:
        for operator in operators:
            print(operator)
        operator = input("what operator you want to choose? ")
        num2 = float(input("provide second number: "))
        result = operators[operator](num1, num2)
        print(f"the result is {result}")
        if (input(f"type y to continue calculating with {result} and n to stop and start all again.") == "y"):
            num1 = result

        else:
            continue_operation = False
            calculator()


calculator()
