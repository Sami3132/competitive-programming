class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        minHeap = []
        maxVal = float('-inf')
        n = len(nums)

        for i in range(n):
            heapq.heappush(minHeap, (nums[i][0], i, 0))
            maxVal = max(maxVal, nums[i][0])

        ans = [float('-inf'), float('inf')]
        
        while len(minHeap) == n:
            minVal, row, col = heapq.heappop(minHeap)

            if maxVal - minVal < ans[1] - ans[0]:
                ans = [minVal, maxVal]

            if col + 1 < len(nums[row]):
                nextVal = nums[row][col + 1]
                heapq.heappush(minHeap, (nextVal, row, col + 1))
                maxVal = max(maxVal, nextVal)
            else:
                break

        return ans
