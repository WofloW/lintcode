# 257 · 最长字符串链
# https://www.lintcode.com/problem/257/description?utm_source=sc-libao-zyq
# Medium
# DP
from typing import (
    List,
)


class Solution:
    """
    @param words: the list of word.
    @return: the length of the longest string chain.
    """

    def longest_str_chain(self, words: List[str]) -> int:
        words = sorted(words, key=lambda x: len(x))
        dp = {}
        for i in range(len(words)):
            dp[i] = 1

            for k in range(i):
                if self.isPredecessor(words[k], words[i]):
                    dp[i] = max(dp[i], dp[k] + 1)
        return max(dp.values())

    def isPredecessor(self, word1, word2):
        if len(word1) != len(word2) - 1:
            return False

        for i in range(len(word1)):
            if word1[i] != word2[i]:
                return word1[i:] == word2[i + 1:]
        else:
            return True