#!/usr/bin/python3
"""Print the alphabet in lowercase, not followed by new line."""
for letter in range(97, 123):
    print("{}".format(chr(letter)), end="")
