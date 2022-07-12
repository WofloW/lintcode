# 300 · 会议室4
# https://www.lintcode.com/problem/300/description?utm_source=sc-libao-zyq

# Medium

# DP, binary search
import bisect
class Solution:
    def max_value(self, meeting, value):
        meeting=[meeting[i]+[value[i]] for i in range(len(meeting))]
        meeting.append([-1,0,0])
        meeting.sort(key=lambda x:(x[1],x[0]))
        a=[i[1] for i in meeting]
        res=[0]
        for i in range(1,len(meeting)):
            res.append(max(res[-1],res[bisect.bisect(a,meeting[i][0],0,i)-1]+meeting[i][2]))
        return res[-1]


# DP
MAX_TIME = 50000

class Solution:
    """
    @param meeting: the meetings
    @param value: the value
    @return: calculate the max value
    """

    def maxValue(self, meetings, values):
        meeting_end_time_to_index_value = collections.defaultdict(list)
        for i in range(len(meetings)):
            meeting_end_time_to_index_value[meetings[i][1]].append((meetings[i][0], values[i]))

        dp = [0] * (MAX_TIME + 1)
        for i in range(1, MAX_TIME + 1):
            dp[i] = dp[i - 1]
            for j in range(len(meeting_end_time_to_index_value[i])):
                start = meeting_end_time_to_index_value[i][j][0]
                value = meeting_end_time_to_index_value[i][j][1]
                dp[i] = max(dp[i], dp[start] + value)
        return max(dp)