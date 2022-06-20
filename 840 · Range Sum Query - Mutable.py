class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.list = nums
        self.bits = [0] * (len(nums) + 1)
        self.n = len(nums)
        for i in range(self.n):
            self.add(i, nums[i])

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        self.add(i, val - self.list[i])
        self.list[i] = val

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sum(j) - self.sum(i - 1)

    def add(self, i, val):
        i += 1
        while i <= self.n:
            self.bits[i] += val
            i += self.low_bit(i)

    def low_bit(self, x):
        return x & -x

    def sum(self, i):
        i += 1
        res = 0
        while i > 0:
            res += self.bits[i]
            i -= self.low_bit(i)
        return res

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)