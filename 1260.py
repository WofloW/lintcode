# 1260 · 轮转函数
# https://www.lintcode.com/problem/1260/description?fromId=15&_from=collection
# Medium
# math
from typing import (
    List,
)

class Solution:
    """
    @param a: an array
    @return: the maximum value of F(0), F(1), ..., F(n-1)
    """
    def max_rotate_function(self, a: List[int]) -> int:
        # Write your code here
        n = len(a)
        s = sum(a)
        current = sum([i * v for i, v in enumerate(a)])
        max_result = current
        for i in range(1, n):
            current += s - n * a[n - i]
            max_result = max(max_result, current)
        return max_result