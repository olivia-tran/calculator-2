"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


def is_float(str_num):
    try:
        float(str_num)
        return True
    except ValueError:
        print('Please enter valid numbers. ')
        return False


two_arg_func = {'+', '-', '*', '/', 'pow', 'mod', 'power'}
one_arg_func = {'cube', 'square'}

while True:
    input_string = input("Enter your equation: ")
    tokens = input_string.split(' ')

    if 'q' in tokens:
        print('Goodbye. Thanks for using our calculator. ')
        break
    elif len(tokens) == 3 and tokens[0] in two_arg_func:
        operator = tokens[0]
        if not is_float(tokens[1]) or not is_float(tokens[2]):
            continue
        else:
            num1 = float(tokens[1])
            num2 = float(tokens[2])

    elif len(tokens) == 2 and tokens[0] in one_arg_func:
        operator = tokens[0]
        if not is_float(tokens[1]):
            continue
        else:
            num = float(tokens[1])

    else:
        print("Wrong operation")
        continue

    if operator == "+":
        print("Result: ", add(num1, num2))
    elif operator == "-":
        print("Result: ", subtract(num1, num2))
    elif operator == "*":
        print("Result: ", multiply(num1, num2))
    elif operator == "/":
        print("Result: ", divide(num1, num2))
    elif operator == "square":
        print("Result: ", square(num))
    elif operator == "cube":
        print("Result: ", cube(num))
    elif operator == "pow" or operator == "power":
        print("Result: ", power(num1, num2))
    elif operator == "mod":
        print("Result: ", mod(num1, num2))
