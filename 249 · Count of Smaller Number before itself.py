import math


class Solution:
    """
    @param A: an integer array
    @return: A list of integers includes the index of the first number and the index of the last number
    """

    def countOfSmallerNumberII(self, A):
        # write your code here
        block_array = Block_Array(10000)
        results = []
        for i in A:
            results.append(block_array.count_smaller(i))
            block_array.insert(i)

        return results


class Block:
    def __init__(self):
        self.total = 0
        self.counter = {}


class Block_Array:
    def __init__(self, M):
        self.block_num = int(math.sqrt(M))
        self.blocks = [
            Block()
            for _ in range(self.block_num + 1)
        ]

    def count_smaller(self, num):
        count = 0

        block_index = num // self.block_num
        for i in range(block_index):
            count += self.blocks[i].total

        for val, counter in self.blocks[block_index].counter.items():
            if val < num:
                count += counter
        return count

    def insert(self, num):
        block_index = num // self.block_num
        block = self.blocks[block_index]
        block.total += 1
        block.counter[num] = block.counter.get(num, 0) + 1


'''
Algorithm:
Bucket sort
Bucket count

Note:
value from 0 to 10000
Bucket size = sqrt(M)
Bucket num = sqrt(M)
'''