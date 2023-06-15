#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    key = list(a_dictionary.keys())
    for elm in key:
        if a_dictionary.get(elm) == value:
            del a_dictionary[elm]
    return (a_dictionary)
