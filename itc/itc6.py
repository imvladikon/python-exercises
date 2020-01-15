import numpy as np

B = np.random.randint(-100,100,size=100000)

def max_subarray(A):
    max_so_far = max_ending_here = 0
    for x in A:
        max_ending_here = max(0, max_ending_here + x)
        max_so_far      = max(max_so_far, max_ending_here)
    return max_so_far


measurements = np.zeros(100, dtype='float')

B = np.array([[1, 1, 1, 1, 1],

       [1, 1, 1, 0, 0],

       [1, 1, 1, 0, 0],

       [1, 1, 1, 0, 0],

       [1, 1, 1, 1, 1]])


def largestMatrix(arr):
    array = np.array(arr)
    num_rows = array.shape[0] #len(array)
    num_cols = array.shape[1] #len(array)
    matrix = np.zeros(shape=(num_rows, num_cols), dtype=np.int)
    matrix[0, :] = array[0, :]
    matrix[:, 0] = array[:, 0]
    for row in range(1, num_rows):
        for col in range(1, num_cols):
            if array[row, col] == 0:`
                matrix[row, col] = 0
                continue
            diag = matrix[row - 1, col - 1]
            top = matrix[row - 1, col]
            left = matrix[row, col - 1]
            matrix[row, col] = min(diag, min(top, left)) + 1
    return matrix.max()




print(largestMatrix(B))