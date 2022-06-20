# 用heap
"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
import heapq

ListNode.__lt__ = lambda x, y: (x.val < y.val)


class Solution1:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """

    def mergeKLists(self, lists):
        # write your code here
        dummy = ListNode(0)
        tail = dummy

        heap = []
        for l in lists:
            if l:
                heapq.heappush(heap, l)

        while heap:
            node = heapq.heappop(heap)
            tail.next = node
            tail = node
            if node.next:
                heapq.heappush(heap, node.next)

        return dummy.next

# 自顶向下归并
"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution2:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """

    def mergeKLists(self, lists):
        # write your code here
        if not lists:
            return None

        return self.merge(lists, 0, len(lists) - 1)

    def merge(self, lists, start, end):
        if start == end:
            return lists[start]

        mid = (start + end) // 2
        left_merge_result = self.merge(lists, start, mid)
        right_merge_result = self.merge(lists, mid + 1, end)
        return self.two_way_merge(left_merge_result, right_merge_result)

    def two_way_merge(self, head0, head1):
        dummy = ListNode(0)
        tail = dummy
        while head0 and head1:
            if head0.val < head1.val:
                tail.next = head0
                head0 = head0.next
            else:
                tail.next = head1
                head1 = head1.next
            tail = tail.next

        if head0:
            tail.next = head0

        if head1:
            tail.next = head1

        return dummy.next

# 自底向上归并
"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution3:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """

    def mergeKLists(self, lists):
        if not lists:
            return None

        while len(lists) > 1:
            next_lists = []

            for i in range(0, len(lists), 2):
                if i + 1 < len(lists):
                    new_list = self.two_way_merge(lists[i], lists[i + 1])
                else:
                    new_list = lists[i]
                next_lists.append(new_list)

            lists = next_lists

        return lists[0]

    def two_way_merge(self, head0, head1):
        dummy = ListNode(0)
        tail = dummy
        while head0 and head1:
            if head0.val < head1.val:
                tail.next = head0
                head0 = head0.next
            else:
                tail.next = head1
                head1 = head1.next
            tail = tail.next

        if head0:
            tail.next = head0

        if head1:
            tail.next = head1

        return dummy.next

