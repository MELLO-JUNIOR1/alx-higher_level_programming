#!/usr/bin/python3
n = 0
for i in range(122, 96, -1):
    print("{}".format(chr(i - n)), end="")
    n = 32 if n == 0 else 0
