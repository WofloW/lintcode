# 讲解在这
# https://www.lintcode.com/problem/130/note/161424?showListFe=false&page=1&pageSize=50

from typing import (
    List,
)


class Solution:

    def heapify(self, A):
        # 从最右下角的父节点开始
        # 递归对比父节点和两个子节点的大小，挑出三个节点里最小的，
        # 如果是子节点，那父子交换，再对这个换过的子节点进行递归
        # 如果是父节点，那什么都不用做，跳出递归
        for i in range((len(A)) // 2, -1, -1):
            self.sift_down(A, i)

    def sift_down(self, A, index):
        n = len(A)
        while index < n:
            left = index * 2 + 1
            right = index * 2 + 2
            min_index = index
            if left < n and A[left] < A[min_index]:
                min_index = left
            if right < n and A[right] < A[min_index]:
                min_index = right

            if min_index == index:
                return
            A[index], A[min_index] = A[min_index], A[index]
            index = min_index