#!/usr/bin/python3

if __name__ == "__main__":
    # Handle basic arithmetic ops.
    from calculator_1 import add, sub, mul, div
    from sys import argv

    argc = len(argv)

    if argc < 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    ops = {"+": add, "-": sub, "*": mul, "/": div}
    if argv[2] not in list(ops.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        if argv[2] == "+":
            c = add(int(argv[1]), int(argv[3]))
            print("{} {} {} = {}".format(argv[1], argv[2], argv[3], c))
        elif argv[2] == "-":
            c = sub(int(argv[1]), int(argv[3]))
            print("{} {} {} = {}".format(argv[1], argv[2], argv[3], c))
        elif argv[2] == "*":
            c = mul(int(argv[1]), int(argv[3]))
            print("{} {} {} = {}".format(argv[1], argv[2], argv[3], c))
        elif argv[2] == "/":
            c = div(int(argv[1]), int(argv[3]))
            print("{} {} {} = {}".format(argv[1], argv[2], argv[3], c))
