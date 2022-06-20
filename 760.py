# 760 · 二叉树的右视图
# https://www.lintcode.com/problem/760/description?fromId=15&_from=collection

# 描述
# 给定一棵二叉树，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。

# 输入: {1,2,3,#,5,#,4}
# 输出: [1,3,4]
# 说明:
#    1
#  /   \
# 2     3
#  \     \
#   5     4

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
    @param root: the root of the given tree
    @return: the values of the nodes you can see ordered from top to bottom
    """

    # BFS
    def right_side_view(self, root: TreeNode) -> List[int]:
        # write your code here
        if not root:
            return []

        queue = collections.deque([root])
        result = []
        while queue:
            result.append(queue[-1].val)
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return result

    # DFS
    def right_side_view1(self, root: TreeNode) -> List[int]:
        result = []

        def dfs(node, depth):
            if node:
                if depth == len(result):
                    result.append(node.val)
                dfs(node.right, depth + 1)
                dfs(node.left, depth + 1)

        dfs(root, 0)
        return result
