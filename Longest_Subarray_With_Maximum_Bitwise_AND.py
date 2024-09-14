class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ans, size = 0, 0
        currMax = 0

        for num in nums:
            if num > currMax:
                currMax = num
                size = 1
                ans = 0
            elif num == currMax:
                size += 1
            else:
                size = 0
            
            ans = max(ans, size)
        
        return ans
