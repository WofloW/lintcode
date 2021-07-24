"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param hashTable: A list of The first node of linked list
    @return: A list of The first node of linked list which have twice size
    """
    def rehashing(self, hashTable):
        # write your code here
        original_size = len(hashTable)
        new_size = 2 * original_size
        new_table = [None] * new_size

        for i in hashTable:
            if i:
                node = i
                while node:
                    temp = node.next
                    self.insert_node(node, new_table, new_size)
                    node = temp
        return new_table

    def insert_node(self, node, new_table, new_size):
        index = node.val % new_size
        slot = new_table[index]
        if slot:
            while slot.next:
                slot = slot.next
            slot.next = node
        else:
            new_table[index] = node
        node.next = None
