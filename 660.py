# 660 · 用Read4从文件中读取N个字符 II-多次调用
# https://www.lintcode.com/problem/660/description?utm_source=sc-libao-zyq
# Hard

"""
The read4 API is already defined for you.
@param buf a list of characters
@return an integer
you can call Reader.read4(buf)
"""


class Solution:
    def __init__(self):
        self.buf4, self.i4, self.n4 = [0] * 4, 0, 0

    # @param {char[]} buf destination buffer
    # @param {int} n maximum number of characters to read
    # @return {int} the number of characters read
    def read(self, buf, n):
        i = 0
        while i < n:
            if self.i4 == self.n4:
                self.i4, self.n4 = 0, Reader.read4(self.buf4)
                if not self.n4:
                    break
            buf[i], self.i4, i = self.buf4[self.i4], self.i4 + 1, i + 1
        return i