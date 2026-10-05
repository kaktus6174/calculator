from pycalc_consts import PLUS_SIGN, MINUS_SIGN, MULTIPLY_SIGN, DIVIDE_SIGN
from pycalc_consts import OPERATORS


while True:
    while True:
        try:
            a = float(input("Enter first number: "))
            break
        except ValueError:
            print("Error: Invalid first number")


    op = input("Enter operator (+, -, *, /): ")
    if op not in OPERATORS:
        print("Error: Invalid operator")
        continue

    while True:
        try:
            b = float(input("Enter second number: "))
            break
        except ValueError:
            print("Error: Invalid second number")


    if op == PLUS_SIGN:
        result = a + b
    elif op == MINUS_SIGN:
        result = a - b
    elif op == MULTIPLY_SIGN:
        result = a * b
    elif op == DIVIDE_SIGN:
        if b != 0:
            result = a / b
        else:
            print("Error: Cannot divide by zero")
            continue
    else:
        print("Error: Unexpected error occurred")
        continue

    print(f"Result: {result}")