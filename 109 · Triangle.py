class Solution:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """

    def minimumTotal(self, triangle):
        # write your code here
        return self.find_min_path(triangle, 0, 0, {})

    def find_min_path(self, triangle, x, y, memo):
        if x == len(triangle):
            return 0

        if (x, y) in memo:
            return memo[(x, y)]

        path0 = self.find_min_path(triangle, x + 1, y, memo)
        path1 = self.find_min_path(triangle, x + 1, y + 1, memo)
        memo[(x, y)] = min(path0, path1) + triangle[x][y]
        return memo[(x, y)]

'''
Algorithm:
memo search

Note:
use x, y tuple as the key of dict
'''