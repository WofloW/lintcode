# 707 · 最优账户结余
# https://www.lintcode.com/problem/707/?utm_source=sc-libao-zyq
# super hard


import math
class Solution:
    """
    @param edges: a directed graph where each edge is represented by a tuple
    @return: the number of edges
    """

    def balanceGraph(self, edges):
        def ksum(k, index, target):
            if k == 2:
                left = index
                right = len(weights_ls) - 1
                while left < right:
                    if weights_ls[left] + weights_ls[right] < target:
                        left += 1
                    elif weights_ls[left] + weights_ls[right] > target:
                        right -= 1
                    else:
                        return [left, right]
                return None

            for i in range(index + 1, len(weights_ls) - 1):
                temp = ksum(k - 1, i, target - weights_ls[index])
                if temp != None:
                    return [index] + temp
            return None

        weights = {}
        for edge in edges:
            [node1, node2, weight] = edge
            weights.setdefault(node1, 0)
            weights.setdefault(node2, 0)
            weights[node1] -= weight
            weights[node2] += weight

        weights_ls = sorted([val for _, val in weights.items() if val != 0])
        if not weights_ls:
            return 0

        left, right = math.floor(len(weights_ls) / 2), math.ceil(len(weights_ls) / 2)

        res = 0
        while left >= 0 or right < len(weights_ls):
            if not weights_ls:
                break
            comp = []
            if left == right:
                comp.append(weights_ls[left])
            else:
                comp.insert(0, weights_ls[left])
                comp.append(weights_ls[right])
            if left >= 0:
                left -= 1
            if right < len(weights_ls):
                right += 1
            for k in range(2, len(weights_ls) + 1):
                indices = ksum(k, 0, 0)
                if indices != None:
                    weights_ls = [val for ind, val in enumerate(weights_ls) if ind not in indices]
                    left, right = math.floor(len(weights_ls) / 2), math.ceil(len(weights_ls) / 2)
                    res += len(indices) - 1
                    break

        return res