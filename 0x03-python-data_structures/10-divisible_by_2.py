#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = my_list.copy()
    for n in range(0, len(my_list)):
        if my_list[n] % 2 == 0:
            new_list[n] = 1
        else:
            new_list[n] = 0
    return new_list
