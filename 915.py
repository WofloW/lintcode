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
    @param p: the given node
    @return: the in-order predecessor of the given node in the BST
    """

    # Find the largest number which is smaller than p.val
    # Numbers in tree 1 2 3 4 5
    # Given 4 return 3

    # Given and return type Node not number
    # Consider 3 scenarios
    #   5
    # /  \
    # 4    10
    #     /
    #     9
    #    /
    #   8
    # Scenario #1: result in the left subtree
    # Given 9, result is 8
    # Given 5, result is 4

    # Scenario #2: result in the parent when iterating and go right.
    # Whenever we go right, the root must be smaller than given
    # Given 8, result is 5

    # Scenarios #3: no result
    # Given 4, result None
    
    def inorderPredecessor(self, root, p):
        result = None

        while root:
            # Find the root larger than given, go left subtree
            if root.val >= p.val:
                root = root.left
            else:
                # root.val < p.val means potential result
                # If result None, we mark root as result
                # Otherwise, compare current result with root, which is better result
                if result is None or root.val > result.val:
                    result = root
                root = root.right
        return result
