class Solution:
    def rob(self, nums: List[int]) -> int:

        def dp(i):
            if i == 0:
                return nums[0]
            if i == 1:
                return max(nums[0], nums[1])
            if newArr[i] != -1:
                return newArr[i]                

            s1 = nums[i] + dp(i - 2)
            s2 = dp(i - 1)
            newArr[i] = max(s1, s2)

            return newArr[i]

        n = len(nums)
        newArr = [-1] * n

        return dp(len(nums) - 1)
