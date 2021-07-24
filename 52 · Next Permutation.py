class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers
    """

    def nextPermutation(self, nums):
        # write your code here
        if not nums or len(nums) <= 1:
            return nums

        n = len(nums)
        up_hill = -1
        for i in range(n - 1, -1, -1):
            if nums[i - 1] < nums[i]:
                up_hill = i - 1
                break

        if up_hill == -1:
            return nums[:: -1]

        for j in range(n - 1, up_hill, -1):
            if nums[j] > nums[up_hill]:
                nums[j], nums[up_hill] = nums[up_hill], nums[j]
                break

        nums[up_hill + 1: n] = nums[n - 1: up_hill: -1]

        return nums


'''
Algorithm:
Find the rule of permutation
1 2 3 4
1 2 4 3
1 3 2 4
1 3 4 2
1 4 2 3
1 4 3 2
2 1 3 4

Find the first uphill
Swap the uphill with a rightmost number larger than it
Reverse  uphill + 1 to the end 

If no uphill, reverse the whole permutation
'''