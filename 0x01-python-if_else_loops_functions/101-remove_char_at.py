#!/usr/bin/python3
def remove_char_at(str, n):
    c = ""
    for i in range(len(str)):
        if i != n:
            c += str[i]
    return (c)
