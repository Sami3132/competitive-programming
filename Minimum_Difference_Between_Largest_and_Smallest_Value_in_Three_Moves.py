class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        
        maxHeap = heapq.nlargest(4, nums)[::-1]
        minHeap = heapq.nsmallest(4, nums)

        ans = float("inf")

        for i in range(4):
            ans = min(ans, maxHeap[i] - minHeap[i])

        return ans
