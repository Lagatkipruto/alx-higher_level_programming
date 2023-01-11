#!/usr/bin/python3
# Roman to Integer test file
roman_to_int = __import__('12-roman_to_int').roman_to_int

roman_number = "X"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "IX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "XXI"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "DVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "MCVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))
