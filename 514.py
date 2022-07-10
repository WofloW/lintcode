# 514 · 栅栏染色
# https://www.lintcode.com/problem/514/description?fromId=18&_from=collection
# Easy
# DP

# 本能的反应是用dfs，但是后面数据量大的时候会TLE，只好看答案用DP了。
#
# dp[i] = dp[i - 1] * (k - 1) + dp[i - 2] * (k - 1)
#
# 当前和上一个不同色，已知n-1时有dp[n - 1]种可能，然后n选和n-1不一样的k-1种新颜色，
#
# 当前和上一个同色的时候, 已知n-2有dp[n - 2]种可能，然后n-1 n-2都选一样的颜色，但需要和n-2不同，有k-1种选择
#
# 滚动数组是dp里的小技巧，当dp[n]只和dp[n-1] dp[n-2]有关的时候，之前的都可以忘记了，实现滚动数组的两种方法
# 其实我个人更推荐的是用数组长度为3，然后%3的方法，这样扩展性能强
# 当n只和n-1 n-2有关的时候，可以用后面一种prev prev_prev的方法，好处是不用考虑%3的情况

class Solution:
    """
    @param n: non-negative integer, n posts
    @param k: non-negative integer, k colors
    @return: an integer, the total number of ways
    """

    def num_ways(self, n: int, k: int) -> int:
        dp = [0, k, k * k]
        if n <= 2:
            return dp[n]

        if k == 0:
            return 0

        result = None
        for i in range(n - 2):
            dp[i % 3] = result = (k - 1) * (dp[(i - 1) % 3] + dp[(i - 2) % 3])
        return result


class Solution1:
    """
    @param n: non-negative integer, n posts
    @param k: non-negative integer, k colors
    @return: an integer, the total number of ways
    """

    def num_ways(self, n: int, k: int) -> int:

        if k == 0:
            return 0

        edge_cases = [0, k, k * k]
        if n <= 2:
            return edge_cases[n]

        prev = k * k
        prev_prev = k

        for _ in range(n - 2):
            prev, prev_prev = (prev + prev_prev) * (k - 1), prev
        return prev