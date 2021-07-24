class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @return: The maximum size
    """

    def backPack(self, m, A):
        # write your code here
        n = len(A)
        dp = [[False] * (m + 1) for _ in range(n + 1)]

        dp[0][0] = True
        for i in range(1, n + 1):
            for j in range(0, m + 1):
                if A[i - 1] <= j:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - A[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]

        for i in range(m, -1, -1):
            if dp[n][i]:
                return i
        return -1


'''
Algorithm:
Dynamic programming

Note:
dp[i][j] means use first i items to get a weight j
so dp is size of [n + 1][m + 1]
'''


class Solution1:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @return: The maximum size
    """

    def backPack(self, m, A):
        # write your code here
        n = len(A)
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(m + 1):
                if j >= A[i - 1]:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - A[i - 1]] + A[i - 1])
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[n][m]


'''
Algorithm:
Dynamic programming

Note:
dp[i][j] means use first i items to get max weight <= j
so dp is size of [n + 1][m + 1]
result is dp[n][m]

'''