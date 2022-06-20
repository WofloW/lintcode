class Solution1:
    """
    @param nums: an integer array
    @param k: An integer
    @return: the top k largest numbers in array
    """

    def topk(self, nums, k):
        # write your code here
        self.quick_select(0, len(nums) - 1, nums, k)
        return sorted(nums[:k], reverse=True)

    def quick_select(self, left, right, nums, k):
        if left == right:
            return

        i = left
        j = right
        pivot = nums[left]
        while i <= j:
            while i <= j and nums[i] > pivot:
                i += 1
            while i <= j and nums[j] < pivot:
                j -= 1

            if i <= j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        if j - left + 1 > k:
            self.quick_select(left, j, nums, k)
        if i - left + 1 < k:
            self.quick_select(i, right, nums, k - i + left)





class Solution2:
    """
    @param nums: an integer array
    @param k: An integer
    @return: the top k largest numbers in array
    """

    def topk(self, nums, k):
        start = 0
        end = len(nums) - 1
        index = self.partition(nums, start, end)
        while index != len(nums) - k:
            if index > len(nums) - k:
                end = index - 1
                index = self.partition(nums, start, end)
            else:
                start = index + 1
                index = self.partition(nums, start, end)
        result = nums[index:]
        result.sort()
        return result[::-1]

    def partition(self, A, start, end):
        index = start
        for i in range(start, end):
            if A[i] > A[end]: continue
            A[index], A[i] = A[i], A[index]
            index += 1
        A[index], A[end] = A[end], A[index]
        return index


# import heapq
# Solution3

# heap = []
# for num in nums:
#     heapq.heappush(heap, num)
#     if len(heap) > k:
#         heapq.heappop(heap)
#
# heap.sort(reverse=True)
# return heap
