# 1369 · 最频繁单词
# https://www.lintcode.com/problem/1369/?fromId=15&_from=collection

from typing import (
    List,
)

class Solution:
    """
    @param paragraph:
    @param banned:
    @return:
    """
    def most_common_word(self, paragraph: str, banned: List[str]) -> str:
        banned = set(banned)
        words = [word.strip("!?',;.") for word in paragraph.split(' ')]
        words = [word.lower() for word in words if word.lower() not in banned]
        counter = collections.Counter(words)
        max_freq = 0
        result = None
        for word, freq in counter.items():
            if freq > max_freq:
                max_freq = freq
                result = word
        return result

