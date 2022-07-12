# 1149 · 有效的正方形
# https://www.lintcode.com/problem/1149/description?utm_source=sc-libao-zyq

# Sort

from typing import (
    List,
)

class Solution:
    """
    @param p1: the first point
    @param p2: the second point
    @param p3: the third point
    @param p4: the fourth point
    @return: whether the four points could construct a square
    """
    def valid_square(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        # Write your code here
        def calc_distance(p0, p1):
            return (p0[0] - p1[0]) ** 2 + (p0[1] - p1[1]) ** 2

        p = [p1, p2, p3, p4]
        p.sort()
        return calc_distance(p[0], p[1]) != 0 and \
        calc_distance(p[0], p[1]) == calc_distance(p[1], p[3]) and \
        calc_distance(p[0], p[1]) == calc_distance(p[3], p[2]) and \
        calc_distance(p[0], p[1]) == calc_distance(p[2], p[0]) and \
        calc_distance(p[0], p[3]) == calc_distance(p[1], p[2])