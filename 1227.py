# 1227 · 重复的子串模式
# https://www.lintcode.com/problem/1227/?fromId=15&_from=collection

# Easy
# 挨个测试
class Solution:
    """
    @param s: a string
    @return: return a boolean
    """
    def repeated_substring_pattern(self, s: str) -> bool:
        # write your code here
        n = len(s)
        for i in range(1, n // 2 + 1):
            if n % i == 0:
                for j in range(i, n):
                    if s[j] != s[j - i]:
                        break
                else:
                    return True
        return False

# 利用string查找
class Solution:
    """
    @param s: a string
    @return: return a boolean
    """
    def repeated_substring_pattern(self, s: str) -> bool:
        return (s + s).find(s, 1) != len(s)