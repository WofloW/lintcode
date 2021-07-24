class Solution:
    """
    @param n: a integer
    @param logs: a list of integers
    @return: return a list of integers
    """

    def exclusiveTime(self, n, logs):
        # write your code here
        stack = []
        result = [0 for i in range(n)]
        last_timestamp = 0
        for str in logs:
            log = str.split(':')
            id, status, timestamp = int(log[0]), log[1], int(log[2])
            if status == 'start':
                if stack:
                    result[stack[-1]] += timestamp - last_timestamp
                stack.append(id)
            else:
                timestamp += 1
                result[stack.pop()] += timestamp - last_timestamp
            last_timestamp = timestamp
        return result
'''
Algorithm:
Use stack to simulate the function stack
Use list to caculate the function exclusive time

Note:
end time 3 is the end of time 3
start time is the start of time 3
'''