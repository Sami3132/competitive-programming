class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k == 0:
            return 0

        total = 1
        ans = 0
        left = right = 0

        while right < len(nums):
            total *= nums[right]

            while total >= k:
                total /= nums[left]
                left += 1
            
            ans += right - left + 1
            right += 1
        
        return ans
