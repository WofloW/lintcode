# 200 · 最长回文子串
# https://www.lintcode.com/problem/200/description?utm_source=sc-libao-zyq
# Medium
# DP
class Solution:
    """
    @param s: input string
    @return: a string as the longest palindromic substring
    """

    def longest_palindrome(self, s: str) -> str:
        # write your code here
        if not s:
            return ''

        n = len(s)
        dp = [[False] * n for _ in range(n)]
        max_len = 1
        start = 0
        for i in range(n):
            dp[i][i] = True

        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = s[i] == s[i + 1]
                start = i
                max_len = 2

        for width in range(3, n + 1):
            for left in range(n - width + 1):
                right = left + width - 1
                dp[left][right] = dp[left + 1][right - 1] and s[left] == s[right]
                if dp[left][right] and width > max_len:
                    max_len = width
                    start = left

        return s[start:start + max_len]
