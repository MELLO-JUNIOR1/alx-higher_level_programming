#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    '''
    if a_dictionary.get(key) is not None:
        del a_dictionary[key]
    return (a_dictionary)
    '''
    if key in a_dictionary.keys():
        a_dictionary.pop(key)
    return a_dictionary
