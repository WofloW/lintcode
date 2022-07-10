# 17 · 子集
# https://www.lintcode.com/problem/17/
class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """
    def subsets(self, nums):
        # write your code here
        results = []
        subset = []
        nums.sort()
        self.dfs(nums, 0, subset, results)
        return results

    def dfs(self, nums, index, subset, results):
        if index == len(nums):
            return results.append(list(subset))

        subset.append(nums[index])
        self.dfs(nums, index + 1, subset, results)
        subset.pop()
        self.dfs(nums, index + 1, subset, results)

'''
Algorithm:
DFS
pick one
    do dfs
Don't pick one
    do dfs
Meet leaf
    append subset

Note:
sort first
shallow copy subset
'''

import collections


class Solution2:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """

    def subsets(self, nums):
        # write your code here
        results = []
        if not nums:
            return [[]]
        nums.sort()

        queue = collections.deque()
        queue.append([])

        while queue:
            subset = queue.popleft()
            results.append(subset)

            for i in range(len(nums)):
                if not subset or subset[-1] < nums[i]:
                    new_subset = list(subset)
                    new_subset.append(nums[i])
                    queue.append(new_subset)

        return results


'''
Algorithm:
BFS
'''
