# 1250 · 第三大的数
# https://www.lintcode.com/problem/1250/description?fromId=15&_from=collection
# Easy

# heap
from typing import (
    List,
)

import heapq

class Solution:
    """
    @param nums: the array
    @return: the third maximum number in this array
    """
    def third_max(self, nums: List[int]) -> int:
        # Write your code here.
        nums = set(nums)
        if len(nums) < 3:
            return max(nums)
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > 3:
                heapq.heappop(heap)

        return heapq.heappop(heap)


# quick select
from typing import (
    List,
)


class Solution1:
    """
    @param nums: the array
    @return: the third maximum number in this array
    """

    def third_max(self, nums: List[int]) -> int:
        # Write your code here.
        nums = list(set(nums))
        if len(nums) < 3:
            return max(nums)

        return self.quick_select(nums, 0, len(nums) - 1, 2)

    def quick_select(self, nums, start, end, k):
        if start == end:
            return nums[start]
        pivot = nums[(start + end) // 2]
        left, right = start, end
        while left <= right:
            while left <= right and nums[left] > pivot:
                left += 1
            while left <= right and nums[right] < pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        if k <= right:
            return self.quick_select(nums, start, right, k)
        if k >= left:
            return self.quick_select(nums, left, end, k)

        return nums[left - 1]
