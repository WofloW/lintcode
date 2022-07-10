# 553 · 炸弹袭击
# https://www.lintcode.com/problem/553/description?fromId=18&_from=collection

# DP
# 预处理得到每个点上下左右能炸到的数字，最后跑一边求最大值
from typing import (
    List,
)


class Solution:
    """
    @param grid: Given a 2D grid, each cell is either 'W', 'E' or '0'
    @return: an integer, the maximum enemies you can kill using one bomb
    """

    def max_killed_enemies(self, grid: List[List[str]]) -> int:
        # write your code here
        if not grid or not grid[0]:
            return 0

        m = len(grid)
        n = len(grid[0])

        up = [[0] * n for _ in range(m)]
        left = [[0] * n for _ in range(m)]
        down = [[0] * n for _ in range(m)]
        right = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'W':
                    continue
                if grid[i][j] == 'E':
                    up[i][j] += 1
                    left[i][j] += 1
                if i != 0:
                    up[i][j] += up[i - 1][j]
                if j != 0:
                    left[i][j] += left[i][j - 1]

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if grid[i][j] == 'W':
                    continue
                if grid[i][j] == 'E':
                    down[i][j] += 1
                    right[i][j] += 1
                if i != m - 1:
                    down[i][j] += down[i + 1][j]
                if j != n - 1:
                    right[i][j] += right[i][j + 1]

        max_result = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0':
                    current = up[i][j] + left[i][j] + right[i][j] + down[i][j]
                    max_result = max(max_result, current)
        return max_result