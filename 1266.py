# 1266 · 找不同
# https://www.lintcode.com/problem/1266/description?fromId=18&_from=collection
# Easy


# 找哪个数多一个
class Solution:
    """
    @param s: a string
    @param t: a string
    @return: the letter that was added in t
    """
    def find_the_difference(self, s: str, t: str) -> str:
        # Write your code here
        if len(s) == 0:
            return t
        s_counter = collections.Counter(s)
        t_counter = collections.Counter(t)
        for c in t_counter:
            if c not in s_counter:
                return c
            if t_counter[c] - s_counter[c] > 0:
                return c

# 位的运算，一个数异或两次会抵消，最后没抵消的数就是答案
class Solution1:
    """
    @param s: a string
    @param t: a string
    @return: the letter that was added in t
    """
    def find_the_difference(self, s: str, t: str) -> str:
        # Write your code here
        result = 0
        for c in s:
            result ^= ord(c)

        for c in t:
            result ^= ord(c)

        return chr(result)
