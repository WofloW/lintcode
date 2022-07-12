# 919 · 会议室 II
# https://www.lintcode.com/problem/919/description?utm_source=sc-libao-zyq
# Medium

# line sweep扫描线


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
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        # Write your code here
        points = []
        for interval in intervals:
            points.append((interval.start, 1))
            points.append((interval.end, -1))

        result = ongoing_meetings = 0
        for _, delta in sorted(points):
            ongoing_meetings += delta
            result = max(result, ongoing_meetings)
        return result