# 70 · 二叉树的层次遍历 II
# https://www.lintcode.com/problem/70/description?utm_source=sc-libao-zyq
# Medium
# BFS
from typing import (
    List,
)
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
    @param root: A tree
    @return: buttom-up level order a list of lists of integer
    """
    def level_order_bottom(self, root: TreeNode) -> List[List[int]]:
        # write your code here
        if not root:
            return []
        queue = [root]
        result = []
        while queue:
            new_queue = []
            result.append([node.val for node in queue])
            for node in queue:
                if node.left:
                    new_queue.append(node.left)
                if node.right:
                    new_queue.append(node.right)
            queue = new_queue
        return list(reversed(result))