# 1024 · 满足要求的子串个数
# https://www.lintcode.com/problem/1024/description?utm_source=sc-libao-zyq
# Medium
# Hashmap, binary search
from typing import (
    List,
)
import bisect


class Solution:
    """
    @param s: a string
    @param words: a dictionary of words
    @return: the number of words[i] that is a subsequence of S
    """

    def num_matching_subseq(self, s: str, words: List[str]) -> int:
        def check(word) -> int:
            prev = -1
            for c in word:
                if c not in s_dic or prev + 1 > s_dic[c][-1]:
                    return 0
                idx = bisect.bisect_left(s_dic[c], prev + 1)  # 从prev+1开始找（闭区间）
                prev = s_dic[c][idx]
            return 1

        words_dic = collections.Counter(words)
        s_dic = collections.defaultdict(list)  # character -> list of all index
        for i, c in enumerate(s):
            s_dic[c].append(i)
        return sum(check(word) * freq for word, freq in words_dic.items())