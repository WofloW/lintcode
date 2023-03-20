"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


# 我想的最傻的解法
# 如果两个有交点，那么从后向前一定有一节是一样的
# 先计算两个长度，找到长的，先走到和短的一样长的位置，两个指针一起往后走
# 如果有交点那一定在一起走双指针的时候会发现
class Solution1:
    """
    @param headA: the first list
    @param headB: the second list
    @return: a ListNode
    """

    def getIntersectionNode(self, headA, headB):
        # write your code here
        tmpA = headA
        tmpB = headB
        lenA = 0
        lenB = 0
        while tmpA:
            lenA += 1
            tmpA = tmpA.next

        while tmpB:
            lenB += 1
            tmpB = tmpB.next

        tmpA = headA
        tmpB = headB
        if lenA > lenB:
            for i in range(lenA - lenB):
                tmpA = tmpA.next
        else:
            for i in range(lenB - lenA):
                tmpB = tmpB.next

        for i in range(min(lenA, lenB)):
            if tmpA == tmpB:
                return tmpA

            tmpA = tmpA.next
            tmpB = tmpB.next

        return None


# 神仙解法
# https://www.lintcode.com/problem/380/solution/56596
# 我看懂了但是我想不出来这么巧妙的解法，不建议使用
# 本质上和最傻解法一样，因为两个长度可能不同，所以巧妙的把两个链表拼起来了，如果两个长度一样，那一定能找到交叉或者一起走完变成None
# 如果两个链表不一样长，一个指针走的是链表a+链表b，另一个指针走的链表b+链表a，这样长度就一样了
# 链表a 1 -> 2 -> 3    链表b 2 -> 3
# 因为那个切换的代码
# 指针a 1 -> 2 -> 3 -> 2 -> 3
# 指针b 2 -> 3 -> 1 -> 2 -> 3
"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param headA: the first list
    @param headB: the second list
    @return: a ListNode
    """
    def getIntersectionNode(self, headA, headB):
        # write your code here
        pA, pB = headA, headB
        while pA != pB:
            pA = pA.next if pA else headB
            pB = pB.next if pB else headA
        return pA
