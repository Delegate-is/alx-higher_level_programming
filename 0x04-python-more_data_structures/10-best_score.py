#!/usr/bin/python3
def best_score(a_dictionary):
    new_d = {}
    for n in a_dictionary:
        new_d[n] = a_dictionary[n] * 2
    return new_d
