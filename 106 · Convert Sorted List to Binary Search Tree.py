"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: head: The first node of linked list.
    @return: a tree node
    """

    def sortedListToBST(self, head):
        # write your code here
        length = self.get_length(head)
        root, next = self.convert(head, length)
        return root

    def convert(self, head, length):
        if length == 0:
            return None, head

        left_root, middle = self.convert(head, length // 2)
        right_root, next = self.convert(middle.next, length - length // 2 - 1)
        root = TreeNode(middle.val)
        root.left = left_root
        root.right = right_root
        return root, next

    def get_length(self, head):
        length = 0
        while head:
            length += 1
            head = head.next
        return length


