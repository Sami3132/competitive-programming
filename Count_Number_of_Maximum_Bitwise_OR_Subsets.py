class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        maxOR = 0

        for num in nums:
            maxOR |= num
        
        def backtrack(i, curOR):
            if i == len(nums):
                return 1 if curOR == maxOR else 0
            
            return(
                backtrack(i + 1, curOR | nums[i]) +
                backtrack(i + 1, curOR)
                )
        
        return backtrack(0, 0)
