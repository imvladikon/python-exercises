#!/bin/python3

import math
import os
import random
import re
import sys


import numpy as np
from itertools import combinations
import time
# start_time = time.time()
max_weight = 1001

# modification of floyd-warshall alg. with threshold,
# 'cause we are not intrested in nodes greater than distanceThreshold


def floyd_warshall(G, distanceThreshold):
    M = G
    n = len(M[0])
    # nanarray = np.argwhere(np.isnan(M))
    # if not len(nanarray):
    #     return M
    for k in range(n):
        # for row in nanarray:
        #     i = row[0]
        #     j = row[1]
        #     M[i, j] = np.nanmin([M[i, j], M[i, k] + M[k, j]])
        for i in range(n):
            if not M[i][k] == max_weight and M[i][k] > distanceThreshold:
                continue
            for j in range(i):
                M[j, i] = min([M[i, j], M[i, k] + M[k, j]])
                M[i, j] = M[j, i]
    return M

# [0, 2, 1, 2, 2]
# [2, 0, 1, 2, 2]
# [1, 1, 0, 1, 1]
# [2, 2, 1, 0, 2]
# [2, 2, 1, 2, 0]


def build_symmetric_matrix(city_nodes, city_from, city_to, city_weight):
    matrix = max_weight * \
        np.full((city_nodes, city_nodes), max_weight, dtype=int)
    for idx in range(city_nodes):
        matrix[idx, idx] = 0
    length = len(city_weight)
    for idx in range(length):
        i = city_from[idx] - 1
        j = city_to[idx] - 1
        matrix[i, j] = city_weight[idx]
        matrix[j, i] = city_weight[idx]
    return matrix

#
# Complete the 'findBestCity' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER distanceThreshold
#  2. WEIGHTED_INTEGER_GRAPH city
#

#
# For the weighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] and <name>_to[i]. The weight of the edge is <name>_weight[i].
#
#


def findBestCity(distanceThreshold, city_nodes, city_from, city_to, city_weight):
    matrix = build_symmetric_matrix(
        city_nodes, city_from, city_to, city_weight)
    matrix = floyd_warshall(matrix, distanceThreshold)
    neighbors = [0] * (len(matrix))
    for i, row in enumerate(matrix):
        count = 0
        for j, cell in enumerate(row):
            if i == j:
                continue
            if cell == 0 or cell > distanceThreshold:
                continue
            count += 1
        neighbors[i] = count
    return len(neighbors) - neighbors[::-1].index(min(neighbors))


if __name__ == '__main__':
