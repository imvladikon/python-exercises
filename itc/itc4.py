import math
from heapq import *

def minSum(num, k):
    """
    >>> minSum([10, 20, 7], 4)
    14
    """
    m = list(map(lambda x: -x, num))
    heapify(m)
    for _ in range(k):
       do_one_op()
    return -sum(m)

def do_one_op():
    item = heappop(m)
    heappush(m, -int(math.ceil(-item / 2)))

def f(x):
    return -x


if __name__ == "__main__":
    import doctest

    doctest.testmod()

