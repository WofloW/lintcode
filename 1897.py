# 1897 · 会议室 3
# https://www.lintcode.com/problem/1897/solution/50586?utm_source=sc-libao-zyq
# Medium
# line sweep, prefix

# 扫描线 + 前缀和精华版
# 这道题之所以被称为精华版， 是因为这个题目把2种算法用到了极致。
#
# 首先， 开一个范围那么大的数组， 然后对于每个interval， mark一下不available。 也就是用了 + 1, 没用 - 1.
# 然后， 其实可以另外开一个数组， 等等再常数级别优化， 这个时候， 我们有了整个所有time的占用情况， 这个时候知道每个时间， 占用了几个。
# 然后我们根据占用情况， 反推出可用情况， 就是占用跟总房间去比。
# 然后妙的来啦， 怎么样在常数时间， 知道每个ask行不行呢？这里我们直接把available的时间标成1， 不available标成0.然后再去算一个前缀和。 然后看一下前缀和和出来， 和区间长度比较， 如果区间里面都是1，那么加起来肯定等于区间长度。 那么这个题目答案就出来了


class Solution:
    """
    @param intervals: the intervals
    @param rooms: the sum of rooms
    @param ask: the ask
    @return: true or false of each meeting
    """

    def meetingRoomIII(self, intervals, rooms, asks):
        time = [0] * 500001
        for interval in intervals:
            time[interval[0]] += 1
            time[interval[1]] -= 1

        last = time[0]
        available = [0] * 500001
        available[0] = 1 if last < rooms else 0
        for i in range(1, len(available)):
            curr = last + time[i]
            if curr < rooms:
                available[i] = available[i - 1] + 1
            else:
                available[i] = available[i - 1]
            last = curr

        results = []
        for ask in asks:
            result = available[ask[1] - 1] - available[ask[0] - 1] >= ask[1] - ask[0]
            results.append(result)
        return results