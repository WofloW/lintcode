# 902 · BST中第K小的元素
# https://www.lintcode.com/problem/902/description?fromId=18&_from=collection

# BST Iterator

from lintcode import (
    TreeNode,
)

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: the given BST
    @param k: the given k
    @return: the kth smallest element in BST
    """

    def kth_smallest(self, root: TreeNode, k: int) -> int:
        # write your code here
        stack = []
        cur = root
        count = 0
        while stack or cur:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                node = stack.pop()
                count += 1
                if count == k:
                    return node.val
                if node.right:
                    cur = node.right

