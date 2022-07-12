# 804 · 不同岛屿的数量II
# https://www.lintcode.com/problem/804/description?utm_source=sc-libao-zyq
# DFS
# 解决越界的原理是，3*3的矩阵在右边和下边加了一列和一排0以后，[0,3]会跑到新加的0，[0,-1]还是会跑到新加的0那里去，这方法好巧妙
# 至于翻转，想象俄罗斯方块，
# 除了上下左右转 shapes = [[(a*i, b*j) for i, j in shape] for a, b in ((1,1),(1,-1),(-1,1),(-1,-1))]
# 再加上镜像转[[(j, i) for i, j in shape] for shape in shapes]，
# 然后排序，和第一个点做相对坐标转换，变成字符串，最后求最小字符串，这样凡是符合条件相同的岛屿都能被这个字符串囊括。
class Solution:

    def numDistinctIslands2(self, grid):

        grid += [0] * len(grid[0]),
        for row in grid:
            row += 0,

        def canonical(shape):

            def encode(shape):
                x, y = shape[0]
                return "".join(str(i - x) + ':' + str(j - y) for i, j in shape)

            shapes = [[(a * i, b * j) for i, j in shape] for a, b in ((1, 1), (1, -1), (-1, 1), (-1, -1))]
            shapes += [[(j, i) for i, j in shape] for shape in shapes]

            return min(encode(sorted(shape)) for shape in shapes)

        def dfs(i, j):
            if not grid[i][j]: return []

            grid[i][j] = 0
            shape = [(i, j)]
            for di, dj in ((0, -1), (0, 1), (-1, 0), (1, 0)):
                shape += dfs(i + di, j + dj)
            return shape

        islands = set()
        for i, row in enumerate(grid):
            for j, num in enumerate(row):
                if num == 1:
                    islands.add(canonical(dfs(i, j)))
        return len(islands)