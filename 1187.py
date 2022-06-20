# 1187 · 数组中的K-diff对
# https://www.lintcode.com/problem/1187/?fromId=15&_from=collection
# Easy

from typing import (
    List,
)

class Solution:
    """
    @param nums: an array of integers
    @param k: an integer
    @return: the number of unique k-diff pairs
    """
    def find_pairs(self, nums: List[int], k: int) -> int:
        # Write your code here
        counter = collections.Counter(nums)
        result = 0
        for num in counter:
            if k != 0:
                if counter[num + k] > 0:
                    result += 1
            else:
                if counter[num + k] > 1:
                    result += 1

        return result