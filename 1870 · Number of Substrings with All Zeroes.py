class Solution:
    """
    @param str: the string
    @return: the number of substrings
    """

    def stringCount(self, str):
        # Write your code here.
        if not str:
            return 0

        n = len(str)
        j, ans = 1, 0
        for i in range(n):
            j = max(i + 1, j)
            if str[i] != '0':
                continue
            while j < n and str[j] == '0':
                j += 1
            ans += j - i
        return ans


'''
Algorithm:
Two pointers in same direction

Note:
j = max(i + 1, j) when i == j make j += 1
'''