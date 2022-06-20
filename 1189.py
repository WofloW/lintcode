# 1189 · 扫雷游戏
# https://www.lintcode.com/problem/1189/solution?fromId=15&_from=collection
# Medium

# DFS
from typing import (
    List,
)

NEIGHBORS = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]


class Solution:

    def update_board(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        x, y = click
        if board[x][y] == 'M':
            board[x][y] = 'X'
        else:
            self.dfs(board, x, y)
        return board

    def dfs(self, board, x, y):
        m = len(board)
        n = len(board[0])
        mines = 0
        for dx, dy in NEIGHBORS:
            i, j = x + dx, y + dy
            if not (0 <= i < m and 0 <= j < n):
                continue
            mines += board[i][j] == 'M'

        if mines > 0:
            board[x][y] = str(mines)
        else:
            board[x][y] = 'B'
            for dx, dy in NEIGHBORS:
                i, j = x + dx, y + dy
                if not (0 <= i < m and 0 <= j < n) or board[i][j] == 'B':
                    continue

                self.dfs(board, i, j)
