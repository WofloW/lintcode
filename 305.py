# 305 · 矩阵中的最长递增路径
# https://www.lintcode.com/problem/305/description?utm_source=sc-libao-zyq
# Hard

# DP

from typing import (
    List,
)

DIR = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0)
]

class Solution:
    """
    @param matrix: A matrix
    @return: An integer.
    """
    def longestIncreasingPath(self, matrix):
        points = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                points.append((matrix[i][j], i, j))
        points.sort()

        parsed_to_index = {}
        dp = [1] * len(points)
        for i in range(len(points)):
            for dx, dy in DIR:
                x = points[i][1] + dx
                y = points[i][2] + dy
                if (x, y) in parsed_to_index:
                    k = parsed_to_index[(x, y)]
                    if points[i][0] > points[k][0]:
                        dp[i] = max(dp[i], dp[k] + 1)
            parsed_to_index[(points[i][1], points[i][2])] = i
        return max(dp)

# DFS with memo
from typing import (
    List,
)

DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
class Solution1:


    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        memo = {}
        if not matrix:
            return 0

        def dfs(row: int, column: int) -> int:
            if (row, column) in memo:
                return memo[(row, column)]
            best = 1
            for dx, dy in DIRS:
                newRow, newColumn = row + dx, column + dy
                if 0 <= newRow < rows and 0 <= newColumn < columns and matrix[newRow][newColumn] > matrix[row][column]:
                    best = max(best, dfs(newRow, newColumn) + 1)
            memo[(row, column)] = best
            return best

        ans = 0
        rows, columns = len(matrix), len(matrix[0])
        for i in range(rows):
            for j in range(columns):
                ans = max(ans, dfs(i, j))
        return ans