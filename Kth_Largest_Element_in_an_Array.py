class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        self.heapify(heap)
        
        for num in nums[k:]:
            if num > heap[0]:
                heap[0] = num
                self.minHeapify(heap, 0, k)
        
        return heap[0]
    
    def heapify(self, nums):
        n = len(nums)
        for i in range((n // 2) - 1, -1, -1):
            self.minHeapify(nums, i, n)
    
    def minHeapify(self, nums, current, heapLen):
        left = 2 * current + 1
        right = 2 * current + 2
        smallest = current
        
        if left < heapLen and nums[left] < nums[smallest]:
            smallest = left
        
        if right < heapLen and nums[right] < nums[smallest]:
            smallest = right
        
        if smallest != current:
            nums[current], nums[smallest] = nums[smallest], nums[current]
            self.minHeapify(nums, smallest, heapLen)
