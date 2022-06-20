# 1126 · 合并两棵二叉树
# https://www.lintcode.com/problem/1126/description?fromId=15&_from=collection
# Easy

# recursive
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
    @param t1: the root of the first tree
    @param t2: the root of the second tree
    @return: the new binary tree after merge
    """

    def merge_trees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        # Write your code here
        if not t1:
            return t2
        if not t2:
            return t1

        node = TreeNode(t1.val + t2.val)
        node.left = self.merge_trees(t1.left, t2.left)
        node.right = self.merge_trees(t1.right, t2.right)
        return node
