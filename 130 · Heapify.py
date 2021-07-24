class Solution:

    def heapify(self, A):

        for i in range((len(A)) // 2, -1, -1):
            self.sift_down(A, i)

    def sift_down(self, A, index):

        n = len(A)
        while index < n:
            left = index * 2 + 1
            right = index * 2 + 2
            min_index = index
            if left < n and A[left] < A[min_index]:
                min_index = left
            if right < n and A[right] < A[min_index]:
                min_index = right

            if min_index == index:
                return
            A[index], A[min_index] = A[min_index], A[index]
            index = min_index


'''
Algorithm:
sift down
O(n)

Note:
start from the bottom: reversed   n//2, n//2 - 1, ...,  0
find the smaller child: son_index
swap node and smaller child
sift down until node < smaller child or no child
'''