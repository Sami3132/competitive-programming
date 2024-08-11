class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        myDict = dict()

        def dp(i, total):
            if i == len(nums):
                return 1 if total == target else 0
            
            if (i, total) in myDict:
                return myDict[(i, total)]
            
            myDict[(i, total)] = (dp(i + 1, total + nums[i]) + dp(i + 1, total - nums[i]))
            return myDict[(i, total)]
        
        return dp(0, 0)
