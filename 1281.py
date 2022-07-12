# 1281 · 前K个高频元素
# https://www.lintcode.com/problem/1281/description?utm_source=sc-libao-zyq
# Medium

# Heap
from typing import (
    List,
)
import heapq


class Solution:
    """
    @param nums: the given array
    @param k: the given k
    @return: the k most frequent elements
             we will sort your return value in output
    """

    def top_k_frequent(self, nums: List[int], k: int) -> List[int]:
        # Write your code here
        counter = collections.Counter(nums)
        heap = []
        for num, freq in counter.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)
        result = []
        for _ in range(len(heap)):
            result.append(heapq.heappop(heap)[1])
        return result
