# Greedy
class Solution:
    """
    @param A: A list of integers
    @return: A boolean
    """

    def canJump(self, A):
        # write your code here
        if not A:
            return False

        n = len(A)
        right_most = 0
        for i in range(n):
            if right_most >= i:
                right_most = max(right_most, i + A[i])
                if right_most >= n - 1:
                    return True

        return False

# Dynamic Programming
