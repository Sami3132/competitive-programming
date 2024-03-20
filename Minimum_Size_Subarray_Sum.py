class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        total = left = right = 0
        ans = float('inf')

        while right < len(nums):
            total += nums[right]
            right += 1

            while total >= target:
                ans = min(ans, right - left)
                total -= nums[left]
                left += 1
        
        return 0 if ans == float('inf') else ans
