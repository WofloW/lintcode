# 1001 · 小行星的碰撞
# https://www.lintcode.com/problem/1001/description?utm_source=sc-libao-zyq

from typing import (
    List,
)


class Solution:
    """
    @param asteroids: a list of integers
    @return: return a list of integers
    """

    def asteroid_collision(self, asteroids: List[int]) -> List[int]:
        # write your code here
        result = []
        i = 0
        n = len(asteroids)
        while i < n:
            if asteroids[i] > 0:
                result.append(asteroids[i])
            elif not result or result[-1] < 0:
                result.append(asteroids[i])
            elif result[-1] <= -asteroids[i]:
                if result[-1] < -asteroids[i]:
                    i -= 1
                result.pop()
            i += 1
        return result
