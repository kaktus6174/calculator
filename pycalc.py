from pycalc_consts import PLUS_SIGN, MINUS_SIGN, MULTIPLY_SIGN, DIVIDE_SIGN

a = float(input("Enter first number: "))
op = input("Enter operator (+, -, *, /): ")
b = float(input("Enter second number: "))

if op == PLUS_SIGN:
    result = a + b
elif op == MINUS_SIGN:
    result = a - b
elif op == MULTIPLY_SIGN:
    result = a * b
elif op == DIVIDE_SIGN:
    result = a / b
else:
    exit("Error: Invalid operator")

print(f"Result: {result}")