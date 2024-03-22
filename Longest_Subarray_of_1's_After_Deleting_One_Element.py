class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        zeros = 0

        for right in range(len(nums)):
            zeros += abs(nums[right] - 1)
            if zeros > 1:
                zeros -= abs(nums[left] - 1)
                left += 1
        
        return right - left
