# 215 · 限制器
# https://www.lintcode.com/problem/215/description?utm_source=sc-libao-zyq
# Hard

# hashmap, sortedlist, binary search
from collections import defaultdict
from sortedcontainers import SortedList


class Solution:
    """
    @param: timestamp: the current timestamp
    @param: event: the string to distinct different event
    @param: rate: the format is [integer]/[s/m/h/d]
    @param: increment: whether we should increase the counter
    @return: true or false to indicate the event is limited or not
    """

    def __init__(self):
        self.hashmap = defaultdict(SortedList)

    def isRatelimited(self, timestamp, event, rate, increment):
        # write your code here
        limit_num, unit = rate.split('/')
        limit_num = int(limit_num)

        interval = 1
        if unit == 'm':
            interval *= 60
        if unit == 'h':
            interval *= 60 * 60
        if unit == 'd':
            interval *= 24 * 60 * 60

        start_time = timestamp - interval
        existing_num = self.calc_num(self.hashmap[event], start_time)
        if existing_num < limit_num:
            if increment:
                self.hashmap[event].add(timestamp)
            return False
        return True

    def calc_num(self, existing_list, start_time):
        n = len(existing_list)
        if n == 0 or existing_list[n - 1] < start_time:
            return 0

        if start_time < 0:
            return len(existing_list)

        left, right = 0, n - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if existing_list[mid] > start_time:
                right = mid
            else:
                left = mid

        if existing_list[left] > start_time:
            return n - left
        if existing_list[right] > start_time:
            return n - right
        return 0


