class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        count = ans = 1

        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                count += 1
                ans = max(ans, count)
            else:
                count = 1
                    
        count = 1
        
        for i in range(1, n):
            if nums[i] < nums[i - 1]:
                count += 1
                ans = max(ans, count)
            else:
                count = 1
                    
        return ans
