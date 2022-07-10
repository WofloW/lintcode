# 983 · 棒球游戏
# https://www.lintcode.com/problem/983/?fromId=15&_from=collection

from typing import (
    List,
)

class Solution:
    """
    @param ops: the list of operations
    @return:  the sum of the points you could get in all the rounds
    """
    def cal_points(self, ops: List[str]) -> int:
        # Write your code here
        points = []
        for op in ops:
            if op == '+':
                points.append(points[-1] + points[-2])
            elif op == 'D':
                points.append(points[-1] * 2)
            elif op == 'C':
                points.pop()
            else:
                points.append(int(op))
        return sum(points)