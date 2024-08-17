class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        ones = nums.count(1)
        l = 0
        windowOnes = maxWindowOnes = 0

        for r in range(2 * len(nums)):
            if nums[r % len(nums)]:
                windowOnes += 1
            
            if r - l + 1 > ones:
                windowOnes -= nums[l % len(nums)]
                l += 1
            
            maxWindowOnes = max(maxWindowOnes, windowOnes)
        
        return ones - maxWindowOnes
