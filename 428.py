# 428 · x的n次幂
# https://www.lintcode.com/problem/428/description?fromId=18&_from=collection

# Medium
# Iterative
class Solution:
    """
    @param x {float}: the base number
    @param n {int}: the power number
    @return {float}: the result
    """
    def myPow(self, x, n):
        if n < 0:
            x = 1 / x
            n = -n

        result = 1.0
        tmp = x

        while n:
            if n & 1:
                result *= tmp
            tmp *= tmp
            n >>= 1
        return result

# Recursive
class Solution1:
    def myPow(self, x, n):
        def recursive(n):
            if n == 0:
                return 1.0
            y = recursive(n // 2)
            return y * y * (x if n & 1 == 1 else 1)

        return recursive(n) if n >= 0 else 1.0 / recursive(-n)

