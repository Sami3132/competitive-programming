class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        sum1 = [0, 0]
        sum2 = [sum(nums[0::2]), sum(nums[1::2])]
        ans = 0

        for i in range(len(nums)):
            sum2[i % 2] -= nums[i]

            if sum1[0] + sum2[1] == sum1[1] + sum2[0]:
                ans += 1

            sum1[i % 2] += nums[i]
        
        return ans
