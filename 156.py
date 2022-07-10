# 156 · 合并区间
# https://www.lintcode.com/problem/156/description?fromId=18&_from=collection

# data structure

from typing import (
    List,
)
from lintcode import (
    Interval,
)

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: interval list.
    @return: A new interval list.
    """
    def merge(self, intervals: List[Interval]) -> List[Interval]:
        # write your code here
        intervals.sort(key=lambda x:x.start)
        results = []
        for interval in intervals:
            if results and interval.start <= results[-1].end:
                results[-1].end = max(results[-1].end, interval.end)
            else:
                results.append(interval)
        return results
