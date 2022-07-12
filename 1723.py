# 1723 · 网格中的最短路径
# https://www.lintcode.com/problem/1723/description?utm_source=sc-libao-zyq
# Medium

# BFS with parameter

from typing import (
    List,
)
from collections import deque

DIRECTIONS = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0)
]


class Solution:
    """
    @param grid: a list of list
    @param k: an integer
    @return: Return the minimum number of steps to walk
    """

    def shortest_path(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        start = (0, 0, 0)
        queue = deque([start])
        visited = {start}
        steps = 0
        while queue:
            for _ in range(len(queue)):
                i, j, destroy = queue.popleft()
                if i == m - 1 and j == n - 1:
                    return steps

                for dx, dy in DIRECTIONS:
                    x = i + dx
                    y = j + dy

                    if not (0 <= x < m and 0 <= y < n):
                        continue

                    obs = destroy + grid[x][y]
                    if obs > k or (x, y, obs) in visited:
                        continue

                    queue.append((x, y, obs))
                    visited.add((x, y, obs))

            steps += 1
        return -1