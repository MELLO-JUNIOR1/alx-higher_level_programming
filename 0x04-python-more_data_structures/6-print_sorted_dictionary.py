#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):

    key = sorted(a_dictionary.keys())
    for elm in key:
        print("{}: {}".format(elm, a_dictionary[elm]))
