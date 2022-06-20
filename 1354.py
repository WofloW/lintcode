# 1354 · 杨辉三角形II
# https://www.lintcode.com/problem/1354/?fromId=15&_from=collection

from typing import (
    List,
)

class Solution:
    """
    @param row_index: a non-negative index
    @return: the kth index row of the Pascal's triangle
    """
    def get_row(self, row_index: int) -> List[int]:
        # write your code here
        row = []
        for _ in range(row_index + 1):
            for i in range(len(row) - 1, 0, -1):
                row[i] += row[i - 1]
            row.append(1)
        return row