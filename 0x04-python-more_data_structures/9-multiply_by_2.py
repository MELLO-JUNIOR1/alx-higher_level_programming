#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    key = list(a_dictionary.keys())
    new = dict()
    for i in key:
        new[i] = a_dictionary[i] * 2
    return new
