class Solution:
    """
    @param nums: an array of integers
    @return: the number of unique integers
    """
    def deduplication(self, nums):
        # write your code here
        if not nums:
            return 0

        nums.sort()
        n = len(nums)
        j = 1
        for i in range(n):
            while j < n and nums[j] == nums[i]:
                j += 1
            if j >= n:
                break
            nums[i + 1] = nums[j]
        return i + 1