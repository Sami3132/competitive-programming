class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        maxSum, minSum = 0, 0
        currMax, currMin = 0, 0
        
        for num in nums:
            currMax = max(num, currMax + num)
            currMin = min(num, currMin + num)
            
            maxSum = max(maxSum, currMax)
            minSum = min(minSum, currMin)
        
        return max(abs(maxSum), abs(minSum))
