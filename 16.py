# 16 · 带重复元素的排列
# https://www.lintcode.com/problem/16/
# Medium

class Solution:
    """
    @param: :  A list of integers
    @return: A list of unique permutations
    """

    def permuteUnique(self, nums):
        # write your code here
        if not nums:
            return [[]]

        permutations = []
        nums.sort()
        self.dfs(nums, [], set(), permutations)
        return permutations

    def dfs(self, nums, permutation, visited, permutations):
        if len(permutation) == len(nums):
            permutations.append(list(permutation))
            return

        for i in range(len(nums)):
            num = nums[i]
            if i > 0 and nums[i - 1] == nums[i] and not (i - 1) in visited:
                continue

            if i in visited:
                continue
            visited.add(i)
            permutation.append(num)
            self.dfs(nums, permutation, visited, permutations)
            permutation.pop()
            visited.remove(i)

'''
Algorithm:
DFS
Duplicated check

Note:
For example
2' 2''
If 2' is not visited, don't visit 2''. That will cause duplicated permutation.
'''