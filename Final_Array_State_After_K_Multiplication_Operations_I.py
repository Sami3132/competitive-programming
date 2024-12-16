class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap = []

        for i, num in enumerate(nums):
            heapq.heappush(heap, (num, i))
        
        for _ in range(k):
            num, ind = heapq.heappop(heap)
            nums[ind] *= multiplier
            heapq.heappush(heap, (nums[ind], ind))
        
        return nums
