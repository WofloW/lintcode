# 1844 · 子数组和为K II
# https://www.lintcode.com/problem/1844/description?utm_source=sc-libao-zyq
# Medium
# prefix sum

from typing import (
    List,
)


class Solution:
    """
    @param nums: a list of integer
    @param k: an integer
    @return: return an integer, denote the minimum length of continuous subarrays whose sum equals to k
    """

    def subarray_sum_equals_k_i_i(self, nums: List[int], k: int) -> int:
        # write your code here
        n = len(nums)
        prefix = [0] * (n + 1)
        for i, num in enumerate(nums):
            prefix[i + 1] = prefix[i] + num

        hashmap = collections.defaultdict(int)
        min_len = float('inf')
        for end in range(n + 1):
            if prefix[end] - k in hashmap:
                start = hashmap[prefix[end] - k]
                min_len = min(min_len, end - start)
            hashmap[prefix[end]] = end

        return min_len if min_len != float('inf') else -1
