# 1042 · 托普利兹矩阵
# https://www.lintcode.com/problem/1042/description?fromId=18&_from=collection

from typing import (
    List,
)


class Solution:
    """
    @param matrix: the given matrix
    @return: True if and only if the matrix is Toeplitz
    """

    def is_toeplitz_matrix(self, matrix: List[List[int]]) -> bool:
        # Write your code here
        m = len(matrix)
        n = len(matrix[0])

        for i in range(m - 1):
            for j in range(n - 1):
                if matrix[i][j] != matrix[i + 1][j + 1]:
                    return False
        return True