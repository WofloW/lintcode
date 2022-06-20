# 1102 · 图片平滑器
# https://www.lintcode.com/problem/1102/description?fromId=15&_from=collection

# Easy
# 遍历
from typing import (
    List,
)


class Solution:
    """
    @param m: a 2D integer matrix
    @return: a 2D integer matrix
    """

    def image_smoother(self, A: List[List[int]]) -> List[List[int]]:
        # Write your code here
        if not A or not A[0]:
            return []
        m = len(A)
        n = len(A[0])
        result = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                avg = self.cal_avg(A, i, j)
                result[i][j] = avg
        return result

    def cal_avg(self, A, i, j):
        m = len(A)
        n = len(A[0])
        total = 0
        count = 0
        for x in range(i - 1, i + 2):
            for y in range(j - 1, j + 2):
                if 0 <= x < m and 0 <= y < n:
                    total += A[x][y]
                    count += 1

        return total // count
