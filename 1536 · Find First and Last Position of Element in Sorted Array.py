class Solution:
    """
    @param nums: the array of integers
    @param target:
    @return: the starting and ending position
    """

    def searchRange(self, nums, target):
        # Write your code here.
        if not nums:
            return [-1, -1]

        first = self.binary_search(nums, target, 'first')
        last = self.binary_search(nums, target, 'last')
        return [first, last]

    def binary_search(self, nums, target, first_or_last):
        index = -1
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid
            elif nums[mid] == target:
                if first_or_last == 'first':
                    end = mid
                else:
                    start = mid
            else:
                end = mid

        if first_or_last == 'first':
            if nums[start] == target:
                index = start
            elif nums[end] == target:
                index = end
        else:
            if nums[end] == target:
                index = end
            elif nums[start] == target:
                index = start
        return index


'''
Algorithm:
Binary search template for first and last position

Note:
Difference between first and last position
'''