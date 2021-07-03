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
            return results.append(subset.copy())

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

Notice:
sort first
shallow copy subset
'''