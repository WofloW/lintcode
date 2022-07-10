# 407 · 加一
# https://www.lintcode.com/problem/407/description?fromId=18&_from=collection

class Solution:
    """
    @param digits: a number represented as an array of digits
    @return: the result
    """

    def plusOne(self, digits):
        # write your code here
        carry = 1
        queue = collections.deque(digits)
        i = len(digits) - 1
        while i >= 0 and carry:
            sum_digit = (queue[i] + carry)
            queue[i] = sum_digit % 10
            carry = sum_digit // 10
            i -= 1
        if carry:
            queue.appendleft(1)
        return list(queue)