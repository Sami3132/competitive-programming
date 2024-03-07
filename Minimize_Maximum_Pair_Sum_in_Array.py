class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        length = len(nums) - 1
        i = 0
        ans = nums[i] + nums[length]

        while length - i > 0:
            ans = max(ans, nums[i] + nums[length])
            i += 1
            length -= 1
        
        print(nums)

        return ans
