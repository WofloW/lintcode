# 11 · 二叉查找树中搜索区间
# https://www.lintcode.com/problem/11/
# Medium

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

# Recursive
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


# Iterative
class Solution1:
    """
    @param root: param root: The root of the binary search tree
    @param k1: An integer
    @param k2: An integer
    @return: return: Return all keys that k1<=key<=k2 in ascending order
    """

    def search_range(self, root: TreeNode, k1: int, k2: int) -> List[int]:
        # write your code here
        result = []

        stack = []
        cur = root
        while cur or stack:
            if cur:
                stack.append(cur)
                if cur.val >= k1:
                    cur = cur.left
                else:
                    cur = None
            else:
                node = stack.pop()
                if k1 <= node.val <= k2:
                    result.append(node.val)
                if node.right and node.val <= k2:
                    cur = node.right
        return result

'''
Algorithm:
inorder traversal

Note:
Pruning

'''