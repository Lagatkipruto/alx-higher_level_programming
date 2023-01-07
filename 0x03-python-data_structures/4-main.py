#!/usr/bin/python3
new_in_list = __import__('4-new_in_list').new_in_list

my_list = [0, 1, 2, 3, 4, 5, 6]
idx = 4
new_element = 88
new_list = new_in_list(my_list, idx, new_element)

print(new_list)
print(my_list)
