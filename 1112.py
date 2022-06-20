# 1112 · 寻找数据错误
# https://www.lintcode.com/problem/1112/

# counter
from typing import (
    List,
)


class Solution:
    """
    @param nums: an array
    @return: the number occurs twice and the number that is missing
    """

    def find_error_nums(self, nums: List[int]) -> List[int]:
        # Write your code here
        counter = [0] * (len(nums) + 1)
        result = [0, 0]
        for num in nums:
            counter[num] += 1
            if counter[num] == 2:
                result[0] = num

        for i in range(1, len(nums) + 1):
            if counter[i] == 0:
                result[1] = i
        return result