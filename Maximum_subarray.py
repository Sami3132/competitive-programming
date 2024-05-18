class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        count = nums[0]

        for i in range(1, len(nums)):
            if count < 0:
                count = nums[i]
            else:
                count += nums[i]
            
            if count > maxSum:
                maxSum = count

        return maxSum
