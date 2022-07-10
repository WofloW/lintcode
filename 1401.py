# 1401 · 抽搐词
# https://www.lintcode.com/problem/1401/?fromId=18&_from=collection


from typing import (
    List,
)

class Solution:
    """
    @param str: the origin string
    @return: the start and end of every twitch words
    """
    def twitch_words(self, str: str) -> List[List[int]]:
        # Write your code here
        count = 1
        start = 0
        result = []
        for i, c in enumerate(str):
            if i == 0:
                continue
            if c == str[i - 1]:
                count += 1
            else:
                if count >= 3:
                    result.append([start, i - 1])
                count = 1
                start = i
        if count >= 3:
            result.append([start, len(str) - 1])
        return result



class Solution1:
    """
    @param str: the origin string
    @return: the start and end of every twitch words
    """
    def twitch_words(self, str: str) -> List[List[int]]:
        # Write your code here
        i = j = 0
        n = len(str)
        result = []
        while i < n and j < n:
            while j < n and str[i] == str[j]:
                j += 1
            if j - i >= 3:
                result.append([i, j - 1])
            i = j
        return result