class Solution:
    """
    @param A: an integer array
    @return: nothing
    """

    def heapify(self, A):
        for i in range(len(A) // 2, -1, -1):
            self.sift_down(A, i, len(A))

    def sift_down(self, A, index, upper):
        while index < upper:
            left_child = index * 2 + 1
            right_child = index * 2 + 2
            max_index = index
            if left_child < upper and A[left_child] > A[max_index]:
                max_index = left_child
            if right_child < upper and A[right_child] > A[max_index]:
                max_index = right_child

            if max_index == index:
                return

            A[index], A[max_index] = A[max_index], A[index]
            index = max_index

    def sortIntegers(self, A):
        # write your code here
        self.heapify(A)
        for i in range(len(A) - 1, -1, -1):
            A[0], A[i] = A[i], A[0]
            self.sift_down(A, 0, i)
        return A

'''
Algorithm:
max-heap sort

Note:
max heap

'''