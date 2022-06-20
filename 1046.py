# 1046 · 二进制表示中质数个计算置位
# https://www.lintcode.com/problem/1046/description?fromId=15&_from=collection

class Solution:
    """
    @param l: an integer
    @param r: an integer
    @return: the count of numbers in the range [L, R] having a prime number of set bits in their binary representation
    """
    def count_prime_set_bits(self, l: int, r: int) -> int:
        # Write your code here
        return sum([self.is_prime(bin(i).count('1')) for i in range(l, r + 1)])

    def is_prime(self, n):
        if n == 1:
            return False
        i = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i += 1
        return True
