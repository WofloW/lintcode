class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """

    def ladderLength(self, start, end, dict):
        # write your code here
        if start == end:
            return 1

        dict.add(start)
        dict.add(end)
        graph = self.construct_graph(dict)

        forward_queue = collections.deque([start])
        forward_set = set([start])
        backward_queue = collections.deque([end])
        backward_set = set([end])

        distance = 1
        while forward_queue and backward_queue:
            distance += 1
            if self.extend_queue(
                    graph,
                    forward_queue,
                    forward_set,
                    backward_set,
            ):
                return distance
            distance += 1
            if self.extend_queue(
                    graph,
                    backward_queue,
                    backward_set,
                    forward_set
            ):
                return distance
        return 0

    def construct_graph(self, dict):
        graph = {}
        for word in dict:
            graph[word] = set()
            for i in range(len(word)):
                char = word[i]
                prefix = word[:i]
                suffix = word[i + 1:]
                alphabet = list('abcdefghijklmnopqrstuvwxyz')
                alphabet.remove(char)
                for c in alphabet:
                    new_word = prefix + c + suffix
                    if new_word in dict:
                        graph[word].add(new_word)
        return graph

    def extend_queue(
            self,
            graph,
            queue,
            visited,
            opposite_visited
    ):
        for _ in range(len(queue)):
            word = queue.popleft()
            for neighbor in graph[word]:
                if neighbor in opposite_visited:
                    return True
                if neighbor in visited:
                    continue
                queue.append(neighbor)
                visited.add(neighbor)
        return False


'''
Algorithm:
Two way BFS

Note:
Use alphabet to optimize the transformation
'''