#!/usr/bin/python3
for i in range(0, 100):
    between = ", "
    if i == 99:
        between = "\n"
    print("{:02d}".format(i), end=between)
