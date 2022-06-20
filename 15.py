# 15 · 全排列
# https://www.lintcode.com/problem/15/
# Medium

class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """

    def permute(self, nums):
        # write your code here
        if not nums:
            return [[]]

        permutations = []
        self.dfs(nums, [], set(), permutations)
        return permutations

    def dfs(self, nums, permutation, visited, permutations):
        if len(permutation) == len(nums):
            permutations.append(list(permutation))
            return

        for num in nums:
            if num in visited:
                continue
            visited.add(num)
            permutation.append(num)
            self.dfs(nums, permutation, visited, permutations)
            permutation.pop()
            visited.remove(num)

'''
Algorithm:
DFS

Note:
Shallow copy of permutation
'''