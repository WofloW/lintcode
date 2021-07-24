"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: param root: The root of the binary search tree
    @param k1: An integer
    @param k2: An integer
    @return: return: Return all keys that k1<=key<=k2 in ascending order
    """

    def searchRange(self, root, k1, k2):
        # write your code here
        if not root or k2 < k1:
            return []

        ans = []
        self.inorder(root, ans, k1, k2)
        return ans

    def inorder(self, root, ans, k1, k2):
        if not root:
            return

        if root.val > k1:
            self.inorder(root.left, ans, k1, k2)
        if root and k1 <= root.val <= k2:
            ans.append(root.val)
        if root.val < k2:
            self.inorder(root.right, ans, k1, k2)


'''
Algorithm:
inorder traversal

Note:
Pruning

'''