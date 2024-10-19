class Solution:
    def findGCD(self, nums: List[int]) -> int:
        minVal, maxVal = min(nums), max(nums)

        if minVal == maxVal:
            return minVal
        
        a, b = maxVal, minVal

        while b != 0:
            a, b = b, a % b
        
        return a
