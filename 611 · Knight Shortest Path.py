"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""

DIRECTIONS = [
    [1, 2],
    [1, -2],
    [2, 1],
    [2, -1],
    [-1, 2],
    [-1, -2],
    [-2, 1],
    [-2, -1],
]


class Solution:
    """
    @param grid: a chessboard included 0 (false) and 1 (true)
    @param source: a point
    @param destination: a point
    @return: the shortest path
    """

    def shortestPath(self, grid, source, destination):
        # write your code here

        if grid[destination.x][destination.y] == 1:
            return -1

        if not grid or not grid[0]:
            return -1

        source_tuple = (source.x, source.y)
        destination_tuple = (destination.x, destination.y)

        if source_tuple == destination_tuple:
            return 0

        forward_queue = collections.deque([source_tuple])
        forward_set = set([source_tuple])
        backward_queue = collections.deque([destination_tuple])
        backward_set = set([destination_tuple])

        distance = 0
        while forward_queue and backward_queue:
            distance += 1
            if self.extend_queue(
                    grid,
                    forward_queue,
                    forward_set,
                    backward_set
            ):
                return distance
            distance += 1
            if self.extend_queue(
                    grid,
                    backward_queue,
                    backward_set,
                    forward_set
            ):
                return distance
        return -1

    def extend_queue(self, grid, queue, visited, opposite_visited):
        for i in range(len(queue)):
            point = queue.popleft()
            for direction in DIRECTIONS:
                next_point = (
                    point[0] + direction[0],
                    point[1] + direction[1]
                )
                if next_point in opposite_visited:
                    return True
                if not self.is_valid(grid, next_point, visited):
                    continue
                queue.append(next_point)
                visited.add(next_point)
        return False

    def is_valid(self, grid, point, visited):
        x = point[0]
        y = point[1]

        if not 0 <= x < len(grid):
            return False
        if not 0 <= y < len(grid[0]):
            return False
        if point in visited:
            return False
        if grid[x][y] == 1:
            return False
        return True


'''
Algorithm:
Two way BFS

Note:
source == destination
check x y in range before checking visited and barrier
'''