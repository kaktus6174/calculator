from pycalc_consts import PLUS_SIGN, MINUS_SIGN, MULTIPLY_SIGN, DIVIDE_SIGN
from pycalc_consts import OPERATORS


def get_number():
    while True:
        try:
            return float(input("Enter a number: "))
        except ValueError:
            print("Error: Invalid number")

def get_operator(list_of_ops):
    while True:
        op = input(f"Enter operator {list_of_ops}: ")
        if op in OPERATORS:
            return op
        else:
            print("Error: Invalid operator")


while True:
    a = get_number()
    op = get_operator(OPERATORS)
    b = get_number()

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
    if input("Do you want to perform another calculation? (y/n): ").lower() != 'y':
        break