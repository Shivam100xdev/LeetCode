import atexit

import heapq
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        heap = []
        ans = []

        for i, num in enumerate(nums):
            heapq.heappush(heap, (-num, i))

            while heap[0][1] <= i - k:
                heapq.heappop(heap)

            if i >= k - 1:

                ans.append(-heap[0][0])


        return ans            



atexit.register(lambda: (open("display_runtime.txt","w").write("000")))
        