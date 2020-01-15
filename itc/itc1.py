import math


def getIdealNums(low, high):
    """
    >>> getIdealNums(200, 405)
    4
    """
    count = 0
    for x in range(int(math.log(high, 3)) + 1):
        for y in range(int(math.log(high, 5)) + 1):
            if low <= 3 ** x * 5 ** y <= high:
                count += 1
    return count


if __name__ == "__main__":
    import doctest
    doctest.testmod()
