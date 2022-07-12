# 1251 · 拆分子数组
# https://www.lintcode.com/problem/1251/description?utm_source=sc-libao-zyq
# Hard
# Binary search

from typing import (
    List,
)


class Solution:
    """
    @param nums: a list of integers
    @param m: an integer
    @return: return a integer
    """

    def split_array(self, nums: List[int], m: int) -> int:
        # write your code here
        def check(limit):
            current_sum = 0
            count = 1
            for num in nums:
                if current_sum + num > limit:
                    count += 1
                    current_sum = 0
                current_sum += num
            return count

        left = max(nums)
        right = sum(nums)
        while left + 1 < right:
            mid = (left + right) // 2
            if check(mid) > m:
                left = mid
            else:
                right = mid
        if check(left) <= m:
            return left

        return right

