#!/usr/bin/python3
safe_print_division = __import__('3-safe_print_division').safe_print_division

a = 27
b = 3
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))

a = 12
b = 0
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))
