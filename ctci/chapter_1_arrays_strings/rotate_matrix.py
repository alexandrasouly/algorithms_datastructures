# nxn matrix , rotate image by 90 degress
from math import floor
from typing import List


def rotate(matrix: List[List[int]]):
    n = len(matrix)
    # for number of layers
    for i in range(floor(n/2)):
        # for number of elements in layer
        for j in range(n-i*2-1):
            # top to temp
            temp = matrix[i][i+j]
            # left one to top
            matrix[i][i+j] = matrix[n-j-i-1][i]
            # bottom one to left
            matrix[n-i-j-1][i] = matrix[n-i-1][n-j-i-1]
            # right one to bottom
            matrix[n-i-1][n-j-i-1] = matrix[j+i][n-i-1]
            # top one to right
            matrix[j+i][n-i-1] = temp
    return matrix


if __name__ == '__main__':
    print(rotate([[1, 2, 3, 4], [5, 6, 7, 8],
          [9, 10, 11, 12], [13, 14, 15, 16]]))
