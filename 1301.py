# 1301 · 生命游戏
# https://www.lintcode.com/problem/1301/description?fromId=18&_from=collection

# 用额外状态2表示死细胞复活，-1表示活细胞死亡，
# 如果活细胞存活或者死细胞保持，就维持原样
# 这样既知道了之后的状态，又能知道这个细胞之前的状态
# 用abs(board[x][y]) == 1判断之前这个细胞是存活的
# 最后把>0的当作下一步为存活的改成1
from typing import (
    List,
)

class Solution:
    """
    @param board: the given board
    @return: nothing
    """
    def game_of_life(self, board: List[List[int]]):
        # Write your code here
        if not board or not board[0]:
            return []

        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                count = self.count_near_alive(board, i, j)
                if board[i][j] == 1 and self.alive_next_dead(count):
                        board[i][j] = -1
                elif board[i][j] == 0 and self.dead_next_alive(count):
                        board[i][j] = 2
        for i in range(m):
            for j in range(n):
                board[i][j] = 1 if board[i][j] > 0 else 0

    def count_near_alive(self, board, i, j):
        m = len(board)
        n = len(board[0])
        count = 0
        for x, y in [
            (i - 1, j),
            (i - 1, j - 1),
            (i - 1, j + 1),
            (i + 1, j),
            (i + 1, j + 1),
            (i + 1, j - 1),
            (i, j + 1),
            (i, j - 1)
            ]:
            if 0 <= x < m and 0 <= y < n and abs(board[x][y]) == 1:
                count += 1
        return count

    def alive_next_dead(self, count):
        return not (2 <= count <= 3)

    def dead_next_alive(self, count):
        return count == 3