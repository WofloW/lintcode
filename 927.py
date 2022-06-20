# 927 · 翻转字符串II
# https://www.lintcode.com/problem/927/description?fromId=15&_from=collection

# 输入: s = "the sky is blue"
# 输出: "blue is sky the"

# in place swap

class Solution:
    """
    @param str: a string
    @return: return a string
    """
    def reverseWords(self, s):
        S = list(s)
        self.reverse(S, 0, len(S) - 1)
        start = 0
        for i in range(len(S)):
            if S[i] == " ":
                self.reverse(S, start, i - 1)
                start = i + 1
        self.reverse(S, start, len(S) - 1)
        return "".join(S)

    def reverse(self, S, start, end):
        while start < end:
            S[start], S[end] = S[end], S[start]
            start += 1
            end -= 1