#!/bin/python3

import math
import os
import random
import re
import sys



import math
#
# Complete the 'interpolate' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY instances
#  3. FLOAT_ARRAY price
#



def clean_data(instances, price):
    i_result, p_result = [], []
    for i, p in enumerate(price):
        if p > 0:
            p_result.append(p)
            i_result.append(instances[i])
    return i_result, p_result


def interpolate_n(n, instances, price):
    instances, price = clean_data(instances, price)
    quantity = n
    if quantity in instances:
        return price[instances.index(quantity)]
    if len(instances) == 1:
        return price[0]
    index1, index2 = 0, 1
    prev = instances[0]
    for i in range(1, len(instances)):
        if prev < quantity < instances[i]:
            index1, index2 = i - 1, i
            break
        prev = instances[i]
    if quantity > instances[len(instances) - 1]:
        index1, index2 = len(instances) - 2, len(instances) - 1
    x = [instances[index1], instances[index2]]
    y = [price[index1], price[index2]]
    # y = ax+b
    a = (y[1] - y[0]) / (x[1] - x[0])
    b = y[1] - a * x[1]
    result = a * n + b
    return result if result>0 else -result

def round_near(n, p):
    """Round a number to the closest half integer.
        >>> round_near(1.341, 2)
        1.34
        >>> round_near(5.65, 2)
        5.65
        >>> round_near(5.0, 2)
        5.0
        >>> round_near(1.125, 2)
        1.13"""
    base = 10**p

    return math.ceil(round(base * n * 2) / 2) / base

def interpolate(n, instances, price):
    result = round_near(interpolate_n(n, instances, price), 2)
    return "{:.2f}".format(result).rstrip('0').rstrip('.')


n = 2000
instances = [10, 25, 50, 100, 500]
price = [27.32, 23.13, 21.25, 18.0, 15.5]

n = 40
instances = [10,25,50,100,500]
price = [17.0,18.0,20.0,22.0,29.15]
n = 33
instances = [10, 150, 606, 1038, 1664, 2000]
price = [33.58, 52.93, 30.1, 24.31, 28.69, 15.13]

n = 2
instances = [10, 25, 61, 118, 290, 334, 366, 468, 631, 804, 869, 970, 1000]
price = [31.48, 42.84, -1.0, 48.69, 48.85, 50.82, -1.0, 50.44, 51.44, 50.0, 46.88, 44.13, 44.19]

n = 1730
instances = [10, 40, 47, 60, 67, 83, 645, 664, 760, 790, 870, 933, 1000]
price = [19.36, 1.36, 4.38, 4.66, 6.54, 5.82, 1.0, 5.49, 6.56, 8.83, 1.28, 1.71, 1.0]
print(interpolate_n(n, instances, price))
print(interpolate(n, instances, price))
#6.13