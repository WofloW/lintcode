# 1212 · 最大连续1的个数
# https://www.lintcode.com/problem/1212/?fromId=18&_from=collection

from typing import (
    List,
)

class Solution:
    """
    @param nums: a binary array
    @return:  the maximum number of consecutive 1s
    """
    def find_max_consecutive_ones(self, nums: List[int]) -> int:
        # Write your code here
        result = 0
        curr = 0
        for i, num in enumerate(nums):
            if num == 0:
                result = max(result, curr)
                curr = 0
            else:
                curr += 1
        result = max(result, curr)
        return result
