# 1869 · 统计全为 1 的正方形子矩阵
# https://www.lintcode.com/problem/1869/description?utm_source=sc-libao-zyq
# Medium
# DP, max side length of 1 square

from typing import (
    List,
)


class Solution:
    """
    @param matrix: a matrix
    @return: return how many square submatrices have all ones
    """

    def count_squares(self, matrix: List[List[int]]) -> int:
        # write your code here
        m, n = len(matrix), len(matrix[0])

        dp = [[0] * n for _ in range(m)]

        result = 0
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dp[i][j] = matrix[i][j]
                elif matrix[i][j] == 0:
                    dp[i][j] = 0
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                result += dp[i][j]
        return result