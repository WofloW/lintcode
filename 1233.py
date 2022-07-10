# 1233 · 根据字符出现频率排序
# https://www.lintcode.com/problem/1233/description?fromId=18&_from=collection
# Medium

# Sort by -freq and then char
class Solution:
    """
    @param s:
    @return: return a string
    """
    def frequency_sort(self, s: str) -> str:
        # write your code here
        counter = collections.Counter(s)
        char_freq = []
        for char, freq in counter.items():
            char_freq.append((-freq, char))
        char_freq.sort()
        result = []
        for freq, char in char_freq:
            result += [char] * -freq
        return ''.join(result)
