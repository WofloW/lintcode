class Solution:
    """
    @param: n: a positive integer
    @return: n x 3 matrix
    """

    def consistentHashing(self, n):
        # write your code here
        if n == 0:
            return []

        results = [[0, 359, 1]]
        for i in range(1, n):
            index = 0
            for j in range(i):
                if results[j][1] - results[j][0] > \
                        results[index][1] - results[index][0]:
                    index = j
            left = results[index][0]
            right = results[index][1]
            results[index][1] = (left + right) // 2
            results.append([(left + right) // 2 + 1, right, i + 1])
        return results

'''
Algorithm:
Brute force find the largest size
Cut it into half

Note:
(left + right) // 2
'''