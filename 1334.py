# 1334 · 旋转数组
# https://www.lintcode.com/problem/1334/?fromId=15&_from=collection

# in place
from typing import (
    List,
)


class Solution:
    """
    @param nums: an array
    @param k: an integer
    @return: rotate the array to the right by k steps
    """

    def rotate(self, nums: List[int], k: int) -> List[int]:
        # Write your code here
        k %= len(nums)
        n = len(nums)
        self.reverse(nums, 0, n - k - 1)
        self.reverse(nums, n - k, n - 1)
        self.reverse(nums, 0, n - 1)
        return nums

    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

# array copy
from typing import (
    List,
)

class Solution:
    """
    @param nums: an array
    @param k: an integer
    @return: rotate the array to the right by k steps
    """
    def rotate(self, nums: List[int], k: int) -> List[int]:
        # Write your code here
        k %= len(nums)
        return nums[-k:] + nums[:-k]