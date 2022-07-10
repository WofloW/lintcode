# 914 · 翻转游戏
# https://www.lintcode.com/problem/914/?fromId=18&_from=collection

from typing import (
    List,
)

class Solution:
    """
    @param s: the given string
    @return: all the possible states of the string after one valid move
             we will sort your return value in output
    """
    def generate_possible_next_moves(self, s: str) -> List[str]:
        # write your code here
        results = []
        s_list = list(s)
        for i in range(1, len(s)):
            if s[i] == s[i - 1] == '+':
                s_list[i] = s_list[i - 1] = '-'
                results.append(''.join(s_list))
                s_list[i] = s_list[i - 1] = '+'
        return results
