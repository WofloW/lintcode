class Solution:
    """
    @param s: A string
    @param k: An integer
    @return: An integer
    """
    def lengthOfLongestSubstringKDistinct(self, s, k):
        # write your code here
        if not s or not k:
            return 0

        ans = 0
        n = len(s)
        counter = {}
        i = 0
        for j in range(n):
            counter[s[j]] = counter.get(s[j], 0) + 1
            while i <= j and len(counter) > k:
                counter[s[i]] -= 1
                if counter[s[i]] == 0:
                    del counter[s[i]]
                i += 1
            ans = max(ans, j - i + 1)
        return ans


'''
Algorithm:
Two pointer same direction

Note:
for right pointer
move left pointer if hashmap size > k
'''