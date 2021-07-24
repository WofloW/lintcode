class Solution:
    """
    @param grid: a list of lists of integers
    @return: An integer, minimizes the sum of all numbers along its path
    """

    def minPathSum(self, grid):
        # write your code here
        if not grid:
            return 0
        return self.search(grid, 0, 0, {})

    def search(self, grid, x, y, memo):
        max_row = len(grid) - 1
        max_col = len(grid[0]) - 1
        if x == max_row and y == max_col:
            return grid[x][y]

        if (x, y) in memo:
            return memo[(x, y)]

        go_right = sys.maxsize
        go_down = sys.maxsize
        if y <= max_col - 1:
            go_right = self.search(grid, x, y + 1, memo)
        if x <= max_row - 1:
            go_down = self.search(grid, x + 1, y, memo)
        memo[(x, y)] = min(go_right, go_down) + grid[x][y]
        return memo[(x, y)]

'''
Memo search
'''

class Solution1:
    def minPathSum(self, grid):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j > 0:
                    grid[i][j] += grid[i][j - 1]
                elif j == 0 and i > 0:
                    grid[i][j] += grid[i - 1][j]
                elif i > 0 and j > 0:
                    grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
        return grid[len(grid) - 1][len(grid[0] - 1)]