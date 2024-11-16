from typing import List

class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
            
        n = len(nums)
        result = []
        left, right = 0, 1
        
        while right < n:
            notConsecutive = nums[right] - nums[right - 1] != 1
            
            if notConsecutive:
                while left < right and left + k - 1 < n:
                    result.append(-1)
                    left += 1
                left = right
            elif right - left == k - 1:
                result.append(nums[right])
                left += 1
                
            right += 1
            
        return result
