# 1310 · 数组除了自身的乘积
# https://www.lintcode.com/problem/1310/description?fromId=15&_from=collection

from typing import (
    List,
)

class Solution:
    """
    @param nums: an array of integers
    @return: the product of all the elements of nums except nums[i].
    """
    def product_except_self(self, nums: List[int]) -> List[int]:
        # write your code here
        n = len(nums)
        result = [1] * n
        left = 1
        for i in range(1, n):
            left *= nums[i - 1]
            result[i] *= left
        right = 1
        for i in range(n - 2, -1, -1):
            right *= nums[i + 1]
            result[i] *= right
        return result