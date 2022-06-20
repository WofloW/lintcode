# 1137 · 从二叉树构建字符串
# https://www.lintcode.com/problem/1137/?fromId=15&_from=collection


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
    @param t: the root of tree
    @return: return a string
    """

    def tree2str(self, t: TreeNode) -> str:
        # write your code here
        if not t:
            return ''

        left = self.tree2str(t.left)
        right = self.tree2str(t.right)

        if t.right:
            return f'{t.val}({left})({right})'
        elif t.left:
            return f'{t.val}({left})'
        else:
            return t.val

