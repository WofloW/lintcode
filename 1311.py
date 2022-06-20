# 1311 · 二叉搜索树的最近公共祖先
# https://www.lintcode.com/problem/1311/?fromId=15&_from=collection

# Easy
# recursive

# 利用二叉搜索树的特性
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: root of the tree
    @param p: the node p
    @param q: the node q
    @return: find the LCA of p and q
    """
    def lowestCommonAncestor(self, root, p, q):
        # write your code here

        ancestor = root
        big = max(p.val, q.val)
        small = min(p.val, q.val)
        while True:
            if ancestor.val > big:
                ancestor = ancestor.left
            elif ancestor.val < small:
                ancestor = ancestor.right
            else:
                return ancestor


# 不利用二叉搜索树
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution1:
    """
    @param root: root of the tree
    @param p: the node p
    @param q: the node q
    @return: find the LCA of p and q
    """

    def lowestCommonAncestor(self, root, p, q):
        # write your code here
        if not root:
            return
        if root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        if left or right:
            return left if left else right
        return None
