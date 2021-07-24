"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param: : the root of tree
    @param: : the target sum
    @return: two numbers from tree which sum is n
    """

    def twoSum(self, root, n):
        if not root:
           return
        self.res = None
        node_set = set()
        self.inorder(root, n, node_set)
        return self.res

    def inorder(self, root, n, node_set):
        if not root:
            return
        self.inorder(root.left, n, node_set)
        if root.val in node_set:
            self.res = [n - root.val, root.val]
        else:
            node_set.add(n - root.val)
        self.inorder(root.right, n, node_set)


'''
Algorithm:
inorder

Note:
set
'''