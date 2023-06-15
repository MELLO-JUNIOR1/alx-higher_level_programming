#!/usr/bin/python3
def weight_average(my_list):
    if not my_list:
        return 0

    summ = 0
    wt = 0

    for i, weight in my_list:
        summ += i * weight
        wt += weight

    avg = summ / wt
    return avg
