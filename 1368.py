# 1368 · 相同数字
# https://www.lintcode.com/problem/1368/?fromId=18&_from=collection
# Easy

from typing import (
    List,
)


class Solution:
    """
    @param nums: the arrays
    @param k: the distance of the same number
    @return: the ans of this question
    """

    def same_number(self, nums: List[int], k: int) -> str:
        # Write your code here
        positions = {}
        for i, c in enumerate(nums):
            if c in positions:
                if i - positions[c] < k:
                    return 'YES'
            positions[c] = i

        return 'NO'
