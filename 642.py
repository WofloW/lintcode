# https://www.lintcode.com/problem/642/solution/59489
from collections import deque
class MovingAverage:
    def __init__(self, size: int):
        self.size = size
        self.queue = deque()
        self.window_sum = 0

    def next(self, val: int) -> float:
        # calculate the new sum by shifting the window
        self.queue.append(val)

        # len() cost O(1)   no need to maintain variable for actual count

        # two scenarios
        # [1,2,3] append 4
        # popleft 1       new queue [2, 3, 4]

        # [1, 2] append 3
        # no need to popleft 1
        head = self.queue.popleft() if len(self.queue) > self.size else 0

        # minus 1 from window_sum
        self.window_sum = self.window_sum - head + val

        return self.window_sum / min(self.size, len(self.queue))
