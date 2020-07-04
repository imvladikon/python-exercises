#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getIdealNums' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. LONG_INTEGER low
#  2. LONG_INTEGER high
#

def getIdealNums(low, high):
    numbers = []
    pow_low = int(math.log(low, 5))
    pow_up = int(math.log(high, 3)) + 1
    for x in range(0, pow_up):
        for y in range(0, pow_up):
            if x + y < pow_low or x + y > pow_up:
                continue
            number = pow(3, x) * pow(5, y)
            if (low <= number) and (number <= high):
                numbers.append(number)
    return len(numbers)


if __name__ == '__main__':
