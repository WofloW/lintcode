from typing import (
    List,
)

class Solution:
    """
    @param nums: a list of integer
    @param target: an integer
    @return: nothing
    """
    def MoveTarget(self, nums: List[int], target: int):
        # write your code here
        n = len(nums)
        left = n - 1
        right = n - 1
        count = 0
        while left >= 0:
            if nums[left] != target:
                nums[right] = nums[left]
                right -= 1
            else:
                count += 1
            left -= 1
        for i in range(count):
            nums[i] = target