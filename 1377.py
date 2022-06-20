# 1377 · 寻找子串
# https://www.lintcode.com/problem/1377/description?fromId=15&_from=collection

# window and set
class Solution:
    """
    @param str: The string
    @param k: The length of the substring
    @return: The answer
    """

    def find_substring(self, str: str, k: int) -> int:
        # Write your code here
        if k > 26:
            return 0

        word_set = set()
        ch_set = set()

        start = end = 0
        while end < len(str):
            if str[end] not in ch_set:
                ch_set.add(str[end])
                print(str[end], len(ch_set))
                end += 1
                if len(ch_set) == k:
                    word_set.add(str[start: end])
                    ch_set.remove(str[start])
                    start += 1
            else:
                ch_set.remove(str[start])
                start += 1
        return len(word_set)

# 暴力穷举
class Solution:
    """
    @param str: The string
    @param k: The length of the substring
    @return: The answer
    """

    def check(self, str):
        counter = {}
        for c in str:
            if c not in counter:
                counter[c] = 1
            else:
                return False
        return True

    def find_substring(self, str: str, k: int) -> int:
        # Write your code here
        if k > 26:
            return 0
        current = set()
        n = len(str)
        for i in range(len(str) - k + 1):
            sub_str = str[i: i + k]
            if self.check(sub_str):
                current.add(sub_str)
        return len(current)
