class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = dict()
        LIS = ans = 0

        for i in range(len(nums) - 1, -1, -1):
            currLIS = currCount = 1

            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    length, count = dp[j]

                    if length + 1 > currLIS:
                        currLIS, currCount = length + 1, count
                    elif length + 1 == currLIS:
                        currCount += count
            
            if currLIS > LIS:
                LIS, ans = currLIS, currCount
            elif currLIS == LIS:
                ans += currCount
            
            dp[i] = [currLIS, currCount]
        
        return ans
