#!/usr/bin/python3
for abc in range(ord('a'), ord('z')+1):
    if abc == ord('q') or abc == ord('e'):
        continue
    print("{}".format(chr(abc)), end='')
