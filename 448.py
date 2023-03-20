"""
Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""

# 讲解https://www.lintcode.com/problem/448/solution/16603

class Solution:
    """
    @param: root: The root of the BST.
    @param: p: You need find the successor node of p.
    @return: Successor of p.
    """

    # 3 scenarios
    #    8
    #   /   \
    #  3     10
    # 3 is given node. 8 is result

    # 8 is given node, 10 is result

    # 10 is given node, None is result

    def inorderSuccessor(self, root, p):
        successor = None
        while root:
            # if root larger than p, root is possible to be the successor. But maybe not exact the one closest to p
            # maintain the successor whenever we go left
            if root.val > p.val:
                successor = root
                root = root.left
            else:
                root = root.right
        return successor
