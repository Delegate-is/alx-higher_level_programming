#!/usr/bin/python3
def uniq_add(my_list=[]):
    new = set(my_list)
    res = 0
    for n in new:
        res += n
    return res
