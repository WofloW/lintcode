class Solution:
    """
    @param nums: a list of integers.
    @param k: length of window.
    @return: the sum of the element inside the window at each moving.
    """

    def winSum(self, nums, k):
        # write your code here
        if not nums or k > len(nums):
            return []

        ans = []
        j, window_sum = 0, 0
        n = len(nums)
        for i in range(n):
            while j < n and j - i < k:
                window_sum += nums[j]
                j += 1

            if j - i == k:
                ans.append(window_sum)

            window_sum -= nums[i]

        return ans


'''
Algorithm:
Two pointers same direction

'''