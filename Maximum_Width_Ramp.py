class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        newArr = [0] * len(nums)
        prevSum = 0

        for i in range(len(nums) - 1, -1, -1):
            newArr[i] = max(prevSum, nums[i])
            prevSum = newArr[i]
        
        ans = 0
        l = 0

        for r in range(len(nums)):
            while nums[l] > newArr[r]:
                l += 1
            
            ans = max(ans, r - l)

        return ans
