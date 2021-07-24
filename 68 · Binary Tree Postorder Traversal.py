"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: A Tree
    @return: Postorder in ArrayList which contains node values.
    """
    def postorderTraversal(self, root):
        # write your code here
        if not root:
            return []
        result = []
        stack = [root]
        prev, current = None, root
        while len(stack) > 0:
            current = stack[-1]
            # Traverse down the tree
            if not prev or prev.left == current or prev.right == current:
                if current.left:
                    stack.append(current.left)
                elif current.right:
                    stack.append(current.right)
            # Traverse up from the left child
            elif current.left == prev:
                if current.right:
                    stack.append(current.right)
            # Prev == current. Add the leaf to the result and pop the stack
            else:
                result.append(current.val)
                stack.pop()
            prev = current
        return result


'''
Algorithm:
Binary Tree Postorder Traversal

Note:
prev current
stack

'''