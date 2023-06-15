#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return 0
    if not isinstance(roman_string, str):
        return 0
    roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    summ = 0
    prv = 0

    for i in reversed(roman_string):
        value = roman_values.get(i, 0)
        if value >= prv:
            summ += value
        else:
            summ -= value
        prv = value
    return summ
