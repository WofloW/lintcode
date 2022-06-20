# 605 · 序列重构
# https://www.lintcode.com/problem/605/description
# 描述
# 判断是否序列 org 能唯一地由 seqs重构得出. org是一个由从1到n的正整数排列而成的序列，1 <= n <= 10^4
#  重构表示组合成seqs的一个最短的父序列 (意思是，一个最短的序列使得所有 seqs里的序列都是它的子序列).
# 判断是否有且仅有一个能从 seqs重构出来的序列，并且这个序列是org。
#
# seqs 中可能存在重复序列
#
# 样例
# 例1:
#
# 输入:org = [1,2,3], seqs = [[1,2],[1,3]]
# 输出: false
# 解释:
# [1,2,3] 并不是唯一可以被重构出的序列，还可以重构出 [1,3,2]
# 例2:
#
# 输入: org = [1,2,3], seqs = [[1,2]]
# 输出: false
# 解释:
# 能重构出的序列只有 [1,2]，无法重构出 [1,2,3]
# 例3:
#
# 输入: org = [1,2,3], seqs = [[1,2],[1,3],[2,3]]
# 输出: true
# 解释:
# 序列 [1,2], [1,3], 和 [2,3] 可以唯一重构出 [1,2,3].
# 例4:
#
# 输入:org = [4,1,5,2,6,3], seqs = [[5,2,6,3],[4,1,5,2]]
# 输出:true

# topological sort

from typing import (
    List,
)
from collections import defaultdict, deque
class Solution:
    """
    @param org: a permutation of the integers from 1 to n
    @param seqs: a list of sequences
    @return: true if it can be reconstructed only one or false
    """
    def sequence_reconstruction(self, org: List[int], seqs: List[List[int]]) -> bool:
        # write your code here
        graph = defaultdict(list)
        indegrees = defaultdict(int)
        node_seqs = set()

        for seq in seqs:
            node_seqs |= set(seq)
            for i in range(1, len(seq)):
                indegrees[seq[i]] += 1
                graph[seq[i - 1]].append(seq[i])

        if len(node_seqs) != len(org):
            return False

        queue = deque()
        for i in range(1, len(org) + 1):
            if indegrees[i] == 0:
                queue.append(i)

        result = []
        while queue:
            if len(queue) > 1:
                return False
            num = queue.popleft()
            result.append(num)
            for neighbor in graph[num]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    queue.append(neighbor)
        return result == org