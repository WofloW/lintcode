# 134 · LRU Cache
# https://www.lintcode.com/problem/134/description?fromId=15&_from=collection


class LinkedNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    """
    @param: capacity: An integer
    """

    def __init__(self, capacity):
        self.key_to_node = {}
        # head denote most recently used
        self.head = LinkedNode()
        # tail denote least recently used
        self.tail = LinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity

    def add_to_head(self, node):
        self.key_to_node[node.key] = node
        old_first = self.head.next

        self.head.next = node
        old_first.prev = node

        node.prev = self.head
        node.next = old_first

    def move_to_head(self, node):
        self.remove_node(node)
        self.add_to_head(node)

    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.key_to_node.pop(node.key)

    def remove_tail(self):
        self.remove_node(self.tail.prev)

    """
    @param: key: An integer
    @return: An integer
    """

    def get(self, key):
        if key not in self.key_to_node:
            return -1

        node = self.key_to_node[key]
        self.move_to_head(node)

        return node.value

    """
    @param: key: An integer
    @param: value: An integer
    @return: nothing
    """

    def set(self, key, value):
        if key in self.key_to_node:
            node = self.key_to_node[key]
            node.value = value
            self.move_to_head(node)
        else:
            node = LinkedNode(key, value)
            self.add_to_head(node)
            if len(self.key_to_node) > self.capacity:
                self.remove_tail()






