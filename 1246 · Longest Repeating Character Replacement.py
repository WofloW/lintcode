class Solution:
    """
    @param s: a string
    @param k: a integer
    @return: return a integer
    """

    def characterReplacement(self, s, k):
        # write your code here

        if not s:
            return 0

        # j 指向满足条件的子字符串的后面一个位置
        j = 0
        ans = 0
        n = len(s)
        counter = {}
        max_freq = 0
        for i in range(n):
            while j < n and j - i - max_freq <= k:
                counter[s[j]] = counter.get(s[j], 0) + 1
                max_freq = max(max_freq, counter[s[j]])
                j += 1
            if j - i - max_freq > k:
                # i ~ j-1 的 substring 需要 k +  1
                # i ~ j-2 的 substring 只需要k次替换
                ans = max(ans, j - 1 - i)
            else:
                # i ~ j-1 的substring <= k替换
                ans = max(ans, j - i)

            counter[s[i]] -= 1
            max_freq = max(counter.values())
        return ans


'''
Algorithm:
Two pointers same direction


'''